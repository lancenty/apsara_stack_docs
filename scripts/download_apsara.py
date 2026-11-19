#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Apsara Stack 文档一键下载脚本
================================
从 oss_links.json（同目录）读取 OSS 公开读直链，并发下载全部 PDF 到
apsara_stack_docs/<version>/<filename>。

特性：
  - 8 线程并发（可调 --workers）
  - 断点续传：已存在且大小与 Content-Length 一致的自动跳过
  - 自动跳过 status == "404_source_removed" 的失效直链
  - 中文文件名按解码后的原名保存（OSS 路径本就是 UTF-8 URL 编码）
  - 单文件失败不影响整体，结束后汇总

用法：
  python3 download_apsara.py            # 默认 8 线程下载到 ./apsara_stack_docs
  python3 download_apsara.py --workers 12
  python3 download_apsara.py --out /path/to/dir
"""
import json
import os
import sys
import time
import argparse
import concurrent.futures as cf
import requests

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
LINKS_JSON = os.path.join(ROOT, "data", "oss_links.json")
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36")


def load_links():
    if not os.path.exists(LINKS_JSON):
        sys.exit(f"[FATAL] 找不到 {LINKS_JSON}，请确认 data/ 目录与脚本的相对位置")
    with open(LINKS_JSON, encoding="utf-8") as f:
        return json.load(f)


def safe_name(name, used):
    """避免同一目录下文件名冲突：冲突时追加序号。"""
    base, ext = os.path.splitext(name)
    cand = name
    i = 1
    while cand in used:
        cand = f"{base}_{i}{ext}"
        i += 1
    used.add(cand)
    return cand


def download_one(item, out_root):
    url = item["url"]
    version = item.get("version") or "unknown"
    fname = item.get("filename") or os.path.basename(url.split("?")[0])
    dest_dir = os.path.join(out_root, version)
    os.makedirs(dest_dir, exist_ok=True)
    dest = os.path.join(dest_dir, fname)

    # 已下载且大小一致 -> 跳过
    try:
        h = requests.head(url, headers={"User-Agent": UA}, timeout=20, allow_redirects=True)
        total = int(h.headers.get("Content-Length", 0) or 0)
    except Exception:
        total = 0
    if os.path.exists(dest) and total and os.path.getsize(dest) == total:
        return ("skip", version, fname, "exists")

    tmp = dest + ".part"
    try:
        with requests.get(url, headers={"User-Agent": UA}, timeout=120, stream=True) as r:
            r.raise_for_status()
            with open(tmp, "wb") as fp:
                for chunk in r.iter_content(chunk_size=1 << 16):
                    if chunk:
                        fp.write(chunk)
        sz = os.path.getsize(tmp)
        if total and sz != total:
            os.remove(tmp)
            return ("fail", version, fname, f"size {sz}!={total}")
        os.replace(tmp, dest)
        return ("ok", version, fname, f"{sz}B")
    except Exception as e:
        if os.path.exists(tmp):
            os.remove(tmp)
        return ("fail", version, fname, f"{type(e).__name__}: {e}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--out", default=os.path.join(ROOT, "downloads"))
    args = ap.parse_args()

    links = load_links()
    todo = [x for x in links if x.get("status", "ok") == "ok"]
    skipped_404 = [x for x in links if x.get("status") == "404_source_removed"]
    print(f"[INFO] 总计 {len(links)} 条；可下载 {len(todo)} 条；跳过 404 {len(skipped_404)} 条")

    os.makedirs(args.out, exist_ok=True)
    counters = {"ok": 0, "skip": 0, "fail": 0}
    t0 = time.time()
    with cf.ThreadPoolExecutor(max_workers=args.workers) as ex:
        futs = {ex.submit(download_one, it, args.out): it for it in todo}
        done = 0
        for fut in cf.as_completed(futs):
            status, ver, name, info = fut.result()
            counters[status] = counters.get(status, 0) + 1
            done += 1
            if status != "ok" or done % 25 == 0:
                print(f"[{status}] {ver} {name}  ({info})  [{done}/{len(todo)}]")
    dt = time.time() - t0
    print("\n==== 下载完成 ====")
    print(f"成功 {counters['ok']} | 跳过(已存在) {counters['skip']} | 失败 {counters['fail']}")
    print(f"耗时 {dt/60:.1f} 分；输出目录 {args.out}")
    # 统计体积
    total_bytes = 0
    for root, _, files in os.walk(args.out):
        for fn in files:
            if fn.endswith(".pdf"):
                total_bytes += os.path.getsize(os.path.join(root, fn))
    print(f"本地 PDF 总体积 {total_bytes/1024/1024/1024:.2f} GB")


if __name__ == "__main__":
    main()
