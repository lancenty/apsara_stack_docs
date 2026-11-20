Alibaba Cloud  
Apsara Stack Enterprise  
Apsara Stack Security  
Developer Guide  
Product Version: V3.12.0  
Document Version: 20220928

**Table of Contents**

- [1.API overview](#section-1)
- [2.Apsara Stack Security Console](#section-2)
    - [2.1. List of operations](#section-2-1)
    - [2.2. Make API requests](#section-2-2)
        - [2.2.1. Request structure](#section-2-2-1)
        - [2.2.2. Request signatures](#section-2-2-2)
        - [2.2.3. Common parameters](#section-2-2-3)
        - [2.2.4. Response structure](#section-2-2-4)
    - [2.3. APIs](#section-2-3)
        - [2.3.1. DescribeAliyunAccounts](#section-2-3-1)
        - [2.3.2. ModifyAliyunAccount](#section-2-3-2)
        - [2.3.3. DescribeFeatures](#section-2-3-3)
- [3.Threat Detection Service (TDS)](#section-3)
    - [3.1. List of operations by function](#section-3-1)
    - [3.2. Make API requests](#section-3-2)
        - [3.2.1. Request structure](#section-3-2-1)
        - [3.2.2. Signature mechanism](#section-3-2-2)
        - [3.2.3. Common request parameters](#section-3-2-3)
        - [3.2.4. Response structure](#section-3-2-4)
    - [3.3. Asset management](#section-3-3)
        - [3.3.1. DescribeAllEntity](#section-3-3-1)
        - [3.3.2. DescribeFieldStatistics](#section-3-3-2)
        - [3.3.3. DescribeGroupedTags](#section-3-3-3)
        - [3.3.4. DescribeAllGroups](#section-3-3-4)
        - [3.3.5. DeleteGroup](#section-3-3-5)
        - [3.3.6. CreateOrUpdateAssetGroup](#section-3-3-6)
        - [3.3.7. ModifyTagWithUuid](#section-3-3-7)
        - [3.3.8. DescribeInstanceStatistics](#section-3-3-8)
        - [3.3.9. DescribeCloudProductFieldStatistics](#section-3-3-9)
        - [3.3.10. DescribeDomainCount](#section-3-3-10)
        - [3.3.11. DescribeDomainList](#section-3-3-11)
        - [3.3.12. DescribeDomainDetail](#section-3-3-12)
        - [3.3.13. DescribeCloudCenterInstances](#section-3-3-13)
        - [3.3.14. DescribeSummaryInfo](#section-3-3-14)
        - [3.3.15. DescribeSearchCondition](#section-3-3-15)
        - [3.3.16. DescribeAssetDetailByUuid](#section-3-3-16)
        - [3.3.17. DescribeSasAssetStatisticsColumn](#section-3-3-17)
        - [3.3.18. DescribePropertyUsageNewest](#section-3-3-18)
        - [3.3.19. DeleteTagWithUuid](#section-3-3-19)
        - [3.3.20. ModifyPushAllTask](#section-3-3-20)
        - [3.3.21. DescribeCriteria](#section-3-3-21)
        - [3.3.22. DescribeExportInfo](#section-3-3-22)
        - [3.3.23. ModifyLoginSwitchConfig](#section-3-3-23)
        - [3.3.24. ModifyLoginBaseConfig](#section-3-3-24)
        - [3.3.25. DeleteLoginBaseConfig](#section-3-3-25)
        - [3.3.26. DescribeAssetDetailByUuids](#section-3-3-26)
    - [3.4. Secure score](#section-3-4)
        - [3.4.1. DescribeSecureSuggestion](#section-3-4-1)
    - [3.5. Security alerts](#section-3-5)
        - [3.5.1. HandleSecurityEvents](#section-3-5-1)
        - [3.5.2. DescribeSecurityStatInfo](#section-3-5-2)
        - [3.5.3. DescribeAlarmEventList](#section-3-5-3)
        - [3.5.4. DescribeAlarmEventDetail](#section-3-5-4)
        - [3.5.5. DescribeSuspEvents](#section-3-5-5)
        - [3.5.6. DescribeSuspEventDetail](#section-3-5-6)
        - [3.5.7. HandleSimilarSecurityEvents](#section-3-5-7)
        - [3.5.8. DescribeSecurityEventOperations](#section-3-5-8)
        - [3.5.9. DescribeSecurityEventOperationStatus](#section-3-5-9)
        - [3.5.10. CreateSimilarSecurityEventsQueryTask](#section-3-5-10)
        - [3.5.11. DescribeSimilarSecurityEvents](#section-3-5-11)
        - [3.5.12. DescribeSimilarEventScenarios](#section-3-5-12)
        - [3.5.13. DescribeUserLayoutAuthorization](#section-3-5-13)
        - [3.5.14. RollbackSuspEventQuaraFile](#section-3-5-14)
        - [3.5.15. DescribeSuspEventQuaraFiles](#section-3-5-15)
    - [3.6. Configuration assessment](#section-3-6)
        - [3.6.1. DescribeRiskItemType](#section-3-6-1)
        - [3.6.2. StartBaselineSecurityCheck](#section-3-6-2)
        - [3.6.3. DescribeRiskCheckSummary](#section-3-6-3)
        - [3.6.4. ModifyRiskCheckStatus](#section-3-6-4)
        - [3.6.5. DescribeRiskCheckResult](#section-3-6-5)
        - [3.6.6. DescribeSecurityCheckScheduleConfig](#section-3-6-6)
        - [3.6.7. ModifyRiskSingleResultStatus](#section-3-6-7)
        - [3.6.8. ModifySecurityCheckScheduleConfig](#section-3-6-8)
        - [3.6.9. DescribeRiskCheckItemResult](#section-3-6-9)
    - [3.7. Brute-force attacks protection](#section-3-7)
        - [3.7.1. CreateAntiBruteForceRule](#section-3-7-1)
        - [3.7.2. ModifyAntiBruteForceRule](#section-3-7-2)
    - [3.8. Vulnerability management](#section-3-8)
        - [3.8.1. ModifyVulTargetConfig](#section-3-8-1)
        - [3.8.2. ModifyStartVulScan](#section-3-8-2)
        - [3.8.3. DescribeVulList](#section-3-8-3)
        - [3.8.4. DescribeEmgVulGroup](#section-3-8-4)
        - [3.8.5. DescribeVulWhitelist](#section-3-8-5)
        - [3.8.6. DescribeConcernNecessity](#section-3-8-6)
        - [3.8.7. DescribeGroupedVul](#section-3-8-7)
        - [3.8.8. ModifyCreateVulWhitelist](#section-3-8-8)
        - [3.8.9. ModifyEmgVulSubmit](#section-3-8-9)
        - [3.8.10. DescribeAutoDelConfig](#section-3-8-10)
        - [3.8.11. ModifyOperateVul](#section-3-8-11)
    - [3.9. Baseline check](#section-3-9)
        - [3.9.1. DescribeCheckWarningSummary](#section-3-9-1)
        - [3.9.2. DescribeStratety](#section-3-9-2)
        - [3.9.3. DescribeStrategyExecDetail](#section-3-9-3)
        - [3.9.4. DescribeCheckWarnings](#section-3-9-4)
        - [3.9.5. DescribeCheckWarningDetail](#section-3-9-5)
        - [3.9.6. DescribeWarningMachines](#section-3-9-6)
        - [3.9.7. DescribeUserBaselineAuthorization](#section-3-9-7)
        - [3.9.8. ValidateHcWarnings](#section-3-9-8)
        - [3.9.9. FixCheckWarnings](#section-3-9-9)
    - [3.10. Asset fingerprints](#section-3-10)
        - [3.10.1. DescribePropertyCount](#section-3-10-1)
        - [3.10.2. DescribePropertyPortDetail](#section-3-10-2)
        - [3.10.3. DescribePropertyProcDetail](#section-3-10-3)
        - [3.10.4. DescribePropertyPortItem](#section-3-10-4)
        - [3.10.5. DescribePropertyProcItem](#section-3-10-5)
        - [3.10.6. DescribePropertySoftwareDetail](#section-3-10-6)
        - [3.10.7. DescribePropertySoftwareItem](#section-3-10-7)
        - [3.10.8. DescribePropertyUserDetail](#section-3-10-8)
        - [3.10.9. DescribePropertyUserItem](#section-3-10-9)
        - [3.10.10. DescribeModuleConfig](#section-3-10-10)
    - [3.11. Notifications](#section-3-11)
        - [3.11.1. DescribeDingTalk](#section-3-11-1)
        - [3.11.2. DescribeNoticeConfig](#section-3-11-2)
    - [3.12. Agent client](#section-3-12)
        - [3.12.1. SasInstallCode](#section-3-12-1)
        - [3.12.2. PauseClient](#section-3-12-2)
    - [3.13. Export check results](#section-3-13)
        - [3.13.1. ExportRecord](#section-3-13-1)
    - [3.14. Virus detection](#section-3-14)
        - [3.14.1. OperateSuspiciousTargetConfig](#section-3-14-1)
- [4.Server Guard](#section-4)
    - [4.1. List of operations](#section-4-1)
    - [4.2. Make API requests](#section-4-2)
        - [4.2.1. Request structure](#section-4-2-1)
        - [4.2.2. Signature mechanism](#section-4-2-2)
        - [4.2.3. Common request parameters](#section-4-2-3)
        - [4.2.4. Response structure](#section-4-2-4)
    - [4.3. Asset management](#section-4-3)
        - [4.3.1. CreateGroup](#section-4-3-1)
        - [4.3.2. DescribeGroupSummary](#section-4-3-2)
        - [4.3.3. DescribeGroupStruct](#section-4-3-3)
        - [4.3.4. DeleteGroup](#section-4-3-4)
        - [4.3.5. DescribeAllTag](#section-4-3-5)
        - [4.3.6. DescribeBetachTag](#section-4-3-6)
        - [4.3.7. ModifyBetachTag](#section-4-3-7)
        - [4.3.8. DeleteTag](#section-4-3-8)
        - [4.3.9. DescribeAllEntity](#section-4-3-9)
        - [4.3.10. DescribeEntityList](#section-4-3-10)
        - [4.3.11. ModifyEntityGroup](#section-4-3-11)
        - [4.3.12. DescribeMachines](#section-4-3-12)
        - [4.3.13. DescribeMachineDetail](#section-4-3-13)
        - [4.3.14. DescribePropertyScheduleConfig](#section-4-3-14)
        - [4.3.15. ModifyPropertyScheduleConfig](#section-4-3-15)
        - [4.3.16. DescribePropertyStatistic](#section-4-3-16)
        - [4.3.17. DescribePropertyPortItem](#section-4-3-17)
        - [4.3.18. DescribePropertyPortDetail](#section-4-3-18)
        - [4.3.19. DescribePropertyPortDiff](#section-4-3-19)
        - [4.3.20. DescribePropertyProcItem](#section-4-3-20)
        - [4.3.21. DescribePropertyProcDetail](#section-4-3-21)
        - [4.3.22. DescribePropertyProcDiff](#section-4-3-22)
        - [4.3.23. DescribePropertySoftwareItem](#section-4-3-23)
        - [4.3.24. DescribePropertySoftwareDetail](#section-4-3-24)
        - [4.3.25. DescribePropertySoftwareDiff](#section-4-3-25)
        - [4.3.26. DescribePropertyUserItem](#section-4-3-26)
        - [4.3.27. DescribePropertyUserDetail](#section-4-3-27)
        - [4.3.28. DescribePropertyUserDiff](#section-4-3-28)
        - [4.3.29. PushAllTask](#section-4-3-29)
        - [4.3.30. DescribeTopRiskyAssets](#section-4-3-30)
        - [4.3.31. UnbindAegis](#section-4-3-31)
        - [4.3.32. UninstallAegis](#section-4-3-32)
    - [4.4. Vulnerability management](#section-4-4)
        - [4.4.1. DescribeTarget](#section-4-4-1)
        - [4.4.2. ModifyVulTarget](#section-4-4-2)
        - [4.4.3. DescribeVulTargetStatistics](#section-4-4-3)
        - [4.4.4. DescribeTargetConfig](#section-4-4-4)
        - [4.4.5. ModifyTargetConfig](#section-4-4-5)
        - [4.4.6. DescribeVulConfig](#section-4-4-6)
        - [4.4.7. ModifyVulConfig](#section-4-4-7)
        - [4.4.8. DescribeAutoDelConfig](#section-4-4-8)
        - [4.4.9. ModifyAutoDelConfig](#section-4-4-9)
        - [4.4.10. DescribeVulLevel](#section-4-4-10)
        - [4.4.11. ModifyVulLevel](#section-4-4-11)
        - [4.4.12. CreateVulWhitelist](#section-4-4-12)
        - [4.4.13. DescribeVulWhitelist](#section-4-4-13)
        - [4.4.14. DeleteVulWhitelist](#section-4-4-14)
        - [4.4.15. DescribeGroupedVul](#section-4-4-15)
        - [4.4.16. DescribeVulList](#section-4-4-16)
        - [4.4.17. DescribeVulDetails](#section-4-4-17)
        - [4.4.18. DescribeVulNumStatistics](#section-4-4-18)
        - [4.4.19. DescribeVulLevelStatistics](#section-4-4-19)
        - [4.4.20. DescribeVulMachineList](#section-4-4-20)
        - [4.4.21. OperateVul](#section-4-4-21)
        - [4.4.22. ModifyBatchIgnoreVul](#section-4-4-22)
        - [4.4.23. DeleteVulBatch](#section-4-4-23)
        - [4.4.24. ExportVul](#section-4-4-24)
        - [4.4.25. DescribeVulExportInfo](#section-4-4-25)
    - [4.5. Baseline check](#section-4-5)
        - [4.5.1. DescribeStrategy](#section-4-5-1)
        - [4.5.2. DescribeStratetyDetail](#section-4-5-2)
        - [4.5.3. ModifyStrategy](#section-4-5-3)
        - [4.5.4. DeleteStrategy](#section-4-5-4)
        - [4.5.5. DescribeStrategyTarget](#section-4-5-5)
        - [4.5.6. ModifyStrategyTarget](#section-4-5-6)
        - [4.5.7. DescribeUuidConfig](#section-4-5-7)
        - [4.5.8. ModifyMachineConfig](#section-4-5-8)
        - [4.5.9. DescribeUserSetting](#section-4-5-9)
        - [4.5.10. CreateUserSetting](#section-4-5-10)
        - [4.5.11. DescribeRiskWhiteList](#section-4-5-11)
        - [4.5.12. BatchDeleteWhiteList](#section-4-5-12)
        - [4.5.13. CreateUserWhiteList](#section-4-5-13)
        - [4.5.14. DescribeStratety](#section-4-5-14)
        - [4.5.15. DescribeStrategyExecDetail](#section-4-5-15)
        - [4.5.16. DescribeRiskType](#section-4-5-16)
        - [4.5.17. Describesummary](#section-4-5-17)
        - [4.5.18. OperateWarning](#section-4-5-18)
        - [4.5.19. ExportWarning](#section-4-5-19)
        - [4.5.20. DescribeExportInfo](#section-4-5-20)
    - [4.6. Unusual logon detection](#section-4-6)
        - [4.6.1. DescribeBaseConfigs](#section-4-6-1)
        - [4.6.2. ModifyBaseConfig](#section-4-6-2)
        - [4.6.3. DeleteBaseConfig](#section-4-6-3)
        - [4.6.4. DescribeSwitchConfigs](#section-4-6-4)
        - [4.6.5. ModifySwitchConfig](#section-4-6-5)
        - [4.6.6. DescribeConfigTarget](#section-4-6-6)
    - [4.7. Webshell detection](#section-4-7)
        - [4.7.1. DescribeWebPath](#section-4-7-1)
        - [4.7.2. ModifyWebPath](#section-4-7-2)
        - [4.7.3. DescribeCategoryCount](#section-4-7-3)
        - [4.7.4. DescribeWebshell](#section-4-7-4)
        - [4.7.5. OperateTrojan](#section-4-7-5)
        - [4.7.6. DescribeQuaraFile](#section-4-7-6)
        - [4.7.7. RollbackQuaraFile](#section-4-7-7)
    - [4.8. Exception detection on hosts](#section-4-8)
        - [4.8.1. DescribeSuspEventTypes](#section-4-8-1)
        - [4.8.2. DescribeSuspTrendStatistics](#section-4-8-2)
        - [4.8.3. OperateSuspiciousEvent](#section-4-8-3)
        - [4.8.4. OperateLoginLog](#section-4-8-4)
        - [4.8.5. CreateSuspiciousExport](#section-4-8-5)
        - [4.8.6. DescribeSuspiciousExportInfo](#section-4-8-6)
        - [4.8.7. DescribeVirusInfo](#section-4-8-7)
    - [4.9. Retrieval of host logs](#section-4-9)
        - [4.9.1. CreateLogQuery](#section-4-9-1)
        - [4.9.2. DescribeLogQuery](#section-4-9-2)
        - [4.9.3. DeleteLogQuery](#section-4-9-3)
        - [4.9.4. DescribeFilterFields](#section-4-9-4)
        - [4.9.5. DescribeHistogram](#section-4-9-5)
        - [4.9.6. DescribeLogInfo](#section-4-9-6)
        - [4.9.7. DescribeLogItems](#section-4-9-7)
- [5.Anti-DDoS](#section-5)
    - [5.1. List of operations](#section-5-1)
    - [5.2. Make API requests](#section-5-2)
        - [5.2.1. Request structure](#section-5-2-1)
        - [5.2.2. Signature mechanism](#section-5-2-2)
        - [5.2.3. Common request parameters](#section-5-2-3)
        - [5.2.4. Response structure](#section-5-2-4)
    - [5.3. APIs](#section-5-3)
        - [5.3.1. CheckIpSegment](#section-5-3-1)
        - [5.3.2. DescribeRegionName](#section-5-3-2)
        - [5.3.3. CreateIpSegment](#section-5-3-3)
        - [5.3.4. DescribeIpSegment](#section-5-3-4)
        - [5.3.5. DeleteIpSegment](#section-5-3-5)
        - [5.3.6. ModifyIpSegment](#section-5-3-6)
        - [5.3.7. CreateDdosPolicy](#section-5-3-7)
        - [5.3.8. DescribeDdosPolicies](#section-5-3-8)
        - [5.3.9. DeleteDdosPolicy](#section-5-3-9)
        - [5.3.10. ModifyDdosPolicy](#section-5-3-10)
        - [5.3.11. DescribeBlockSwitchs](#section-5-3-11)
        - [5.3.12. ModifyBlockSwitchs](#section-5-3-12)
        - [5.3.13. DescribeDdosEvents](#section-5-3-13)
        - [5.3.14. DescribeFlowAnalysisResult](#section-5-3-14)
        - [5.3.15. DescribeFlowDetails](#section-5-3-15)
        - [5.3.16. CancelCleanStatus](#section-5-3-16)
        - [5.3.17. CreateWhiteList](#section-5-3-17)
        - [5.3.18. DescribeWhiteList](#section-5-3-18)
        - [5.3.19. DeleteWhiteList](#section-5-3-19)
        - [5.3.20. DescribeConsoleDdosPolicies](#section-5-3-20)
- [6.Cloud Firewall](#section-6)
    - [6.1. List of operations by function](#section-6-1)
    - [6.2. Make API requests](#section-6-2)
        - [6.2.1. Request structure](#section-6-2-1)
        - [6.2.2. Signature mechanism](#section-6-2-2)
        - [6.2.3. Common request parameters](#section-6-2-3)
        - [6.2.4. Response structure](#section-6-2-4)
    - [6.3. Access control](#section-6-3)
        - [6.3.1. DescribePolicyPriorUsed](#section-6-3-1)
        - [6.3.2. ModifyControlPolicyPosition](#section-6-3-2)
        - [6.3.3. DescribeControlPolicy](#section-6-3-3)
        - [6.3.4. AddControlPolicy](#section-6-3-4)
        - [6.3.5. DeleteControlPolicy](#section-6-3-5)
        - [6.3.6. ModifyControlPolicy](#section-6-3-6)
        - [6.3.7. VPC firewalls](#section-6-3-7)
            - [6.3.7.1. CreateVpcFirewallControlPolicy](#section-6-3-7-1)
            - [6.3.7.2. DescribeVpcFirewallControlPolicy](#section-6-3-7-2)
            - [6.3.7.3. ModifyVpcFirewallControlPolicy](#section-6-3-7-3)
            - [6.3.7.4. ModifyVpcFirewallControlPolicyPosition](#section-6-3-7-4)
            - [6.3.7.5. DeleteVpcFirewallControlPolicy](#section-6-3-7-5)
            - [6.3.7.6. DescribeVpcFirewallPolicyPriorUsed](#section-6-3-7-6)
            - [6.3.7.7. DescribeVpcFirewallAclGroupList](#section-6-3-7-7)
            - [6.3.7.8. ResetVpcFirewallRuleHitCount](#section-6-3-7-8)
    - [6.4. Firewall switch](#section-6-4)
        - [6.4.1. PutEnableFwSwitch](#section-6-4-1)
        - [6.4.2. PutDisableFwSwitch](#section-6-4-2)
        - [6.4.3. PutEnableAllFwSwitch](#section-6-4-3)
        - [6.4.4. PutDisableAllFwSwitch](#section-6-4-4)
    - [6.5. Address books](#section-6-5)
        - [6.5.1. AddAddressBook](#section-6-5-1)
        - [6.5.2. DeleteAddressBook](#section-6-5-2)
        - [6.5.3. ModifyAddressBook](#section-6-5-3)
        - [6.5.4. DescribeAddressBook](#section-6-5-4)
- [7.Sensitive Data Discovery and Protection](#section-7)
    - [7.1. List of operations by function](#section-7-1)
    - [7.2. Make API requests](#section-7-2)
        - [7.2.1. Request structure](#section-7-2-1)
        - [7.2.2. Request signatures](#section-7-2-2)
        - [7.2.3. Common parameters](#section-7-2-3)
        - [7.2.4. Responses](#section-7-2-4)
    - [7.3. APIs](#section-7-3)
        - [7.3.1. DescribeDataAssets](#section-7-3-1)
        - [7.3.2. DescribeInstances](#section-7-3-2)
        - [7.3.3. DescribeTables](#section-7-3-3)
        - [7.3.4. DescribePackages](#section-7-3-4)
        - [7.3.5. DescribeColumns](#section-7-3-5)
        - [7.3.6. DescribeOssObjects](#section-7-3-6)
        - [7.3.7. DescribeOssObjectDetail](#section-7-3-7)
        - [7.3.8. DescribeDeparts](#section-7-3-8)
        - [7.3.9. DescribeAccounts](#section-7-3-9)
        - [7.3.10. DescribeAccountDetail](#section-7-3-10)
        - [7.3.11. DescribePrivileges](#section-7-3-11)
        - [7.3.12. DescribeEventTypes](#section-7-3-12)
        - [7.3.13. DescribeEvents](#section-7-3-13)
        - [7.3.14. DescribeEventDetail](#section-7-3-14)
        - [7.3.15. ModifyEventStatus](#section-7-3-15)
        - [7.3.16. ModifyEventTypeStatus](#section-7-3-16)
        - [7.3.17. ModifyDefaultLevel](#section-7-3-17)
        - [7.3.18. DescribeRules](#section-7-3-18)
        - [7.3.19. CreateRule](#section-7-3-19)
        - [7.3.20. ModifyRule](#section-7-3-20)
        - [7.3.21. ModifyRuleStatus](#section-7-3-21)
        - [7.3.22. DeleteRule](#section-7-3-22)
        - [7.3.23. DescribeDataLimitSet](#section-7-3-23)
        - [7.3.24. CreateDataLimit](#section-7-3-24)
        - [7.3.25. DeleteDataLimit](#section-7-3-25)
    - [7.4. Data dictionaries](#section-7-4)
        - [7.4.1. Operation type definition](#section-7-4-1)
        - [7.4.2. Resource type definition](#section-7-4-2)
        - [7.4.3. Risk level definition](#section-7-4-3)
- [8.Security Operations Center](#section-8)
    - [8.1. List of operations by function](#section-8-1)
    - [8.2. Request method](#section-8-2)
        - [8.2.1. Request syntax](#section-8-2-1)
        - [8.2.2. Sign API requests](#section-8-2-2)
        - [8.2.3. Common parameters](#section-8-2-3)
        - [8.2.4. Response structure](#section-8-2-4)
    - [8.3. Operations](#section-8-3)
        - [8.3.1. QueryDataCount](#section-8-3-1)
        - [8.3.2. GetAssetCount](#section-8-3-2)
        - [8.3.3. GetEcsProtectCount](#section-8-3-3)
        - [8.3.4. DescribeAttacks](#section-8-3-4)
        - [8.3.5. DescribeAlarms](#section-8-3-5)
        - [8.3.6. DescribeVulFrangs](#section-8-3-6)
        - [8.3.7. DescribeHcFrangs](#section-8-3-7)
        - [8.3.8. DescribePBLineFrangs](#section-8-3-8)
        - [8.3.9. QueryDataEnum](#section-8-3-9)
        - [8.3.10. QueryDataCodeValue](#section-8-3-10)
        - [8.3.11. QueryDataDistribution](#section-8-3-11)
        - [8.3.12. SaveOrUpdateSocReportTask](#section-8-3-12)
        - [8.3.13. QuerySocReportTasks](#section-8-3-13)
        - [8.3.14. DelSocReportTask](#section-8-3-14)
        - [8.3.15. QuerySocReportRecords](#section-8-3-15)
        - [8.3.16. GetDeptMap](#section-8-3-16)
        - [8.3.17. GetRegionMap](#section-8-3-17)
        - [8.3.18. DownloadFile](#section-8-3-18)
        - [8.3.19. GetEcsList](#section-8-3-19)
        - [8.3.20. GetDiskList](#section-8-3-20)
        - [8.3.21. GetSecurityGroupList](#section-8-3-21)
        - [8.3.22. GetEcsInfo](#section-8-3-22)
        - [8.3.23. GetRdsList](#section-8-3-23)
        - [8.3.24. GetRdsInstanceIPArrayList](#section-8-3-24)
        - [8.3.25. GetRdsInfo](#section-8-3-25)
        - [8.3.26. GetOssList](#section-8-3-26)
        - [8.3.27. GetSlbList](#section-8-3-27)
        - [8.3.28. GetEipList](#section-8-3-28)
        - [8.3.29. GetAlarmConfig](#section-8-3-29)
        - [8.3.30. UpdateAlarmConfig](#section-8-3-30)
        - [8.3.31. GetAlarmContacts](#section-8-3-31)
        - [8.3.32. AddAlarmContacts](#section-8-3-32)
        - [8.3.33. DeleteAlarmContacts](#section-8-3-33)
        - [8.3.34. SendAlarm](#section-8-3-34)
        - [8.3.35. QuerySource](#section-8-3-35)
        - [8.3.36. QueryType](#section-8-3-36)
        - [8.3.37. QueryLog](#section-8-3-37)
        - [8.3.38. GetVpcList](#section-8-3-38)
        - [8.3.39. GetMachineList](#section-8-3-39)
        - [8.3.40. GetMachineInfo](#section-8-3-40)
        - [8.3.41. DescribeSocUsers](#section-8-3-41)
        - [8.3.42. DeleteSocUser](#section-8-3-42)
        - [8.3.43. SaveOrUpdateSocUser](#section-8-3-43)
- [9.Error codes](#section-9)

<a id="section-1"></a>

# 1.API overview

This document introduces all of the operations that you can call by using Apsara Stack Security service APIs.

<a id="section-2"></a>

# 2.Apsara Stack Security Console

<a id="section-2-1"></a>

## 2.1. List of operations

This topic introduces all of the Apsara Stack Security console operations that you can call. For more information, see the corresponding operation description.

| Operation | Description |
| --- | --- |
| DescribeAliyunAccounts | Queries Alibaba Cloud accounts. |
| ModifyAliyunAccount | Modifies the information of an Alibaba Cloud account. |
| DescribeFeatures | Queries the deployed Apsara Stack Security features. |

<a id="section-2-2"></a>

## 2.2. Make API requests

<a id="section-2-2-1"></a>

### 2.2.1. Request structure

Apsara Stack Security API operations use the RPC protocol. This topic describes the structure of API requests.

Description

You can call Apsara Stack Security API operations by sending HTTP requests. The request syntax is as follows:

```text
http://endpoint/?Action=xx&parameters
```

where:

- `endpoint` : the endpoint used to call a cloud service. The endpoint for the Apsara Stack Security console is  `yundunprivate.[ RegionId].example.com` .

  Note

  example.com indicates the domain name of Apsara Stack.

- `Action` : the name of the operation being performed.

  For example, to obtain Apsara Stack Security features that have been deployed, you must set the Action parameter to DescribeFeatures.

- `parameters` : the request parameters for the operation. Separate multiple parameters with ampersands (&). Request parameters include both common parameters and operation-specific parameters.

  - Common parameters include information such as the API version and authentication information.

  - For more information about operation-specific parameters, see the corresponding operation description.

Example

Call the DescribeFeatures operation to query the Apsara Stack Security features that are deployed.

```text
https://yundunprivate.[ RegionId].example.com/?Action=DescribeFeatures&AccessKeyId=key-test&Format=JSON&SecureTransport=true&SignatureMethod=HMAC-SHA1&SignatureNonce=15215528852396&SignatureVersion=1.0&SourceIp=1xxxx6&Timestamp=2018-03-02Txxxxxxx&Version=2018-01-16&Signature=xxxx%xxxx%3D
```

API requests are presented in the following easy-to-read format in this document:

```text
https://yundunprivate.[ RegionId].example.com/?Action=DescribeFeatures
&Format=JSON
&Version=2018-01-16
&Signature=xxxx%xxxx%3D
&SignatureMethod=HMAC-SHA1
&SignatureNonce=15215528852396
&SignatureVersion=1.0
&AccessKeyId=key-test
&Timestamp=2012-06-01T12:00:00Z
```

<a id="section-2-2-2"></a>

### 2.2.2. Request signatures

Apsara Stack Security authenticates each access request. You need to include a signature for the submitted HTTP or HTTPS request.

Authorization

To ensure the security of your account, we recommend that you use a Resource Access Management (RAM) user to call operations. Before you use a RAM user to call an API operation, you must grant the RAM user the corresponding permission to call the operation by creating an authorization policy and attaching the policy to the RAM user.

Signature

You must sign all API requests to ensure security. Alibaba Cloud uses the request signature to verify the identity of the API caller. When you manually make an API request, you need to use the AccessKey Secret to calculate the signature, that is, the hash-based message authentication code (HMAC) value, based on the encoded and sorted request string. For more information, see the definition in RFC 2104.

This section uses the raw access parameters in the following table to describe how to create an operation signature.

| Parameter | Description |
| --- | --- |
| Access point | <code>http://tds.[ RegionId].example.com/?</code> |
| Operation-specific parameters | <code>Action=DescribeFeatures</code> |
| Common parameters except Signature | <code>&amp;Timestamp=2018-12-24T12:46:24Z</code><br><code>&amp;Format=JSON</code><br><code>&amp;AccessKeyId=&lt;yourAccessKeyId&gt;</code><br><code>&amp;SignatureMethod=HMAC-SHA1</code><br><code>&amp;SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf</code><br><code>&amp;Version=2018-12-03</code><br><code>&amp;SignatureVersion=1.0</code> |
| AccessKey Secret | <code>&lt;yourAccessKeySecret&gt;</code> |

1. Create a canonicalized query string by arranging the request parameters.

   Note

   The request parameters include operation-specific parameters and all common

   request parameters except Signature.

   <ol type="i">

   <li>

   Sort the parameters.

   </li>

   </ol>

   Sort the request parameters in alphabetical order.

   <ol type="i" start="2">

   <li>

   Encode the parameters.

   </li>

   </ol>

   Use UTF-8 to URL-encode the parameter names and values. The encoding rules are as follows:

   - Uppercase letters, lowercase letters, digits, and some special characters such as hyphens (-), underscores (_), periods (.), and tildes (~) do not need to be encoded.

   - Other characters must be percent encoded in %XY format. XY represents the ASCII code of the characters in hexadecimal notation. For example, double quotation marks (") are encoded as %22.

   - Extended UTF-8 characters are encoded in %XY%ZA... format.

   - Spaces must be encoded as %20. Do not encode spaces as plus signs (+).

   <ol type="i" start="3">

   <li>

   Connect the encoded parameter names and values with equal signs (=).

   </li>

   <li>

   Then, sort the parameter name and value pairs connected by equal signs in alphabetical order.

   </li>

   </ol>

   Connect them with ampersands (&) to canonicalize a query string.

2. Use the canonicalized query string to construct the string for signature calculation based on the following rules:

   ```text
   StringToSign=HTTPMethod + "&" + percentEncode("/") + "&" +
   percentEncode(CanonicalizedQueryString)
   ```

3. Calculate the HMAC value of the StringToSign based on the definition in RFC 2104.

   Note

   The key used for signature calculation is your AccessKey Secret jointed with an

   ampersand (&) (ASCII 38). Secure Hash Algorithm 1 (SHA1) is used as the hash algorithm.

4. Encode the HMAC value in Base64 to obtain the signature string.

   ```text
   LEW8N4y7Uasop******
   ```

5. Add the signature string to the request as the Signature parameter.

<a id="section-2-2-3"></a>

### 2.2.3. Common parameters

Common request parameters must be included in all Apsara Stack Security API requests, such as the API version number and authentication information.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Version | String | Yes | The version number of the API. The value is in the format of YYYY-MM-DD.<br>Set the value to <em>2018-01-16</em>. |
| AccessKeyId | String | Yes | The AccessKey ID provided to you by Alibaba Cloud. |
| Signature | String | Yes | The signature string of the current request. |
| SignatureMethod | String | Yes | The encryption method of the signature string.<br>Set the value to <em>HMAC-SHA1</em>. |
| Timestamp | String | Yes | The timestamp of the request. Specify the time in the ISO 8601 standard in the <code> YYYY-MM-DDThh:mm:ssZ </code> format. The time must be in UTC.<br>For example, 2014-05-26T12:00:00Z indicates 20:00:00 on May 26, 2014 (UTC+8). |
| SignatureVersion | String | Yes | The version of the signature encryption algorithm. Set the value to <em>1.0</em>. |
| SignatureNonce | String | Yes | A unique, random number used to prevent replay attacks. You must use different numbers for different requests. |
| ResourceOwnerAc count | String | No | The owner account (the logon username) of the resource you want to access by using this API request. |
| Format | String | No | The format of the response.<br>Valid values: <em>JSON and XML</em>. Default value: XML. |

<a id="section-2-2-4"></a>

### 2.2.4. Response structure

Apsara Stack Security API responses can be returned in either the XML or JSON format. Every response returns a unique ID (indicated by RequestId) regardless of whether the call is successful.

Sample responses (XML format)

```xml
<? xml version="1.0" encoding="UTF-8"? >
<! --The root node of the result-->
<Operation name+Response>
    <! --Returned request ID-->
    <RequestId>4C467B38-3910-447D-87BC-AC049166F216</RequestId>
    <! --Returned data-->
</Operation name+Response>
```

Sample responses (JSON format)

```json
{
"RequestId": "4C467B38-3910-447D-87BC-AC049166F216",
/* Returned data */
}
```

<a id="section-2-3"></a>

## 2.3. APIs

<a id="section-2-3-1"></a>

### 2.3.1. DescribeAliyunAccounts

Description

You can call this operation to query Alibaba Cloud accounts.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set this parameter to <em>DescribeAliyunAccounts</em>. |
| CurrentPage | Integer | Yes | The number of the page to return. |
| PageSize | Integer | Yes | The number of records to return on each page. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| CurrentPage | Integer | The number of the current page returned. |
| PageSize | Integer | The number of records returned on each page. |
| TotalCount | Integer | The total number of returned pages. |
| HttpStatusCode | Integer | The HTTP status code returned. |
| AliyunAccounts | Array | The Alibaba Cloud accounts. For more information, see the following descriptions. |
| Id | Integer | The account record ID. |
| Aliuid | Long | The ID of the Alibaba Cloud account. |
| Account | String | The name of the Alibaba Cloud account. |
| AccessKey | String | The AccessKey ID of the Alibaba Cloud account. |
| AccessSecret | String | The AccessKey secret of the Alibaba Cloud account. |
| DataSecret | String | The DataSecret of the Alibaba Cloud account. |
| LicenseAegisNum | Integer | The number of Server Guard licenses. |
| LicenseTime | Long | The time when the licenses expire, in timestamp format. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample request

  ```text
  https://yundunprivate.[ RegionId].example.com/?Action=DescribeAliyunAccounts
  &CurrentPage=1
  &PageSize=10
  &<Common request parameters>
  ```

- Sample response (JSON format)

  ```json
  {
   "TotalCount":1,
   "PageSize":30,
   "RequestId":"7E33A454-20AA-49B1-8A9B-8979EFBDEDFC",
   "CurrentPage":1,
   "AliyunAccounts":[
    {
     "Account":"1113454564",
     "AccessSecret":"*****",
     "AccessKey":"<yourAccessKeyId>",
     "Id":2,
     "LicenseAegisNum":0,
     "Aliuid":1441871509587522,
     "LicenseTime":1589596257000,
     "DataSecret":"*****"
    }
   ],
   "HttpStatusCode":200
  }
  ```

<a id="section-2-3-2"></a>

### 2.3.2. ModifyAliyunAccount

Description

You can call this operation to modify the information of an Alibaba Cloud account with a specified account record ID.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set this parameter to <em>ModifyAliyunAccount</em>. |
| Id | Integer | Yes | The account record ID. |
| Aliuid | Long | No | The ID of the Alibaba Cloud account. |
| Account | String | No | The name of the Alibaba Cloud account. |
| AccessKey | String | No | The AccessKey ID of the Alibaba Cloud account. |
| AccessSecret | String | No | The AccessKey secret of the Alibaba Cloud account. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample request

  ```text
  https://yundunprivate.[ RegionId].example.com/?Action=ModifyAliyunAccount
  &Id=2
  &Account=1113454564
  &Aliuid=1441871509587522
  &AccessKey=<yourAccessKeyId>
  &AccessSecret=xxxxxxxxx
  &<Common request parameters>
  ```

- Sample response (JSON format)

  ```json
  {
   "RequestId":"C92B6187-603B-4E01-B0D7-74817F43852D"
  }
  ```

<a id="section-2-3-3"></a>

### 2.3.3. DescribeFeatures

Description

You can call this operation to obtain a list of the deployed Apsara Stack Security features.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>DescribeFeatures</em>. |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| Features | List | The list of the deployed Apsara Stack Security features. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://yundunprivate.[ RegionId].example.com/?Action=DescribeFeatures
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
   "RequestId":"BAEF6CE3-9990-4BDA-A056-4D269A724817",
   "Features":[
    "Basic",
    "Audit",
    "Sas",
    "Waf"
   ]
  }
  ```

<a id="section-3"></a>

# 3.Threat Detection Service (TDS)

<a id="section-3-1"></a>

## 3.1. List of operations by function

The following tables list API operations available for use in Threat Detection Service.

- Cloud service configuration checks

- Security alerts

- Vulnerability management

- Baseline checks

- Asset management

- Asset fingerprints

- Notifications

Cloud service configuration checks

| API operation | Description |
| --- | --- |
| DescribeRiskItemType | Queries the types of items for cloud service configuration checks. |
| StartBaselineSecurityCheck | Starts the baseline check. |
| DescribeRiskCheckSummary | Queries check results. |
| ModifyRiskCheckStatus | Modifies the status of a check result. |
| DescribeRiskCheckResult | Queries the result of a check item. |
| DescribeSecurityCheckScheduleCo nfig | Queries the custom check cycle and time period. |
| ModifyRiskSingleResultStatus | Modifies the status of an asset affected by a check item. |

Security alerts

| API operation | Description |
| --- | --- |
| DescribeAlarmEventDetail | Queries the details of an alert event. |
| DescribeSuspEventDetail | Queries the details of an unusual event. |
| DescribeAlarmEventList | Queries alert events of the security alert module. |
| DescribeSuspEvents | Queries exceptions. |

Vulnerability management

| API operation | Description |
| --- | --- |
| DescribeVulList | Queries vulnerabilities. |
|  |  |
| API operation | Description |

<table>
  <tr>
    <td>DescribeEmgVulGroup</td>
    <td>Queries urgent vulnerabilities by group.</td>
  </tr>
  <tr>
    <td>DescribeVulWhitelist</td>
    <td>Queries the vulnerability whitelist by page.</td>
  </tr>
  <tr>
    <td>DescribeGroupedVul</td>
    <td>Queries vulnerabilities by group.</td>
  </tr>
  <tr>
    <td>ModifyCreateVulWhitelist</td>
    <td>Creates a vulnerability whitelist.</td>
  </tr>
  <tr>
    <td>DescribeAutoDelConfig</td>
    <td>Queries the configurations of automatic vulnerability deletion.</td>
  </tr>
  <tr>
    <td>ModifyOperateVul</td>
    <td>Manages a detected vulnerability. For example, you can verify, ignore, or fix a vulnerability.</td>
  </tr>
</table>

Baseline checks

| API operation | Description |
| --- | --- |
| DescribeWarningMachines | Queries information about servers where baseline check policies are performed. |
| DescribeStrategyExecDetail | Queries detailed results of the last baseline check. |
| DescribeCheckWarnings | Queries specified risk items and check items on a specified server. |
| DescribeCheckWarningDetail | Queries the details of a specified check item. |
| DescribeCheckWarningSummary | Queries the statistics of baseline check results. |
| DescribeStratety | Queries the configurations of baseline check policies. |

Asset management

| API operation | Description |
| --- | --- |
| DescribeFieldStatistics | Queries asset instances. |
| DescribeGroupedTags | Queries tag statistics. |
| DescribeAllGroups | Queries information about all asset groups. |
| DeleteGroup | Deletes a server group. |
| CreateOrUpdateAssetGroup | Modifies the relationship between an asset and an asset group. |
| ModifyTagWithUuid | Modifies the relationship between a tag and a server or a cloud service. |
| DescribeInstanceStatistics | Queries the statistics of an asset. |
| DescribeCloudProductFieldStatisti cs | Queries the statistics of a cloud service. |
| DescribeDomainCount | Queries the number of domain assets. |
| DescribeDomainList | Queries domain assets. |
| DescribeDomainDetail | Queries the details of a domain asset. |
| DescribeCloudCenterInstances | Queries the asset information on the Assets page, such as the name and region of an asset instance. |
| DescribeSummaryInfo | Queries the security score of assets, the number of protected assets, and the number of unprotected assets. |

Asset fingerprints

| API operation | Description |
| --- | --- |
| DescribePropertyCount | Queries asset fingerprints. You can query the following types of asset fingerprints: process, port, software, and account. |
| DescribePropertyPortDetail | Queries the details of a specific port. |
| DescribePropertyProcDetail | Queries the details of a specific process. |
| DescribePropertyPortItem | Queries port information. |
| DescribePropertyProcItem | Queries process information. |
| DescribePropertySoftwareDetail | Queries the details of a software asset. |
| DescribePropertySoftwareItem | Queries software assets. |
| DescribePropertyUserDetail | Queries the details of a specific account. |
| DescribePropertyUserItem | Queries account information. |

<a id="section-3-2"></a>

## 3.2. Make API requests

<a id="section-3-2-1"></a>

### 3.2.1. Request structure

Apsara Stack Security API operations use the RPC protocol. This topic describes the structure of API requests.

Description

You can call Apsara Stack Security API operations by sending HTTP requests. The request syntax is as follows:

```text
http://endpoint/?Action=xx&parameters
```

where:

- `endpoint` : the endpoint of the Threat Detection Service API is  `tds.[RegionId].example.com` .

- `Action` : the name of the operation being performed.

  For example, to query the Apsara Stack Security features that are deployed, you must set the Action parameter to DescribeFeatures.

- `parameters` : the request parameters for the operation. Separate multiple parameters with ampersands (&). Request parameters include both common parameters and operation-specific parameters.

  - Common parameters include information such as the API version and identity authentication.

  - For more information about operation-specific parameters, see the corresponding operation description.

Example

The following example demonstrates how to call the DescribeFeatures operation to query the Apsara Stack Security features that are deployed.

```text
https://yundunprivate.[RegionId].example.com/?Action=DescribeFeatures&AccessKeyId=key-test&
Format=JSON&SecureTransport=true&SignatureMethod=HMAC-SHA1&SignatureNonce=15215528852396&SignatureVersion=1.0&SourceIp=1xxxx6&Timestamp=2018-03-02Txxxxxxx&Version=2018-01-16&Signature=xxxx%xxxx%3D
```

API requests are presented in the following easy-to-read format in this document:

```text
https://yundunprivate.[RegionId].example.com/?Action=DescribeFeatures
&Format=JSON
&Version=2018-01-16
&Signature=xxxx%xxxx%3D
&SignatureMethod=HMAC-SHA1
&SignatureNonce=15215528852396
&SignatureVersion=1.0
&AccessKeyId=key-test
&Timestamp=2012-06-01T12:00:00Z
```

<a id="section-3-2-2"></a>

### 3.2.2. Signature mechanism

Apsara Stack Security authenticates each access request. You need to include a signature for the submitted HTTP or HTTPS request.

API authorization

To ensure the security of your account, we recommend that you use a Resource Access Management (RAM) user to call API operations. Before using a RAM user to call an API operation, you must grant the RAM user the corresponding permission to call the API by creating an authorization policy and attaching the policy to the RAM user.

API signature

To ensure secure calls to the API, Alibaba Cloud authenticates each API request through the signature. When you manually make an API request, you need to use AccessKey Secret to calculate the signature, that is, the hash-based message authentication code (HMAC) value, based on the encoded and sorted request string. For more information, see the definition in RFC 2104.

This topic uses the raw access parameters in the following table to describe how to create an API signature.

| Parameter | Description |
| --- | --- |
| Access point | <code>http://semawaf.[ RegionId].example.com/?</code> |
| API-specific parameters | <code>Action=DescribeFeatures</code> |
| Common parameters (excluding the Signature parameter) | <code>&amp;Timestamp=2016-02-23T12:46:24Z</code><br><code>&amp;Format=JSON</code><br><code>&amp;AccessKeyId=&lt;yourAccessKeyId&gt;</code><br><code>&amp;SignatureMethod=HMAC-SHA1</code><br><code>&amp;SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf</code><br><code>&amp;Version=2018-01-16</code><br><code>&amp;SignatureVersion=1.0</code> |
| AccessKey secret | <code>&lt;yourAccessKeySecret&gt;</code> |

1. Use the request parameters to construct a canonicalized query string.

   Note

   The request parameters include common request parameters (excluding the

   Signature parameter) and API-specific parameters.

   <ol type="i">

   <li>

   Sort the parameters.

   </li>

   </ol>

   Sort the request parameters in alphabetical order.

   <ol type="i" start="2">

   <li>

   Encode the parameters.

   </li>

   </ol>

   Use UTF-8 to URL-encode the parameter names and values. The encoding rules are as follows:

   - Letters, digits, hyphens (-), underscores (_), periods (.), and tildes (~) are not encoded.

   - Other characters are encoded in the %XY format, where XY is the hexadecimal representation of the character in ASCII. For example, the double quotation mark (") is encoded as %22.

   - Extended UTF-8 characters are encoded in the %XY%ZA… format.

   - Note that a space is encoded as %20, instead of a plus sign (+).

   <ol type="i" start="3">

   <li>

   Connect the encoded parameter names and values with equal signs (=).

   </li>

   <li>

   Then, sort the parameter name and value pairs connected by equal signs in alphabetical order,

   </li>

   </ol>

   and connect them with ampersands (&) to produce the canonicalized query string.

2. Use the canonicalized query string to construct the string for signature calculation based on the following rules:

   ```text
   StringToSign=HTTPMethod + “&” + percentEncode(“/”) + ”&” +
   percentEncode(CanonicalizedQueryString)
   ```

3. Calculate the HMAC value of the StringToSign string according to the definition in RFC 2104.

   Note

   The key used for signature calculation is your AccessKey secret adding the

   ampersand (&) (ASCII 38). Secure Hash Algorithm 1 (SHA1) is used as the hash algorithm.

4. Encode the preceding HMAC value into a string based on Base64 encoding rules to obtain the signature value.

   ```text
   LEW8N4y7Uasop******
   ```

5. Set the Signature parameter in the request parameters to this signature value to sign the request.

<a id="section-3-2-3"></a>

### 3.2.3. Common request parameters

The following table describes the common request parameters that are used to indicate information such as the API version and authentication information.

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Version | String | Yes | The API version in the format of YYYY-MM-DD.<br>Set the value to <em>2018-01-16</em>. |
| AccessKeyId | String | Yes | The key ID that Alibaba Cloud assigns to a user for service access. |
| Signature | String | Yes | The signature string. |
| SignatureMethod | String | Yes | The signature method.<br>Set the value to <em>HMAC-SHA1</em>. |
| Timestamp | String | Yes | The timestamp of the request. Follow the ISO 8601 standard to specify the date and use the offset from Coordinated Universal Time (UTC) to specify the time zone.<br>The format is <code> YYYY-MM-</code><code>DDThh:mm:ssZ </code>.<br>For example, 2014-05-26T12:00:00Z indicates 20:00:00 on May 26, 2014, Beijing time. |
| SignatureVersion | String | Yes | The signature algorithm version.<br>Set the value to <em>1.0</em>. |
| SignatureNonce | String | Yes | The unique random number used to prevent network replay attacks. You must use different random numbers for different requests. |
| ResourceOwnerAc count | String | No | The owner account of the resource to be accessed through this API request, that is, the logon username. |
| Format | String | No | The format of the response.<br>Set the value to <em>JSON or XML</em>.<br>Note Default value: XML. |

<a id="section-3-2-4"></a>

### 3.2.4. Response structure

Apsara Stack Security API responses support both the XML and JSON formats. The system always returns a unique identification code RequestId each time you send a request to call an operation, no matter whether the call is successful or not.

Sample responses (XML format)

```xml
<? xml version="1.0" encoding="UTF-8"? >
<! -- The root node of the result -->
<Operation name+Response>
    <! -- Returned request ID -->
    <RequestId>4C467B38-3910-447D-87BC-AC049166F216</RequestId>
    <! -- Returned data -->
</Operation name+Response>
```

Sample responses (JSON format)

```json
{
"RequestId": "4C467B38-3910-447D-87BC-AC049166F216",
/* Returned data */
}
```

<a id="section-3-3"></a>

## 3.3. Asset management

<a id="section-3-3-1"></a>

### 3.3.1. DescribeAllEntity

Queries information about all assets, such as asset group IDs and asset names.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeAllEntity | The operation that you want to perform.<br>Set the value to DescribeAllEntity. |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | 7E0618A9-D5EF-4220-9471-C42B5E92719F | The ID of the request. |
| EntityList | Array | - | The list of instances. |
| GroupId | Integer | 281801 | The ID of the group. |
| InstanceName | String | wasdsfasfdasfds | The name of the instance. |
| Ip | String | 10.0.0.183 | The IP address of the server. |
| Uuid | String | edc897d6-xxxxx-xxxxx-xxxxx-xxxxx | The UUID of the server. |
| InternetIp | String | 101.202.20.20 | The public IP address of the server. |
| IntranetIp | String | 10.10.10.10 | The private IP address of the server. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribeAllEntity
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<code>200</code>
<data>
    <EntityList>
        <InstanceName>wasdsfasfdasfds</InstanceName>
        <Uuid>edc897d6-xxxxx-xxxxx-xxxxx-xxxxx</Uuid>
        <IntranetIp>10.10.10.10</IntranetIp>
        <InternetIp>101.202.20.20</InternetIp>
        <Ip>10.0.0.183</Ip>
        <GroupId>281801</GroupId>
    </EntityList>
</data>
<requestId>7E0618A9-D5EF-4220-9471-C42B5E92719F</requestId>
```

`JSON`  format

```json
{
  "code": 200,
  "data": {
    "EntityList": [{
      "InstanceName": "wasdsfasfdasfds",
      "Uuid": "edc897d6-xxxxx-xxxxx-xxxxx-xxxxx",
      "IntranetIp": "10.10.10.10",
      "InternetIp": "101.202.20.20",
      "Ip": "10.0.0.183",
      "GroupId": 281801
    }]
  },
  "requestId": "7E0618A9-D5EF-4220-9471-C42B5E92719F"
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-3-2"></a>

### 3.3.2. DescribeFieldStatistics

Queries statistics of the assets.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeFieldStati stics | The operation that you want to perform. Set the value to DescribeFieldStatistics. |
| MachineTypes | String | No | ecs | The types of the assets. If the asset type is not specified, the statistics of all types of assets are queried.<br>• ecs: an ECS instance<br>• cloud_product: a cloud service |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| GroupedFields | - | - | The asset information. |
| GroupCount | Integer | 20 | The number of server groups. |
| InstanceCount | Integer | 100 | The total number of assets. |
| NewInstanceCo unt | Integer | 10 | The number of new servers. |
| NotRunningStat usCount | Integer | 10 | The number of servers that are not started. |
| OfflineInstance Count | Integer | 21 | The number of offline servers. |
| RegionCount | Integer | 11 | The number of regions to which the servers belong. |
| RiskInstanceCou nt | Integer | 90 | The number of assets that are at risk. |
| UnprotectedIns tanceCount | Integer | 10 | The number of unprotected assets. |
| VpcCount | Integer | 5 | The number of VPCs. |
| RequestId | String | 7E0618A9-D5EF-4220-9471-C42B5E92719F | The ID of the request. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribeFieldStatistics
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<DescribeFieldStatistics>
  <RequestId>20CB6B41-0ED9-4679-BF5D-B84B8F7E70FC</RequestId>
  <GroupedFields>
        <InstanceCount>216</InstanceCount>
        <GroupCount>3</GroupCount>
        <NewInstanceCount>11</NewInstanceCount>
        <VpcCount>109</VpcCount>
        <RiskInstanceCount>121</RiskInstanceCount>
        <OfflineInstanceCount>48</OfflineInstanceCount>
        <UnprotectedInstanceCount>48</UnprotectedInstanceCount>
        <RegionCount>25</RegionCount>
        <NotRunningStatusCount>9</NotRunningStatusCount>
  </GroupedFields>
</DescribeFieldStatistics>
```

`JSON`  format

```json
{
 "RequestId":"20CB6B41-0ED9-4679-BF5D-B84B8F7E70FC",
 "GroupedFields":{
  "InstanceCount":216,
  "NewInstanceCount":11,
  "GroupCount":3,
  "VpcCount":109,
  "RiskInstanceCount":121,
  "UnprotectedInstanceCount":48,
  "OfflineInstanceCount":48,
  "RegionCount":25,
  "NotRunningStatusCount":9
 }
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-3-3"></a>

### 3.3.3. DescribeGroupedTags

Queries the statistics of asset tags.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeGrouped Tags | The operation that you want to perform. Set the value to DescribeGroupedTags. |
| MachineTypes | String | No | ecs | The types of the assets. If the asset type is not specified, the statistics of all asset tags are queried.<br>• ecs: an ECS instance<br>• cloud_product: a cloud service |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| Count | Integer | 2 | The number of entries returned on the current page. |
| GroupedFileds | Array |  | The statistics of the asset tag. |
| Count | String | 2 | The number of assets to which a tag attaches. |
| Name | String | test | The name of the tag. |
| TagId | Integer | 8704 | The ID of the tag. |
| HttpStatusCod e | Integer | 200 | The HTTP status code of the returned results. |
| RequestId | String | 7E0618A9-D5EF-4220-9471-C42B5E92719F | The ID of the request. |
| Success | Boolean | true | Indicates whether the request was successful.<br>• true: successful<br>• false: failed |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribeGroupedTags
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<DescribeGroupedTags>
  <HttpStatusCode>200</HttpStatusCode>
  <Count>1</Count>
  <RequestId>DD5AFF52-0827-4FC9-B6EA-B233FF3AFF91</RequestId>
  <Success>true</Success>
  <GroupedFileds>
        <Name>test</Name>
        <Count>167</Count>
        <TagId>8704</TagId>
  </GroupedFileds>
</DescribeGroupedTags>
```

`JSON`  format

```json
{
 "HttpStatusCode":200,
 "Count":1,
 "RequestId":"DD5AFF52-0827-4FC9-B6EA-B233FF3AFF91",
 "Success":true,
 "GroupedFileds":[
  {
   "Name":"test",
   "Count":"167",
   "TagId":8704
  }
 ]
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-3-4"></a>

### 3.3.4. DescribeAllGroups

Queries the grouping information about servers.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeAllGroup s | The operation that you want to perform. Set the value to DescribeAllGroups. |
| Lang | String | No | zh | The natural language of the request and response. Valid values:<br>• zh: Chinese<br>• en: English |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| Count | Integer | 2 | The number of entries returned on the current page. |
| Groups | Array |  | The grouping information about the servers. |
| GroupFlag | Integer | 1 | The type of the server group.<br>• 0: default group<br>• 1: other groups |
| GroupId | Integer | 8834224 | The ID of the server group. |
| GroupName | String | test | The name of the server group. |
| RequestId | String | "requestId": "7E0618A9-D5EF-4220-9471-C42B5E92719F", | The ID of the request. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribeAllGroups
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<DescribeAllGroups>
  <Groups>
        <GroupFlag>0</GroupFlag>
        <GroupName>Ungrouped</GroupName>
        <GroupId>4120080</GroupId>
  </Groups>
  <Groups>
        <GroupFlag>1</GroupFlag>
        <GroupName>leaves</GroupName>
        <GroupId>8831497</GroupId>
  </Groups>
  <Groups>
        <GroupFlag>1</GroupFlag>
        <GroupName>test</GroupName>
        <GroupId>8834224</GroupId>
  </Groups>
  <Count>3</Count>
  <RequestId>9DD4B19B-CA32-41DA-AED7-77B4F84A91D5</RequestId>
</DescribeAllGroups>
```

`JSON`  format

```json
{
 "Groups":[
  {
   "GroupFlag":0,
   "GroupName":"Ungrouped",
   "GroupId":4120080
  },
  {
   "GroupFlag":1,
   "GroupName":"leaves",
   "GroupId":8831497
  },
  {
   "GroupFlag":1,
   "GroupName":"test",
   "GroupId":8834224
  }
 ],
 "Count":3,
 "RequestId":"9DD4B19B-CA32-41DA-AED7-77B4F84A91D5"
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-3-5"></a>

### 3.3.5. DeleteGroup

Deletes a server group.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DeleteGroup | The operation that you want to perform.<br>Set the value to DeleteGroup. |
| GroupId | Long | Yes | 11111 | The ID of the server group.<br>Note To delete a server group, you must provide the ID of the server group. You can call the DescribeAllGroups operation to obtain the ID. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | 7E0618A9-D5EF-4220-9471-C42B5E92719F | The ID of the request. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=DeleteGroup
&GroupId=1111
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<DeleteGroup>
      <code>200</code>
      <requestId>7E0618A9-D5EF-4220-9471-C42B5E92719F</requestId>
      <success>true</success>
    </DeleteGroup>
```

`JSON`  format

```json
{
  "code": 200,
  "requestId": "7E0618A9-D5EF-4220-9471-C42B5E92719F",
  "success": true
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-3-6"></a>

### 3.3.6. CreateOrUpdateAssetGroup

Modifies the relationship between an asset and an asset group. For example, you can modify the group to which the asset belongs or the list of assets.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | CreateOrUpdateA ssetGroup | The operation that you want to perform.<br>Set the value to CreateOrUpdateAssetGroup. |
| Uuids | String | No | aq12-\*\*\*,s23\*\*\* | The ID of the asset.<br>Note To modify the relationship between an asset and an asset group, you must provide the ID of the asset. You can call the DescribeCloudCenterInstances operation to obtain the ID. |
| GroupName | String | No | test | The name of the asset group.<br>Note To modify the relationship between an asset and an asset group, you must provide the name of the asset group. You can call the DescribeAllGroups operation to obtain the name. If GroupId is not specified, you must specify GroupName. |
| GroupId | Long | No | 111111 | The ID of the asset group.<br>Note To modify the relationship between an asset and an asset group, you must provide the ID of the asset group. You can call the DescribeAllGroups operation to obtain the ID. |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | 7E0618A9-D5EF-4220-9471-C42B5E92719F | The ID of the request. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=CreateOrUpdateAssetGroup
&GroupName=test
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<CreateOrUpdateAssetGroupResponse>
  <RequestId>7E0618A9-D5EF-4220-9471-C42B5E92719F</RequestId>
</CreateOrUpdateAssetGroupResponse>
```

`JSON`  format

```json
{
  "RequestId": "7E0618A9-D5EF-4220-9471-C42B5E92719F"
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-3-7"></a>

### 3.3.7. ModifyTagWithUuid

Modifies the relationship between tags and servers or cloud services.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | ModifyTagWithUu id | The operation that you want to perform.<br>Set the value to ModifyTagWithUuid. |
| TagList | String | Yes | ac,ad | The list of tags.<br>Note To modify the relationship between tags and assets, you must provide the list of tags. You can call the DescribeGroupedTags operation to obtain the list. |
| UuidList | String | No | 111-xx,aa-bb | The IDs of the assets.<br>Note To modify the relationship between tags and assets, you must provide the lDs of the assets. You can call the DescribeCloudCenterInstances operation to obtain the IDs. |
| TagId | String | No | 7E0618A9-D5EF-4220-9471-C42B5E92719F | The ID of the tag.<br>Note To modify the relationship between a tag and an asset, you must provide the ID of the tag. You can call the DescribeGroupedTags operation to obtain the ID. |
| MachineTypes | String | No | ecs | The types of the assets. Valid values:<br>• ecs: an ECS instance<br>• cloud_product: a cloud service |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | 7E0618A9-D5EF-4220-9471-C42B5E92719F | The ID of the request. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=ModifyTagWithUuid
&TagList=ac,ad
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<ModifyTagWithUuidResponse>
      <requestId>70C4B40D-D55E-4B7B-9992-8535E396B2F4</requestId>
</ModifyTagWithUuidResponse>
```

`JSON`  format

```json
{
    "RequestId": "70C4B40D-D55E-4B7B-9992-8535E396B2F4"
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-3-8"></a>

### 3.3.8. DescribeInstanceStatistics

Queries risk information about an asset.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| From | String | Yes | sas | The source of the data. Set the value to sas. |
| Uuid | String | Yes | a51cec37-ed73-4c53-b467-\*\*\* | The IDs of the assets. Separate multiple IDs with commas (,).<br>Note To query the risk information about an asset, you must provide the ID of the asset.You can call the DescribeCloudCenterInstances operation to obtain the ID. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Lang | String | No | zh | The natural language of the request and response. Valid values:<br>• zh: Chinese<br>• en: English |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | 7E0618A9-D5EF-4220-9471-C42B5E92719F | The ID of the request. |
| Data | Array |  | The risk information about the asset. |
| Uuid | String | us1233\*\*\*\*\*\* | The ID of the asset. |
| Account | Integer | 1 | The type of the asset group. Valid values:<br>• 0: default group<br>• 1: other groups |
| Health | Integer | 1 | The number of issues detected by the baseline check. |
| Trojan | Integer | 1 | The number of trojans. |
| Suspicious | Integer | 2 | The number of alerts. |
| Vul | Integer | 4 | The total number of vulnerabilities: CveNum + EmgNum + SysNum + CmsNum + AppNum. |
| CveNum | Integer | 1 | The number of Linux software vulnerabilities. |
| EmgNum | Integer | 0 | The number of emergency vulnerabilities. |
| SysNum | Integer | 1 | The number of Windows vulnerabilities. |
| CmsNum | Integer | 2 | The number of Web CMS vulnerabilities. |
| AppNum | Integer | 0 | The number of application vulnerabilities. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribeInstanceStatistics
&From=sas
&Uuid=a51cec37-ed73-4c53-b467-***
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<DescribeInstanceStatisticsResponse>
  <Data>
        <SysNum>1</SysNum>
        <Uuid>a51cec37-ed73-4c53-b467-***</Uuid>
        <CveNum>1</CveNum>
        <Suspicious>1</Suspicious>
        <Trojan>0</Trojan>
        <Account>0</Account>
        <CmsNum>1</CmsNum>
        <EmgNum>1</EmgNum>
        <Health>0</Health>
        <AppNum>1</AppNum>
        <Vul>5</Vul>
  </Data>
  <Data>
        <SysNum>2</SysNum>
        <Uuid>33f107a3-4653-4228-a428-***</Uuid>
        <CveNum>1</CveNum>
        <Suspicious>2</Suspicious>
        <Trojan>0</Trojan>
        <Account>0</Account>
        <CmsNum>1</CmsNum>
        <EmgNum>2</EmgNum>
        <Health>0</Health>
        <AppNum>1</AppNum>
        <Vul>7</Vul>
  </Data>
  <RequestId>44AE72D4-2DDF-4CEC-9957-64C470CC90FC</RequestId>
</DescribeInstanceStatisticsResponse>
```

`JSON`  format

```json
{
    "Data": [
        {
            "SysNum": 1,
            "Uuid": "a51cec37-ed73-4c53-b467-***",
            "CveNum": 1,
            "Suspicious": 1,
            "Trojan": 0,
            "Account": 0,
            "CmsNum": 1,
            "EmgNum": 1,
            "Health": 0,
            "AppNum": 1,
            "Vul": 5
        },
        {
            "SysNum": 2,
            "Uuid": "33f107a3-4653-4228-a428-***",
            "CveNum": 1,
            "Suspicious": 2,
            "Trojan": 0,
            "Account": 0,
            "CmsNum": 1,
            "EmgNum": 2,
            "Health": 0,
            "AppNum": 1,
            "Vul": 7
        }
    ],
    "RequestId": "44AE72D4-2DDF-4CEC-9957-64C470CC90FC"
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-3-9"></a>

### 3.3.9. DescribeCloudProductFieldStatistics

Queries the statistics of cloud services that are protected by Threat Detection Service.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeCloudPro ductFieldStatistic s | The operation that you want to perform. Set the value to DescribeCloudProductFieldStatistics. |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | 7E0618A9-D5EF-4220-9471-C42B5E92719F | The ID of the request. |
| GroupedFields | Struct |  | The statistics of cloud services that are protected by Threat Detection Service. |
| RiskInstanceCou nt | Integer | 90 | The number of assets that are at risk. |
| InstanceCount | Integer | 100 | The total number of assets. |
| CategoryCount | String | \[{"MachineType":1," Count":11}\] | The statistics of different types of assets.MachineType represents the type of the asset. Count represents the number of assets of a specific type.<br>Valid values of MachineType:<br>• 1: Server Load Balancer<br>• 2: NAT Gateway<br>• 3: ApsaraDB for RDS<br>• 4: ApsaraDB for MongoDB |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribeCloudProductFieldStatistics
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<DescribeCloudProductFieldStatistics>
      <code>200</code>
      <data>
            <GroupedFields>
                  <InstanceCount>100</InstanceCount>
                  <RiskInstanceCount>90</RiskInstanceCount>
                  <categoryCount>
                        <MachineType>1</MachineType>
                        <Count>11</Count>
                  </categoryCount>
            </GroupedFields>
      </data>
      <requestId>7E0618A9-D5EF-4220-9471-C42B5E92719F</requestId>
      <success>true</success>
</DescribeCloudProductFieldStatistics>
```

`JSON`  format

```json
{
  "code": 200,
  "data": {
    "GroupedFields": {
      "InstanceCount": 100,
      "RiskInstanceCount": 90,
      "categoryCount":[{"MachineType":1,"Count":11}]
    }
  },
  "requestId": "7E0618A9-D5EF-4220-9471-C42B5E92719F",
  "success": true
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-3-10"></a>

### 3.3.10. DescribeDomainCount

Queries the number of domain assets.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeDomainC ount | The operation that you want to perform. Set the value to DescribeDomainCount. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | 6FAFB857-FE24-4226-A09F-52EA5023C987 | The ID of the request. |
| RootDomainsC ount | Integer | 27 | The number of returned root domains. |
| TotalDomainsC ount | Integer | 1 | The number of subdomains. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribeDomainCount
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<DescribeDomainCount>
   <code>200</code>
   <data>
      <TotalDomainsCount>27</TotalDomainsCount>
      <RootDomainsCount>1</RootDomainsCount>
   </data>
   <requestId>6FAFB857-FE24-4226-A09F-52EA5023C987</requestId>
   <success>true</success>
    </DescribeDomainCount>
```

`JSON`  format

```json
{
 "requestId":"6FAFB857-FE24-4226-A09F-52EA5023C987",
 "data":{
  "TotalDomainsCount":27,
  "RootDomainsCount":1
 },
 "code":200,
 "success":true
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-3-11"></a>

### 3.3.11. DescribeDomainList

Queries information about domain assets.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| FuzzyDomain | String | No | sas | The information used to query domains by fuzzy match. |
| DomainType | String | No | root | The type of the domain. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. |
| CurrentPage | Integer | No | 1 | The page number of the current page. |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | 0B48AB3C-84FC-424D-A01D-B9270EF46038 | The ID of the request. |
| DomainListResp onseList | Array |  | The information about the domain asset. |
| Domain | String | tst.com | The name of the domain or website. |
| IpList | String | 1.2.3.4,1.2.3.5 | The list of IP addresses that correspond to the domain. |
| PageInfo | Struct |  | The page information. |
| Count | Integer | 10 | The number of entries returned on the current page. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| TotalCount | Integer | 27 | The total number of entries in the list of domain assets. |
| CurrentPage | Integer | 1 | The page number of the current page. |

Examples

Sample requests

```text
http(s)://[Endpoint]/? Action=DescribeDomainList
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<DomainListResponseList>
    <Domain>tst.com</Domain>
</DomainListResponseList>
<DomainListResponseList>
    <Domain>p.tst.com</Domain>
</DomainListResponseList>
<DomainListResponseList>
    <IpList>1.2.3.4,1.2.3.5</IpList>
    <Domain>b.tst.com</Domain>
</DomainListResponseList>
<DomainListResponseList>
    <Domain>r.tst.com</Domain>
</DomainListResponseList>
<DomainListResponseList>
    <Domain>t.tst.com</Domain>
</DomainListResponseList>
<DomainListResponseList>
    <Domain>k.tst.com</Domain>
</DomainListResponseList>
<DomainListResponseList>
    <Domain>{a.tst.com</Domain>
</DomainListResponseList>
<DomainListResponseList>
    <Domain>w.tst.com</Domain>
</DomainListResponseList>
<DomainListResponseList>
    <Domain>l.tst.com</Domain>
</DomainListResponseList>
<DomainListResponseList>
    <Domain>v.tst.com</Domain>
</DomainListResponseList>
<PageInfo>
    <TotalCount>27</TotalCount>
    <PageSize>10</PageSize>
    <CurrentPage>1</CurrentPage>
    <Count>10</Count>
</PageInfo>
<requestId>0B48AB3C-84FC-424D-A01D-B9270EF46038</requestId>
```

`JSON`  format

```json
{
    "DomainListResponseList":[
        {
            "Domain":"tst.com"
        },
        {
            "Domain":"p.tst.com"
        },
        {
            "IpList":"1.2.3.4,1.2.3.5",
            "Domain":"b.tst.com"
        },
        {
            "Domain":"r.tst.com"
        },
        {
            "Domain":"t.tst.com"
        },
        {
            "Domain":"k.tst.com"
        },
        {
            "Domain":"{a.tst.com"
        },
        {
            "Domain":"w.tst.com"
        },
        {
            "Domain":"l.tst.com"
        },
        {
            "Domain":"v.tst.com"
        }
    ],
    "PageInfo":{
        "TotalCount":27,
        "PageSize":10,
        "CurrentPage":1,
        "Count":10
    },
    "requestId":"0B48AB3C-84FC-424D-A01D-B9270EF46038"
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-3-12"></a>

### 3.3.12. DescribeDomainDetail

Queries details about a domain asset.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeDomainD etail | The operation that you want to perform.<br>Set the value to DescribeDomainDetail. |
| DomainName | String | Yes | \*.test.com | The name of the domain or website. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | 3A85CFCF-05C8-451A-9E41-C0D5E96BA407 | The ID of the request. |
| Domain | String | b.tst.com | The name of the returned domain. |
| RootDomain | String | tst.com | The name of the root domain that corresponds to the returned domain. |
| DomainDetailIte ms | Array |  | The details about the domain asset. |
| InternetIp | String | 1.2.3.1 | The public IP address of the asset instance. |
| InstanceId | String | i-m5e6w7dzsktt6mz4 yime | The ID of the asset instance. |
| Uuid | String | lb-bp1g9dohoyin9cjhn 6itt | The UUID of the asset instance. |
| AssetType | String | 0 | The type of the asset. Valid values:<br>• 0: Elastic Compute Service (ECS) instance<br>• 1: Server Load Balancer<br>• 2: NAT Gateway<br>• 3: ApsaraDB for RDS<br>• 4: ApsaraDB for MongoDB |
| InstanceName | String | iZm5e6w7dzsktt6m z4yimeZ-60288 | The name of the asset. |
| IntranetIp | String | 1.2.3.2 | The private IP address of the asset. |

Examples

Sample requests

```text
http(s)://[Endpoint]/? Action=DescribeDomainDetail
&DomainName=*.test.com
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<DescribeDomainDetailResponse>
  <Domain>b.***tst.com</Domain>
  <DomainDetailItems>
        <InstanceName>iZm5e6***</InstanceName>
        <AssetType>0</AssetType>
        <Uuid>d664e15e-488b-4f3c-a80f-***</Uuid>
        <InternetIp>1.2.3.1</InternetIp>
        <InstanceId>i-m5e***e</InstanceId>
        <IntranetIp>1.2.3.2</IntranetIp>
  </DomainDetailItems>
  <DomainDetailItems>
        <InstanceName>iZ***</InstanceName>
        <AssetType>0</AssetType>
        <Uuid>0d804403-8d36-4642-a5f1-***</Uuid>
        <InternetIp>1.2.3.3</InternetIp>
        <InstanceId>i-m5ehn8ugwvsp2k4xdzok</InstanceId>
        <IntranetIp>1.2.3.5</IntranetIp>
  </DomainDetailItems>
  <DomainDetailItems>
        <AssetType>2</AssetType>
        <Uuid>eip-wz9***</Uuid>
        <InternetIp>1.2.3.6</InternetIp>
        <InstanceId>eip-wz9***</InstanceId>
  </DomainDetailItems>
  <DomainDetailItems>
        <InstanceName>***test</InstanceName>
        <AssetType>1</AssetType>
        <Uuid>lb-bp***</Uuid>
        <InternetIp>1.2.3.7</InternetIp>
        <InstanceId>lb-bp***</InstanceId>
  </DomainDetailItems>
  <RootDomain>***tst.com</RootDomain>
  <requestId>3A85CFCF-05C8-451A-9E41-C0D5E96BA407</requestId>
</DescribeDomainDetailResponse>
```

`JSON`  format

```json
{
    "Domain":"b.***tst.com",
    "DomainDetailItems":[
            {
                "InstanceName":"iZm5e6***",
                "AssetType":"0",
                "Uuid":"d664e15e-488b-4f3c-a80f-***",
                "InternetIp":"1.2.3.1",
                "InstanceId":"i-m5e***e",
                "IntranetIp":"1.2.3.2"
            },
            {
                "InstanceName":"iZ***",
                "AssetType":"0",
                "Uuid":"0d804403-8d36-4642-a5f1-***",
                "InternetIp":"1.2.3.3",
                "InstanceId":"i-m5ehn8ugwvsp2k4xdzok",
                "IntranetIp":"1.2.3.5"
            },
            {
                "AssetType":"2",
                "Uuid":"eip-wz9***",
                "InternetIp":"1.2.3.6",
                "InstanceId":"eip-wz9***"
            },
            {
                "InstanceName":"***test",
                "AssetType":"1",
                "Uuid":"lb-bp***",
                "InternetIp":"1.2.3.7",
                "InstanceId":"lb-bp***"
            }
        ],
    "RootDomain":"***tst.com",
    "requestId":"3A85CFCF-05C8-451A-9E41-C0D5E96BA407"
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-3-13"></a>

### 3.3.13. DescribeCloudCenterInstances

Queries the asset information on the Assets page, such as the name and region of an asset instance.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeCloudCen terInstances | The operation that you want to perform. Set the value to DescribeCloudCenterInstances. |
| Criteria | String | No | \[{"name":"riskSta tus","value":"YES "}, {"name":"internet Ip","value":"1.2."}\] | Specifies the search conditions, such as instance IDs, instance names, VPC IDs, regions, and IP addresses. |
| CurrentPage | Integer | No | 1 | The page number of the current page. |
| LogicalExp | String | No | OR | The logical relationship between search conditions. Valid values:<br>• OR: The logical relationship between search conditions is OR.<br>• AND: The logical relationship between search conditions is AND. |
| MachineTypes | String | No | ecs | The type of the asset.<br>• ecs: an Elastic Compute Service (ECS) instance<br>• cloud_product: a cloud service |
| NoPage | Boolean | No | true | Specifies whether to enable paged query. Valid values:<br>• true: enables paged query.<br>• false: disables paged query. |
| PageSize | Integer | No | 20 | The number of entries to return on each page. |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| Instances | Array |  | The asset details. |
| AlarmStatus | String | NO | Indicates whether alerts are configured for the asset instance. Valid values:<br>• YES<br>• NO |
| AssetType | String | ecs | The type of the asset. |
| ClientStatus | String | online | Indicates whether the asset instance is protected by the agent. Valid values:<br>• online: The protection status of the asset is Enabled.<br>• offline: The protection status of the asset is Disabled.<br>• pause: The protection status of the asset is Paused. |
| Flag | Integer | 0 | Indicates whether the asset instance is provided by Alibaba Cloud. Valid values:<br>• 0: The asset instance is provided by Alibaba Cloud.<br>• 1: The asset instance is not provided by Alibaba Cloud. |
| GroupId | String | 4120080 | The ID of the group to which the asset instance belongs. |
| HcStatus | String | YES | Indicates whether the asset instance is exposed to baseline risks. Valid values:<br>• YES<br>• NO |
| HealthCheckCo unt | Integer | 1 | The number of issues that are detected in baseline checks. |
| InstanceId | String | i-m5\*\*\* | The ID of the asset instance. |
| InstanceName | String | yztest-l\*\*\* | The name of the asset instance. |
| InternetIp | String | 1.2.3.4 | The public IP address of the asset instance. |
| IntranetIp | String | 1.2.3.0 | The private IP address of the asset instance. |
| Ip | String | 1.2.3.4 | The public IP address of the asset instance. |
| Os | String | Linux | The operating system of the asset instance. |
| OsName | String | CentOS 7.6 64-bit | The kernel version of the asset instance. |
| Region | String | cn-hangzhou-cm\*\*\*-\*\*\* | The region where the asset instance is deployed. |
| RegionId | String | cn-hanghzou | The ID of the region where the asset instance is deployed. |
| RegionName | String | China (Qingdao) | The name of the region where the asset instance is deployed. |
| RiskStatus | String | NO | Indicates whether the asset instance is exposed to security risks. Valid values:<br>• YES<br>• NO |
| SafeEventCount | Integer | 5 | The number of alerts detected on the asset instance. |
| Status | String | Running | The status of the asset instance. Valid values:<br>• Running: The instance is running.<br>• notRunning: The instance is not running. |
| Tag | String | InternetIp | The tag of the asset instance. |
| Uuid | String | c9107c04-942f-40c1-981a-f1c1\*\*\* | The ID of the asset instance. |
| VpcInstanceId | String | classic | The ID of the VPC to which the asset instance belongs. |
| VulCount | Integer | 2 | The number of vulnerabilities detected on the asset instance. |
| VulStatus | String | YES | Indicates whether the asset instance is exposed to vulnerabilities. Valid values:<br>• YES<br>• NO |
| PageInfo |  |  | The page information. |
| Count | Integer | 10 | The number of entries returned on the current page. |
| CurrentPage | Integer | 1 | The page number of the current page. |
| PageSize | Integer | 20 | The number of entries returned per page. |
| TotalCount | Integer | 50 | The total number of entries. |
| RequestId | String | 32A73759-4C0F-4801-BE98-901223ACEE9A | The ID of the request. |
| Success | Boolean | true | Indicates whether the request is successful.<br>• true: successful<br>• false: failed |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribeCloudCenterInstances
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<DescribeCloudCenterInstances>
  <RequestId>32A73759-4C0F-4801-BE98-901223ACEE9A</RequestId>
  <PageInfo>
        <Count>0</Count>
        <TotalCount>691</TotalCount>
        <PageSize>20</PageSize>
        <CurrentPage>1</CurrentPage>
  </PageInfo>
  <Instances>
        <RiskStatus>NO</RiskStatus>
        <Uuid>88f7ce77-595e-4580-b655-3***</Uuid>
        <Ip>1.2.3.4</Ip>
        <Flag>0</Flag>
        <RegionName>China (Hangzhou)</RegionName>
        <OsName>CentOS 7.6 64-bit</OsName>
        <AssetType>0</AssetType>
        <InstanceId>i-m5e50***</InstanceId>
        <InternetIp>1.2.3.4</InternetIp>
        <HealthCheckCount>0</HealthCheckCount>
        <HcStatus>NO</HcStatus>
        <Os>linux</Os>
        <ClientStatus>online</ClientStatus>
        <Status>Running</Status>
        <Region>cn-hangzhou-cm***-***</Region>
        <VpcInstanceId>classic</VpcInstanceId>
        <VulStatus>NO</VulStatus>
        <Tag>InternetIp</Tag>
        <RegionId>cn-hangzhou</RegionId>
        <IntranetIp>1.2.3.0</IntranetIp>
        <AlarmStatus>NO</AlarmStatus>
        <VulCount>0</VulCount>
        <SafeEventCount>0</SafeEventCount>
        <InstanceName>yztest-l***</InstanceName>
  </Instances>
  <Instances>
        <RiskStatus>NO</RiskStatus>
        <Uuid>7a4735d6-75a4-4555-a18f-b***</Uuid>
        <Ip>1.2.3.4</Ip>
        <Flag>0</Flag>
        <RegionName>China (Hangzhou)</RegionName>
        <OsName>CentOS 7.6 64-bit</OsName>
        <AssetType>0</AssetType>
        <InstanceId>i-m5e5***</InstanceId>
        <InternetIp>1.2.3.4</InternetIp>
        <HealthCheckCount>0</HealthCheckCount>
        <HcStatus>NO</HcStatus>
        <Os>linux</Os>
        <ClientStatus>online</ClientStatus>
        <Status>Running</Status>
        <Region>cn-hangzhou-cm***-***</Region>
        <VpcInstanceId>classic</VpcInstanceId>
        <VulStatus>NO</VulStatus>
        <Tag>InternetIp</Tag>
        <RegionId>cn-hangzhou</RegionId>
        <IntranetIp>1.2.3.0</IntranetIp>
        <AlarmStatus>NO</AlarmStatus>
        <VulCount>0</VulCount>
        <SafeEventCount>0</SafeEventCount>
        <InstanceName>yztest-l***</InstanceName>
  </Instances>
  <Success>true</Success>
</DescribeCloudCenterInstances>
```

`JSON`  format

```json
{
 "RequestId":"32A73759-4C0F-4801-BE98-901223ACEE9A",
 "Instances":[
  {
   "RiskStatus":"NO",
   "Uuid":"88f7ce77-595e-4580-b655-3***",
   "Ip":"1.2.3.4",
   "Flag":0,
   "RegionName":"China (Hangzhou)",
   "OsName":"CentOS 7.6 64-bit",
   "AssetType":"0",
   "InstanceId":"i-m5e50***",
   "InternetIp":"1.2.3.4",
   "HealthCheckCount":0,
   "HcStatus":"NO",
   "Os":"linux",
   "Status":"Running",
   "ClientStatus":"online",
   "Region":"cn-hangzhou-cm***-***",
   "VpcInstanceId":"classic",
   "Tag":"InternetIp",
   "VulStatus":"NO",
   "IntranetIp":"1.2.3.0",
   "RegionId":"cn-hangzhou",
   "AlarmStatus":"NO",
   "VulCount":0,
   "InstanceName":"yztest-l***",
   "SafeEventCount":0
  },
  {
   "RiskStatus":"NO",
   "Uuid":"7a4735d6-75a4-4555-a18f-b***",
   "Ip":"1.2.3.4",
   "Flag":0,
   "RegionName":"China (Hangzhou)",
   "OsName":"CentOS 7.6 64-bit",
   "AssetType":"0",
   "InstanceId":"i-m5e5***",
   "InternetIp":"1.2.3.4",
   "HealthCheckCount":0,
   "HcStatus":"NO",
   "Os":"linux",
   "Status":"Running",
   "ClientStatus":"online",
   "Region":"cn-hangzhou-cm***-***",
   "VpcInstanceId":"classic",
   "Tag":"InternetIp",
   "VulStatus":"NO",
   "IntranetIp":"1.2.3.0",
   "RegionId":"cn-hangzhou",
   "AlarmStatus":"NO",
   "VulCount":0,
   "InstanceName":"yztest-l***",
   "SafeEventCount":0
  }
 ],
 "PageInfo":{
  "Count":0,
  "TotalCount":691,
  "PageSize":20,
  "CurrentPage":1
 },
 "Success":true
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-3-14"></a>

### 3.3.14. DescribeSummaryInfo

Queries the security information about an asset, such as the security score and the numbers of protected and unprotected assets.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeSummary Info | The operation that you want to perform. Set the value to DescribeSummaryInfo. |
| Lang | String | No | zh | The natural language of the request and response. Valid values:<br>• zh: Chinese<br>• en: English |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| AegisClientOffli neCount | Integer | 12 | The number of unprotected assets. |
| AegisClientOnli neCount | Integer | 127 | The number of protected assets. |
| RequestId | String | D40198E1-6EA8-482E-B3C7-D9573D75C0CA | The ID of the request. |
| SecurityScore | Integer | 44 | The security score of assets. Valid values:<br>• 95 to 100: The assets are secure.<br>• 85 to 94: The assets are exposed to a few security risks. We recommend that you reinforce your security system as soon as possible.<br>• 70 to 84: The assets are exposed to many security risks. We recommend that you reinforce your security system as soon as possible.<br>• 69 or lower: The current security system is unable to protect the assets against attacker intrusions. We recommend that you reinforce your security system as soon as possible. |
| Success | Boolean | true | Indicates whether the request is successful. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribeSummaryInfo
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<DescribeSummaryInfo>
  <SecurityScore>44</SecurityScore>
  <AegisClientOnlineCount>127</AegisClientOnlineCount>
  <RequestId>D40198E1-6EA8-482E-B3C7-D9573D75C0CA</RequestId>
  <Success>true</Success>
  <AegisClientOfflineCount>12</AegisClientOfflineCount>
</DescribeSummaryInfo>
```

`JSON`  format

```json
{
 "AegisClientOnlineCount":127,
 "SecurityScore":44,
 "RequestId":"D40198E1-6EA8-482E-B3C7-D9573D75C0CA",
 "Success":true,
 "AegisClientOfflineCount":12
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-3-15"></a>

### 3.3.15. DescribeSearchCondition

Queries the filter conditions of specified assets.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeSearchCo ndition | The operation that you want to perform.<br>Set the value to DescribeSearchCondition |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Lang | String | No | zh | The natural language of the request and response. Valid values:<br>• zh: Chinese<br>• en: English |
| Type | String | No | ecs | The type of the asset that you want to query. Valid values:<br>• ecs: ECS instances<br>• cloud_product: cloud services |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | 3AEC47AF-8CFA-485E-AC9A-3A8ABC06EA7F | The ID of the request. |
| ConditionList | Array |  | The information about the filter conditions. |
| Name | String | Running | The name of the condition. |
| FilterConditions | String | {\\"filterParams\\": \[{\\"labelKey\\":\\"a\|b\\ ",\\"value\\":\\" {\\\\\\"name\\\\\\":\\\\\\"s adsasd\\\\\\",\\\\\\"valu e\\\\\\":\\\\\\"dasdsdas \\\\\\"}\\"}\],\\"LogicalEx p\\":\\"OR\\"} | Filter conditions. |
| NameKey | String | stop_machine | The key of the condition name. |
| ConditionType | String | system | The type of the filter condition.<br>Valid values:<br>• system: default filter conditions<br>• user: custom filter conditions |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribeSearchCondition
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<code>200</code>
<data>
    <ConditionList>
        <FilterConditions>{"filterParams":[{"labelKey":"aaaaaaaa|bbbbbbb","value":"{\"name\
":\"sadsasd\",\"value\":\"dasdsdas\"}"}],"LogicalExp":"OR"}</FilterConditions>
        <ConditionType>system</ConditionType>
        <NameKey>stop_machine</NameKey>
    </ConditionList>
    <ConditionList>
        <FilterConditions>{"filterParams":[{"labelKey":"aaaaaaaa|bbbbbbb","value":"{\"name\
":\"sadsasd\",\"value\":\"dasdsdas\"}"}],"LogicalExp":"OR"}</FilterConditions>
        <ConditionType>system</ConditionType>
        <NameKey>new_machine_has_risk</NameKey>
    </ConditionList>
    <ConditionList>
        <FilterConditions>{"filterParams":[{"label":"At risk or not: At risk","value":"{\"name\":\"aaaaaa\",\"value\":\"YES\"}"}],"LogicalExp":"OR"}</FilterConditions>
        <ConditionType>user</ConditionType>
        <Name>Running</Name>
    </ConditionList>
</data>
<requestId>3AEC47AF-8CFA-485E-AC9A-3A8ABC06EA7F</requestId>
```

`JSON`  format

```json
{
  "code": 200,
  "data": {
    "ConditionList": [
      {
        "FilterConditions": "{\"filterParams\":[{\"labelKey\":\"aaaaaaaa|bbbbbbb\",\"value\
":\"{\\\"name\\\":\\\"sadsasd\\\",\\\"value\\\":\\\"dasdsdas\\\"}\"}],\"LogicalExp\":\"OR\"
}",
        "ConditionType": "system",
        "NameKey": "stop_machine"
      },
      {
        "FilterConditions": "{\"filterParams\":[{\"labelKey\":\"aaaaaaaa|bbbbbbb\",\"value\
":\"{\\\"name\\\":\\\"sadsasd\\\",\\\"value\\\":\\\"dasdsdas\\\"}\"}],\"LogicalExp\":\"OR\"
}",
        "ConditionType": "system",
        "NameKey": "new_machine_has_risk"
      },
      {
        "FilterConditions": "{\"filterParams\":[{\"label\":\"At risk or not: At risk\",\"value\":\"{\\\"name\\\":\\\"aaaaaa\\\",\\\"value\\\":\\\"YES\\\"}\"}],\"LogicalExp\":\"OR\"}",
        "ConditionType": "user",
        "Name": "Running"
      }
    ]
  },
  "requestId": "3AEC47AF-8CFA-485E-AC9A-3A8ABC06EA7F"
}
```

Error codes

For a list of error codes, see Error codes

<a id="section-3-3-16"></a>

### 3.3.16. DescribeAssetDetailByUuid

Queries details and extended information about a server based on its UUID.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeAssetDet ailByUuid | The operation that you want to perform.<br>Set the value to DescribeAssetDetailByUuid. |
| Uuid | String | Yes | 123213-13dwe-2412431-dafadfa | The UUID of the server. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Lang | String | No | zh | The natural language of the request and response. Valid values:<br>• zh: Chinese<br>• en: English |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | F7BA0B6C-4D33-49A7-AB7B-A221B2E40817 | The ID of the request. |
| AssetDetail | Struct |  | The details of the server. |
| InternetIp | String | 10.10.10.10 | The public IP address of the server. |
| IntranetIp | String | 10.0.0.211 | The internal IP address of the server. |
| InstanceName | Integer | 1312412341 | The name of the server. |
| InstanceId | Integer | 1234124124 | The ID of the server. |
| Ip | String | 10.10.10.101 | The IP address of the ECS instance. |
| Uuid | String | 1234214-ujuj-weqweq-111-vbbbb | The UUID of the server. |
| AssetType | String | 0 | The type of the server. |
| Os | String | linux | The type of the operating system. |
| ClientStatus | String | online | The status of the agent. |
| Region | String | shanghaixxxxxx | The region where the server is deployed. |
| RegionName | String | China (Shanghai) | The name of the region. |
| Tag | String | InternetIp | The tag attached to the server. |
| GroupTrace | String | Ungrouped | The grouping information. |
| Cpu | Integer | 2 | The number of CPU cores. |
| CpuInfo | String | Intel(R) Xeon(R) Platinum 8163 CPU @ 2.50GHz | The CPU details. |
| Kernel | String | 4.18.0-80.11.2.el8_0.x86_64 | The kernel version. |
| OsDetail | String | Linux 64bit | The operating system version and architecture. |
| Mem | Integer | 0 | The memory size. |
| SysInfo | String | CentOS Linux 8.0.1905 | The operating system. |
| HostName | String | qewrqwerqsadas | The hostname. |
| OsName | String | CentOS 8.0 64-bit | The name of the operating system. |
| VpcInstanceId | String | i-xxxx-xxxx-xxxxx-xxxxx | The ID of the VPC. |
| OsName | String | CentOS 8.0 64-bit | The name of the operating system. |
| IpList | List | \[ "10.0.0.123" \] | The IP address of the host. |
| MacList | List | \[ "00:11:3e:20:38" \] | The Media Access Control (MAC) address of the host. |
| DiskInfoList | List | \[ { "diskName": "/dev/vda1", "totalSize": 20, "useSize": 2 } \] | The disk information. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribeAssetDetailByUuid
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<code>200</code>
<data>
    <AssetDetail>
        <GroupName>Ungrouped</GroupName>
        <ClientStatus>online</ClientStatus>
        <Os>linux</Os>
        <InstanceId>rqreqwrq</InstanceId>
        <IpList>10.0.0.123</IpList>
        <CpuInfo>Intel(R) Xeon(R) Platinum 8163 CPU @ 2.50GHz</CpuInfo>
        <Ip>10.10.10.101</Ip>
        <OsName>CentOS 8.0 64-bit</OsName>
        <Cpu>2</Cpu>
        <SysInfo>CentOS Linux 8.0.1905</SysInfo>
        <OsDetail>Linux 64bit</OsDetail>
        <IntranetIp>10.0.0.211</IntranetIp>
        <DiskInfoList>
            <diskName>/dev/vda1</diskName>
            <totalSize>20</totalSize>
            <useSize>2</useSize>
        </DiskInfoList>
        <MacList>00:11:3e:20:38</MacList>
        <InstanceName>wqreqwerqwer</InstanceName>
        <AssetType>0</AssetType>
        <Uuid>1234214-ujuj-weqweq-111-vbbbb</Uuid>
        <Mem>8</Mem>
        <InternetIp>10.10.10.10</InternetIp>
        <RegionName>China (Shanghai)</RegionName>
        <Region>shanghaixxxxxx</Region>
        <Tag>InternetIp</Tag>
        <Kernel>4.18.0-80.11.2.el8_0.x86_64</Kernel>
        <HostName>qewrqwerqsadas</HostName>
    </AssetDetail>
</data>
<requestId>F7BA0B6C-4D33-49A7-AB7B-A221B2E40817</requestId>
```

`JSON`  format

```json
{
  "code": 200,
  "data": {
    "AssetDetail": {
      "GroupTrace": "Ungrouped",
      "ClientStatus": "online",
      "Os": "linux",
      "InstanceId": "rqreqwrq",
      "IpList": [
        "10.0.0.123"
      ],
      "CpuInfo": "Intel(R) Xeon(R) Platinum 8163 CPU @ 2.50GHz",
      "Ip": "10.10.10.101",
      "OsName": "CentOS 8.0 64-bit",
      "Cpu": 2,
      "SysInfo": "CentOS Linux 8.0.1905",
      "OsDetail": "Linux 64bit",
      "IntranetIp": "10.0.0.211",
      "DiskInfoList": [
        {
          "diskName": "/dev/vda1",
          "totalSize": 20,
          "useSize": 2
        }
      ],
      "MacList": [
        "00:11:3e:20:38"
      ],
      "InstanceName": "wqreqwerqwer",
      "AssetType": "0",
      "Uuid": "1234214-ujuj-weqweq-111-vbbbb",
      "Mem": 8,
      "InternetIp": "10.10.10.10",
      "RegionName": "China (Shanghai)",
      "Region": "shanghaixxxxxx",
      "Tag": "InternetIp",
      "Kernel": "4.18.0-80.11.2.el8_0.x86_64",
      "HostName": "qewrqwerqsadas"
    }
  },
  "requestId": "F7BA0B6C-4D33-49A7-AB7B-A221B2E40817"
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-3-17"></a>

### 3.3.17. DescribeSasAssetStatisticsColumn

Queries asset details based on the displayed columns on the Server tab. The detailed information includes the server information, tag, VPC, operating system, and region.

The Server tab displays columns based on the column filter. Displayed columns include the default and custom columns.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeSasAsset StatisticsColumn | The operation that you want to perform.<br>Set the value to DescribeSasAssetStatisticsColumn. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | FA04081D-25A1-486C-822A-61108E85B3BD | The ID of the request. |
| StatisticsColum n | String | ServerInfo,tag,vpc,o s,region | The information in the displayed columns on the Server tab.<br>The Server tab displays columns based on the column filter. Displayed columns include the default and custom columns. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribeSasAssetStatisticsColumn
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<DescribeSasAssetStatisticsColumnResponse>
      <RequestId>EB28FE45-2E90-4F01-A5FF-EF5C1591104F</RequestId>
      <StatisticsColumn>serverInfo,tag,vpc,os,region,defense,riskStatus,operate,alarm,hc,vul</StatisticsColumn>
</DescribeSasAssetStatisticsColumnResponse>
```

`JSON`  format

```json
{
    "RequestId": "EB28FE45-2E90-4F01-A5FF-EF5C1591104F",
    "StatisticsColumn": "serverInfo,tag,vpc,os,region,defense,riskStatus,operate,alarm,hc,vul"
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-3-18"></a>

### 3.3.18. DescribePropertyUsageNewest

Queries information about five most recently created accounts.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeProperty UsageNewest | The operation that you want to perform.<br>Set the value to DescribePropertyUsageNewest. |
| Type | String | No | user | The type of the account.<br>Valid values:<br>• user<br>• system |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | 27C78A20-0833-4519-B392-F7963CCFC6AC | The ID of the request. |
| ItemCount | Integer | 5 | The number of accounts. |
| Type | String | user | The type of the account created on the server. Set the value to user, which indicates user accounts. |
| NewestStatistic Items | Array |  | The account information. |
| Name | String | root | The name of the account. |
| Create | Long | 1566178646000 | The timestamp when the account was created. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribePropertyUsageNewest
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<code>200</code>
<data>
    <NewestStatisticItems>
        <Create>1566178646000</Create>
        <Name>dbus</Name>
    </NewestStatisticItems>
    <NewestStatisticItems>
        <Create>1566178646000</Create>
        <Name>halt</Name>
    </NewestStatisticItems>
    <NewestStatisticItems>
        <Create>1566178646000</Create>
        <Name>root</Name>
    </NewestStatisticItems>
    <NewestStatisticItems>
        <Create>1566178646000</Create>
        <Name>postfix</Name>
    </NewestStatisticItems>
    <NewestStatisticItems>
        <Create>1566178646000</Create>
        <Name>operator</Name>
    </NewestStatisticItems>
    <Type>user</Type>
    <ItemCount>5</ItemCount>
</data>
<requestId>27C78A20-0833-4519-B392-F7963CCFC6AC</requestId>
<success>true</success>
```

`JSON`  format

```json
{
    "code":200,
    "data":{
        "NewestStatisticItems":[
            {
                "Create":1566178646000,
                "Name":"dbus"
            },
            {
                "Create":1566178646000,
                "Name":"halt"
            },
            {
                "Create":1566178646000,
                "Name":"root"
            },
            {
                "Create":1566178646000,
                "Name":"postfix"
            },
            {
                "Create":1566178646000,
                "Name":"operator"
            }
        ],
        "Type":"user",
        "ItemCount":5
    },
    "requestId":"27C78A20-0833-4519-B392-F7963CCFC6AC",
    "success":true
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-3-19"></a>

### 3.3.19. DeleteTagWithUuid

Removes tags from the assets on the Assets page.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DeleteTagWithUu id | The operation that you want to perform.<br>Set the value to DeleteTagWithUuid. |
| TagName | String | Yes | aaaa | The name of the tag. |
| UuidList | String | No | 111-xx,aa-bb | The list of server UUIDs.<br>Note If UuidList is specified, Threat Detection Service removes the tag from the servers whose UUIDs are specified in the list. If UuidList is not specified, Threat Detection Service removes the tag from all servers. |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | 7E0618A9-D5EF-4220-9471-C42B5E92719F | The ID of the request. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=DeleteTagWithUuid
&TagName=aaaa
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<DeleteTagWithUuidResponse>
      <requestId>7E0618A9-D5EF-4220-9471-C42B5E92719F</requestId>
</DeleteTagWithUuidResponse>
```

`JSON`  format

```json
{
  "requestId": "7E0618A9-D5EF-4220-9471-C42B5E92719F"
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-3-20"></a>

### 3.3.20. ModifyPushAllTask

Dispatches all security check tasks.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | ModifyPushAllTas k | The operation that you want to perform.<br>Set the value to ModifyPushAllTask. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Uuids | String | No | uuid1,uuid2,uuid3 | The list of server UUIDs. |
| Tasks | String | No | HEALTH_CHECK,O VAL_ENTITY | The list of tasks. |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | 91EB4AC7-7FEF-4C72-BE49-4414E459AEC2 | The ID of the request. |
| PushTaskRsp | Struct |  | The result of the task dispatch. |
| PushTaskResult List | Array |  | The list of tasks failed to be dispatched. |
| InstanceId | String | i-xxxsasssss | The ID of the server. |
| OsVersion | String | linux | The version of the operating system. |
| InstanceName | String | Pay-as-you-go online monitoring | The name of the server. |
| Success | Boolean | false | The result of the task dispatch. |
| GroupId | Long | 226 | The ID of the group. |
| Ip | String | 127.0.0.1 | The IP address of the server. |
| Online | Boolean | true | Indicates whether the agent is connected. |
| Message | String | {\\"code\\":\\"clinent_offline\\",\\"message \\":\\"The agent is disconnected",\\"suc cess\\":false} | The message indicating task details. |
| Region | String | cn-beijing-ss-10 | The region where the server is deployed. |
| Uuid | String | inet-xxxxx-xxxx-xxxx-xxx-xxx | The UUID of the server. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=ModifyPushAllTask
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<PushTaskRsp>
    <PushTaskResultList>
        <GroupId>336</GroupId>
        <InstanceId>i-xxxsasssss</InstanceId>
        <InstanceName>Pay-as-you-go online monitoring</InstanceName>
        <Ip>127.0.0.1</Ip>
        <Message>{"code":"clinent_offline","message":"The agent is disconnected","success":false}</Message>
        <Online>false</Online>
        <OsVersion>linux</OsVersion>
        <Region>cn-beijing-ss-10</Region>
        <Success>false</Success>
        <Uuid>inet-xxxxx-xxxx-xxxx-xxx-xxx</Uuid>
    </PushTaskResultList>
</PushTaskRsp>
<RequestId>91EB4AC7-7FEF-4C72-BE49-4414E459AEC2</RequestId>
```

`JSON`  format

```json
{
  "PushTaskRsp":{
    "PushTaskResultList":[{
      "GroupId":336,
      "InstanceId":"i-xxxsasssss",
      "InstanceName":"Pay-as-you-go online monitoring",
      "Ip":"127.0.0.1",
      "Message":"{\"code\":\"clinent_offline\",\"message\":\"The agent is disconnected\",\"success\":false}",
      "Online":false,
      "OsVersion":"linux",
      "Region":"cn-beijing-ss-10",
      "Success":false,
      "Uuid":"inet-xxxxx-xxxx-xxxx-xxx-xxx"
    }]
  },
  "RequestId":"91EB4AC7-7FEF-4C72-BE49-4414E459AEC2"
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-3-21"></a>

### 3.3.21. DescribeCriteria

Queries fuzzy match conditions that return the properties of a queried asset.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeCriteria | The operation that you want to perform.<br>Set the value to DescribeCriteria. |
| MachineTypes | String | No | ecs | The type of the asset that you want to query. Valid values:<br>• ecs: Elastic Compute Service (ECS) instances<br>• cloud_product: cloud services except ECS |
| Value | String | No | xxx | The value of the fuzzy match condition. |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | 3F6E4741-6CE6-47CA-80E8-CF5CB145DBE2 | The ID of the request. |
| CriteriaList | Array |  | The list of search conditions. |
| Values | String | NO,YES,UNKNOWN | If the search condition is an option, the value of the option is returned.<br>If the search condition is an input, no value is returned. |
| Name | String | riskStatus | The names of all properties queried by the search conditions. |
| Type | String | input | The type of the search condition. Valid values:<br>• input: an input. The search condition is manually set.<br>• select: an option. The search condition is selected from a drop-down list. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribeCriteria
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<code>200</code>
<data>
    <CriteriaList>
        <Type>input</Type>
        <Values/>
        <Name>internetIp</Name>
    </CriteriaList>
    <CriteriaList>
        <Type>select</Type>
        <Values>NO,YES</Values>
        <Name>vulStatus</Name>
    </CriteriaList>
</data>
<requestId>3F6E4741-6CE6-47CA-80E8-CF5CB145DBE2</requestId>
```

`JSON`  format

```json
{
  "code": 200,
  "data": {
    "CriteriaList": [
      {
        "Type": "input",
        "Values": "",
        "Name": "internetIp"
      },
      {
        "Type": "select",
        "Values": "NO,YES",
        "Name": "vulStatus"
      }
    ]
  },
  "requestId": "3F6E4741-6CE6-47CA-80E8-CF5CB145DBE2"
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-3-22"></a>

### 3.3.22. DescribeExportInfo

Queries the progress of the task to export baseline check results.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeExportInf o | The operation that you want to perform.<br>Set the value to DescribeExportInfo. |
| ExportId | Long | Yes | 111 | The ID of the export task. |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | 4C1AE3F3-18FA-4108-BBB9-AFA1A032756C | The ID of the request. |
| Id | Long | 11 | The ID of the export task. |
| FileName | String | health_check_export _20171123 | The name of the exported Excel file. |
| CurrentCount | Integer | 1 | The number of the entries that have been exported. |
| TotalCount | Integer | 1 | The total number of the entries in the Excel file. |
| Progress | Integer | 100 | The progress of the export task. |
| ExportStatus | String | success | The status of the export task.<br>Valid values:<br>• init: The export task is initializing.<br>• exporting: The export task is in progress.<br>• success: The export task is completed. |
| Message | String | success | The message that shows the task result.<br>Set the value to success, which indicates the export task is completed. |
| Link | String | http://www.aliyun.com | The URL at which you can download the exported Excel file. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribeExportInfo
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<code>200</code>
<data>
    <TotalCount>1</TotalCount>
    <GmtCreate>1511439067000</GmtCreate>
    <Progress>100</Progress>
    <Message>success</Message>
    <ExportStatus>success</ExportStatus>
    <FileName>health_check_export_20171123</FileName>
    <CurrentCount>1</CurrentCount>
    <Id>11</Id>
    <Link>http://www.aliyun.com</Link>
</data>
<requestId>4C1AE3F3-18FA-4108-BBB9-AFA1A032756C</requestId>
```

`JSON`  format

```json
{
  "code": "200",
  "data": {
    "TotalCount":1,
    "GmtCreate":1511439067000,
    "Progress":100,
    "Message":"success",
    "ExportStatus":"success",
    "FileName":"health_check_export_20171123",
    "CurrentCount":1,
    "Id":11,
    "Link":"http://www.aliyun.com"
  },
  "requestId": "4C1AE3F3-18FA-4108-BBB9-AFA1A032756C"
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-3-23"></a>

### 3.3.23. ModifyLoginSwitchConfig

Enables or disables the logon security settings for a specific asset.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | ModifyLoginSwitc hConfig | The operation that you want to perform.<br>Set the value to: ModifyLoginSwitchConfig. |
| Item | String | Yes | login_common_a ccount | The type of the alert that you want to enable or disable. Valid values:<br>• login_common_ip: uncommon logon IP address alerts<br>• login_common_time: uncommon logon time alerts<br>• login_common_account: uncommon logon account alerts |
| Status | Integer | Yes | 0 | The status of the logon security settings. Valid values:<br>• 0: disabled<br>• 1: enabled |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | B256A525-7E42-4BB9-A27C-9017FDDFF1A2 | The ID of the request. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=ModifyLoginSwitchConfig
&Item=login_common_account
&Status=0
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<ModifyLoginSwitchConfigResponse>
      <requestId>B256A525-7E42-4BB9-A27C-9017FDDFF1A2</requestId>
</ModifyLoginSwitchConfigResponse>
```

`JSON`  format

```json
{ 
  "requestId": "B256A525-7E42-4BB9-A27C-9017FDDFF1A2"
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-3-24"></a>

### 3.3.24. ModifyLoginBaseConfig

Modifies the logon security settings for a specific asset.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | ModifyLoginBase Config | The operation that you want to perform.<br>Set the value to ModifyLoginBaseConfig. |
| Config | String | Yes | {"startTime":"00: 00","endTime":"0 2:00"} | The logon security settings for the specified asset. |
| Target | String | Yes | i-ecs-ssssasss-xxxx | The UUID of the server whose settings you want to modify. |
| Type | String | Yes | login_common_ti me | The type of the common logon that you want to modify. Valid values:<br>• login_common_ip: common logon IP addresses<br>• login_common_time: common logon time<br>• login_common_account: common logon accounts |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | 6BD40006-2A29-4769-8AB5-BC0F0E25C273 | The ID of the request. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=ModifyLoginBaseConfig
&Config={"startTime":"00:00","endTime":"02:00"}
&Target=i-ecs-ssssasss-xxxx
&Type=login_common_time
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<ModifyLoginBaseConfigResponse>
      <requestId>6BD40006-2A29-4769-8AB5-BC0F0E25C273</requestId>
</ModifyLoginBaseConfigResponse>
```

`JSON`  format

```json
{
    "requestId":"6BD40006-2A29-4769-8AB5-BC0F0E25C273"
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-3-25"></a>

### 3.3.25. DeleteLoginBaseConfig

Deletes basic configurations in the logon security settings for a specific asset.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DeleteLoginBaseC onfig | The operation that you want to perform.<br>Set the value to DeleteLoginBaseConfig. |
| Config | String | Yes | {"startTime":"06: 00:00","endTime":"16:00:00"} | The detailed configurations. The configurations depend on logon types.Valid values:<br>• login_common_ip: common logon IP addresses<br>Example: {"ip":"10.23.23.23"}.<br>• login_common_time: common logon time<br>Example: {"startTime":"06:00:00", "endTime":"16:00:00"}.<br>• login_common_account: common logon accounts<br>Example: {"account":"test_account_001"}.<br>• login_common_location: common logon locations<br>Example: {"location":"Shanghai"}. |
| Type | String | Yes | login_common_ti me | The type of the common logon that you want to delete. Valid values:<br>• login_common_ip: common logon IP addresses<br>• login_common_time: common logon time<br>• login_common_account: common logon accounts<br>• login_common_location: common logon locations |
| Target | String | No | 123-abc | The UUID of the server whose settings you want to delete. |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | 7E0618A9-D5EF-4220-9471-C42B5E92719F | The ID of the request. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=DeleteLoginBaseConfig
&Config={"startTime":"06:00:00","endTime":"16:00:00"}
&Type=login_common_time
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<DeleteLoginBaseConfigResponse>
      <requestId>7E0618A9-D5EF-4220-9471-C42B5E92719F</requestId>
</DeleteLoginBaseConfigResponse>
```

`JSON`  format

```json
{
  "requestId": "7E0618A9-D5EF-4220-9471-C42B5E92719F"
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-3-26"></a>

### 3.3.26. DescribeAssetDetailByUuids

Queries the details of specific ECS instances.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeAssetDet ailByUuids | The operation that you want to perform.<br>Set the value to: DescribeAssetDetailByUuids. |
| Uuids | String | Yes | 0687b17f-2a36-4e5c-b3d9 | The list of ECS instances. |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| AssetList | Array |  | The details of the assets. |
| AssetType | String | 0 | The type of the assets.<br>Set the value to 0, which indicates ECS instances. |
| ClientStatus | String | online | The status of the agent. Valid values:<br>• online<br>• offline |
| InstanceId | Integer | 1312332131 | The ID of the ECS instance. |
| InstanceName | Integer | 11 | The name of the ECS instance. |
| InternetIp | String | 10.10.10.10 | The public IP address of the ECS instance. |
| IntranetIp | String | 10.10.10.10 | The private IP address of the ECS instance. |
| Ip | String | 10.10.10.10 | The public IP address of the ECS instance, which is the same as the InternetIp parameter. |
| Os | String | linux | The type of the operating system run by the ECS instance. |
| OsName | String | CentOS 7.6 64-bit | The name of the operating system run by the ECS instance. |
| Region | String | cn-huhehaote-123-323 | The region where the ECS instance is deployed. |
| RegionName | String | China (Hohhot) | The name of the region. |
| Uuid | String | 01111-asdad-assd | The UUID of the ECS instance. |
| VpcInstanceId | String | 13231-331331 | The ID of the VPC. |
| RequestId | String | 92016EC8-D52D-49D8-9FF7-9EA340A950B9 | The ID of the request. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribeAssetDetailByUuids
&Uuids=0687b17f-2a36-4e5c-b3d9
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<DescribeAssetDetailByUuidsResponse>
  <AssetDetail>
        <ClientStatus>online</ClientStatus>
        <Os>linux</Os>
        <InstanceId>1312332131</InstanceId>
        <Ip>10.10.10.10</Ip>
        <OsName>CentOS 7.6 64-bit</OsName>
        <OsDetail>Linux 64bit</OsDetail>
        <IntranetIp>100.10.10.10</IntranetIp>
        <InstanceName>Server 1</InstanceName>
        <AssetType>0</AssetType>
        <Uuid>01111-asdad-assd</Uuid>
        <InternetIp>10.10.10.10</InternetIp>
        <RegionName>China (Hohhot)</RegionName>
        <Region>cn-huhehaote-123-323</Region>
  </AssetDetail>
  <requestId>92016EC8-D52D-49D8-9FF7-9EA340A950B9</requestId>
</DescribeAssetDetailByUuidsResponse>
```

`JSON`  format

```json
{
    "AssetDetail": {
        "ClientStatus": "online",
        "Os": "linux",
        "InstanceId": "1312332131",
        "Ip": "10.10.10.10",
        "OsName": "CentOS 7.6 64bit",
        "OsDetail": "Linux 64bit",
        "IntranetIp": "100.10.10.10",
        "InstanceName": "Server 1",
        "AssetType": "0",
        "Uuid": "01111-asdad-assd",
        "InternetIp": "10.10.10.10",
        "RegionName": "China (Hohhot)",
        "Region": "cn-huhehaote-123-323"    
    },
    "requestId": "92016EC8-D52D-49D8-9FF7-9EA340A950B9"
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-4"></a>

## 3.4. Secure score

<a id="section-3-4-1"></a>

### 3.4.1. DescribeSecureSuggestion

Queries detailed suggestions about how to manage the security risks related to the security score.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeSecureSu ggestion | The operation that you want to perform.<br>Set the value to DescribeSecureSuggestion. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Lang | String | No | zh | The natural language of the request and response.<br>Valid values:<br>• zh: Chinese<br>• en: English |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | F35F45B0-5D6B-4238-BE02-A62D0760E840 | The ID of the request. |
| Suggestions | Array |  | The list of risk management suggestions. |
| Detail | Array |  | The details of the suggestion for security risk mitigation. |
| Description | String | You have four ApsaraDB for RDS instances at risk. | The description of the suggestion for security risk mitigation. |
| SubType | String | CLOUD_HC_RDS | The type of the unhandled security risk. |
| Title | String | The check on security policies of ApsaraDB for RDS instances has failed.The instances are at risk. | The name of the unhandled security risk. |
| Points | Integer | 40 | The penalty points of each item. |
| SuggestType | String | SS_ALARM | The type of the unhandled security risk.<br>Valid values:<br>• SS_REINFORCE: Key features, such as the anti-virus feature, are not configured.<br>• SS_ALARM: unhandled alerts.<br>• SS_VUL: unhandled vulnerabilities.<br>• SS_HC: baseline check risks.<br>• SS_AK: AccessKey pair leaks.<br>• SS_CLOUD_HC: configuration risks in Alibaba Cloud services.<br>• OTHER: other risks. |
| TotalCount | Integer | 15 | The total number of unhandled security risks. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribeSecureSuggestion
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<DescribeSecureSuggestionResponse>
  <Suggestions>
        <Points>40</Points>
        <SuggestType>SS_ALARM</SuggestType>
        <Detail>
              <Description>You have 691 security alerts, which affects 56 assets.</Description>
              <SubType>ALARM_HIGH</SubType>
              <Title>You have unhandled high-risk alerts</Title>
        </Detail>
        <Detail>
              <Description>You have 501 security alerts, which affects 119 assets.</Description>
              <SubType>ALARM_MEDIUM</SubType>
              <Title>You have unhandled middle-risk alerts</Title>
        </Detail>
  </Suggestions>
  <Suggestions>
        <Points>12</Points>
        <SuggestType>SS_VUL</SuggestType>
        <Detail>
              <Description>You have five vulnerabilities.</Description>
              <SubType>VUL_CMS</SubType>
              <Title>You have unhandled CMS vulnerabilities</Title>
        </Detail>
        <Detail>
              <Description>You have 107 vulnerabilities, which affects 68 servers.</Description>
              <SubType>VUL_WIN</SubType>
              <Title>You have unhandled Windows host vulnerabilities</Title>
        </Detail>
        <Detail>
              <Description>You have 701 vulnerabilities, which affects 87 servers.</Description>
              <SubType>VUL_LINUX</SubType>
              <Title>You have unhandled Linux host vulnerabilities</Title>
        </Detail>
        <Detail>
              <Description>You have one unhandled emergency vulnerability.</Description>
              <SubType>VUL_EMR_UNFIX</SubType>
              <Title>You have unhandled emergency vulnerabilities</Title>
        </Detail>
  </Suggestions>
  <Suggestions>
        <Points>2</Points>
        <SuggestType>SS_HC</SuggestType>
        <Detail>
              <Description>You have 46 baseline check risks, which affects 260 servers.</Description>
              <SubType>HC_WARN</SubType>
              <Title>You have unhandled baseline risks</Title>
        </Detail>
  </Suggestions>
  <Suggestions>
        <Points>30</Points>
        <SuggestType>SS_AK</SuggestType>
        <Detail>
              <Description>You have 12 AccessKey pair leaks.</Description>
              <SubType>ACCESSKEY_LEAK</SubType>
              <Title>You have potential AccessKey pair leaks</Title>
        </Detail>
  </Suggestions>
  <Suggestions>
        <Points>35</Points>
        <SuggestType>SS_CLOUD_HC</SuggestType>
        <Detail>
              <Description>You have four ApsaraDB for RDS instances at risk.</Description>
              <SubType>CLOUD_HC_RDS</SubType>
              <Title>The check on security policies of ApsaraDB for RDS instances failed. The instances are at risk</Title>
        </Detail>
        <Detail>
              <Description>You have three unhandled high configuration risks for Alibaba Cloud services.</Description>
              <SubType>CLOUD_HC_HIGH_LEVEL</SubType>
              <Title>You have high configuration risks for Alibaba Cloud services</Title>
        </Detail>
        <Detail>
              <Description>You have 28 unhandled medium or low configuration risks for Alibaba Cloud services.</Description>
              <SubType>CLOUD_HC_OTHER_LEVEL</SubType>
              <Title>You have medium or low configuration risks for Alibaba Cloud services</Title>
        </Detail>
  </Suggestions>
  <Suggestions>
        <Points>5</Points>
        <SuggestType>OTHER</SuggestType>
        <Detail>
              <Description>You have been attacked 5,767 times.</Description>
              <SubType>OTHER_ATTACH</SubType>
              <Title>You are under attack</Title>
        </Detail>
  </Suggestions>
  <TotalCount>12</TotalCount>
  <requestId>F35F45B0-5D6B-4238-BE02-A62D0760E840</requestId>
</DescribeSecureSuggestionResponse>
```

`JSON`  format

```json
{
    "Suggestions": [{
        "Points": 40,
        "SuggestType": "SS_ALARM",
        "Detail": [{
            "Description": "You have 691 security alerts, which affects 56 assets",
            "SubType": "ALARM_HIGH",
            "Title": "You have unhandled high-risk alerts"
        }, {
            "Description": "You have 501 security alerts, which affects 119 assets",
            "SubType": "ALARM_MEDIUM",
            "Title": "You have unhandled medium-risk alerts"
        }]
    }, {
        "Points": 12,
        "SuggestType": "SS_VUL",
        "Detail": [{
            "Description": "You have five vulnerabilities",
            "SubType": "VUL_CMS",
            "Title": "You have unhandled CMS vulnerabilities."
        }, {
            "Description": "You have 107 vulnerabilities, which affects 68 servers",
            "SubType": "VUL_WIN",
            "Title": "You have unhandled Windows host vulnerabilities"
        }, {
            "Description": "You have 701 vulnerabilities, which affects 87 servers",
            "SubType": "VUL_LINUX",
            "Title": "You have unhandled Linux host vulnerabilities"
        }, {
            "Description": "You have one unhandled emergency vulnerability",
            "SubType": "VUL_EMR_UNFIX",
            "Title": "You have unhandled emergency vulnerabilities"
        }]
    }, {
        "Points": 2,
        "SuggestType": "SS_HC",
        "Detail": [{
            "Description": "You have 46 baseline check risks, which affects 260 servers",
            "SubType": "HC_WARN",
            "Title": "You have baseline check risks"
        }]
    }, {
        "Points": 30,
        "SuggestType": "SS_AK",
        "Detail": [{
            "Description": "You have 12 potential AccessKey pair leaks",
            "SubType": "ACCESSKEY_LEAK",
            "Title": "You have potential AccessKey pair leaks"
        }]
    }, {
        "Points": 35,
        "SuggestType": "SS_CLOUD_HC",
        "Detail": [{
            "Description": "You have four ApsaraDB for RDS instances at risk",
            SubType: CLOUD_HC_RDS,
            "Title": "The check on security policies of ApsaraDB for RDS instances has failed. The instances are at risk"
        }, {
            "Description": "You have three high configuration risks for Alibaba Cloud services",
            "SubType": "CLOUD_HC_HIGH_LEVEL",
            "Title": "You have high configuration risks for Alibaba Cloud services"
        }, {
            "Description": "You have 28 medium or low configuration risks for Alibaba Cloudservices",
            "SubType": "CLOUD_HC_OTHER_LEVEL",
            "Title": "You have medium or low configuration risks for Alibaba Cloud services
"
        }]
    }, {
        "Points": 5,
        "SuggestType": "OTHER",
        "Detail": [{
            "Description": "You have been attacked 5,767 times",
            "SubType": "OTHER_ATTACH",
            "Title": "You are under attack"
        }]
    }],
    "TotalCount": 12,
    "requestId": "F35F45B0-5D6B-4238-BE02-A62D0760E840"
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-5"></a>

## 3.5. Security alerts

<a id="section-3-5-1"></a>

### 3.5.1. HandleSecurityEvents

Handles alerts.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| SecurityEventIds.N | RepeatLi st | No | \["909361"\] | The ID of the alert. |
| OperationCode | String | No | ignore | The operation that is performed to handle alerts of the same type at a time. Valid values:<br>• deal: quarantines the source file of the malicious process.<br>• kill_and_quara: kills the malicious process and quarantines the source file.<br>• kill_virus: deletes the source file of the malicious process.<br>• block_ip: blocks the source IP addresses.<br>• ignore: ignores the alerts.<br>• mark_mis_info: marks the alerts as false positives by adding them to the whitelist.<br>• rm_mark_mis_info: cancels false positives by removing the alerts from the whitelist.<br>• offline_handled: marks the alerts as handled. |
| OperationParams | String | No | {"expireTime":15 78475919533} | The parameter values of the operation that is performed to handle alerts of the same type at a time.<br>This parameter must be specified if the OperationCode parameter is set to the following values:<br><code>kill_and_quara</code><br><code>block_ip</code> |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | D929B6F9-EE5E-4F26-A22F-65D4088B6F24 | The ID of the request. |
| HandleSecurityE ventsResponse | Struct |  | The response of the processing result. |
| TaskId | Long | 3187 | The ID of the task to handle the alerts. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=HandleSecurityEvents
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<HandleSecurityEventsResponse>
    <TaskId>3817</TaskId>
</HandleSecurityEventsResponse>
<requestId>D929B6F9-EE5E-4F26-A22F-65D4088B6F24</requestId>
```

`JSON`  format

```json
{
    "HandleSecurityEventsResponse": {
            "TaskId": 3817
    },
    "requestId": "D929B6F9-EE5E-4F26-A22F-65D4088B6F24"
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-5-2"></a>

### 3.5.2. DescribeSecurityStatInfo

Queries the statistics on each security check item and the daily statistics in the trend chart based on each security check item.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeSecurityS tatInfo | The operation that you want to perform.<br>Set the value to DescribeSecurityStatInfo. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Lang | String | No | zh | The natural language of the request and response. Valid values:<br>• zh: Chinese<br>• en: English |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| AttackEvent | Struct |  | The detailed attack statistics. |
| DateArray | List | \["2020-01-04", "2020-01-05", "2020-01-06", "2020-01-07", "2020-01-08", "2020-01-09", "2020-01-10"\] | The time points when attack data is collected in the trend chart. |
| TotalCount | Integer | 1096 | The number of attacks detected on the current day. |
| ValueArray | List | \[2620, 10405, 2377, 2411, 11146, 2057, 1096\] | The number of attacks at each time point. |
| HealthCheck | Struct |  | The detailed statistics on baseline risks. |
| DateArray | List | \["2020-01-04", "2020-01-05", "2020-01-06", "2020-01-07", "2020-01-08", "2020-01-09", "2020-01-10"\] | The time points when baseline risk data is collected in the trend chart. |
| HighCount | Integer | 10 | The number of high-level baseline risks on the current day. |
| HighList | List | \[11, 11, 11, 10, 10, 10, 10\] | The number of high-level baseline risks at each time point. |
| LevelsOn | List | \[ "high", "low", "medium" \] | The list of baseline risk levels. Valid values:<br>• high<br>• medium<br>• low |
| LowCount | Integer | 0 | The number of low-level baseline risks on the current day. |
| LowList | List | \[0, 0, 0, 0, 0, 0, 0\] | The number of low-level baseline risks at each time point. |
| MediumCount | Integer | 21 | The number of medium-level baseline risks on the current day. |
| MediumList | List | \[21, 21, 21, 21, 21, 21, 21\] | The number of medium-level baseline risks at each time point. |
| TotalCount | Integer | 32 | The total number of baseline risks on the current day. |
| ValueArray | List | \[32, 32, 32, 31, 31, 31, 31\] | The total number of baseline risks at each time point. |
| RequestId | String | A3E61730-85E2-4789-8017-B9B1B70F0568 | The ID of the request. |
| SecurityEvent | Struct |  | The details of pending alerts. |
| DateArray | List | \["2020-01-04", "2020-01-05", "2020-01-06", "2020-01-07", "2020-01-08", "2020-01-09", "2020-01-10"\] | The time points when data of pending alerts is collected in the trend chart. |
| LevelsOn | List | \["remind", "suspicious", "serious"\] | The level of the pending alerts. Valid values:<br>• remind<br>• suspicious<br>• serious |
| RemindCount | Integer | 0 | The number of remind alerts on the current day. |
| RemindList | List | \[5, 5, 0, 0, 0, 0, 0\] | The number of remind alerts at each time point. |
| SeriousCount | Integer | 404 | The number of serious alerts on the current day. |
| SeriousList | List | \[315, 350, 336, 378, 384, 398, 404\] | The number of serious alerts at each time point. |
| SuspiciousCoun t | Integer | 148 | The number of suspicious alerts on the current day. |
| SuspiciousList | List | \[124, 133, 111, 123, 135, 145, 148\] | The number of suspicious alerts at each time point. |
| TotalCount | Integer | 552 | The total number of pending alerts on the current day. |
| ValueArray | List | \[444, 488, 447, 501, 519, 543, 552\] | The number of pending alerts at each time point. |
| Success | Boolean | true | The status of the request. Valid values:<br>• true: The request succeeded.<br>• false: The request failed. |
| Vulnerability | Struct |  | The detailed statistics on pending vulnerabilities. |
| AsapCount | Integer | 109 | The number of high-risk pending vulnerabilities on the current day. |
| AsapList | List | \[60, 65, 63, 97, 103, 109, 109\] | The number of high-risk pending vulnerabilities at each time point. |
| DateArray | List | \["2020-01-04", "2020-01-05", "2020-01-06", "2020-01-07", "2020-01-08", "2020-01-09", "2020-01-10"\] | The time points when data of pending vulnerabilities is collected in the trend chart. |
| LaterCount | Integer | 275 | The number of medium-risk pending vulnerabilities on the current day. |
| LaterList | List | \[0, 0, 0, 0, 0, 275, 275\] | The number of medium-risk pending vulnerabilities at each time point. |
| LevelsOn | List | \["asap", "later","Nntf"\] | The risk level of the pending vulnerabilities.Valid values:<br>• asap : high-risk<br>• later : medium-risk<br>• Nntf : low-risk |
| NntfCount | Integer | 0 | The number of low-risk pending vulnerabilities on the current day. |
| NntfList | List | \[0, 0, 0, 0, 0, 0, 0\] | The number of low-risk pending vulnerabilities at each time point. |
| TotalCount | Integer | 384 | The number of pending vulnerabilities on the current day. |
| ValueArray | List | \[60, 65, 63, 97, 103, 384, 384\] | The number of pending vulnerabilities at each time point. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribeSecurityStatInfo
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<DescribeSecurityStatInfoResponse>
      <SecurityEvent>
            <SuspiciousList>124</SuspiciousList>
            <SuspiciousList>133</SuspiciousList>
            <SuspiciousList>111</SuspiciousList>
            <SuspiciousList>123</SuspiciousList>
            <SuspiciousList>135</SuspiciousList>
            <SuspiciousList>145</SuspiciousList>
            <SuspiciousList>148</SuspiciousList>
            <LevelsOn>remind</LevelsOn>
            <LevelsOn>suspicious</LevelsOn>
            <LevelsOn>serious</LevelsOn>
            <TotalCount>552</TotalCount>
            <SuspiciousCount>148</SuspiciousCount>
            <SeriousList>315</SeriousList>
            <SeriousList>350</SeriousList>
            <SeriousList>336</SeriousList>
            <SeriousList>378</SeriousList>
            <SeriousList>384</SeriousList>
            <SeriousList>398</SeriousList>
            <SeriousList>404</SeriousList>
            <RemindCount>0</RemindCount>
            <ValueArray>444</ValueArray>
            <ValueArray>488</ValueArray>
            <ValueArray>447</ValueArray>
            <ValueArray>501</ValueArray>
            <ValueArray>519</ValueArray>
            <ValueArray>543</ValueArray>
            <ValueArray>552</ValueArray>
            <SeriousCount>404</SeriousCount>
            <RemindList>5</RemindList>
            <RemindList>5</RemindList>
            <RemindList>0</RemindList>
            <RemindList>0</RemindList>
            <RemindList>0</RemindList>
            <RemindList>0</RemindList>
            <RemindList>0</RemindList>
            <DateArray>2020-01-04</DateArray>
            <DateArray>2020-01-05</DateArray>
            <DateArray>2020-01-06</DateArray>
            <DateArray>2020-01-07</DateArray>
            <DateArray>2020-01-08</DateArray>
            <DateArray>2020-01-09</DateArray>
            <DateArray>2020-01-10</DateArray>
      </SecurityEvent>
      <HealthCheck>
            <LevelsOn>high</LevelsOn>
            <LevelsOn>low</LevelsOn>
            <LevelsOn>medium</LevelsOn>
            <TotalCount>31</TotalCount>
            <HighList>11</HighList>
            <HighList>11</HighList>
            <HighList>11</HighList>
            <HighList>10</HighList>
            <HighList>10</HighList>
            <HighList>10</HighList>
            <HighList>10</HighList>
            <HighCount>10</HighCount>
            <LowList>0</LowList>
            <LowList>0</LowList>
            <LowList>0</LowList>
            <LowList>0</LowList>
            <LowList>0</LowList>
            <LowList>0</LowList>
            <LowList>0</LowList>
            <MediumList>21</MediumList>
            <MediumList>21</MediumList>
            <MediumList>21</MediumList>
            <MediumList>21</MediumList>
            <MediumList>21</MediumList>
            <MediumList>21</MediumList>
            <MediumList>21</MediumList>
            <LowCount>0</LowCount>
            <ValueArray>32</ValueArray>
            <ValueArray>32</ValueArray>
            <ValueArray>32</ValueArray>
            <ValueArray>31</ValueArray>
            <ValueArray>31</ValueArray>
            <ValueArray>31</ValueArray>
            <ValueArray>31</ValueArray>
            <MediumCount>21</MediumCount>
            <DateArray>2020-01-04</DateArray>
            <DateArray>2020-01-05</DateArray>
            <DateArray>2020-01-06</DateArray>
            <DateArray>2020-01-07</DateArray>
            <DateArray>2020-01-08</DateArray>
            <DateArray>2020-01-09</DateArray>
            <DateArray>2020-01-10</DateArray>
      </HealthCheck>
      <Vulnerability>
            <LevelsOn>asap</LevelsOn>
            <LevelsOn>later</LevelsOn>
            <TotalCount>384</TotalCount>
            <AsapList>60</AsapList>
            <AsapList>65</AsapList>
            <AsapList>63</AsapList>
            <AsapList>97</AsapList>
            <AsapList>103</AsapList>
            <AsapList>109</AsapList>
            <AsapList>109</AsapList>
            <LaterList>0</LaterList>
            <LaterList>0</LaterList>
            <LaterList>0</LaterList>
            <LaterList>0</LaterList>
            <LaterList>0</LaterList>
            <LaterList>275</LaterList>
            <LaterList>275</LaterList>
            <LaterCount>275</LaterCount>
            <AsapCount>109</AsapCount>
            <NntfList>0</NntfList>
            <NntfList>0</NntfList>
            <NntfList>0</NntfList>
            <NntfList>0</NntfList>
            <NntfList>0</NntfList>
            <NntfList>0</NntfList>
            <NntfList>0</NntfList>
            <ValueArray>60</ValueArray>
            <ValueArray>65</ValueArray>
            <ValueArray>63</ValueArray>
            <ValueArray>97</ValueArray>
            <ValueArray>103</ValueArray>
            <ValueArray>384</ValueArray>
            <ValueArray>384</ValueArray>
            <NntfCount>0</NntfCount>
            <DateArray>2020-01-04</DateArray>
            <DateArray>2020-01-05</DateArray>
            <DateArray>2020-01-06</DateArray>
            <DateArray>2020-01-07</DateArray>
            <DateArray>2020-01-08</DateArray>
            <DateArray>2020-01-09</DateArray>
            <DateArray>2020-01-10</DateArray>
      </Vulnerability>
      <AttackEvent>
            <TotalCount>1096</TotalCount>
            <ValueArray>2620</ValueArray>
            <ValueArray>10405</ValueArray>
            <ValueArray>2377</ValueArray>
            <ValueArray>2411</ValueArray>
            <ValueArray>11146</ValueArray>
            <ValueArray>2057</ValueArray>
            <ValueArray>1096</ValueArray>
            <DateArray>2020-01-04</DateArray>
            <DateArray>2020-01-05</DateArray>
            <DateArray>2020-01-06</DateArray>
            <DateArray>2020-01-07</DateArray>
            <DateArray>2020-01-08</DateArray>
            <DateArray>2020-01-09</DateArray>
            <DateArray>2020-01-10</DateArray>
      </AttackEvent>
      <requestId>9C92EF15-B9F7-4DCF-BCE3-5B2B85927744</requestId>
      <success>true</success>
</DescribeSecurityStatInfoResponse>
```

`JSON`  format

```json
{
        "SecurityEvent": {
            "SuspiciousList": [
                124,
                133,
                111,
                123,
                135,
                145,
                148
            ],
            "LevelsOn": [
                "remind",
                "suspicious",
                "serious"
            ],
            "TotalCount": 552,
            "SuspiciousCount": 148,
            "SeriousList": [
                315,
                350,
                336,
                378,
                384,
                398,
                404
            ],
            "RemindCount": 0,
            "ValueArray": [
                444,
                488,
                447,
                501,
                519,
                543,
                552
            ],
            "SeriousCount": 404,
            "RemindList": [
                5,
                5,
                0,
                0,
                0,
                0,
                0
            ],
            "DateArray": [
                "2020-01-04",
                "2020-01-05",
                "2020-01-06",
                "2020-01-07",
                "2020-01-08",
                "2020-01-09",
                "2020-01-10"
            ]
        },
        "HealthCheck": {
            "LevelsOn": [
                "high",
                "low",
                "medium"
            ],
            "TotalCount": 31,
            "HighList": [
                11,
                11,
                11,
                10,
                10,
                10,
                10
            ],
            "HighCount": 10,
            "LowList": [
                0,
                0,
                0,
                0,
                0,
                0,
                0
            ],
            "MediumList": [
                21,
                21,
                21,
                21,
                21,
                21,
                21
            ],
            "LowCount": 0,
            "ValueArray": [
                32,
                32,
                32,
                31,
                31,
                31,
                31
            ],
            "MediumCount": 21,
            "DateArray": [
                "2020-01-04",
                "2020-01-05",
                "2020-01-06",
                "2020-01-07",
                "2020-01-08",
                "2020-01-09",
                "2020-01-10"
            ]
        },
        "Vulnerability": {
            "LevelsOn": [
                "asap",
                "later"
            ],
            "TotalCount": 384,
            "AsapList": [
                60,
                65,
                63,
                97,
                103,
                109,
                109
            ],
            "LaterList": [
                0,
                0,
                0,
                0,
                0,
                275,
                275
            ],
            "LaterCount": 275,
            "AsapCount": 109,
            "NntfList": [
                0,
                0,
                0,
                0,
                0,
                0,
                0
            ],
            "ValueArray": [
                60,
                65,
                63,
                97,
                103,
                384,
                384
            ],
            "NntfCount": 0,
            "DateArray": [
                "2020-01-04",
                "2020-01-05",
                "2020-01-06",
                "2020-01-07",
                "2020-01-08",
                "2020-01-09",
                "2020-01-10"
            ]
        },
        "AttackEvent": {
            "TotalCount": 1096,
            "ValueArray": [
                2620,
                10405,
                2377,
                2411,
                11146,
                2057,
                1096
            ],
            "DateArray": [
                "2020-01-04",
                "2020-01-05",
                "2020-01-06",
                "2020-01-07",
                "2020-01-08",
                "2020-01-09",
                "2020-01-10"
            ]
        },
        "requestId": "9C92EF15-B9F7-4DCF-BCE3-5B2B85927744",
        "success": true
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-5-3"></a>

### 3.5.3. DescribeAlarmEventList

Queries alert events on the Alerts page. An alert event consists of alerts and exceptions. Each alert event is related to multiple exceptions.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeAlarmEve ntList | The operation that you want to perform. Set the value to DescribeAlarmEventList. |
| CurrentPage | Integer | Yes | 1 | The page number of the current page.Pages start from page 1. Default value: 1. |
| From | String | Yes | sas | The ID of the request source. Set the value to sas. |
| PageSize | String | Yes | 20 | The number of entries to return on each page. Default value: 20. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Lang | String | No | zh | The natural language of the request and response. Valid values:<br>• zh: Chinese<br>• en: English |
| Dealed | String | No | Y | The status of the alert event. Valid values:<br>• N: unhandled<br>• Y: handled |
| Levels | String | No | serious | The severity levels of the alert events.Separate multiple levels with commas (,). Valid values:<br>• serious<br>• suspicious<br>• remind |
| Remark | String | No | database_server | The name of the alert, or the asset information. |
| GroupId | String | No | tst\*\*\* | The group ID of the affected asset. |
| AlarmEventName | String | No | DDoS trojans | The name of the alert event. |
| AlarmEventType | String | No | Malicious process (cloud threat detection) | The type of the alert event. |
| OperateErrorCode List.N | RepeatLi st | No | ignore. Success | Alert handling result code N. The value is in the format of Operation type.Operation result code.<br>Operation types include:<br>• Common: performs common operations.<br>• deal: handles the alert.<br>• ignore: ignores the alert.<br>• offline_handled: marks the alert as handled.<br>• mark_mis_info: marks the alerts as false positives by adding them to the whitelist.<br>• rm_mark_mis_info: cancels false positives by removing the alerts from the whitelist.<br>• quara: quarantines the source file of the malicious process.<br>• kill_and_quara: kills the malicious process and quarantines the source file.<br>• kill_virus: deletes the source file of the malicious process.<br>• block_ip: blocks the source IP addresses.<br>• manual_handled: manually handles the alert.<br>Operation result codes:<br>• Success: The operation is successful.<br>• Failure: The operation fails.<br>• AgentOffline: The agent is offline. |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | 28267723-D857-4DD8-B295-013100000000 | The ID of the request. |
| SuspEvents | Array |  | The information about the alert event. |
| AlarmUniqueInf o | String | 8df914418f4211fbf 756efe7a6f40cbc | The ID of the alert event. |
| Solution | String | Check the malicious URLs that have been listed in the alert.Check the directory for malicious files.Terminate the malicious processes.If you manually run the processes, you can mark them as false positives in the console. | The solution to handle the alert event. |
| Level | String | serious | The severity level of the alert event. Valid values:<br>• serious<br>• suspicious<br>• remind |
| CanBeDealOnLin e | Boolean | true | Indicates whether the online processing of the alert event is supported, such as quarantining the source file of the malicious process, adding the alert event to the whitelist, and ignoring the alert event.<br>• true: Online processing is supported.<br>• false: Online processing is not supported. |
| Description | String | After an attacker accesses a victim server, to keep the malicious programs running, the attacker may have imported malicious shell scripts into scheduled tasks such as crontab and systemd. | The description of the alert event. |
| StartTime | Long | 1543740301000 | The time when the alert event starts. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC. |
| EndTime | Long | 1543740301000 | The time when the alert event ends. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC. |
| AlarmEventTyp e | String | Suspicious processes | The type of the alert event. |
| SuspiciousEvent Count | Integer | 1 | The number of exceptions related to the alert event. |
| Uuid | String | 47900178-885d-4fa4-9d77-\*\*\* | The ID of the related asset. |
| InstanceName | String | Test server | The name of the affected asset. |
| InternetIp | String | 1.2.3.4 | The public IP address of the affected asset. |
| IntranetIp | String | 1.2.3.5 | The private IP address of the affected asset. |
| AlarmEventNa me | String | Running malicious commands | The name of the alert event. |
| SaleVersion | String | 1 | The version in which the alert event detection can be enabled. Valid values:<br>• 0: Basic Edition<br>• 1: Enterprise Edition |
| DataSource | String | aegis_\*\*\* | The source of data. |
| CanCancelFault | Boolean | false | Indicates whether you can cancel marking this alert event as a false positive. |
| Dealed | Boolean | false | Indicates whether the alert has been handled. Valid values:<br>• true: handled<br>• false: unhandled |
| GmtModified | Long | 1569235879000 | The last time when the alert was triggered.This value is a UNIX timestamp representing the number of milliseconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC. |
| HasTraceInfo | Boolean | true | Indicates whether the alert has trace information.<br>• true: The alert has trace information.<br>• false: The alert does not have trace information. |
| SecurityEventId s | String | 270789 | The ID of the related exception. |
| OperateErrorCo de | String | kill_and_quara.Succe ss | The handling result code of the alert event. |
| AlarmEventNa meOriginal | String | Precise defense against malicious commands | The original parent name of the alert event. |
| InstanceId | String | i-e\*\*\* | The ID of the affected asset. |
| PageInfo | Struct |  | The page information. |
| Count | Integer | 1 | The number of entries returned on the current page. |
| PageSize | Integer | 20 | The number of entries returned per page. |
| TotalCount | Integer | 1 | The total number of the alert events. |
| CurrentPage | Integer | 1 | The page number of the current page. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribeAlarmEventList
&CurrentPage=1
&From=sas
&PageSize=20
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<DescribeAlarmEventList>
  <RequestId>1D7FB2DD-4B80-41F4-94CF-C484EF6A5CAC</RequestId>
  <PageInfo>
        <Count>1</Count>
        <TotalCount>58</TotalCount>
        <PageSize>1</PageSize>
        <CurrentPage>1</CurrentPage>
  </PageInfo>
  <SuspEvents>
        <Uuid>c4678332-ef35-4ad4-8358-681ebbc0ccab</Uuid>
        <Dealed>true</Dealed>
        <SecurityEventIds>261401</SecurityEventIds>
        <Description>Cloud threat detection (mining programs)</Description>
        <CanCancelFault>false</CanCancelFault>
        <InstanceId>i-bp***</InstanceId>
        <OperateErrorCode></OperateErrorCode>
        <InternetIp>1.2.3.5</InternetIp>
        <GmtModified>1572524936000</GmtModified>
        <SuspiciousEventCount>1</SuspiciousEventCount>
        <HasTraceInfo>false</HasTraceInfo>
        <AlarmUniqueInfo>8b59e7bd134797758709983c26ece2a2</AlarmUniqueInfo>
        <AlarmEventName>Mining programs</AlarmEventName>
        <AlarmEventType>Precise defense</AlarmEventType>
        <IntranetIp>1.2.3.4</IntranetIp>
        <Level>serious</Level>
        <EndTime>1572524936000</EndTime>
        <StartTime>1572524936000</StartTime>
        <AlrmEventNameOriginal>Precise defense against mining programs</AlarmEventNameOriginal>
        <SaleVersion>0</SaleVersion>
        <CanBeDealOnLine>false</CanBeDealOnLine>
        <InstanceName>cit***</InstanceName>
  </SuspEvents>
</DescribeAlarmEventList>
```

`JSON`  format

```json
{
    "RequestId": "1D7FB2DD-4B80-41F4-94CF-C484EF6A5CAC",
    "PageInfo": {
        "Count": 1,
        "TotalCount": 58,
        "PageSize": 1,
        "CurrentPage": 1
    },
    "SuspEvents": [
        {
            "Uuid": "c4678332-ef35-4ad4-8358-681ebbc0ccab",
            "Dealed": true,
            "SecurityEventIds": "261401",
            "Description": "Cloud threat detection (mining programs)",
            "CanCancelFault": false,
            "InstanceId": "i-bp***",
            "OperateErrorCode": "",
            "InternetIp": "1.2.3.5",
            "GmtModified": 1572524936000,
            "SuspiciousEventCount": 1,
            "HasTraceInfo": false,
            "AlarmUniqueInfo": "8b59e7bd134797758709983c26ece2a2",
            "AlarmEventName": "Mining programs",
            "AlarmEventType": "Precise defense",
            "IntranetIp": "1.2.3.4",
            "Level": "serious",
            "EndTime": 1572524936000,
            "StartTime": 1572524936000,
            "AlarmEventNameOriginal": "Precise defense against mining programs",
            "SaleVersion": "0",
            "CanBeDealOnLine": false,
            "InstanceName": "cit***"
        }
    ]
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-5-4"></a>

### 3.5.4. DescribeAlarmEventDetail

Queries details of an alert event. An alert event consists of alerts and exceptions. Each alert event contains multiple exceptions.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeAlarmEve ntDetail | The operation that you want to perform.<br>Set the value to DescribeAlarmEventDetail. |
| AlarmUniqueInfo | String | Yes | 8df914418f4211f bf756efe7a6f40c bc | The ID of the alert event.<br>Note To query details of an alert event, you must specify the ID of the alert event. You can call the DescribeAlarmEventList operation to obtain the ID. |
| From | String | Yes | sas | The ID of the request source. Set the value to sas. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Lang | String | No | zh | The natural language of the request and response. Valid values:<br>• zh: Chinese<br>• en: English |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| Data | Struct |  | The details of the alert event. |
| AlarmEventAlia sName | String | Suspicious process behavior-execution of suspicious commands in scheduled Linux tasks | The complete name of the alert event. |
| AlarmEventDes c | String | After an attacker accesses a victim server, to keep the malicious programs running, the attacker may have imported malicious shell scripts into scheduled tasks such as crontab and systemd. | The description of the alert event. |
| AlarmUniqueInf o | String | 8df914418f4211fbf 756efe700000000 | The ID of the alert event. |
| CanBeDealOnLin e | Boolean | false | Indicates whether processing alert events online is supported, such as blocking an alert, adding an alert to the whitelist, and ignoring an alert. Valid values:<br>• true: Online processing is supported.<br>• false: Online processing is not supported. |
| CanCancelFault | Boolean | false | Indicates whether you can cancel labelling this alert event as a false positive. Valid values:<br>• true: You can cancel labeling this alert event as a false positive.<br>• false: You cannot cancel labeling this alert event as a false positive. |
| CauseDetails | Array |  | The cause of the alert event (the information used to trace the alert). |
| Key | String | item | The format of the text. Valid values:<br>• text<br>• html |
| Value | Array |  | The value of the field displaying the information used to trace alerts. |
| Name | String | Solutions | The key of the field displaying the information used to trace alerts. |
| Type | String | html | The format of the field displaying the information used to trace alerts. |
| Value | String | Check for the exploited pages of your Web services and vulnerabilities in parameter configuration, and resolve these issues. | The value of the field displaying the information used to trace alerts. |
| DataSource | String | aegis_\*\*\* | The source of data. |
| EndTime | Long | 1542366542000 | The end time of the alert event. |
| InstanceName | String | Test server | The name of the associated instance. |
| InternetIp | String | 1.2.3.1 | The public IP address of the associated instance. |
| IntranetIp | String | 1.2.3.5 | The private IP address of the associated instance. |
| Level | String | serious | The level of the alert event. Valid values:<br>• serious<br>• suspicious<br>• remind |
| Solution | String | Check the malicious URLs that have been listed in the alert.Check the directory for malicious file downloads. Stop the malicious processes that are running. If you trust the processes, mark the alert as a false positive in the console, and submit a ticket to security engineers. | The solution to the alert event. |
| StartTime | Long | 1542378601000 | The timestamp when the alert event was detected. |
| Type | String | Suspicious network connections | The type of the alert event. |
| Uuid | String | 47900178-885d-4fa4-9d77-XXXXXXXXXXXX | The ID of the related instance. |
| RequestId | String | 5A1DDB3C-798C-4A84-BF6E-3DC700000000 | The ID of the request. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribeAlarmEventDetail
&AlarmUniqueInfo=8df914418f4211fbf756efe7a6f40cbc
&From=sas
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<DescribeAlarmEventDetailResponse>
  <Data>
        <Uuid>47900178-885d-4fa4-9d77-XXXXXXXXXXXX</Uuid>
        <AlarmEventAliasName>Suspicious Process - Command Exceptions in Scheduled Linux Tasks</AlarmEventAliasName>
        <Type>Suspicious process behavior</Type>
        <InternetIp>1.2.3.1</InternetIp>
        <AlarmEventDesc>After accessing a victim server, the attacker may have imported malicious shell scripts into scheduled tasks such as crontab and systemd, to enable persistentexecution of malicious backdoor programs. </AlarmEventDesc>
        <IntranetIp>1.2.3.5</IntranetIp>
        <CauseDetails>
              <Value>
                    <Type>text</Type>
                    <Value>An attacker has logged on to your server and has written webshells by editing the configuration file.</Value>
                    <Name>Intrusion cause</Name>
              </Value>
              <Value>
                    <Type>text</Type>
                    <Value>2018-11-16 19:09:02</Value>
                    <Name>Attack time</Name>
              </Value>
              <Value>
                    <Type>text</Type>
                    <Value>N/A</Value>
                    <Name>Source IP of attack</Name>
              </Value>
              <Value>
                    <Type>text</Type>
                    <Value>N/A</Value>
                    <Name>Payload of attack</Name>
              </Value>
              <Value>
                    <Type>text</Type>
                    <Value>Check for the exploited pages of your Web services and vulnerabilities in parameter configuration, and resolve these issues. </Value>
                    <Name>Solutions</Name>
              </Value>
              <Key>item</Key>
        </CauseDetails>
        <Level>serious</Level>
        <EndTime>1543741201000</EndTime>
        <StartTime>1543312803000</StartTime>
        <CanBeDealOnLine>false</CanBeDealOnLine>
        <InstanceName>serve***</InstanceName>
  </Data>
  <RequestId>5A1DDB3C-798C-4A84-BF6E-3DC7F7D7EB4A</RequestId>
</DescribeAlarmEventDetailResponse>
```

`JSON`  format

```json
{
    "Data": {
        "Uuid": "47900178-885d-4fa4-9d77-XXXXXXXXXXXX",
        "AlarmEventAliasName": "Suspicious process behavior-execution of suspicious commands in scheduled Linux tasks",
        "Type": "Suspicious process behavior",
        "InternetIp": "1.2.3.1",
        "AlarmEventDesc": "After an attacker accesses a victim server, to keep the malicious programs running, the attacker may have imported malicious shell scripts into scheduled tasks such as crontab and systemd.",
        "IntranetIp": "1.2.3.5",
        "CauseDetails": [
            {
                "Value": [
                    {
                        "Type": "text",
                        "Value": "An attacker has logged on to your ECS instance and has written webshells by editing files.",
                        "Name": "Intrusion cause"
                    },
                    {
                        "Type": "text",
                        "Value": "2018-11-16 19:09:02",
                        "Name": "Time of attack"
                    },
                    {
                        "Type": "text",
                        "Value": "N/A",
                        "Name": "Source IP of attack"
                    },
                    {
                        "Type": "text",
                        "Value": "N/A",
                        "Name": "Payload of attack"
                    },
                    {
                        "Type": "text",
                        "Value": "Check for the exploited pages of your Web services and vulnerabilities in parameter configuration, and resolve these issues.",
                        "Name": "Solutions"
                    }
                ],
                "Key": "item"
            }
        ],
        "Level": "serious",
        "EndTime": 1543741201000,
        "StartTime": 1543312803000,
        "CanBeDealOnLine": false,
        "InstanceName": "serve***"
    },
    "RequestId": "5A1DDB3C-798C-4A84-BF6E-3DC7F7D7EB4A"
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-5-5"></a>

### 3.5.5. DescribeSuspEvents

Queries information about exceptions. An alert event consists of alerts and exceptions. Each alert event is related to multiple exceptions.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeSuspEven ts | The operation that you want to perform.<br>Set the value to DescribeSuspEvents. |
| From | String | Yes | sas | The data source on which the exception is detected. Set the value to sas. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Dealed | String | No | N | The status of the exception. Valid values:<br>• N: unhandled<br>• Y: handled |
| Name | String | No | ecs-xxx | The name of the exception or the affected server. Fuzzy match is supported. |
| Levels | String | No | serious | The severity levels of the alert events.Separate multiple levels with commas (,). The following levels are listed in descending order.<br>• serious<br>• suspicious<br>• remind |
| ParentEventTypes | String | No | Webshells | The type of the alert event to which the exception is related. |
| Remark | String | No | Test server | The IP address or name of the server. |
| PageSize | String | No | 20 | The number of entries to return on each page. Default value: 20. |
| CurrentPage | String | No | 1 | The page number of the current page. |
| Lang | String | No | zh | The natural language of the request and response. Valid values:<br>• zh: Chinese<br>• en: English |
| AlarmUniqueInfo | String | No | 8df914418f4211f bf\*\*\* | The alert event to which the exception is related.<br>Note To query details about exceptions of an alert event, you must provide the ID of the alert event. You can call the DescribeAlarmEventList operation to obtain the ID. |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | 43F670F3-AB40-4E91-BC7D-C57400000000 | The ID of the request. |
| Count | Integer | 1 | The number of entries returned on the current page. |
| PageSize | Integer | 20 | The number of entries returned per page. |
| TotalCount | Integer | 100 | The total number of the exceptions. |
| CurrentPage | Integer | 1 | The page number of the current page. |
| SuspEvents | Array |  | The details of the exception. |
| LastTime | String | 2018-09-26 01:51:01 | The last time when the exception occurred. |
| OccurrenceTim e | String | 2018-09-26 01:51:01 | The first time when the exception occurred. |
| Id | Long | 1000 | The ID of the exception to query. |
| UniqueInfo | String | e17e\*\*\* | The ID of the exception. |
| InstanceName | String | nginx | The name of the related asset. |
| InternetIp | String | 1.2.3.1 | The public IP address of the related asset. |
| IntranetIp | String | 1.2.3.5 | The private IP address of the related asset. |
| Uuid | String | bf6b30d3-eea8-4924-9f0a-\*\*\* | The ID of the related asset. |
| Name | String | Malicious processes (cloud threat detection) - XOR DDoS trojan | The complete name of the exception. |
| EventSubType | String | XorDDoS trojan | The name of the exception. |
| Level | String | serious | The severity level of the exception. Valid values:<br>• serious<br>• suspicious<br>• remind |
| EventStatus | Integer | 1 | The status of the exception. Valid values:<br>• 1: unhandled<br>• 2: ignored<br>• 4: confirmed<br>• 8: marked as false positive<br>• 16: handling<br>• 32: handled<br>• 64: expired |
| Desc | String | webshell | The impact of the exception. |
| OperateMsg | String | success | The operation remarks of the exception. |
| DataSource | String | aegis_suspicious_\*\*\* | The data source. |
| CanBeDealOnLin e | Boolean | true | Indicates whether the online processing of the exception is supported. The processing includes quarantining the exception. Valid values:<br>• true: Online processing is supported.<br>• false: Online processing is not supported. |
| SaleVersion | String | 1 | The version in which the exception detection can be enabled. Valid values:<br>• 0: Basic Edition<br>• 1: Enterprise Edition |
| AlarmEventTyp e | String | Suspicious processes | The type of the alert event. |
| AlarmEventNa me | String | Suspicious command running in scheduled Linux tasks | The name of the alert event. |
| AlarmUniqueInf o | String | 8df914418f\*\*\* | The ID of the alert event. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribeSuspEvents
&From=saas
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<DescribeSuspEvents>
  <TotalCount>3</TotalCount>
  <Count>2</Count>
  <PageSize>20</PageSize>
  <RequestId>0C7FAD74-83FA-4671-9250-A5F2A64F437A</RequestId>
  <CurrentPage>1</CurrentPage>
  <SuspEvents>
        <EventStatus>1</EventStatus>
        <SaleVersion>1</SaleVersion>
        <IntranetIp>1.2.3.4</IntranetIp>
        <EventSubType>XOR DDoS trojan</EventSubType>
        <Name>Malicious processes (cloud threat detection) - XOR DDoS trojan</Name>
        <DataSource>aegis_suspiciou***</DataSource>
        <OccurrenceTime>2018-09-26 01:51:01</OccurrenceTime>
        <InstanceName>server01</InstanceName>
        <Desc>After accessing the server, XOR DDoS trojan may have injected malicious code into Linux scheduled tasks. </Desc>
        <CanBeDealOnLine>false</CanBeDealOnLine>
        <Uuid>bf6b30d3-eea8-4924***</Uuid>
        <InternetIp>1.2.3.4</InternetIp>
        <Level>serious</Level>
        <Id>3682</Id>
        <LastTime>2018-10-24 21:06:01</LastTime>
  </SuspEvents>
  <SuspEvents>
        <EventStatus>1</EventStatus>
        <SaleVersion>1</SaleVersion>
        <IntranetIp>1.2.3.5</IntranetIp>
        <EventSubType>XOR DDoS trojan</EventSubType>
        <Name>Malicious processes (cloud threat detection) - XOR DDoS trojan</Name>
        <DataSource>aegis_suspiciou***</DataSource>
        <OccurrenceTime>2018-09-26 02:01:01</OccurrenceTime>
        <InstanceName>server01</InstanceName>
        <Desc>After accessing the server, XOR DDoS trojan may have injected malicious code into Linux scheduled tasks. </Desc>
        <CanBeDealOnLine>false</CanBeDealOnLine>
        <Uuid>bf6b30d3-eea8-4924-***</Uuid>
        <InternetIp>1.2.3.4</InternetIp>
        <Level>serious</Level>
        <Id>3683</Id>
        <LastTime>2018-10-24 21:01:01</LastTime>
  </SuspEvents>
</DescribeSuspEvents>
```

`JSON`  format

```json
{
    "TotalCount": 3,
    "Count": 2,
    "PageSize": 20,
    "RequestId": "0C7FAD74-83FA-4671-9250-A5F2A64F437A",
    "CurrentPage": 1,
    "SuspEvents": [
        {
            "EventStatus": 1,
            "SaleVersion": "1",
            "IntranetIp": "1.2.3.4",
            "EventSubType": "XOR DDoS trojan"
            "Name": "Malicious processes (cloud threat detection) - XOR DDoS trojan",
            "DataSource": "aegis_suspiciou***",
            "OccurrenceTime": "2018-09-26 01:51:01",
            "InstanceName": "server01",
            "Desc": "After accessing the server, XOR DDoS trojan may have injected malicious code into Linux scheduled tasks.",
            "CanBeDealOnLine": false,
            "Uuid": "bf6b30d3-eea8-4924***",
            "InternetIp": "1.2.3.4",
            "Level": "serious",
            "Id": 3682,
            "LastTime": "2018-10-24 21:06:01"
        },
        {
            "EventStatus": 1,
            "SaleVersion": "1",
            "IntranetIp": "1.2.3.5",
            "EventSubType": "XOR DDoS trojan"
            "Name": "Malicious processes (cloud threat detection) - XOR DDoS trojan",
            "DataSource": "aegis_suspiciou***",
            "OccurrenceTime": "2018-09-26 02:01:01",
            "InstanceName": "server01",
            "Desc": "After accessing the server, XOR DDoS trojan may have injected malicious code into Linux scheduled tasks.",
            "CanBeDealOnLine": false,
            "Uuid": "bf6b30d3-eea8-4924-***",
            "InternetIp": "1.2.3.4",
            "Level": "serious",
            "Id": 3683,
            "LastTime": "2018-10-24 21:01:01"
        }
    ]
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-5-6"></a>

### 3.5.6. DescribeSuspEventDetail

Queries details of a specific exception. An alert event consists of alerts and exceptions. Each alert event is related to multiple exceptions.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeSuspEven tDetail | The operation that you want to perform.<br>Set the value to DescribeSuspEventDetail. |
| From | String | Yes | sas | The data source on which the exception is detected. Set the value to sas. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Lang | String | No | zh | The natural language of the request and response. Valid values:<br>• zh: Chinese<br>• en: English |
| SuspiciousEventId | Integer | No | 1 | The ID of the exception to query.<br>Note To query the details of an exception, you must provide the ID of the exception. You can call the DescribeSuspEvents operation to obtain the ID. |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | 1 | The ID of the request. |
| LastTime | String | 2018-10-30 11:43:46 | The last time when the exception occurred. |
| Id | Integer | 1991 | The ID of the exception to query. |
| InstanceName | String | ca_cpm_test1 | The name of the related asset. |
| InternetIp | String | 1.2.3.5 | The public IP address of the related asset. |
| IntranetIp | String | 1.2.3.1 | The private IP address of the related asset. |
| Uuid | String | bffb12c3-590a-4db2-b538-\*\*\* | The ID of the related asset. |
| EventDesc | String | This file may have been uploaded by an attacker that has intruded into your website. Check the validity of this file. | The description of the exception. |
| EventTypeDesc | String | Webshell - Webshell | The type of the exception. |
| Level | String | serious | The severity level of the exception. Valid values:<br>• serious<br>• suspicious<br>• remind |
| EventStatus | String | 1 | The status of the exception. Valid values:<br>• 1: unhandled<br>• 2: ignored<br>• 4: confirmed<br>• 8: marked as false positive<br>• 16: handling<br>• 32: handled<br>• 64: expired |
| SaleVersion | String | 1 | The version in which exception detection can be enabled. Valid values:<br>• 0: Basic Edition<br>• 1: Enterprise Edition |
| DataSource | String | aegis_suspicious_\*\*\* | The data source on which the exception is detected. |
| OperateMsg | String | success | The operation remarks of the exception. |
| SasId | String | 1sdeswdd\*\*\*\* | The ID of the service in Threat Detection Service. |
| EventName | String | WEBSHELL | The name of the exception. |
| CanBeDealOnLin e | Boolean | true | Indicates whether the online processing of the exception is supported. Valid values:<br>• true: Online processing is supported.<br>• false: Online processing is not supported. |
| Details | Array |  | The details of the exception. |
| Name | String | The update time. | The name in the exception details. |
| Type | String | html | The format in the exception details. Valid values:<br>• text<br>• html |
| InfoType | String | download_url | The type of the icon. |
| Value | String | 2018-12-12 12:00:00 | The content in the exception details. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribeSuspEventDetail
&From=sas
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<DescribeSuspEventDetailResponse>
  <RequestId>43F670F3-AB40-4E91-BC7D-C57468834F67</RequestId>
  <EventDesc>This file may have been uploaded by an attacker that has intruded into your website. Check the validity of this file. </EventDesc>
  <EventTypeDesc>Webshell - Webshell</EventTypeDesc>
  <EventStatus>1</EventStatus>
  <EventName>WEBSHELL</EventName>
  <SaleVersion>1</SaleVersion>
  <IntranetIp>1.2.3.4</IntranetIp>
  <DataSource>aegis_suspicious_***</DataSource>
  <InstanceName>ca_***</InstanceName>
  <CanBeDealOnLine>true</CanBeDealOnLine>
  <OperateMsg></OperateMsg>
  <Uuid>bffb12c3-590a-4db2-b538-***</Uuid>
  <Details>
        <Type>text</Type>
        <Value>/data/ftpUser/pub/***</Value>
        <InfoType>trojan_path</InfoType>
        <Name>Trojan path</Name>
  </Details>
  <Details>
        <Type>text</Type>
        <Value>--</Value>
        <Name>Affected domain</Name>
  </Details>
  <Details>
        <Type>text</Type>
        <Value>2018-10-30 05:00:56</Value>
        <InfoType>frist_found_time</InfoType>
        <Name>First detected time<Name>
  </Details>
  <Details>
        <Type>text</Type>
        <Value>2018-10-30 11:43:45</Value>
        <InfoType>update_time</InfoType>
        <Name>Update time</Name>
  </Details>
  <Details>
        <Type>text</Type>
        <Value>Webshell</Value>
        <InfoType>trojan_type</InfoType>
        <Name>Trojan type</Name>
  </Details>
  <Details>
        <Type>html</Type>
        <Value>&lt;a href="http:// bucket*"&gt; Download&lt;/a&gt;</Value>
        <InfoType>download_url</InfoType>
        <Name>Source file download</Name>
  </Details>
  <InternetIp>1.2.3.5</InternetIp>
  <Level>serious</Level>
  <Id>129636</Id>
  <LastTime>2018-10-30 11:43:46</LastTime>
  <SasId>39938056</SasId>
</DescribeSuspEventDetailResponse>
```

`JSON`  format

```json
{
    "RequestId": "43F670F3-AB40-4E91-BC7D-C57468834F67",
    "EventDesc": "This file may have been uploaded by an attacker that has intruded into your website. Check the validity of this file.",
    "EventTypeDesc": "Webshell - Webshell",
    "EventStatus": 1,
    "EventName": "WEBSHELL",
    "SaleVersion": "1",
    "IntranetIp": "1.2.3.4",
    "DataSource": "aegis_suspicious_***",
    "InstanceName": "ca_***",
    "CanBeDealOnLine": true,
    "OperateMsg": "",
    "Uuid": "bffb12c3-590a-4db2-b538-***",
    "Details": [
        {
            "Type": "text",
            "Value": "/data/ftpUser/pub/***",
            "InfoType": "trojan_path",
            "Name": "Trojan path",
        },
        {
            "Type": "text",
            "Value": "--",
            "Name": "Affected domain",
        },
        {
            "Type": "text",
            "Value": "2018-10-30 05:00:56",
            "InfoType": "frist_found_time",
            "Name": "First detected time",
        },
        {
            "Type": "text",
            "Value": "2018-10-30 11:43:45",
            "InfoType": "update_time",
            "Name": "Update time",
        },
        {
            "Type": "text",
            "Value": "Webshell",
            "InfoType": "trojan_type",
            "Name": "Trojan type",
        },
        {
            "Type": "html",
            "Value": "<a href=\" http:// ${* \"> Download </a>",
            "InfoType": "download_url",
            "Name":"Source file download",
        }
    ],
    "InternetIp": "1.2.3.5",
    "Level": "serious",
    "Id": 129636,
    "LastTime": "2018-10-30 11:43:46",
    "SasId": "39938056"
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-5-7"></a>

### 3.5.7. HandleSimilarSecurityEvents

Handles alerts triggered by the same rule or rules of the same type at a time.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | HandleSimilarSec urityEvents | The operation that you want to perform.<br>Set the value to HandleSimilarSecurityEvents. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| TaskId | Long | No | 113 | The ID of the task that handles multiple alerts of the same type at a time. |
| OperationCode | String | No | ignore | The operation that is performed to handle alerts of the same type at a time. Valid values:<br>• deal: quarantines the source file of the malicious process.<br>• kill_and_quara: kills the malicious processes and quarantines the source file.<br>• kill_virus: removes the source file of the malicious process.<br>• block_ip: blocks the source IP addresses.<br>• ignore: ignores the alerts.<br>• mark_mis_info: marks the alerts as false positives by adding them to the whitelist.<br>• rm_mark_mis_info: cancels false positives by removing the alerts from the whitelist.<br>• offline_handled: marks the alerts as handled. |
| OperationParams | String | No | {"expireTime":15 78475919533} | The parameter values of the operation that is performed to handle alerts of the same type at a time.<br>This parameter must be specified if the OperationCode parameter is set to one of the following values:<br><code>kill_and_quara</code><br><code>block_ip</code> |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | 1B080663-F4E6-4736-89B9-48FC43E160A7 | The ID of the request. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=HandleSimilarSecurityEvents
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<requestId>1B080663-F4E6-4736-89B9-48FC43E160A7</requestId>
```

`JSON`  format

```json
{
  "requestId": "1B080663-F4E6-4736-89B9-48FC43E160A7"
  }
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-5-8"></a>

### 3.5.8. DescribeSecurityEventOperations

Queries operations that can be performed to handle alerts.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeSecurityE ventOperations | The operation that you want to perform.<br>Set the value to DescribeSecurityEventOperations. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| SecurityEventId | Long | No | 89621 | The ID of the alert. |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | F661324F-F381-4218-A0F4-7A901FB39EED | The ID of the request. |
| SecurityEventO perationsRespo nse | Array |  | The operation performed on the alert. |
| OperationCode | String | ignore | The code of the operation performed on the alert. |
| OperationPara ms | String | qqqqq | The operation parameters. |
| UserCanOperat e | Boolean | true | Indicates whether you can handle the alert.<br>Valid values:<br>• true: You can handle the alert.<br>• false: You cannot handle the alert. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribeSecurityEventOperations
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<code>200</code>
<data>
    <SecurityEventOperationsResponse>
        <OperationCode>mark_mis_info</OperationCode>
        <UserCanOperate>true</UserCanOperate>
    </SecurityEventOperationsResponse>
    <SecurityEventOperationsResponse>
        <OperationCode>ignore</OperationCode>
        <UserCanOperate>true</UserCanOperate>
    </SecurityEventOperationsResponse>
</data>
<requestId>F661324F-F381-4218-A0F4-7A901FB39EED</requestId>
```

`JSON`  format

```json
{
  "code": 200,
  "data": {
    "SecurityEventOperationsResponse": [
      {
        "OperationCode": "mark_mis_info",
        "UserCanOperate": true
      },
      {
        "OperationCode": "ignore",
        "UserCanOperate": true
      }
    ]
  },
  "requestId": "F661324F-F381-4218-A0F4-7A901FB39EED"
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-5-9"></a>

### 3.5.9. DescribeSecurityEventOperationStatus

Queries the processing status of alerts that are triggered by the same rule or rules of the same type.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeSecurityE ventOperationSta tus | The operation that you want to perform.<br>Set the value to DescribeSecurityEventOperationStatus. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| TaskId | Long | No | 12121 | The ID of the task that handles the alerts. |
| SecurityEventIds.N | RepeatLi st | No | \["909361"\] | The list of alert IDs. |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | 1683940A-E4AE-4473-8C40-F4075434B76B | The ID of the request. |
| SecurityEventO perationStatus Response | Struct |  | The response of the request. |
| TaskStatus | String | Success | The status of the task that handles the alerts. Valid values:<br>• Processing: The task is running.<br>• Success: The task is successful.<br>• Failure: The task failed.<br>• Pending: The task is pending. |
| SecurityEventO perationStatus es | Array |  | The list of the processing status of the alerts. |
| SecurityEventId | String | 12321 | The ID of the alert. |
| Status | String | Success | The processing status of the alert. Valid values:<br>• Processing: The task is running.<br>• Success: The task is successful.<br>• Failed: The task failed. |
| ErrorCode | String | ignore.Success | The code that indicates the processing result of the alert. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribeSecurityEventOperationStatus
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<SecurityEventOperationStatusResponse>
    <SecurityEventOperationStatuses>
        <Status>Success</Status>
        <SecurityEventId>908872</SecurityEventId>
        <ErrorCode>ignore.Success</ErrorCode>
    </SecurityEventOperationStatuses>
    <SecurityEventOperationStatuses>
        <Status>Success</Status>
        <SecurityEventId>909758</SecurityEventId>
        <ErrorCode>ignore.Success</ErrorCode>
    </SecurityEventOperationStatuses>
    <SecurityEventOperationStatuses>
        <Status>Success</Status>
        <SecurityEventId>910655</SecurityEventId>
        <ErrorCode>ignore.Success</ErrorCode>
    </SecurityEventOperationStatuses>
    <TaskStatus>Success</TaskStatus>
</SecurityEventOperationStatusResponse>
<requestId>1683940A-E4AE-4473-8C40-F4075434B76B</requestId>
```

`JSON`  format

```json
{
    "SecurityEventOperationStatusResponse": {
        "SecurityEventOperationStatuses": [{
            "Status": "Success",
            "SecurityEventId": 908872,
            "ErrorCode": "ignore.Success"
        }, {
            "Status": "Success",
            "SecurityEventId": 909758,
            "ErrorCode": "ignore.Success"
        }, {
            "Status": "Success",
            "SecurityEventId": 910655,
            "ErrorCode": "ignore.Success"
        }],
        "TaskStatus": "Success"
    },
    "requestId": "1683940A-E4AE-4473-8C40-F4075434B76B"
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-5-10"></a>

### 3.5.10. CreateSimilarSecurityEventsQueryTask

Creates a task to query alerts triggered by the same rule or rules of the same type.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | CreateSimilarSecu rityEventsQueryT ask | The operation that you want to perform.<br>Set the value to CreateSimilarSecurityEventsQueryTask. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| SecurityEventId | Long | No | 14323 | The ID of the alert. |
| SimilarEventScena rioCode | String | No | default | The codes of alerts that are triggered by the same rule or rules of the same type. |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | 5861EE3E-F0B3-48B8-A5DC-A5080BFBE052 | The ID of the request. |
| CreateSimilarSe curityEventsQue ryTaskRespons e | Struct |  | The response of the task that queries alerts of the same type. |
| TaskId | Long | 2915 | The ID of the task. |
| Status | String | DataRetrieved | The status of the task.<br>• New: The task is new.<br>• RetrievingData: Data is being retrieved.<br>• DataRetrieved: Data is retrieved.<br>• Processing: The task is running.<br>• Success: The task is successful.<br>• Failed: The task failed.<br>• PartialFailed: The task is partially failed. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=CreateSimilarSecurityEventsQueryTask
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<code>200</code>
<data>
    <CreateSimilarSecurityEventsQueryTaskResponse>
        <Status>DataRetrieved</Status>
        <TaskId>2915</TaskId>
    </CreateSimilarSecurityEventsQueryTaskResponse>
</data>
<requestId>5861EE3E-F0B3-48B8-A5DC-A5080BFBE052</requestId>
```

`JSON`  format

```json
{
  "code": 200,
  "data": {
    "CreateSimilarSecurityEventsQueryTaskResponse": {
      "Status": "DataRetrieved",
      "TaskId": 2915
    }
  },
  "requestId": "5861EE3E-F0B3-48B8-A5DC-A5080BFBE052"
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-5-11"></a>

### 3.5.11. DescribeSimilarSecurityEvents

Queries alerts triggered by the same rule or rules of the same type.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeSimilarSe curityEvents | The operation that you want to perform.<br>Set the value to DescribeSimilarSecurityEvents. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Lang | String | No | zh | The natural language of the request and response. Valid values:<br>• zh: Chinese<br>• en: English |
| TaskId | Long | No | 111 | The ID of the task. |
| CurrentPage | Integer | No | 1 | The page number of the current page. |
| PageSize | Integer | No | 5 | The number of entries to return on each page. |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | 97B9CBC6-F869-4860-9CBC-A7310F85AE8E | The ID of the request. |
| SecurityEventsR esponse | Array |  | The list of alerts that are of the same type. |
| SecurityEventId | Long | 123 | The ID of the alert. |
| Uuid | String | qweeqq-13232-daweq-wqeqe | The UUID of the server. |
| EventType | String | Suspicious network connections | The type of the alert. |
| EventName | String | Visiting malicious domains | The name of the alert. |
| OccurrenceTim e | Long | 1577379820000 | The timestamp when the first exception occurred. |
| LastTime | Long | 1577441301000 | The timestamp when the exception last occurred. |
| PageInfo | Struct |  | The page information. |
| Count | Integer | 12 | The number of entries returned on the current page. |
| PageSize | Integer | 20 | The number of entries returned per page. |
| TotalCount | Integer | 23 | The number of alerts that are of the same type. |
| CurrentPage | Integer | 1 | The page number of the current page. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribeSimilarSecurityEvents
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<code>200</code>
<data>
    <PageInfo>
        <TotalCount>2</TotalCount>
        <PageSize>5</PageSize>
        <CurrentPage>1</CurrentPage>
        <Count>2</Count>
    </PageInfo>
    <SecurityEventsResponse>
        <OccurrenceTime>1576686364000</OccurrenceTime>
        <SecurityEventId>124</SecurityEventId>
        <Uuid>123-aasd-dsa-dadsa</Uuid>
        <EventType>Suspicious network connections</EventType>
        <EventName>Visiting malicious domains</EventName>
        <LastTime>1577063771000</LastTime>
    </SecurityEventsResponse>
    <SecurityEventsResponse>
        <OccurrenceTime>1577379820000</OccurrenceTime>
        <SecurityEventId>123</SecurityEventId>
        <Uuid>ewqeqweq-12311-sdfasf-afafsa</Uuid>
        <EventType>Suspicious network connections</EventType>
        <EventName>Visiting malicious domains</EventName>
        <LastTime>1577441301000</LastTime>
    </SecurityEventsResponse>
</data>
<requestId>97B9CBC6-F869-4860-9CBC-A7310F85AE8E</requestId>
```

`JSON`  format

```json
{
  "code": 200,
  "data": {
    "PageInfo": {
      "TotalCount": 2,
      "PageSize": 5,
      "CurrentPage": 1,
      "Count": 2
    },
    "SecurityEventsResponse": [
      {
        "OccurrenceTime": 1576686364000,
        "SecurityEventId": 124,
        "Uuid": "123-aasd-dsa-dadsa",
        "EventType": "Suspicious network connections",
        "EventName": "Visiting malicious domains",
        "LastTime": 1577063771000
      },
      {
        "OccurrenceTime": 1577379820000,
        "SecurityEventId": 123,
        "Uuid": "qweeqq-13232-daweq-wqeqe",
        "EventType": "Suspicious network connections",
        "EventName": "Visiting malicious domains",
        "LastTime": 1577441301000
      }
    ]
  },
  "requestId": "97B9CBC6-F869-4860-9CBC-A7310F85AE8E"
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-5-12"></a>

### 3.5.12. DescribeSimilarEventScenarios

Queries the scenarios where alerts triggered by the same rule or rules of the same type are managed.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeSimilarEv entScenarios | The operation that you want to perform.<br>Set the value to DescribeSimilarEventScenarios. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| SecurityEventId | Long | No | 12321 | The ID of the alert. |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | FDF7B8D9-8493-4B90-8D13-E0C1FFCE5F97 | The ID of the request. |
| Scenarios | Array |  | The list of scenarios where alerts triggered by the same rule or rules of the same type are managed. |
| Code | String | same_url | The code of the scenario. Valid values:<br>• default: the same alert type<br>• same_file_content: the same file content rule<br>• same_ip: the same IP address rule<br>• same_url: the same URL rule |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribeSimilarEventScenarios
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<Scenarios>
    <Code>same_url</Code>
</Scenarios>
<Scenarios>
    <Code>default</Code>
</Scenarios>
<requestId>FDF7B8D9-8493-4B90-8D13-E0C1FFCE5F97</requestId>
```

`JSON`  format

```json
{
    "Scenarios": [{
        "Code": "same_url"
    }, {
        "Code": "default"
    }],
    "requestId": "FDF7B8D9-8493-4B90-8D13-E0C1FFCE5F97"
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-5-13"></a>

### 3.5.13. DescribeUserLayoutAuthorization

Queries whether the brute-force attacks protection feature has been authorized. The brute-force attacks protection feature cannot be used without authorization.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeUserLayo utAuthorization | The operation that you want to perform.<br>Set the value to DescribeUserLayoutAuthorization. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Lang | String | No | zh | The natural language of the request and response. Valid values:<br>• zh: Chinese<br>• en: English |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| Authorized | Boolean | false | The result of the query. Valid values:<br>• true: authorized<br>• false: not authorized |
| RequestId | String | 4A80EE8F-2175-49DA-B8BF-FAE1B3D52E4C | The ID of the request. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribeUserLayoutAuthorization
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<DescribeUserLayoutAuthorizationResponse>
      <Authorized>false</Authorized>
      <requestId>4A80EE8F-2175-49DA-B8BF-FAE1B3D52E4C</requestId>
</DescribeUserLayoutAuthorizationResponse>
```

`JSON`  format

```json
{
    "Authorized": false,
    "requestId": "4A80EE8F-2175-49DA-B8BF-FAE1B3D52E4C"
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-5-14"></a>

### 3.5.14. RollbackSuspEventQuaraFile

Removes a quarantined file from the quarantine box.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | RollbackSuspEven tQuaraFile | The operation that you want to perform.<br>Set the value to RollbackSuspEventQuaraFile. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| QuaraFileId | Integer | No | 3921797 | The ID of the quarantined file.<br>Note If this parameter is not set, the operation does not remove a quarantined file from the quarantine box. You can call the DescribeSuspEventQuaraFiles operation to obtain the ID of the target quarantined file. |
| From | String | No | sas | The ID of the request source. Set the value to sas. |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | 52A3AEE6-114A-499D-8990-4BA9B27FE0AA | The ID of the request. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=RollbackSuspEventQuaraFile
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<RollbackSuspEventQuaraFileResponse>
      <RequestId>52A3AEE6-114A-499D-8990-4BA9B27FE0AA</RequestId>
</RollbackSuspEventQuaraFileResponse>
```

`JSON`  format

```json
{
    "RequestId": "52A3AEE6-114A-499D-8990-4BA9B27FE0AA"
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-5-15"></a>

### 3.5.15. DescribeSuspEventQuaraFiles

Queries the quarantined files by page.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeSuspEven tQuaraFiles | The operation that you want to perform.<br>Set the value to DescribeSuspEventQuaraFiles. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| PageSize | String | No | 20 | The number of quarantined files to return on each page. |
| Status | String | No | quaraDone | The status of the quarantined files to be queried. Valid values:<br>• quaraFailed: The system failed to quarantine the file.<br>• quaraDone: The system has quarantined the file.<br>• quaraing: The file is being quarantined.<br>• rollbackFailed: The system failed to cancel the quarantine.<br>• rollbackDone: The system has canceled the quarantine.<br>• rollbacking: The quarantine is being canceled. |
| CurrentPage | String | No | 1 | The number of pages to be returned. |
| From | String | No | sas | The service of the request. Set the value to sas. |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| Count | Integer | 1 | The total number of pages returned. |
| CurrentPage | Integer | 1 | The page number of the current page. |
| PageSize | Integer | 20 | The number of quarantined files returned per page. |
| QuaraFiles | Array |  | The list of quarantined files. |
| EventName | String | WEBSHELL | The name of the event. |
| EventType | String | WebshellQuaraEvent Type | The type of the event. |
| Id | Integer | 3920516 | The ID of the quarantined file. |
| InstanceName | String | abc | The ID of the server where the file is located. |
| InternetIp | String | 47.XX.XX.131 | The public IP address of the server where the file is located. |
| Ip | String | 47.XX.XX.131 | The public IP address of the server where the file is located. |
| Md5 | String | 5ddebe926acc7ed3 9a664409bfd0ec10 | The MD5 value of the file. |
| ModifyTime | String | 2020-06-11 20:37:08 | The update time. |
| Path | String | /var/www/html/we bshell-sample-master/others/defc 3e21bab59e2a2ab4 9f7eda99f65f83d4d 349.jpg | The path where the quarantined file is stored on the server. |
| Status | String | rollbackDone | The status of quarantine. Valid values:<br>• quaraFailed: The system failed to quarantine the file.<br>• quaraDone: The system has quarantined the file.<br>• quaraing: The file is being quarantined.<br>• rollbackFailed: The system failed to cancel the quarantine.<br>• rollbackDone: The system has canceled the quarantine.<br>• rollbacking: The quarantine is being canceled. |
| Tag | String | 228f890e56eae9eec 6a42c7ea801b538 | The ID of the event. |
| Uuid | String | 04a0e735-ad32-4835-b635-0458d77b\*\*\*\* | The UUID of the server. |
| RequestId | String | 6AD0BA1B-0129-498F-B82A-17C7B8368A08 | The ID of the request. |
| TotalCount | Integer | 20 | The total number of quarantined files. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribeSuspEventQuaraFiles
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<DescribeSuspEventQuaraFilesResponse>
      <TotalCount>20</TotalCount>
      <RequestId>6AD0BA1B-0129-498F-B82A-17C7B8368A08</RequestId>
      <PageSize>20</PageSize>
      <CurrentPage>1</CurrentPage>
      <QuaraFiles>
            <Path>/var/www/html/webshell-sample-master/others/defc3e21bab59e2a2ab49f7eda99f65f83d4d349.jpg</Path>
            <InstanceName>abc</InstanceName>
            <Status>rollbackDone</Status>
            <ModifyTime>2020-06-11 20:37:08</ModifyTime>
            <Uuid>04a0e735-ad32-4835-b635-0458d77b****</Uuid>
            <InternetIp>47.XX.XX.131</InternetIp>
            <EventType>WebshellQuaraEventType</EventType>
            <Ip>47.XX.XX.131</Ip>
            <EventName>WEBSHELL</EventName>
            <Id>3920516</Id>
            <Tag>228f890e56eae9eec6a42c7ea801b538</Tag>
            <Md5>5ddebe926acc7ed39a664409bfd0ec10</Md5>
      </QuaraFiles>
      <Count>1</Count>
</DescribeSuspEventQuaraFilesResponse>
```

`JSON`  format

```json
{
    "TotalCount": "20",
    "RequestId": "6AD0BA1B-0129-498F-B82A-17C7B8368A08",
    "PageSize": "20",
    "CurrentPage": "1",
    "QuaraFiles": [{
        "Path": "/var/www/html/webshell-sample-master/others/defc3e21bab59e2a2ab49f7eda99f65f83d4d349.jpg",
        "InstanceName": "abc",
        "Status": "rollbackDone",
        "ModifyTime": "2020-06-11 20:37:08",
        "Uuid": "04a0e735-ad32-4835-b635-0458d77b****",
        "InternetIp": "47.XX.XX.131",
        "EventType": "WebshellQuaraEventType",
        "Ip": "47.XX.XX.131",
        "EventName": "WEBSHELL",
        "Id": "3920516",
        "Tag": "228f890e56eae9eec6a42c7ea801b538",
        "Md5": "5ddebe926acc7ed39a664409bfd0ec10"
    }],
    "Count": "1"
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-6"></a>

## 3.6. Configuration assessment

<a id="section-3-6-1"></a>

### 3.6.1. DescribeRiskItemType

Queries types of check items for cloud service configurations. Each check item is categorized into a type. Types of check items include identity authentication and permissions, network access control, log auditing, data security, monitoring and alerting, and basic security protection.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeRiskItem Type | The operation that you want to perform.<br>Set the value to DescribeRiskItemType. |
| Lang | String | No | zh | The natural language of the request and response. Valid values:<br>• zh: Chinese<br>• en: English |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| List | Array |  | The information about the check item. |
| Id | Long | 1 | The ID of the check item. |
| Title | String | Identity authentication and permissions | The type of the check item. Example: Identity authentication and permissions. |
| RequestId | String | 3B3F3A90-46A5-4023-A2D8-D68B14262F96 | The ID of the request. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribeRiskItemType
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<DescribeRiskItemType>
   <RequestId>3B3F3A90-46A5-4023-A2D8-D68B14262F96</RequestId>
   <List>
      <Title>Identity authentication and permissions</Title>
      <Id>1</Id>
   </List>
   <List>
      <Title>Network access control</Title>
      <Id>2</Id>
   </List>
   <List>
      <Title>Log auditing</Title>
      <Id>3</Id>
   </List>
   <List>
      <Title>Data security</Title>
      <Id>4</Id>
   </List>
   <List>
      <Title>Basic security protection</Title>
      <Id>6</Id>
   </List>
    </DescribeRiskItemType>
```

`JSON`  format

```json
{
 "RequestId":"3B3F3A90-46A5-4023-A2D8-D68B14262F96",
 "List":[
  {
   "Id":1,
   "Title":"Identity authentication and permissions"
  },
  {
   "Id":2,
   "Title":"Network access control"
  },
  {
   "Id":3,
   "Title":"Log auditing"
  },
  {
   "Id":4,
   "Title":"Data security"
  },
  {
   "Id":6,
   "Title":"Basic security protection"
  }
 ]
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-6-2"></a>

### 3.6.2. StartBaselineSecurityCheck

Checks cloud service configurations. You can check all items or a specific item, and you can verify whether an item is already checked.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | StartBaselineSecu rityCheck | The operation that you want to perform.<br>Set the value to StartBaselineSecurityCheck. |
| Type | String | Yes | check | The type of the check task. Valid values:<br>• check<br>• verify |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Lang | String | No | zh | The natural language of the request and response. Valid values:<br>• zh: Chinese<br>• en: English |
| ItemIds.N | RepeatLi st | No | 1 | The ID of the check item.<br>Note To perform the check task on cloud service configurations, you must provide the ID of the check item. You can call the DescribeRiskItemType operation to obtain the ID. |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | 48D2E9A9-A1B0-4295-B727-0995757C47E9 | The ID of the request. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=StartBaselineSecurityCheck
&Type=check
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<StartBaselineSecurityCheckResponse>
  <RequestId>48D2E9A9-A1B0-4295-B727-0995757C47E9</RequestId>
</StartBaselineSecurityCheckResponse>
```

`JSON`  format

```json
{
    "RequestId":"48D2E9A9-A1B0-4295-B727-0995757C47E9"
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-6-3"></a>

### 3.6.3. DescribeRiskCheckSummary

Queries the summary of check items for cloud service configurations. The operation returns the following information: the number of risk items, the risk rate, the number of affected assets, the last check time, and the statistics of each type of check items.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeRiskChec kSummary | The operation that you want to perform.<br>Set the value to DescribeRiskCheckSummary. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Lang | String | No | zh | The natural language of the request and response. Valid values:<br>• zh: Chinese<br>• en: English |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | 291B49F9-1685-4005-9D34-606B6F78740F | The ID of the request. |
| RiskCheckSumm ary | Struct |  | The summary of check items for cloud service configurations. |
| RiskCount | Integer | 1 | The number of risk items. |
| PreviousCount | Integer | 0 | The number of risk items in the last check. |
| ItemCount | Integer | 4 | The number of check items. |
| RiskRate | Float | 0.25 | The proportion of risk items in the total number to check items. |
| AffectedAssetC ount | Integer | 0 | The number of affected assets. |
| PreviousTime | Long | 1545012926000 | The timestamp of the last check. |
| EnabledRiskCou nt | Integer | 3 | The number of check items that passed the check. |
| DisabledRiskCo unt | Integer | 0 | The number of risk items that failed to pass the check. |
| RiskLevelCount | Array |  | The number of risk items for each level.<br>• high<br>• medium<br>• low |
| Key | String | medium | The severity level of the risk item. |
| Count | Integer | 1 | The number of risk items. |
| Groups | Array |  | The types of check items. |
| Id | Long | 1 | The type ID of the check item. |
| Title | String | Identity authentication and permissions | The type of the check item. |
| Status | String | finish | Indicates whether the check is finished.<br>• finish: The check is finished.<br>• Running: The check is in process.<br>• waiting: The check is pending.<br>• NoStart: The check is not started. |
| RemainingTime | Integer | 0 | The time when the next check will be performed. |
| Sort | Integer | 1 | The sequence number of the check item type in the All Types drop-down list in the console. |
| CountByStatus | Array |  | The statistics of check results. |
| Status | String | pass | The status of the check item after the check is finished. Valid values:<br>• pass: The check item is normal.<br>• failed: The check item is at risk. |
| Count | Integer | 2 | The number of risk items. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribeRiskCheckSummary
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<DescribeRiskCheckSummary>
      <RequestId>291B49F9-1685-4005-9D34-606B6F78740F</RequestId>
      <RiskCheckSummary>
            <RiskCount>1</RiskCount>
            <RiskRate>0.25</RiskRate>
            <PreviousTime>1545012926000</PreviousTime>
            <ItemCount>4</ItemCount>
            <AffectedAssetCount>0</AffectedAssetCount>
            <RiskLevelCount>
                  <Count>1</Count>
                  <Key>medium</Key>
            </RiskLevelCount>
            <Groups>
                  <Status>finish</Status>
                  <CountByStatus>
                        <Status>exception</Status>
                        <Count>2</Count>
                  </CountByStatus>
                  <RemainingTime>0</RemainingTime>
                  <Sort>1</Sort>
                  <Title>Identity authentication and permissions</Title>
                  <Id>1</Id>
            </Groups>
            <Groups>
                  <Status>finish</Status>
                  <CountByStatus>
                        <Status>exception</Status>
                        <Count>5</Count>
                  </CountByStatus>
                  <RemainingTime>0</RemainingTime>
                  <Sort>2</Sort>
                  <Title>Network access control</Title>
                  <Id>2</Id>
            </Groups>
            <Groups>
                  <Status>finish</Status>
                  <CountByStatus>
                        <Status>pass</Status>
                        <Count>1</Count>
                  </CountByStatus>
                  <RemainingTime>0</RemainingTime>
                  <Sort>3</Sort>
                  <Title>Log auditing</Title>
                  <Id>3</Id>
            </Groups>
            <Groups>
                  <Status>finish</Status>
                  <CountByStatus>
                        <Status>exception</Status>
                        <Count>2</Count>
                  </CountByStatus>
                  <RemainingTime>0</RemainingTime>
                  <Sort>4</Sort>
                  <Title>Data security</Title>
                  <Id>4</Id>
            </Groups>
            <Groups>
                  <Status>finish</Status>
                  <CountByStatus>
                        <Status>exception</Status>
                        <Count>2</Count>
                  </CountByStatus>
                  <RemainingTime>0</RemainingTime>
                  <Sort>6</Sort>
                  <Title>Basic security protection</Title>
                  <Id>6</Id>
            </Groups>
            <PreviousCount>0</PreviousCount>
      </RiskCheckSummary>
    </DescribeRiskCheckSummary>
```

`JSON`  format

```json
{
  "RequestId": "291B49F9-1685-4005-9D34-606B6F78740F",
  "RiskCheckSummary": {
    "RiskCount": 1,
    "RiskRate": 0.25,
    "PreviousTime": 1545012926000,
    "ItemCount": 4,
    "AffectedAssetCount": 0,
    "RiskLevelCount": [
      {
        "Count": 1,
        "Key": "medium"
      }
    ],
    "Groups": [
      {
        "Status": "finish",
        "CountByStatus": [
          {
            "Status": "exception",
            "Count": 2
          }
        ],
        "RemainingTime": 0,
        "Sort": 1,
        "Title": "Identity authentication and permissions",
        "Id": 1
      },
      {
        "Status": "finish",
        "CountByStatus": [
          {
            "Status": "exception",
            "Count": 5
          }
        ],
        "RemainingTime": 0,
        "Sort": 2,
        "Title": "Network access control",
        "Id": 2
      },
      {
        "Status": "finish",
        "CountByStatus": [
          {
            "Status": "pass",
            "Count": 1
          }
        ],
        "RemainingTime": 0,
        "Sort": 3,
        "Title": "Log auditing",
        "Id": 3
      },
      {
        "Status": "finish",
        "CountByStatus": [
          {
            "Status": "exception",
            "Count": 2
          }
        ],
        "RemainingTime": 0,
        "Sort": 4,
        "Title": "Data security",
        "Id": 4
      },
      {
        "Status": "finish",
        "CountByStatus": [
          {
            "Status": "exception",
            "Count": 2
          }
        ],
        "RemainingTime": 0,
        "Sort": 6,
        "Title": "Basic security protection",
        "Id": 6
      }
    ],
    "PreviousCount": 0
  }
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-6-4"></a>

### 3.6.4. ModifyRiskCheckStatus

Modifies the status of a check result. You can ignore a result or mark a result as a false positive.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | ModifyRiskCheckS tatus | The operation that you want to perform.<br>Set the value to ModifyRiskCheckStatus. |
| ItemId | Long | Yes | 1 | The ID of the check item. |
| Status | String | Yes | ignored | The method to process the check result. Valid values:<br>• ignored<br>• reset |
| TaskId | Long | Yes | 57 | The ID of the check task to which the check item belongs. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Lang | String | No | zh | The natural language of the request and response. Valid values:<br>• zh: Chinese<br>• en: English |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | 48D2E9A9-A1B0-4295-B727-0995757C47E9 | The ID of the request. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=ModifyRiskCheckStatus
&ItemId=1
&TaskId=57
&Status=ignored
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<ModifyRiskCheckStatusResponse>
      <RequestId>48D2E9A9-A1B0-4295-B727-0995757C47E9</RequestId>
</ModifyRiskCheckStatusResponse>
```

`JSON`  format

```json
{
    "RequestId":"48D2E9A9-A1B0-4295-B727-0995757C47E9"
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-6-5"></a>

### 3.6.5. DescribeRiskCheckResult

Queries the results of check items by type or name.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeRiskChec kResult | The operation that you want to perform.<br>Set the value to DescribeRiskCheckResult. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Lang | String | No | zh | The natural language of the request and response. Valid values:<br>• zh: Chinese<br>• en: English |
| GroupId | Long | No | 21000 | The type ID of the check item. Valid values:<br>• 1: identity authentication and permissions<br>• 2: network access control<br>• 3: log auditing<br>• 4: data security<br>• 5: monitoring and alerting<br>• 6: basic security protection |
| CurrentPage | Integer | No | 1 | The page number of the current page. |
| RiskLevel | String | No | high | The severity level of the check item.Valid values:<br>• high<br>• medium<br>• low |
| Status | String | No | pass | The status of the check result. Valid values:<br>• pass<br>• failed<br>• running<br>• waiting<br>• ignored<br>• falsePositive |
| ItemIds.N | RepeatLi st | No | sde\*\*\* | The ID of the check item. For more information about the description of the check items specified by this parameter, see the check item table in the "Response parameters" section of this topic. |
| AssetType | String | No | RDS | The type of the cloud service. For more information about the description of the cloud services specified by this parameter, see the check item table in the "Response parameters" section of this topic. |
| Name | String | No | Cloud platform -Multi-factor authentication configuration of Apsara Stack tenant accounts | The name of the check item. For more information about the description of the check item name, see the check item table in the "Response parameters" section of this topic. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| Count | Integer | 10 | The number of entries returned on the current page. |
| CurrentPage | Integer | 1 | The page number of the current page. |
| List | Array |  | The information about the check item. |
| AffectedCount | Integer | 0 | The number of the affected assets. |
| CheckTime | Long | 1543991525000 | The timestamp when the last check was performed. |
| ItemId | Long | 1 | The ID of the check item. For more information about the description of the check item ID specified by this parameter, see the check item table in the "Response parameters" section of this topic. |
| RemainingTime | Integer | 0 | The time when the next check will be performed. |
| RepairStatus | String | disabled | Indicates whether the risk of the check item can be fixed. Valid values:<br>• enabled: The risk can be fixed.<br>• disabled: The risk cannot be fixed. |
| RiskAssertType | String | ECS | The type of the affected asset. |
| RiskItemResour ces | Array |  | The details of the check item. |
| ContentResourc e | Json | {"type": "link", "value": "Risk: Multi-factor authentication is disabled\\n", "url": "https://\*\*\*.aliyun.c om/#/secure\\n" } | The content in the check item details. |
| ResourceName | String | bestPractice | The title in the check item details. Valid values:<br>• bestPractice: description<br>• influence: risk<br>• suggestion: solution<br>• helpResource: reference |
| RiskLevel | String | high | The severity level of the check item. Valid values:<br>• high<br>• medium<br>• low |
| Sort | Integer | 1 | The sequence number of the check result.The check items are sorted based on the sequence number. |
| StartStatus | String | enabled | Indicates whether the check item is supported by the cloud service. Valid values:<br>• enabled: supported<br>• disable: unsupported |
| Status | String | pass | The status of the check result. Valid values:<br>• pass<br>• failed<br>• running<br>• waiting<br>• ignored<br>• falsePositive |
| TaskId | Long | 647189 | The ID of the check task. |
| Title | String | Cloud platform -Multi-factor authentication configuration of Apsara Stack tenant accounts | The name of the check item. |
| Type | String | Identity authentication and permissions | The type of the check item. Valid values:<br>• Identity authentication and permissions<br>• Network access control<br>• Log auditing<br>• Data security<br>• Monitoring and alerting<br>• Basic security protection |
| PageCount | Integer | 20 | The total number of pages returned. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| RequestId | String | AD271C07-4ACE-413D-AA9B-F14FD3B7717F | The ID of the request. |
| TotalCount | Integer | 12 | The total number of entries returned. |

The following table describes the check items supported by the cloud platform, including the ID, name, type, risk level, and service type.

| ID | Name | Type | Severity level | Service type | Description |
| --- | --- | --- | --- | --- | --- |
| 1 | ActionTrail -Logging configuration | 3: log auditing | medium | ActionTrail | Checks whether you enable ActionTrail to record operations logs on the cloud and save the logs to Object Storage Service (OSS) buckets. |
| 2 | ApsaraDB for RDS -Database security policy | 4: data security | medium | RDS | Checks whether you enable Secure Sockets Layer (SSL), Transparent Data Encryption (TDE), and SQL audit services for each ApsaraDB for RDS instance. |
| 3 | Apsara Stack tenant account security -Multi-factor authentication | 1: identity authentication and permissions | high | RAM | Checks whether MFA is enabled for Apsara Stack tenant accounts. |
| 4 | Apsara Stack Security - Anti-DDoS Pro or Anti-DDoS Premium back-to-origin configuration | 2: network access control | high | DDOS | Checks whether actual IP addresses of backend servers are hidden after you use Anti-DDoS Pro or Anti-DDoS Premium. If the actual IP addresses are hidden, attackers cannot directly access the actual IP addresses.&lt;note&gt; To hide the actual IP addresses, you can configure whitelist policies, for example, when the actual IP addresses are the IP addresses of Server Load Balancer (SLB) instances.When the IP addresses are the IP addresses of Elastic Compute Service (ECS) instances, you can configure |
|  |  |  |  |  |  |
| ID | Name | Type | Severity level | Service type | access control policies forDescription ECS security |
|  |  |  |  |  | groups. All these policies allow access from only back-to-origin IP addresses of Anti-DDoS Pro or Anti-DDoS Premium.&lt;/note&gt; |
| 5 | ApsaraDB for RDS - Whitelist configuration | 2: network access control | high | RDS | Checks whether the RDS access control policy is set to 0.0.0.0/0, which allows requests from all IP addresses. We recommend that you limit the access scope to a specific range of IP addresses rather than exposing database services to the Internet. |
| 6 | SLB - High-risk port | 2: network access control | high | SLB | Checks whether SLB forwards requests from high-risk ports to the Internet. |
| 7 | Apsara Stack Security - Web Application Firewall (WAF) back-to-origin configuration | 2: network access control | high | WAF | Checks whether the actual IP addresses of backend servers are hidden after you use WAF.If the actual IP addresses are hidden, attackers cannot directly access the actual IP addresses. To hide the actual IP addresses, you can configure whitelist policies, for example, when the actual IP addresses are the IP addresses of Server Load Balancer (SLB) instances.When the IP addresses are the IP addresses of Elastic Compute Service (ECS) instances, you can configure access control policies for ECS security groups. All these policies allow access from only back-to-origin IP addresses of WAF. |
|  |  |  |  |  |  |
| ID | Name | Type | Severity level | Service type | Description |
|  |  |  |  |  |  |
| 8 | Apsara Stack Security -Threat Detection Service agent online status | 6: basic security protection | high | ECS | Checks whether the Threat Detection Service agent on the ECS instance is always online and provides protection. |
| 12 | OSS - Bucket access permissions | 4: data security | high | OSS | Checks whether the access permissions on your OSS buckets is public-read or public-read-write. If yes, the check fails. |
| 13 | Threat Detection Service -AccessKey leak detection | 5: monitoring and alerting | medium | RAM | Checks whether AccessKey leak detection is enabled. If no, the check fails. |
| 14 | ApsaraDB for MongoDB -Whitelist configuration | 2: network access control | high | MongoDB | Checks whether the whitelist is enabled for ApsaraDB for MongDB instances. If the whitelist is enabled and set to 0.0.0.0/0, which allows access from all devices, the check fails. |
| 15 | RAM - MFA configuration for RAM users | 1: identity authentication and permissions | medium | RAM | Checks whether MFA is enabled for RAM users. |
| 16 | OSS - Logging configuration | 4: data security | medium | OSS | Checks whether the logging feature is enabled for all OSS buckets. If no, the check fails. |
| 17 | OSS - Cross-region replication configuration | 4: data security | low | OSS | Checks whether the cross-region replication is enabled for all OSS buckets. If no, the check fails. |
| 18 | ApsaraDB for RDS - Backup configuration | 4: data security | medium | RDS | Checks whether database backup is enabled for ApsaraDB for RDS instances.If no, the check fails. |
| 19 | KVStore for Redis -Whitelist configuration | 2: network access control | high | Redis | Checks access control configurations of KVStore for Redis. |
| 20 | ECS - SSH key pairs | 1: identity authentication and permissions | medium | ECS | Checks whether SSH key pair-based logons are enabled for ECS instances. |
| 21 | SLB - Health status | 5: monitoring and alerting | low | SLB | Checks the health status of SLB instances. |
| 22 | PolarDB -Whitelist configuration | 2: network access control | medium | POLARDB | Checks the whitelist configured for PolarDB. If the whitelist is enabled and set to 0.0.0.0/0, which allows access from all devices, the check fails. |
| 23 | AnalyticDB for PostgreSQL -Whitelist configuration | 2: network access control | medium | PostgreSQL | Checks the whitelist of the AnalyticDB for PostgreSQL instance. If the whitelist is enabled and set to 0.0.0.0/0, which allows access from all devices, the check fails. |
| 24 | ECS - Storage encryption | 4: data security | low | ECS | Checks whether storage encryption is enabled. If no, the check fails. |
| 25 | SLB - Whitelist configuration | 2: network access control | medium | SLB | Checks SLB whitelist configurations. If the whitelist is enabled and set to 0.0.0.0/0, which allows access from all devices, the check fails. |
| 26 | SLB -Certificate expiration | 5: monitoring and alerting | medium | SLB | Checks whether the SLB certificate has expired. |
| 27 | ECS -Automatic snapshot policy | 4: data security | medium | ECS | Checks whether automatic snapshot policies are enabled for ECS instances. |
| 28 | SSL certificate<br>- Expiration check | 4: data security | medium | SSL | Checks whether the SSL certificate is within its validity period. |
| 30 | OSS - Server-side encryption | 4: data security | low | OSS | Checks whether server-side encryption is enabled for OSS buckets. |
| 31 | OSS -Hotlinking protection | 2: network access control | low | OSS | Checks whether hotlinking protection is configured for OSS buckets. |
| 32 | ApsaraDB for RDS - Cross-region backup configuration | 4: data security | low | RDS | Checks whether cross-region backup is enabled for ApsaraDB for RDS instances. |
| 33 | ApsaraDB for MongoDB -Backup configuration | 4: data security | medium | MongoDB | Checks whether data backup is enabled for ApsaraDB for MongoDB instances. |
| 34 | ApsaraDB for MongoDB -Log auditing | 3: log auditing | medium | MongoDB | Checks whether log auditing is enabled for ApsaraDB for MongoDB instances. |
| 35 | ApsaraDB for MongoDB -SSL certificate | 4: data security | medium | MongoDB | Checks whether SSL certificate checks are enabled for ApsaraDB for MongoDB instances. |
| 36 | Cloud Monitor<br>- Host monitoring plug-in | 5: monitoring and alerting | medium | CloudMonitor | Checks whether the status of the Cloud Monitor agent is normal. |
| 37 | ECS - Security group policies | 2: network access control | medium | ECS | Checks the ECS security group policies. |
| 38 | VPC - DNAT management port mapping | 2: network access control | medium | VPC | Checks whether a VPC DNAT rule is configured to map management ports to the Internet. |
| 39 | KVStore for Redis - Backup configuration | 4: data security | medium | Redis | Checks whether data backup is enabled for KVStore for Redis. |
| 40 | Container Registry -Repository permission configurations | 4: data security | high | CR | Checks whether permissions are correctly configured for the repository in Container Registry. |
| 41 | Container Registry -Security scan | 6: basic security protection | low | CR | Checks whether security scan is enabled for Container Registry. |
| 42 | SLB - Access logging configuration | 3: log auditing | medium | SLB | Checks whether access logging is configured for SLB instances. |
| 43 | KVStore for Redis - Log auditing | 3: log auditing | low | Redis | Checks whether log auditing is configured for KVStore for Redis. |
| 44 | OSS -Authorization policy | 1: identity authentication and permissions | medium | OSS | Checks whether correct authorization policies are enabled for OSS. |
| 46 | PolarDB -Backup configuration | 4: data security | medium | POLARDB | Checks whether the backup configuration is enabled for PolarDB. |
| 47 | PolarDB - SQL explorer | 3: log auditing | medium | POLARDB | Checks whether SQL Explorer is enabled for PolarDB. |
| 48 | Apsara Stack tenant account security -AccessKey pair | 1: identity authentication and permissions | medium | RAM | Checks whether the AccessKey pair is enabled for your Apsara Stack tenant account. |
| 50 | CDN - Real-time logging | 3: log auditing | medium | CDN | Checks whether real-time logging push is enabled for CDN. |
| 51 | KVStore for Redis - SSL certificate | 4: data security | medium | Redis | Checks whether KVStore for Redis uses SSL certificates. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribeRiskCheckResult
&GroupId=1
&RiskLevel=high
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<DescribeRiskCheckResultResponse>
      <TotalCount>12</TotalCount>
      <RequestId>AD271C07-4ACE-413D-AA9B-F14FD3B7717F</RequestId>
      <PageCount>20</PageCount>
      <PageSize>10</PageSize>
      <CurrentPage>1</CurrentPage>
      <List>
            <Status>pass</Status>
            <CheckTime>1543991525000</CheckTime>
            <TaskId>647189</TaskId>
            <RemainingTime>0</RemainingTime>
            <Title>Cloud platform - MFA configuration of Apsara Stack tenant accounts</Title>
            <ItemId>1</ItemId>
            <RiskAssertType>ECS</RiskAssertType>
            <Type>Identity authentication and permissions</Type>
            <StartStatus>enabled</StartStatus>
            <AffectedCount>0</AffectedCount>
            <Sort>1</Sort>
            <RepairStatus>disabled</RepairStatus>
            <RiskLevel>high</RiskLevel>
            <RiskItemResources>
                  <ContentResource>{   "type": "link",   "value": "Risk: Multi-factor authentication is disabled\n",   "url": "https://***.aliyun.com/#/secure\n" }</ContentResource>
                  <ResourceName>bestPractice</ResourceName>
            </RiskItemResources>
      </List>
      <Count>10</Count>
</DescribeRiskCheckResultResponse>
```

`JSON`  format

```json
{
    "TotalCount": "12",
    "RequestId": "AD271C07-4ACE-413D-AA9B-F14FD3B7717F",
    "PageCount": "20",
    "PageSize": "10",
    "CurrentPage": "1",
    "List": {
            "Status": "pass",
            "CheckTime": "1543991525000",
            "TaskId": "647189",
            "RemainingTime": "0",
            "Title": "Cloud platform - MFA configuration of Apsara Stack tenant accounts",
            "ItemId": "1",
            "RiskAssertType": "ECS",
            "Type": "Identity authentication and permissions",
            "StartStatus": "enabled",
            "AffectedCount": "0",
            "Sort": "1",
            "RepairStatus": "disabled",
            "RiskLevel": "high",
            "RiskItemResources": {
                "ContentResource": "{   \"type\": \"link\",   \"value\": \"Risk: Multi-factor authentication is disabled\\n\",   \"url\": \"https://***.aliyun.com/#/secure\\n\" }",
                "ResourceName": "bestPractice"
            }
    },
    "Count": "10"
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-6-6"></a>

### 3.6.6. DescribeSecurityCheckScheduleConfig

Queries the custom check cycle and time period.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeSecurityC heckScheduleCon fig | The operation that you want to perform. Set the value to DescribeSecurityCheckScheduleConfig. |
| Lang | String | No | zh | The natural language of the request and response. Valid values:<br>• zh: Chinese<br>• en: English |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | 48D2E9A9-A1B0-4295-B727-0995757C47E9 | The ID of the request. |
| RiskCheckJobCo nfig |  |  | The settings of scheduled checks. |
| DaysOfWeek | String | 1,2,3 | The days when checks are performed every week. You can specify multiple days.Separate multiple days with commas (,).Valid values:<br>• 1: Monday<br>• 2: Tuesday<br>• 3: Wednesday<br>• 4: Thursday<br>• 5: Friday<br>• 6: Saturday<br>• 7: Sunday |
| EndTime | Integer | 12 | The time period during which the configuration check ends. Valid values:<br>• 6: 00:00 to 06:00<br>• 12: 06:00 to 12:00<br>• 18: 12:00 to 18:00<br>• 24: 18:00 to 24:00 |
| StartTime | Integer | 6 | The time period during which the configuration check starts. Valid values:<br>• 0: 00:00 to 06:00<br>• 6: 06:00 to 12:00<br>• 12: 12:00 to 18:00<br>• 18: 18:00 to 24:00 |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribeSecurityCheckScheduleConfig
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<DescribeSecurityCheckScheduleConfig>
  <RiskCheckJobConfig>
        <DaysOfWeek>1,2,3</DaysOfWeek>
        <EndTime>12</EndTime>
        <StartTime>6</StartTime>
  </RiskCheckJobConfig>
  <RequestId>C17F3C01-0AFD-4898-A950-AA0129025B41</RequestId>
</DescribeSecurityCheckScheduleConfig>
```

`JSON`  format

```json
{
 "RequestId":"C17F3C01-0AFD-4898-A950-AA0129025B41",
 "RiskCheckJobConfig":{
  "DaysOfWeek":"1,2,3",
  "EndTime":12,
  "StartTime":6
 }
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-6-7"></a>

### 3.6.7. ModifyRiskSingleResultStatus

Changes the status of an asset affected by a check item. You can ignore an asset or mark an asset as false positive.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | ModifyRiskSingleR esultStatus | The operation that you want to perform. Set the value to ModifyRiskSingleResultStatus. |
| TaskId | Long | Yes | 57 | The ID of the check task to which the affected asset belongs. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Lang | String | No | zh | The natural language of the request and response. Valid values:<br>• zh: Chinese<br>• en: English |
| Ids.N | RepeatLi st | No | 1 | The ID of the affected asset. |
| Status | String | No | ignored | The status of the affected asset. Valid values:<br>• ignored: ignores the asset.<br>• failed: marks the asset as a false positive. |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | 3B3F3A90-46A5-4023-A2D8-D68B14262F96 | The ID of the request. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=ModifyRiskSingleResultStatus
&Ids.1=4
&Status=ignored
&TaskId=57
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<ModifyRiskSingleResultStatusResponse>
  <RequestId>3B3F3A90-46A5-4023-A2D8-D68B14262F96</RequestId>
</ModifyRiskSingleResultStatusResponse>
```

`JSON`  format

```json
{
    "RequestId":"3B3F3A90-46A5-4023-A2D8-D68B14262F96"
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-6-8"></a>

### 3.6.8. ModifySecurityCheckScheduleConfig

Configures the time to automatically run a configuration check. For example, you can specify the time period during a day of the week.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | ModifySecurityCh eckScheduleConfi g | The operation that you want to perform.<br>Set the value to ModifySecurityCheckScheduleConfig. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Lang | String | No | zh | The natural language of the request and response. Valid values:<br>• zh: Chinese<br>• en: English |

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| DaysOfWeek | String | No | 1,2,3 | The days on which the configuration check runs. You can specify multiple days. Separate multiple days with commas (,). Valid values:<br>• 1: Monday<br>• 2: Tuesday<br>• 3: Wednesday<br>• 4: Thursday<br>• 5: Friday<br>• 6: Saturday<br>• 7: Sunday |
| StartTime | Integer | No | 6 | The time period during which the configuration check starts. Valid values:<br>• 0: 00:00 to 06:00<br>• 6: 06:00 to 12:00<br>• 12: 12:00 to 18:00<br>• 18: 18:00 to 24:00 |
| EndTime | Integer | No | 12 | The time period during which the configuration check ends.<br>• 0: 00:00 to 06:00<br>• 6: 06:00 to 12:00<br>• 12: 12:00 to 18:00<br>• 18: 18:00 to 24:00 |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | 48D2E9A9-A1B0-4295-B727-0995757C47E9 | The ID of the request. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=ModifySecurityCheckScheduleConfig
&DaysOfWeek=1,2,3
&StartTime=6
&EndTime=12
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<ModifySecurityCheckScheduleConfig>
  <RequestId>48D2E9A9-A1B0-4295-B727-0995757C47E9</RequestId>
</ModifySecurityCheckScheduleConfig>
```

`JSON`  format

```json
{
    "RequestId":"48D2E9A9-A1B0-4295-B727-0995757C47E9"
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-6-9"></a>

### 3.6.9. DescribeRiskCheckItemResult

Queries the assets that have configuration risks based on a specific check item. Results are returned on different pages.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeRiskChec kItemResult | The operation that you want to perform.<br>Set the value to DescribeRiskCheckItemResult. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Lang | String | No | zh | The natural language of the request and response. Valid values:<br>• zh: Chinese<br>• en: English |
| ItemId | Long | No | 2 | The ID of the check item. |
| CurrentPage | Integer | No | 1 | The page number of the current page. |
| PageSize | Integer | No | 20 | The number of entries to return on each page. |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| PageContentRe source | Struct |  | The affected assets listed on each page. |
| ContentResourc e | Json | { "resultStatus": \[{"id": 32183150, "status": "failed" }\], "columns": \[{ "title": "Zone", "key": "RegionId" }, {"title": "Database instance ID", "key": "DBInstanceId" }, {"title": "Error entry value", "key": "VulValue" }\], "values": \[{"DBInstanceId": {"type": "link", "value": "dds-bp144b42843fed14\\ n", "url": "https://mongodb.console.aliyun.com/replicate/cn-hangzhou/instances/dds-bp144b42843fed14/basicInfo" }, "VulValue": { "type": "link", "value": "0.0.0.0/0", "url": "https://mongodb.console.aliyun.com/replicate/cn-hangzhou/instances/dds-bp144b42843fed14/whiteList" }, "RegionId": { "type": "text", "value": "China(Hangzhou)\\n " } }\], "emptyGridValue": {"type": "text", "value": "No data found" }, "type": "grid" } | The data of affected assets displayed on each page in a dynamic table. |
| Count | Integer | 1 | The number of entries returned on the current page. |
| CurrentPage | Integer | 1 | The page number of the current page. |
| PageCount | Integer | 3 | The total number of returned pages. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| TotalCount | Integer | 1 | The total number of entries. |
| RequestId | String | 3BFB4989-A108-46A4-954E-FF7EF02D1078 | The ID of the request. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribeRiskCheckItemResult
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<DescribeRiskCheckItemResultResponse>
      <PageContentResource>
            <TotalCount>1</TotalCount>
            <ContentResource>
                  <resultStatus>
                        <id>32183150</id>
                        <status>failed</status>
                  </resultStatus>
                  <columns>
                        <title>Zone</title>
                        <key>RegionId</key>
                  </columns>
                  <columns>
                        <title>Database instance ID</title>
                        <key>DBInstanceId</key>
                  </columns>
                  <columns>
                        <title>Error entry value</title>
                        <key>VulValue</key>
                  </columns>
                  <values>
                        <DBInstanceId>
                              <type>link</type>
                              <value>dds-bp144b42843xxxxx</value>
                              <url>https://mongodb.console.aliyun.com/replicate/cn-hangzhou/instances/dds-bp144b42843fed14/basicInfo</url>
                        </DBInstanceId>
                        <VulValue>
                              <type>link</type>
                              <value>0.0.0.0/0</value>
                              <url>https://mongodb.console.aliyun.com/replicate/cn-hangzhou/instances/dds-bp144b42843fed14/whiteList</url>
                        </VulValue>
                        <RegionId>
                              <type>text</type>
                              <value>China (Hangzhou)</value>
                        </RegionId>
                  </values>
                  <emptyGridValue>
                        <type>text</type>
                        <value>No data found</value>
                  </emptyGridValue>
                  <type>grid</type>
            </ContentResource>
            <PageCount>1</PageCount>
            <PageSize>10</PageSize>
            <CurrentPage>1</CurrentPage>
            <Count>1</Count>
      </PageContentResource>
      <requestId>3BFB4989-A108-46A4-954E-FF7EF02D1078</requestId>
</DescribeRiskCheckItemResultResponse>
```

`JSON`  format

```json
{
    "PageContentResource": {
        "TotalCount": 1,
        "ContentResource": {
            "resultStatus": [{
                "id": 32183150,
                "status": "failed"
                }],
            "columns": [{
                "title": "Zone",
                "key": "RegionId"
            }, {
                "title": "Database instance ID",
                "key": "DBInstanceId"
            }, {
                "title": "Error entry value",
                "key": "VulValue"
            }],
            "values": [{
                "DBInstanceId": {
                "type": "link",
                "value": "dds-bp144b42843xxxxx\n",
                "url": "https://mongodb.console.aliyun.com/replicate/cn-hangzhou/instances/dds-bp144b42843fed14/basicInfo"
                },
            "VulValue": {
                "type": "link",
                "value": "0.0.0.0/0",
                "url": "https://mongodb.console.aliyun.com/replicate/cn-hangzhou/instances/dds-bp144b42843fed14/whiteList"
                },
            "RegionId": {
                "type": "text",
                "value": "China (Hangzhou)\n"
                }
            }],
            "emptyGridValue": {
                "type": "text",
                "value": "No data found"
            },
            "type": "grid"
        },
        "PageCount": 1,
        "PageSize": 10,
        "CurrentPage": 1,
        "Count": 1
        },
    "requestId": "3BFB4989-A108-46A4-954E-FF7EF02D1078"
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-7"></a>

## 3.7. Brute-force attacks protection

<a id="section-3-7-1"></a>

### 3.7.1. CreateAntiBruteForceRule

Creates a defense rule against brute-force attacks protection.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | CreateAntiBruteF orceRule | The operation that you want to perform.<br>Set the value to CreateAntiBruteForceRule. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Name | String | No | The defense rules against brute-force attacks protection. | The name of the defense rule. |
| Span | Integer | No | 15 | The time period during which the number of logon attempts are calculated. |
| FailCount | Integer | No | 10 | The maximum number of logon attempts specified in the defense rule. |
| ForbiddenTime | Integer | No | 10 | The time period during which logons from the blocked IP address are blocked. |
| UuidList.N | RepeatLi st | No | uuid-1312133-ssas,uuid-1234-qwer-dss | The list of servers to which the defense rule is applied. |
| DefaultRule | Boolean | No | true | Specifies whether to set the defense rule as the default rule. Valid values:<br>• true: The defense rule is set as the default rule.<br>• false: The defense rule is not set as the default rule. |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| CreateAntiBrute ForceRule | Struct |  | The returned result of the defense rule. |
| RuleId | Long | 6363 | The ID of the defense rule. |
| RequestId | String | FB3E435F-4116-46F9-A5DE-C338DDA04F47 | The ID of the request. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=CreateAntiBruteForceRule
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<CreateAntiBruteForceRuleResponse>
  <CreateAntiBruteForceRule>
        <RuleId>6363</RuleId>
  </CreateAntiBruteForceRule>
  <requestId>FB3E435F-4116-46F9-A5DE-C338DDA04F47</requestId>
</CreateAntiBruteForceRuleResponse>
```

`JSON`  format

```json
{
    "CreateAntiBruteForceRule": {
        "RuleId": 6363
    },
    "requestId": "FB3E435F-4116-46F9-A5DE-C338DDA04F47"
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-7-2"></a>

### 3.7.2. ModifyAntiBruteForceRule

Modifies the defense rule against brute-force attacks protection.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | ModifyAntiBruteF orceRule | The operation that you want to perform.<br>Set the value to ModifyAntiBruteForceRule. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Id | Long | No | 6263 | The ID of the defense rule. |
| Name | String | No | Best practices | The name of the defense rule. |
| Span | Integer | No | 10 | The time period during which the number of logon attempts are calculated. |
| FailCount | Integer | No | 10 | The maximum number of logon attempts specified in the defense rule. |
| ForbiddenTime | Integer | No | 12 | The time period during which logons from the blocked IP address are blocked. |
| UuidList.N | RepeatLi st | No | uuid-13213-dasda | The list of servers to which the defense rule is applied. |
| DefaultRule | Boolean | No | true | Specifies whether to set the defense rule as the default rule.<br>• true: The defense rule is set as the default rule.<br>• false: The defense rule is not set as the default rule. |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | F35F45B0-5D6B-4238-BE02-A62D0760E840 | The ID of the request. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=ModifyAntiBruteForceRule
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<ModifyAntiBruteForceRuleResponse>
  <requestId>F35F45B0-5D6B-4238-BE02-A62D0760E840</requestId>
</ModifyAntiBruteForceRuleResponse>
```

`JSON`  format

```json
{
    "requestId": "F35F45B0-5D6B-4238-BE02-A62D0760E840"
}
```

<a id="section-3-8"></a>

## 3.8. Vulnerability management

<a id="section-3-8-1"></a>

### 3.8.1. ModifyVulTargetConfig

Configures vulnerability detection on a server.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | ModifyVulTarget Config | The operation that you want to perform.<br>Set the value to ModifyVulTargetConfig. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Type | String | No | vul | The type of the configuration. |
| Uuid | String | No | xxxx-xxxx-xxxx-xxxxx-xxxxxx | The UUID of the server. |
| Config | String | No | cms | The details of the configuration items. |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | 3A85CFCF-05C8-451A-9E41-C0D5E96BA407 | The ID of the request. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=ModifyVulTargetConfig
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<requestId>7E0618A9-D5EF-4220-9471-C42B5E92719F</requestId>
```

`JSON`  format

```json
{
  "requestId": "7E0618A9-D5EF-4220-9471-C42B5E92719F"
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-8-2"></a>

### 3.8.2. ModifyStartVulScan

Scans vulnerabilities on the Vulnerabilities page.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | ModifyStartVulSc an | The operation that you want to perform.<br>Set the value to ModifyStartVulScan. |
| Types | String | No | "cve,sys,cms,app, emg" | The types of vulnerabilities that can be detected by Threat Detection Service.Valid values:<br>• cve: Linux software vulnerabilities<br>• sys: Windows vulnerabilities<br>• cms: Web CMS vulnerabilities<br>• app: application vulnerabilities<br>• emg: emergency vulnerabilities<br>• image: container image vulnerabilities<br>Note If this parameter is not specified, all types of vulnerabilities are detected. |
| Uuids | String | No | {"i-sdada-xxxxx","i-ifaedada-sfsasdxxx"} | The list of servers. |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | 4066CAC3-F83A-4729-9995-A5558A61B546 | The ID of the request. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=ModifyStartVulScan
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<ModifyStartVulScanResponse>
      <requestId>4066CAC3-F83A-4729-9995-A5558A61B546</requestId>
</ModifyStartVulScanResponse>
```

`JSON`  format

```json
{    
    "requestId": "4066CAC3-F83A-4729-9995-A5558A61B546"
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-8-3"></a>

### 3.8.3. DescribeVulList

Queries vulnerabilities by type.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeVulList | The operation that you want to perform.<br>Set the value to DescribeVulList. |
| Type | String | Yes | cve | The type of the vulnerability. Valid values:<br>• cve: Linux software vulnerabilities<br>• sys: Windows vulnerabilities<br>• cms: Web CMS vulnerabilities<br>• app: application vulnerabilities<br>• emg: emergency vulnerabilities |
| Lang | String | No | zh | The natural language of the request and response. Valid values:<br>• zh: Chinese<br>• en: English |
| Remark | String | No | 1.2.3.4 | The tag to query, which can be the internal IP address, public IP address, or name of the asset. |
| Uuids | String | No | 1587bedb-fdb4-48c4-9330-\*\*\*\*\*\*\*\*\*\*\*\* | The ID of the asset. Separate multiple IDs with commas (,). |
| AliasName | String | No | RHSA-2019:0230-Important: polkit security update | The alias of the vulnerability. |
| Necessity | String | No | asap,later,nntf | The priority to fix vulnerabilities.Separate multiple priorities with commas (,). Valid values:<br>• asap: high<br>• later: medium<br>• nntf: low |
| Dealed | String | No | n | Specifies whether the vulnerability is handled. Valid values:<br>• y: handled<br>• n: unhandled |
| CurrentPage | Integer | No | 1 | The page number of the current page.Pages start from page 1. Default value: 1. |
| PageSize | Integer | No | 20 | The number of entries to return on each page. Default value: 20. |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | ECDE6715-6286-40E6-A32D-3094051FD74D | The ID of the request. |
| CurrentPage | Integer | 1 | The page number of the current page. |
| PageSize | Integer | 20 | The number of entries returned per page. |
| TotalCount | Integer | 2 | The total number of entries returned. |
| VulRecords | Array |  | The vulnerability information. |
| AliasName | String | RHSA-2017:0574: gnutls security, bug fix, and enhancement update | The alias of the vulnerability. |
| ExtendContentJ son | Struct |  | The extended information. |
| AbsolutePath | String | /roo/www/web | The package path of the software that has the vulnerability. |
| AliasName | String | RHSA-2017:0574: gnutls security, bug fix, and enhancement update | The alias of the vulnerability. |
| Ip | String | 1.2.3.1 | The public IP address of the asset that is affected by the vulnerability. |
| LastTs | Long | 1554189334000 | The timestamp when the vulnerability was last detected. |
| Necessity | Struct |  | Indicates whether the vulnerability needs to be fixed. |
| Assets_factor | String | 1 | The asset score. |
| Cvss_factor | String | 7.8 | The Common Vulnerability Scoring System (CVSS) score. |
| Enviroment_fac tor | String | 1.0 | The environmental score. |
| Gmt_create | String | 20190331 | The creation time. |
| Is_calc | String | 1 | Indicates whether the vulnerability severity score is calculated. Valid values:<br>• 0: The score is not calculated.<br>• 1: The score is calculated. |
| Status | String | normal | The status of the vulnerability severity score.Valid values:<br>• none: No score is generated.<br>• pending: The score is pending calculation.<br>• miss: The score failed to be calculated.<br>• normal: The calculation is normal. |
| Time_factor | String | 1.0 | The temporal score. |
| Total_score | String | 7.8 | The total vulnerability severity score. We recommend that you apply the following rules:<br>• Critical: The severity score is between 13.5 and 15, which typically represents a high-risk vulnerability.<br>• Important: The severity score is between 7.1 and 13.5, which typically represents a medium-risk vulnerability.<br>• Moderate: The severity score is below 7, which typically represents a low-risk vulnerability. |
| Os | String | centos | The operating system. |
| OsRelease | String | 7 | The version of the operating system. |
| PrimaryId | Long | 111 | The ID of the vulnerability. |
| RpmEntityList | Array |  | The details about the RPM package. |
| FullVersion | String | 3.10.0-693.2.2.el7 | The complete version number. |
| MatchDetail | String | python-perf version less than 0:3.10.0-693.21.1.el7 | The detailed matching information of the vulnerability. |
| Name | String | python-perf | The name of the RPM package. |
| Path | String | /usr/lib64/python2.7/site-packages | The path of the software that has the vulnerability. |
| UpdateCmd | String | \*\*\* update python-perf | The command that can be run to fix the vulnerability. |
| Version | String | 3.10.0 | The version of the operating system. |
| Status | Integer | 1 | The status of the vulnerability. Valid values:<br>• 1: unfixed<br>• 2: fix failed<br>• 3: rollback failed<br>• 4: fixing<br>• 5: rolling back<br>• 6: verifying<br>• 7: fixed<br>• 8: fixed and to be restarted<br>• 9: rolled back<br>• 10: ignored<br>• 11: rolled back and to be restarted<br>• 12: not found<br>• 20: expired |
| Tag | String | oval | The tag of the vulnerability. |
| cveList | List | \["CVE-2016-8610", "CVE-2017-5335" \] | The Common Vulnerabilities and Exposures (CVEs) list. |
| FirstTs | Long | 1554189334000 | The first time when the vulnerability was detected. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC. |
| GroupId | Integer | 281801 | The ID of the asset group. |
| InstanceId | String | i-bp18t\*\*\* | The ID of the asset instance. |
| InstanceName | String | Test ECS | The name of the asset instance. |
| InternetIp | String | 1.2.3.1 | The public IP address of the asset. |
| IntranetIp | String | 1.2.3.4 | The private IP address of the asset. |
| LastTs | Long | 1541207563000 | The timestamp when the vulnerability was last detected. |
| ModifyTs | Long | 1541207563000 | The timestamp when the vulnerability was modified. |
| Name | String | oval:com.redhat.rhs a:def:20170574 | The name of the vulnerability. |
| Necessity | String | asap | The priority to fix vulnerabilities. Valid values:<br>• asap: high<br>• later: medium<br>• nntf: low<br>Note We recommend that you fix the high-level vulnerabilities as soon as possible. |
| Online | Boolean | true | Indicates whether the asset instance is online. Valid values:<br>• true: online<br>• false: offline |
| OsVersion | String | linux | The version of the operating system. |
| PrimaryId | Long | 101162078 | The ID of the vulnerability. |
| Related | String | CVE-2017-7518,CVE-2017-12188 | The list of CVEs related to the vulnerability.Separate multiple CVEs with commas (,). |
| RepairTs | Long | 1541207563000 | The timestamp when the vulnerability was fixed. |
| ResultCode | String | 0 | The result code returned after the vulnerability is fixed. |
| ResultMessage | String | timeout | The message returned after the vulnerability is fixed. |
| Status | Integer | 1 | The status of the vulnerability. Valid values:<br>• 1: unfixed<br>• 2: fix failed<br>• 3: rollback failed<br>• 4: fixing<br>• 5: rolling back<br>• 6: verifying<br>• 7: fixed<br>• 8: fixed and to be restarted<br>• 9: rolled back<br>• 10: ignored<br>• 11: rolled back and to be restarted<br>• 12: not found<br>• 20: expired |
| Tag | String | oval | The tag of the vulnerability. |
| Type | String | cve | The type of the vulnerability. Valid values:<br>• cve: Linux vulnerabilities<br>• sys: Windows vulnerabilities<br>• cms: Web CMS vulnerabilities<br>• emg: emergency vulnerabilities<br>• app: application vulnerabilities |
| Uuid | String | 04c56617-23fc-43a5-ab9b-\*\*\*\*\*\*\*\*\*\*\*\* | The ID of the asset. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribeVulList
&Type=cve
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<DescribeVulListResponse>
      <TotalCount>2</TotalCount>
      <RequestId>ECDE6715-6286-40E6-A32D-3094051FD74D</RequestId>
      <PageSize>20</PageSize>
      <VulRecords>
            <Status>1</Status>
            <InstanceId>i-bp18t***</InstanceId>
            <OsVersion>linux</OsVersion>
            <LastTs>1541207563000</LastTs>
            <Necessity>asap</Necessity>
            <ResultMessage>timeout</ResultMessage>
            <IntranetIp>1.2.3.4</IntranetIp>
            <Name>oval:com.redhat.rhsa:def:20170574</Name>
            <GroupId>281801</GroupId>
            <RepairTs>1541207563000</RepairTs>
            <InstanceName>Test ECS</InstanceName>
            <Type>cve</Type>
            <FirstTs>1554189334000</FirstTs>
            <Uuid>04c56617-23fc-43a5-ab9b-************</Uuid>
            <Related>CVE-2017-7518,CVE-2017-12188</Related>
            <ModifyTs>1541207563000</ModifyTs>
            <InternetIp>1.2.3.1</InternetIp>
            <AliasName>RHSA-2017:0574: gnutls security, bug fix, and enhancement update</AliasName>
            <Tag>oval</Tag>
            <Online>true</Online>
            <PrimaryId>101162078</PrimaryId>
            <ResultCode>0</ResultCode>
      </VulRecords>
      <VulRecords>
            <ExtendContentJson>
                  <Status>1</Status>
                  <Os>centos</Os>
                  <AliasName>RHSA-2017:0574: gnutls security, bug fix, and enhancement update</AliasName>
                  <Ip>1.2.3.1</Ip>
                  <LastTs>1554189334000</LastTs>
                  <cveList>["CVE-2016-8610", "CVE-2017-5335" ]</cveList>
                  <Necessity>
                        <Status>normal</Status>
                        <Total_score>7.8</Total_score>
                        <Gmt_create>20190331</Gmt_create>
                        <Cvss_factor>7.8</Cvss_factor>
                        <Time_factor>1.0</Time_factor>
                        <Is_calc>1</Is_calc>
                        <Enviroment_factor>1.0</Enviroment_factor>
                        <Assets_factor>1</Assets_factor>
                  </Necessity>
                  <RpmEntityList>
                        <Path>/usr/lib64/python2.7/site-packages</Path>
                        <UpdateCmd>*** update python-perf</UpdateCmd>
                        <Version>3.10.0</Version>
                        <FullVersion>3.10.0-693.2.2.el7</FullVersion>
                        <MatchDetail>python-perf version less than 0:3.10.0-693.21.1.el7</MatchDetail>
                        <Name>python-perf</Name>
                  </RpmEntityList>
                  <Tag>oval</Tag>
                  <OsRelease>7</OsRelease>
                  <AbsolutePath>/roo/www/web</AbsolutePath>
                  <PrimaryId>111</PrimaryId>
            </ExtendContentJson>
      </VulRecords>
      <CurrentPage>1</CurrentPage>
</DescribeVulListResponse>
```

`JSON`  format

```json
{
        "TotalCount": "2",
        "RequestId": "ECDE6715-6286-40E6-A32D-3094051FD74D",
        "PageSize": "20",
        "VulRecords": [{
            "Status": "1",
            "InstanceId": "i-bp18t***",
            "OsVersion": "linux",
            "LastTs": "1541207563000",
            "Necessity": "asap",
            "ResultMessage": "timeout",
            "IntranetIp": "1.2.3.4",
            "Name": "oval:com.redhat.rhsa:def:20170574",
            "GroupId": "281801",
            "RepairTs": "1541207563000",
            "InstanceName": "Test ECS",
            "Type": "cve",
            "FirstTs": "1554189334000",
            "Uuid": "04c56617-23fc-43a5-ab9b-************",
            "Related": "CVE-2017-7518,CVE-2017-12188",
            "ModifyTs": "1541207563000",
            "InternetIp": "1.2.3.1",
            "AliasName": "RHSA-2017:0574: gnutls security, bug fix, and enhancement update",
            "Tag": "oval",
            "Online": "true",
            "PrimaryId": "101162078",
            "ResultCode": "0"
        }, {
            "ExtendContentJson": {
                "Status": "1",
                "Os": "centos",
                "AliasName": "RHSA-2017:0574: gnutls security, bug fix, and enhancement update",
                "Ip": "1.2.3.1",
                "LastTs": "1554189334000",
                "cveList": "[\"CVE-2016-8610\", \"CVE-2017-5335\" ]",
                "Necessity": {
                    "Status": "normal",
                    "Total_score": "7.8",
                    "Gmt_create": "20190331",
                    "Cvss_factor": "7.8",
                    "Time_factor": "1.0",
                    "Is_calc": "1",
                    "Enviroment_factor": "1.0",
                    "Assets_factor": "1"
                },
                "RpmEntityList": [{
                    "Path": "/usr/lib64/python2.7/site-packages",
                    "UpdateCmd": "*** update python-perf",
                    "Version": "3.10.0",
                    "FullVersion": "3.10.0-693.2.2.el7",
                    "MatchDetail": "python-perf version less than 0:3.10.0-693.21.1.el7",
                    "Name": "python-perf"
                }],
                "Tag": "oval",
                "OsRelease": "7",
                "AbsolutePath": "/roo/www/web",
                "PrimaryId": "111"
            }
        }],
        "CurrentPage": "1"
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-8-4"></a>

### 3.8.4. DescribeEmgVulGroup

Queries emergency vulnerabilities by group.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeEmgVulG roup | The operation that you want to perform.<br>Set the value to DescribeEmgVulGroup. |
| Lang | String | No | zh | The natural language of the request and response. Valid values:<br>• zh: Chinese<br>• en: English |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| EmgVulGroupLi st | Array |  | The information about the group of emergency vulnerabilities. |
| AliasName | String | Jenkins High-risk Remote Security Vulnerability (CVE -2018 - 1999001 and CVE - 2018 -1999002) | The alias of the vulnerability. |
| Description | String | Jenkins is an open-source program written in Java. It can be used to monitor continuous and duplicate jobs for continuous software integration.\\n\\nJenkins contains an arbitrary file read vulnerability.Attackers can remotely send malicious HTTP requests to the Jenkins Web server and obtain the specified file content from responses returned by the server. | The description of the vulnerability. |
| GmtPublish | Long | 1532592480000 | The timestamp when the vulnerability was released. |
| Name | String | scan:ACSV-2018-072601 | The name of the vulnerability. |
| PendingCount | Integer | 0 | The number of pending vulnerabilities. |
| Type | String | scan | How the vulnerability is exploited.<br>• scan: scans data by using plug-ins.<br>• python: scans data by using scripts. |
| RequestId | String | E836EDA2-DBFB-489E-8FD3-5B141EB81A9C | The ID of the request. |
| TotalCount | Integer | 2 | The total number of vulnerabilities. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribeEmgVulGroup
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<DescribeEmgVulGroup>
  <TotalCount>2</TotalCount>
  <EmgVulGroupList>
        <Name>scan:ACSV-2018-072601</Name>
        <Status>30</Status>
        <Description>Jenkins is an open-source program written in Java. It can be used to monitor continuous and duplicate jobs for continuous software integration.
Jenkins contains an arbitrary file read vulnerability. Attackers can remotely send malicious HTTP requests to the Jenkins Web server and obtain the specified file content from responses returned by the server. </Description>
        <PendingCount>0</PendingCount>
        <AliasName>Jenkins High-risk Remote Security Vulnerability (CVE - 2018 - 1999001 and CVE - 2018 - 1999002)</AliasName>
        <Type>scan</Type>
        <GmtPublish>1532592480000</GmtPublish>
  </EmgVulGroupList>
  <EmgVulGroupList>
        <Name>scan:acsv-2018-082001</Name>
        <Status>30</Status>
        <Description>Recently, security researchers revealed multiple high-risk Metinfo vulnerabilities, such as arbitrary file read, XML External Entity (XXE), and sensitive information leak. </Description>
        <PendingCount>0</PendingCount>
        <AliasName>Metinfo Multiple High-risk Vulnerabilities</AliasName>
        <Type>scan</Type>
        <GmtPublish>1534767031000</GmtPublish>
  </EmgVulGroupList>
  <RequestId>E836EDA2-DBFB-489E-8FD3-5B141EB81A9C</RequestId>
</DescribeEmgVulGroup>
```

`JSON`  format

```json
{
 "TotalCount":2,
 "EmgVulGroupList":[
  {
   "Name":"scan:ACSV-2018-072601",
   "Status":30,
   "Description":"Jenkins is an open-source program written in Java. It can be used to monitor continuous and duplicate jobs for continuous software integration. \n\nJenkins containsan arbitrary file read vulnerability. Attackers can remotely send malicious HTTP requests to the Jenkins Web server and obtain the specified file content from responses returned by the server.",
   "PendingCount":0,
   "AliasName":"Jenkins High-risk Remote Security Vulnerability (CVE - 2018 - 1999001 and C
VE - 2018 - 1999002)",
   "Type":"scan",
   "GmtPublish":1532592480000
  },
  {
   "Name":"scan:acsv-2018-082001",
   "Status":30,
   "Description":"Recently, security researchers revealed multiple high-risk Metinfo vulnerabilities, such as arbitrary file read, XML External Entity (XXE), and sensitive information leak.
   "PendingCount":0,
   "AliasName":"Metinfo Multiple High-risk Vulnerabilities",
   "Type":"scan",
   "GmtPublish":1534767031000
  }
 ],
 "RequestId":"E836EDA2-DBFB-489E-8FD3-5B141EB81A9C"
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-8-5"></a>

### 3.8.5. DescribeVulWhitelist

Queries the whitelist of vulnerabilities by page.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeVulWhite list | The operation that you want to perform.<br>Set the value to DescribeVulWhitelist. |
| CurrentPage | Integer | No | 1 | The number of the page to return.Pages start from page 1. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Default value: 20. |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| CurrentPage | Integer | 1 | The page number of the current page. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| RequestId | String | 74F97EF7-B543-43FD-A4E9-18456731F9C5 | The ID of the request. |
| TotalCount | Integer | 1 | The total number of returned entries. |
| VulWhitelists | Array |  | The information about the vulnerability whitelist. |
| AliasName | String | RHSA-2017:3263: curl security update | The alias of the vulnerability. |
| Name | String | oval:com.redhat.rhs a:def:20173263 | The name of the vulnerability. |
| Reason | String | Not urgent | The reason for adding the vulnerability to the whitelist. |
| Type | String | cve | The type of the vulnerability. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribeVulWhitelist
&<Common request parameters>
```

Sample success responses `XML`  format

```xml
<DescribeVulWhitelist>
  <TotalCount>1</TotalCount>
  <VulWhitelists>
        <Name>oval:com.redhat.rhsa:def:20173263</Name>
        <AliasName>RHSA-2017:3263: curl security update</AliasName>
        <Type>cve</Type>
        <Reason>Not urgent</Reason>
  </VulWhitelists>
  <PageSize>3</PageSize>
  <RequestId>74F97EF7-B543-43FD-A4E9-18456731F9C5</RequestId>
  <CurrentPage>1</CurrentPage>
</DescribeVulWhitelist>
```

`JSON`  format

```json
{
 "TotalCount":1,
 "PageSize":3,
 "VulWhitelists":[
  {
   "Name":"oval:com.redhat.rhsa:def:20173263",
   "AliasName":"RHSA-2017:3263: curl security update",
   "Type":"cve",
   "Reason":"Not urgent"
  }
 ],
 "RequestId":"74F97EF7-B543-43FD-A4E9-18456731F9C5",
 "CurrentPage":1
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-8-6"></a>

### 3.8.6. DescribeConcernNecessity

Queries the priority to fix the vulnerability.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeConcern Necessity | The operation that you want to perform. Set the value to DescribeConcernNecessity. |
| Lang | String | No | zh | The natural language of the request and response. Valid values:<br>• zh: Chinese<br>• en: English |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| ConcernNecessi ty | List | \[ "asap", "later", "nntf"\] | The priority to fix the vulnerability. Valid values:<br>• asap: high<br>• later: medium<br>• nntf: low |
| RequestId | String | 9139DAF6-5CE0-49A0-926E-07243A290F70 | The ID of the request. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribeConcernNecessity
&Lang=zh
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<DescribeConcernNecessity>
  <ConcernNecessity>asap</ConcernNecessity>
  <ConcernNecessity>later</ConcernNecessity>
  <ConcernNecessity>nntf</ConcernNecessity>
  <RequestId>9139DAF6-5CE0-49A0-926E-07243A290F70</RequestId>
</DescribeConcernNecessity>
```

`JSON`  format

```json
{
 "ConcernNecessity":[
  "asap",
  "later",
  "nntf"
 ],
 "RequestId":"9139DAF6-5CE0-49A0-926E-07243A290F70"
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-8-7"></a>

### 3.8.7. DescribeGroupedVul

Queries information about vulnerabilities by group.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeGrouped Vul | The operation that you want to perform. Set the value to DescribeGroupedVul. |
| Lang | String | No | zh | The natural language of the request and response. Valid values:<br>• zh: Chinese<br>• en: English |
| Type | String | No | cve | The type of the vulnerability. Valid values:<br>• cve: Linux vulnerabilities<br>• sys: Windows vulnerabilities<br>• cms: Web CMS vulnerabilities<br>• app: application vulnerabilities<br>• emg: emergency vulnerabilities |
| Uuids | String | No | d42f938c-d962-48a0-90f9-05e4ea\*\*\*\*\*\* | The IDs of the asset instances.Separate multiple IDs with commas (,). |
| AliasName | String | No | RHSA-2019:0230-Important: polkit security update | The alias of the vulnerability. |
| Necessity | String | No | asap,later,nntf | The priority to fix the vulnerability.Separate multiple priorities with commas (,). Valid values:<br>• asap: high<br>• later: medium<br>• nntf: low |
| Dealed | String | No | n | Specifies whether the vulnerability is handled.<br>• y: handled<br>• n: unhandled |
| CurrentPage | Integer | No | 1 | The page number of the current page.Pages start from page 1. Default value: 1. |
| PageSize | Integer | No | 20 | The number of entries to return on each page. Default value: 20. |
| GroupId | String | No | weds\*\*\*\* | The ID of the asset group. |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | 0DFCADBA-7065-42DA-AF17-6868B9C2A8CF | The ID of the request. |
| PageSize | Integer | 20 | The number of entries returned per page. |
| CurrentPage | Integer | 1 | The page number of the current page. |
| TotalCount | Integer | 2 | The total number of entries returned. |
| GroupedVulIte ms | Array |  | Details about vulnerabilities by group. |
| Name | String | \*\*\*glibc security and bug fixes | The name of the vulnerability. |
| AliasName | String | RHSA-2019:0230-Important: polkit security update | The alias of the vulnerability. |
| Type | String | cve | The type of the vulnerability. Valid values:<br>• cve: Linux vulnerabilities<br>• sys: Windows vulnerabilities<br>• cms: Web CMS vulnerabilities<br>• app: application vulnerabilities<br>• emg: emergency vulnerabilities |
| GmtLast | Long | 1554185744000 | The time when the vulnerability was last detected. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC. |
| AsapCount | Integer | 0 | The number of high-priority vulnerabilities. |
| LaterCount | Integer | 0 | The number of medium-priority vulnerabilities. |
| NntfCount | Integer | 59 | The number of low-priority vulnerabilities. |
| HandledCount | Integer | 0 | The total number of handled vulnerabilities. |
| Tags | String | Force restart | The tag of the vulnerability. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribeGroupedVul
&Lang=zh
&Type=cve
&AliasName=RHSA-2019:0230-Important: polkit security update
&Necessity=asap,later,nntf
&Dealed=n
&CurrentPage=1
&PageSize=20
&<Common request parameters>
```

Sample success responses `XML`  format

```xml
<DescribeGroupedVul>
  <GroupedVulItems>
        <Tags></Tags>
        <LaterCount>0</LaterCount>
        <AliasName>RHSA-2019:0230-Important: polkit security update</AliasName>
        <AsapCount>0</AsapCount>
        <Type>cve</Type>
        <NntfCount>59</NntfCount>
        <GmtLast>1554185744000</GmtLast>
        <HandledCount>0</HandledCount>
  </GroupedVulItems>
  <GroupedVulItems>
        <Tags></Tags>
        <LaterCount>0</LaterCount>
        <AliasName>RHSA-2019:0368-Important: systemd security update</AliasName>
        <AsapCount>0</AsapCount>
        <Type>cve</Type>
        <NntfCount>59</NntfCount>
        <GmtLast>1554185744000</GmtLast>
        <HandledCount>0</HandledCount>
  </GroupedVulItems>
  <TotalCount>432</TotalCount>
  <PageSize>2</PageSize>
  <RequestId>0DFCADBA-7065-42DA-AF17-6868B9C2A8CF</RequestId>
  <CurrentPage>1</CurrentPage>
</DescribeGroupedVul>
```

`JSON`  format

```json
{
    "GroupedVulItems": [
        {
            "Tags": "",
            "LaterCount": 0,
            "AliasName": "RHSA-2019:0230-Important: polkit security update",
            "AsapCount": 0,
            "Type": "cve",
            "NntfCount": 59,
            "GmtLast": 1554185744000,
            "HandledCount": 0
        },
        {
            "Tags": "",
            "LaterCount": 0,
            "AliasName": "RHSA-2019:0368-Important: systemd security update",
            "AsapCount": 0,
            "Type": "cve",
            "NntfCount": 59,
            "GmtLast": 1554185744000,
            "HandledCount": 0
        }
    ],
    "TotalCount": 432,
    "PageSize": 2,
    "RequestId": "0DFCADBA-7065-42DA-AF17-6868B9C2A8CF",
    "CurrentPage": 1
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-8-8"></a>

### 3.8.8. ModifyCreateVulWhitelist

Creates a vulnerability whitelist. Vulnerabilities added to the whitelist no longer trigger alerts.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | ModifyCreateVul Whitelist | The operation that you want to perform. Set the value to ModifyCreateVulWhitelist. |
| Reason | String | No | The vulnerability does not pose any threat. | The reason for adding the vulnerability to the whitelist. |
| Whitelist | String | No | \[{"name":"oval:c om.redhat.rhsa:d ef:20173263","ty pe":"cve","aliasN ame":"RHSA-2017:3263: curl security update"}\] | The information about the vulnerability added to the whitelist, in the JSON format. |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | DFE4F166-1AC9-4FAC-A4E4-F0608AD705A6 | The ID of the request. |

Examples

Sample requests

```text
/?Action=ModifyCreateVulWhitelist
&Reason=The vulnerability does not pose any threat.
&Whitelist=[{"name":"oval:com.redhat.rhsa:def:20173263","type":"cve","aliasName":"RHSA-2017:3263: curl security update"}]
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<ModifyCreateVulWhitelist>
  <RequestId>DFE4F166-1AC9-4FAC-A4E4-F0608AD705A6</RequestId>
</ModifyCreateVulWhitelist>
```

`JSON`  format

```json
{
 "RequestId":"DFE4F166-1AC9-4FAC-A4E4-F0608AD705A6"
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-8-9"></a>

### 3.8.9. ModifyEmgVulSubmit

Performs a scan task for emergency vulnerabilities.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | ModifyEmgVulSu bmit | The operation that you want to perform.<br>Set the value to ModifyEmgVulSubmit. |
| Lang | String | No | zh | The natural language of the request and response. Valid values:<br>• zh: Chinese<br>• en: English |
| Name | String | No | scan:ASCV-2019-032401 | The name of the vulnerability. |
| UserAgreement | String | No | yes | Specifies whether you want to perform a scan task. Valid values:<br>• yes<br>• no |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | 52A3AEE6-114A-499D-8990-4BA9B27FE0AA | The ID of the request. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=ModifyEmgVulSubmit
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<ModifyEmgVulSubmitResponse>
      <RequestId>52A3AEE6-114A-499D-8990-4BA9B27FE0AA</RequestId>
</ModifyEmgVulSubmitResponse>
```

`JSON`  format

```json
{
    "RequestId": "52A3AEE6-114A-499D-8990-4BA9B27FE0AA"
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-8-10"></a>

### 3.8.10. DescribeAutoDelConfig

Queries the configurations for automatic vulnerability deletion.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeAutoDelC onfig | The operation that you want to perform.<br>Set the value to DescribeAutoDelConfig. |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | 43186B14-5A39-44E0-860E-8B24D1EF82CC | The ID of the request. |
| Days | Integer | 7 | The number of days that a detected vulnerability is retained. |

Examples

Sample requests

```text
/?Action=DescribeAutoDelConfig
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<DescribeAutoDelConfig>
  <RequestId>43186B14-5A39-44E0-860E-8B24D1EF82CC</RequestId>
  <Days>7</Days>
</DescribeAutoDelConfig>
```

`JSON`  format

```json
{
    "RequestId": "43186B14-5A39-44E0-860E-8B24D1EF82CC",
    "Days": 7
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-8-11"></a>

### 3.8.11. ModifyOperateVul

Performs operations on detected vulnerabilities, including verifying, ignoring, fixing.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | ModifyOperateVu l | The operation that you want to perform. Set the value to ModifyOperateVul. |
| Info | String | No | \[{"name":"oval:c om.redhat.rhsa:d ef:20171100","uu id":"e49fb179-bbe7-4b6c-ab65-e106fb58d235","t ag":"oval"}\] | The information required to manage vulnerabilities. It is a JSON string that consists of the UUID, name, and tag fields. |
| OperateType | String | No | vul_ignore | The operation that you want to perform on the vulnerability.<br>• vul_fix: fixes the vulnerability.<br>• vul_verify: verifies the vulnerability.<br>• vul_rebooted: verifies the vulnerability after the server is restarted.<br>• vul_rollback: rolls back the vulnerability.<br>• vul_ignore: ignores the vulnerability.<br>• vul_undo_ignore: cancels the ignore operation on the vulnerability.<br>• vul_delete: deletes the vulnerability. |
| Reason | String | No | Postpone the fix | The reason why the vulnerability is ignored. |
| Type | String | No | cve | The type of the vulnerability.<br>• cve: Linux software vulnerabilities<br>• sys: Windows vulnerabilities<br>• cms: Web CMS vulnerabilities<br>• emg: emergency vulnerabilities |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | DFE4F166-1AC9-4FAC-A4E4-F0608AD705A6 | The ID of the request. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=ModifyOperateVul
&Info=[{"name":"oval:com.redhat.rhsa:def:20171100","uuid":"e49fb179-bbe7-4b6c-ab65-e106fb58d235","tag":"oval"}]
&OperateType=vul_ignore
&Type=cve
&Reason=Postpone the fix
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<ModifyOperateVul>
  <RequestId>DFE4F166-1AC9-4FAC-A4E4-F0608AD705A6</RequestId>
</ModifyOperateVul>
```

`JSON`  format

```json
{
 "RequestId":"DFE4F166-1AC9-4FAC-A4E4-F0608AD705A6"
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-9"></a>

## 3.9. Baseline check

<a id="section-3-9-1"></a>

### 3.9.1. DescribeCheckWarningSummary

Queries the statistical information about baseline check results. The information includes the number of servers on which a baseline check is performed, the number of baseline check items, and the last check pass rate.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeCheckWa rningSummary | The operation that you want to perform.<br>Set the value to DescribeCheckWarningSummary. |
| CurrentPage | Integer | No | 1 | The page number of the current page. |
| Lang | String | No | zh | The natural language of the request and response. Valid values:<br>• zh: Chinese<br>• en: English |
| PageSize | Integer | No | 10 | The number of entries to return on each page. |
| RiskName | String | No | Redis security baseline check | The name of the risk item. |
| RiskStatus | Integer | No | 1 | The status of the baseline check. Valid values:<br>• 1: failed<br>• 3: passed |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Status | String | No | 1 | The status of the check item. Valid values:<br>• 1: failed<br>• 2: verifying<br>• 3: passed<br>• 5: expired<br>• 6: ignored |
| StrategyId | Long | No | 1 | The ID of the baseline check policy. |
| TypeName | String | No | database | The level-1 type of check items. |
| Uuids | String | No | f03259d8-1e81-4fae-bcbb-275fb5\*\*\*\*\*\* | The ID of the server. |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| Count | Integer | 10 | The number of check items returned on the current page. |
| CurrentPage | Integer | 1 | The page number of the current page. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| RequestId | String | 00BD7CE2-284A-4534-BD09-FB69836DD750 | The ID of the request. |
| TotalCount | Integer | 100 | The total number of baseline check items. |
| WarningSumma rys | Array |  | The statistics of check items. |
| CheckCount | Integer | 10 | The number of check items. |
| HighWarningCo unt | Integer | 1 | The number of high-risk items. |
| LastFoundTime | String | 2019-01-01 12:23:00 | The time when the last baseline check was performed. |
| Level | String | high | The severity level of the risk item. Valid values:<br>• High<br>• Medium<br>• Low |
| LowWarningCo unt | Integer | 3 | The number of low-risk check items. |
| MediumWarnin gCount | Integer | 2 | The number of medium-risk check items. |
| RiskId | Long | 1 | The ID of the risk item. |
| RiskName | String | Redis password | The name of the risk item. |
| SubTypeAlias | String | Redis | The level-2 type of the risk item. |
| TypeAlias | String | Database | The type of the check item. Valid values: database, system, weak password, and middleware. |
| WarningMachin eCount | Integer | 11 | The number of assets on which risk items are detected. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribeCheckWarningSummary
&Lang=zh
&TypeName=database
&Status=1
&RiskStatus=1
&RiskName=Redis security baseline check
&StrategyId=1
&Uuids=f03259d8-1e81-4fae-bcbb-275fb55efb34
&CurrentPage=1
&PageSize=20
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<DescribeCheckWarningSummary>
   <TotalCount>25</TotalCount>
   <PageSize>20</PageSize>
   <RequestId>DFA6CDC5-E826-4D18-A499-BEF9DA31F1AD</RequestId>
   <CurrentPage>1</CurrentPage>
   <Count>20</Count>
   <WarningSummarys>
      <RiskId>43</RiskId>
      <LastFoundTime>2019-04-10 00:33:00</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>3</WarningMachineCount>
      <CheckCount>16</CheckCount>
      <HighWarningCount>8</HighWarningCount>
      <Level>high</Level>
      <TypeAlias>System</TypeAlias>
      <SubTypeAlias>
   CentOS Linux 7 security baseline check
                              </SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>
   CentOS Linux 7 security baseline check
                              </RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>47</RiskId>
      <LastFoundTime>2019-04-10 00:58:11</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>2</WarningMachineCount>
      <CheckCount>15</CheckCount>
      <HighWarningCount>7</HighWarningCount>
      <Level>medium</Level>
      <TypeAlias>System</TypeAlias>
      <SubTypeAlias>CentOS Linux 7 security standard compliance - MLPS level-3</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>CentOS Linux 7 security standard compliance - MLPS level-3</RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>48</RiskId>
      <LastFoundTime>2019-04-10 00:58:11</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>2</WarningMachineCount>
      <CheckCount>12</CheckCount>
      <HighWarningCount>6</HighWarningCount>
      <Level>medium</Level>
      <TypeAlias>System</TypeAlias>
      <SubTypeAlias>CentOS Linux 7 security standard compliance - MLPS level-2</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>CentOS Linux 7 security standard compliance - MLPS level-2</RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>3</RiskId>
      <LastFoundTime>2019-04-10 08:31:32</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>1</WarningMachineCount>
      <CheckCount>1</CheckCount>
      <HighWarningCount>1</HighWarningCount>
      <Level>high</Level>
      <TypeAlias>Database</TypeAlias>
      <SubTypeAlias>Redis security baseline check</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>Redis security baseline check</RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>19</RiskId>
      <LastFoundTime>2019-04-10 08:31:32</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>1</WarningMachineCount>
      <CheckCount>1</CheckCount>
      <HighWarningCount>1</HighWarningCount>
      <Level>high</Level>
      <TypeAlias>Weak password</TypeAlias>
      <SubTypeAlias>Linux weak password</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>Linux weak password</RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>12</RiskId>
      <LastFoundTime>2019-04-10 08:31:32</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>1</WarningMachineCount>
      <CheckCount>1</CheckCount>
      <HighWarningCount>1</HighWarningCount>
      <Level>high</Level>
      <TypeAlias>Weak password</TypeAlias>
      <SubTypeAlias>Anonymous FTP logon</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>Anonymous FTP logon</RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>13</RiskId>
      <LastFoundTime>2019-04-10 06:58:58</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>1</WarningMachineCount>
      <CheckCount>1</CheckCount>
      <HighWarningCount>1</HighWarningCount>
      <Level>high</Level>
      <TypeAlias>Weak password</TypeAlias>
      <SubTypeAlias>Windows weak password</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>Windows weak password</RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>23</RiskId>
      <LastFoundTime>2019-04-10 14:00:17</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>0</WarningMachineCount>
      <CheckCount>8</CheckCount>
      <HighWarningCount>0</HighWarningCount>
      <Level>medium</Level>
      <TypeAlias>Middleware</TypeAlias>
      <SubTypeAlias>Apache Tomcat security baseline check</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>Apache Tomcat security baseline check</RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>2</RiskId>
      <LastFoundTime>2019-04-10 08:31:32</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>0</WarningMachineCount>
      <CheckCount>1</CheckCount>
      <HighWarningCount>0</HighWarningCount>
      <Level>high</Level>
      <TypeAlias>Weak password</TypeAlias>
      <SubTypeAlias>PostgreSQL weak password</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>PostgreSQL weak password</RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>11</RiskId>
      <LastFoundTime>2019-04-10 08:31:32</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>0</WarningMachineCount>
      <CheckCount>1</CheckCount>
      <HighWarningCount>0</HighWarningCount>
      <Level>high</Level>
      <TypeAlias>Weak password</TypeAlias>
      <SubTypeAlias>MySQL weak password</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>MySQL weak password</RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>20</RiskId>
      <LastFoundTime>2019-04-10 08:31:32</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>0</WarningMachineCount>
      <CheckCount>1</CheckCount>
      <HighWarningCount>0</HighWarningCount>
      <Level>high</Level>
      <TypeAlias>Weak password</TypeAlias>
      <SubTypeAlias>FTP weak password</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>FTP weak password</RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>17</RiskId>
      <LastFoundTime>2019-04-10 06:58:58</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>0</WarningMachineCount>
      <CheckCount>1</CheckCount>
      <HighWarningCount>0</HighWarningCount>
      <Level>high</Level>
      <TypeAlias>Weak password</TypeAlias>
      <SubTypeAlias>Microsoft SQL Server weak password</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>Microsoft SQL Server weak password</RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>24</RiskId>
      <LastFoundTime>2019-04-10 06:52:05</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>0</WarningMachineCount>
      <CheckCount>2</CheckCount>
      <HighWarningCount>0</HighWarningCount>
      <Level>medium</Level>
      <TypeAlias>Database</TypeAlias>
      <SubTypeAlias>Memcached security baseline check</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>Memcached security baseline check</RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>42</RiskId>
      <LastFoundTime>2019-02-19 14:59:17</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>0</WarningMachineCount>
      <CheckCount>16</CheckCount>
      <HighWarningCount>0</HighWarningCount>
      <Level>high</Level>
      <TypeAlias>System</TypeAlias>
      <SubTypeAlias>CentOS Linux 6 security baseline check</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>CentOS Linux 6 security baseline check</RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>49</RiskId>
      <LastFoundTime>2019-02-19 14:59:17</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>0</WarningMachineCount>
      <CheckCount>12</CheckCount>
      <HighWarningCount>0</HighWarningCount>
      <Level>medium</Level>
      <TypeAlias>System</TypeAlias>
      <SubTypeAlias>CentOS Linux 6 security standard compliance - MLPS level-2</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>CentOS Linux 6 security standard compliance - MLPS level-2</RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>50</RiskId>
      <LastFoundTime>2019-02-19 14:59:17</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>0</WarningMachineCount>
      <CheckCount>15</CheckCount>
      <HighWarningCount>0</HighWarningCount>
      <Level>medium</Level>
      <TypeAlias>System</TypeAlias>
      <SubTypeAlias>CentOS Linux 6 security standard compliance - MLPS level-3</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>CentOS Linux 6 security standard compliance - MLPS level-3</RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>55</RiskId>
      <LastFoundTime>2019-02-19 12:57:23</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>0</WarningMachineCount>
      <CheckCount>14</CheckCount>
      <HighWarningCount>0</HighWarningCount>
      <Level>medium</Level>
      <TypeAlias>System</TypeAlias>
      <SubTypeAlias>Linux Ubuntu security standard compliance - MLPS level-2</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>Linux Ubuntu security standard compliance - MLPS level-2</RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>56</RiskId>
      <LastFoundTime>2019-02-19 12:57:23</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>0</WarningMachineCount>
      <CheckCount>15</CheckCount>
      <HighWarningCount>0</HighWarningCount>
      <Level>medium</Level>
      <TypeAlias>System</TypeAlias>
      <SubTypeAlias>Linux Ubuntu security standard compliance - MLPS level-3</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>Linux Ubuntu security standard compliance - MLPS level-3</RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>54</RiskId>
      <LastFoundTime>2019-02-19 12:57:23</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>0</WarningMachineCount>
      <CheckCount>16</CheckCount>
      <HighWarningCount>0</HighWarningCount>
      <Level>high</Level>
      <TypeAlias>System</TypeAlias>
      <SubTypeAlias>Linux Ubuntu security baseline check</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>Linux Ubuntu security baseline check</RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>51</RiskId>
      <LastFoundTime>2019-02-19 12:44:58</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>0</WarningMachineCount>
      <CheckCount>12</CheckCount>
      <HighWarningCount>0</HighWarningCount>
      <Level>high</Level>
      <TypeAlias>System</TypeAlias>
      <SubTypeAlias>Windows 2012 R2 security baseline check</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>Windows 2012 R2 security baseline check</RiskName>
   </WarningSummarys>
</DescribeCheckWarningSummary>
```

`JSON`  format

```json
{
 "Count":20,
 "TotalCount":25,
 "WarningSummarys":[
  {
   "SubTypeAlias":"CentOS Linux 7 security baseline check\n                                
\n                            ",
   "HighWarningCount":8,
   "WarningMachineCount":3,
   "RiskName":"CentOS Linux 7 security baseline check\n                                \n  
",
   "LowWarningCount":0,
   "CheckCount":16,
   "RiskId":43,
   "Level":"high",
   "MediumWarningCount":0,
   "TypeAlias":"System",
   "LastFoundTime":"2019-04-10 00:33:00"
  },
  {
   "SubTypeAlias":"CentOS Linux 7 security standard compliance - MLPS level-3",
   "HighWarningCount":7,
   "WarningMachineCount":2,
   "RiskName":"CentOS Linux 7 security standard compliance - MLPS level-3",
   "LowWarningCount":0,
   "CheckCount":15,
   "RiskId":47,
   "Level":"medium",
   "MediumWarningCount":0,
   "TypeAlias":"System",
   "LastFoundTime":"2019-04-10 00:58:11"
  },
  {
   "SubTypeAlias":"CentOS Linux 7 security standard compliance - MLPS level-2",
   "HighWarningCount":6,
   "WarningMachineCount":2,
   "RiskName":"CentOS Linux 7 security standard compliance - MLPS level-2",
   "LowWarningCount":0,
   "CheckCount":12,
   "RiskId":48,
   "Level":"medium",
   "MediumWarningCount":0,
   "TypeAlias":"System",
   "LastFoundTime":"2019-04-10 00:58:11"
  },
  {
   "SubTypeAlias":"Redis security baseline check",
   "HighWarningCount":1,
   "WarningMachineCount":1,
   "RiskName":"Redis security baseline check",
   "LowWarningCount":0,
   "CheckCount":1,
   "RiskId":3,
   "Level":"high",
   "MediumWarningCount":0,
   "TypeAlias":"Database",
   "LastFoundTime":"2019-04-10 08:31:32"
  },
  {
   "SubTypeAlias":"Linux weak password",
   "HighWarningCount":1,
   "WarningMachineCount":1,
   "RiskName":"Linux weak password",
   "LowWarningCount":0,
   "CheckCount":1,
   "RiskId":19,
   Level:high,
   "MediumWarningCount":0,
   "TypeAlias":"Weak password",
   "LastFoundTime":"2019-04-10 08:31:32"
  },
  {
   "SubTypeAlias":"Anonymous FTP logon",
   "HighWarningCount":1,
   "WarningMachineCount":1,
   "RiskName":"Anonymous FTP logon",
   "LowWarningCount":0,
   "CheckCount":1,
   "RiskId":12,
   "Level":"high",
   "MediumWarningCount":0,
   "TypeAlias":"Weak password",
   "LastFoundTime":"2019-04-10 08:31:32"
  },
  {
   "SubTypeAlias":"Windows weak password",
   "HighWarningCount":1,
   "WarningMachineCount":1,
   "RiskName":"Windows weak password",
   "LowWarningCount":0,
   "CheckCount":1,
   "RiskId":13,
   "Level":"high",
   "MediumWarningCount":0,
   "TypeAlias":"Weak password",
   "LastFoundTime":"2019-04-10 06:58:58"
  },
  {
   "SubTypeAlias":"Apache Tomcat security baseline check",
   "HighWarningCount":0,
   "WarningMachineCount":0,
   "RiskName":"Apache Tomcat security baseline check",
   "LowWarningCount":0,
   "CheckCount":8,
   "RiskId":23,
   "Level":"medium",
   "MediumWarningCount":0,
   "TypeAlias":"Middleware",
   "LastFoundTime":"2019-04-10 14:00:17"
  },
  {
   "SubTypeAlias":"PostgreSQL weak password",
   "HighWarningCount":0,
   "WarningMachineCount":0,
   "RiskName":"PostgreSQL weak password",
   "LowWarningCount":0,
   "CheckCount":1,
   "RiskId":2,
   "Level":"high",
   "MediumWarningCount":0,
   "TypeAlias":"Weak password",
   "LastFoundTime":"2019-04-10 08:31:32"
  },
  {
   "SubTypeAlias":"MySQL weak password",
   "HighWarningCount":0,
   "WarningMachineCount":0,
   "RiskName":"MySQL weak password",
   "LowWarningCount":0,
   "CheckCount":1,
   "RiskId":11,
   "Level":"high",
   "MediumWarningCount":0,
   "TypeAlias":"Weak password",
   "LastFoundTime":"2019-04-10 08:31:32"
  },
  {
   "SubTypeAlias":"FTP weak password",
   "HighWarningCount":0,
   "WarningMachineCount":0,
   "RiskName":"FTP weak password",
   "LowWarningCount":0,
   "CheckCount":1,
   "RiskId":20,
   "Level":"high",
   "MediumWarningCount":0,
   "TypeAlias":"Weak password",
   "LastFoundTime":"2019-04-10 08:31:32"
  },
  {
   "SubTypeAlias":"Microsoft SQL Server weak password",
   "HighWarningCount":0,
   "WarningMachineCount":0,
   "RiskName":"Microsoft SQL Server weak password",
   "LowWarningCount":0,
   "CheckCount":1,
   "RiskId":17,
   "Level":"high",
   "MediumWarningCount":0,
   "TypeAlias":"Weak password",
   "LastFoundTime":"2019-04-10 06:58:58"
  },
  {
   "SubTypeAlias":"Memcached security baseline check",
   "HighWarningCount":0,
   "WarningMachineCount":0,
   "RiskName":"Memcached security baseline check",
   "LowWarningCount":0,
   "CheckCount":2,
   "RiskId":24,
   "Level":"medium",
   "MediumWarningCount":0,
   "TypeAlias":"Database",
   "LastFoundTime":"2019-04-10 06:52:05"
  },
  {
   "SubTypeAlias":"CentOS Linux 6 security baseline check",
   "HighWarningCount":0,
   "WarningMachineCount":0,
   "RiskName":"CentOS Linux 6 security baseline check",
   "LowWarningCount":0,
   "CheckCount":16,
   "RiskId":42,
   "Level":"high",
   "MediumWarningCount":0,
   "TypeAlias":"System",
   "LastFoundTime":"2019-02-19 14:59:17"
  },
  {
   "SubTypeAlias":"CentOS Linux 6 security standard compliance - MLPS level-2",
   "HighWarningCount":0,
   "WarningMachineCount":0,
   "RiskName":"CentOS Linux 6 security standard compliance - MLPS level-2",
   "LowWarningCount":0,
   "CheckCount":12,
   "RiskId":49,
   "Level":"medium",
   "MediumWarningCount":0,
   "TypeAlias":"System",
   "LastFoundTime":"2019-02-19 14:59:17"
  },
  {
   "SubTypeAlias":"CentOS Linux 6 security standard compliance - MLPS level-3",
   "HighWarningCount":0,
   "WarningMachineCount":0,
   "RiskName":"CentOS Linux 6 security standard compliance - MLPS level-3",
   "LowWarningCount":0,
   "CheckCount":15,
   "RiskId":50,
   "Level":"medium",
   "MediumWarningCount":0,
   "TypeAlias":"System",
   "LastFoundTime":"2019-02-19 14:59:17"
  },
  {
   "SubTypeAlias":"Linux Ubuntu security standard compliance - MLPS level-2",
   "HighWarningCount":0,
   "WarningMachineCount":0,
   "RiskName":"Linux Ubuntu security standard compliance - MLPS level-2",
   "LowWarningCount":0,
   "CheckCount":14,
   "RiskId":55,
   "Level":"medium",
   "MediumWarningCount":0,
   "TypeAlias":"System",
   "LastFoundTime":"2019-02-19 12:57:23"
  },
  {
   "SubTypeAlias":"Linux Ubuntu security standard compliance - MLPS level-3",
   "HighWarningCount":0,
   "WarningMachineCount":0,
   "RiskName":"Linux Ubuntu security standard compliance - MLPS level-3",
   "LowWarningCount":0,
   "CheckCount":15,
   "RiskId":56,
   "Level":"medium",
   "MediumWarningCount":0,
   "TypeAlias":"System",
   "LastFoundTime":"2019-02-19 12:57:23"
  },
  {
   "SubTypeAlias":"Linux Ubuntu security baseline check",
   "HighWarningCount":0,
   "WarningMachineCount":0,
   "RiskName":"Linux Ubuntu security baseline check",
   "LowWarningCount":0,
   "CheckCount":16,
   "RiskId":54,
   "Level":"high",
   "MediumWarningCount":0,
   "TypeAlias":"System",
   "LastFoundTime":"2019-02-19 12:57:23"
  },
  {
   "SubTypeAlias":"Windows 2012 R2 security baseline check",
   "HighWarningCount":0,
   "WarningMachineCount":0,
   "RiskName":"Windows 2012 R2 security baseline check",
   "LowWarningCount":0,
   "CheckCount":12,
   "RiskId":51,
   "Level":"high",
   "MediumWarningCount":0,
   "TypeAlias":"System",
   "LastFoundTime":"2019-02-19 12:44:58"
  }
 ],
 "PageSize":20,
 "RequestId":"DFA6CDC5-E826-4D18-A499-BEF9DA31F1AD",
 "CurrentPage":1
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-9-2"></a>

### 3.9.2. DescribeStratety

Queries the configurations of baseline check policies.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeStratety | The operation that you want to perform.<br>Set the value to DescribeStratety. |
| Lang | String | No | zh | The natural language of the request and response. Valid values:<br>• zh: Chinese<br>• en: English |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| StrategyIds | String | No | test1,test2,test3 | The IDs of the baseline check policies.Separate multiple IDs with commas (,). |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | 16B9826C-B99F-4F8A-8048-EA81D6D3DE8B | The ID of the request. |
| Strategies | Array |  | The information about the baseline check policy. |
| ConfigTargets | Array |  | The information about the group associated with the baseline check policy. |
| Flag | String | add | The related ID. |
| Target | String | 3259405 | The ID of the related group. |
| TargetType | String | groupId | The type of the related group. |
| CycleDays | Integer | 1 | The cycle of the baseline check.<br>• 1: every second day<br>• 3: every fourth day<br>• 7: every eighth day<br>• 30: every 31st day |
| CycleStartTime | Integer | 6 | The time when the baseline check starts.Valid values: 0, 6, 12, and 18. |
| EcsCount | Integer | 5 | The number of servers on which baseline checks were performed based on the specified baseline check policy. |
| ExecStatus | Integer | 1 | The execution status of the baseline check.Valid values:<br>• 1: The baseline check is not running.<br>• 2: The baseline check is running. |
| Id | Integer | 212635 | The ID of the policy. |
| Name | String | test | The name of the policy. |
| PassRate | Integer | 80 | The pass rate of the latest baseline check. |
| ProcessRate | Integer | 80 | The progress of the baseline check. |
| RiskCount | Integer | 5 | The number of selected check items. |
| Type | Integer | 1 | The type of the baseline check policy. Valid values:<br>• 1: default policy<br>• 2: custom policy |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribeStratety
? Lang=zh
&SourceIp=127.0.0.1
&StrategyIds=1,2,3
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<DescribeStratety>
   <RequestId>ACAFE09B-3346-433B-BDA8-369AB3D9B4F9</RequestId>
   <Strategies>
      <CycleStartTime>6</CycleStartTime>
      <EcsCount>0</EcsCount>
      <Type>2</Type>
      <ExecStatus>1</ExecStatus>
      <ProcessRate>0</ProcessRate>
      <CycleDays>3</CycleDays>
      <Id>15161</Id>
      <ConfigTargets>
         <Target>4361221</Target>
         <TargetType>groupId</TargetType>
         <Flag>add</Flag>
      </ConfigTargets>
      <RiskCount>1</RiskCount>
      <Name>test</Name>
   </Strategies>
   <Strategies>
      <CycleStartTime>0</CycleStartTime>
      <EcsCount>17</EcsCount>
      <PassRate>81</PassRate>
      <Type>1</Type>
      <ExecStatus>1</ExecStatus>
      <ProcessRate>0</ProcessRate>
      <CycleDays>1</CycleDays>
      <Id>20</Id>
      <ConfigTargets>
         <Target>281801</Target>
         <TargetType>groupId</TargetType>
         <Flag>del</Flag>
      </ConfigTargets>
      <ConfigTargets>
         <Target>4790960</Target>
         <TargetType>groupId</TargetType>
         <Flag>del</Flag>
      </ConfigTargets>
      <RiskCount>13</RiskCount>
      <Name>Default policy</Name>
   </Strategies>
</DescribeStratety>
```

`JSON`  format

```json
{
 "RequestId":"ACAFE09B-3346-433B-BDA8-369AB3D9B4F9",
 "Strategies":[
  {
   "Name":"test",
   "RiskCount":1,
   "CycleDays":3,
   "Type":2,
   "CycleStartTime":6,
   "ConfigTargets":[
    {
     "Flag":"add",
     "Target":"4361221",
     "TargetType":"groupId"
    }
   ],
   "ProcessRate":0,
   "Id":15161,
   "ExecStatus":1,
   "EcsCount":0
  },
  {
   "Name":"Default policy",
   "RiskCount":13,
   "PassRate":81,
   "CycleDays":1,
   "Type":1,
   "CycleStartTime":0,
   "ConfigTargets":[
    {
     "Flag":"del",
     "Target":"281801",
     "TargetType":"groupId"
    },
    {
     "Flag":"del",
     "Target":"4790960",
     "TargetType":"groupId"
    }
   ],
   "ProcessRate":0,
   "Id":20,
   "ExecStatus":1,
   "EcsCount":17
  }
 ]
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-9-3"></a>

### 3.9.3. DescribeStrategyExecDetail

Queries the details of the latest baseline check by using a baseline check policy. The details include the time when the check is performed, the number of risk items, and the baseline risk details.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeStrategy ExecDetail | The operation that you want to perform.<br>Set the value to DescribeStrategyExecDetail. |
| StrategyId | Integer | Yes | 1 | The ID of the baseline check policy.<br>Note To query the results of a baseline check that uses only one policy, you must specify the ID of the policy. You can call the DescribeStratety operation to obtain the ID. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| EndTime | String | 2019-01-08 20:11:20 | The time when the baseline check ends. |
| FailCount | Integer | 94 | The number of risk items that failed to pass the baseline check. |
| FailedEcsList | Array |  | The list of servers on which risk items were detected. |
| IP | String | 1.2.3.4 | The IP address of the instance on which the baseline check was performed. |
| InstanceName | String | Test-20180703 | The name of the instance. |
| IntranetIp | String | 1.2.3.5 | The internal IP address. |
|  |  |  |  |
| Parameter | Type | Example | Description |

<table>
  <tr>
    <td>Reason</td>
    <td>String</td>
    <td>Detect timeout</td>
    <td>The cause of the baseline check failure.</td>
  </tr>
  <tr>
    <td>InProcessCount</td>
    <td>Integer</td>
    <td>0</td>
    <td>The number of baseline check tasks that are running.</td>
  </tr>
  <tr>
    <td>Percent</td>
    <td>String</td>
    <td>100%</td>
    <td>The progress of the baseline check.</td>
  </tr>
  <tr>
    <td>RequestId</td>
    <td>String</td>
    <td>09322632-4668-4AD9-BD0D-32757DEFBBA6</td>
    <td>The ID of the request.</td>
  </tr>
  <tr>
    <td>Source</td>
    <td>String</td>
    <td>Manual</td>
    <td>The type of the baseline check.<br>• Schedule<br>• Manual</td>
  </tr>
  <tr>
    <td>StartTime</td>
    <td>String</td>
    <td>2019-01-08 19:41:12</td>
    <td>The time when the baseline check starts.</td>
  </tr>
  <tr>
    <td>SuccessCount</td>
    <td>Integer</td>
    <td>81</td>
    <td>The number of check items that passed the baseline check.</td>
  </tr>
</table>

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribeStrategyExecDetail
&StrategyId=1
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<DescribeStrategyExecDetail>
   <RequestId>6489FA6A-D241-4380-9D8C-A8804484CA40</RequestId>
   <EndTime>2019-04-10 00:58:30</EndTime>
   <Percent>100%</Percent>
   <FailCount>1</FailCount>
   <StartTime>2019-04-10 00:19:01</StartTime>
   <SuccessCount>1</SuccessCount>
   <Source>Schedule</Source>
   <FailedEcsList>
      <InstanceName>health-check002</InstanceName>
      <IP>1.2.3.4</IP>
      <IntranetIp>1.2.3.5</IntranetIp>
      <Reason>Agent offline</Reason>
   </FailedEcsList>
   <InProcessCount>0</InProcessCount>
</DescribeStrategyExecDetail>
```

`JSON`  format

```json
{
 "Source":"Schedule",
 "InProcessCount":0,
 "SuccessCount":1,
 "RequestId":"6489FA6A-D241-4380-9D8C-A8804484CA40",
 "Percent":"100%",
 "FailedEcsList":[
  {
   "IntranetIp":"1.2.3.5",
   "IP":"1.2.3.4",
   "InstanceName":"health-check002",
   "Reason":"Agent offline"
  }
 ],
 "EndTime":"2019-04-10 00:58:30",
 "StartTime":"2019-04-10 00:19:01",
 "FailCount":1
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-9-4"></a>

### 3.9.4. DescribeCheckWarnings

Queries specified risk items and check items of a specified server.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeCheckWa rnings | The operation that you want to perform. Set the value to DescribeCheckWarnings. |
| RiskId | Long | Yes | 1 | The ID of the risk item.<br>Note To query specified risk items and check items of a specified server, you must specify the IDs of the risk items. You can call the DescribeCheckWarningSummary operation to obtain the IDs. |
| Uuid | String | Yes | d42f938c-d962-48a0-90f9-05\*\*\*\*\*\*\*\*\*\* | The ID of the server on which a baseline check is performed.<br>The ID of the risk item.<br>Note To query specified risk items and check items of a specified server, you must specify the ID of the server on which the baseline check is run. You can call the DescribeWarningMachines operation to obtain the IDs. |
| CurrentPage | Integer | No | 1 | The number of the current page.<br>Pages start from page 1. The default value is 1, which indicates that the first page is displayed. |
| Lang | String | No | zh | The natural language of the request and response. Valid values:<br>• zh: Chinese<br>• en: English |
| PageSize | Integer | No | 20 | The number of entries to return on each page.<br>The default value is 20, which indicates that 20 entries are returned on each page. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| CheckWarnings | Array |  | The information about the check item. |
| CheckId | Long | 1 | The ID of the check item. |
| CheckWarningId | Long | 10 | The ID of the alert. |
| Item | String | Password expiration alert | The name of the check item. |
| Level | String | high | The severity level of the risk item. Valid values:<br>• high<br>• medium<br>• low |
| Status | Integer | 1 | The status of the check item. Valid values:<br>• 1: failed<br>• 2: verifying<br>• 3: passed<br>• 5: expired<br>• 6: ignored |
| Type | String | Identity authentication | The type of the check item. |
| Uuid | String | d42f938c-d962-48a0-90f9-\*\*\*\*\*\*\*\*\*\*\* | The ID of the server on which the baseline check was performed. |
| Count | Integer | 10 | The number of entries returned on the current page. |
| CurrentPage | Integer | 1 | The page number of the current page. |
| PageSize | Integer | 20 | The number of entries returned per page. |
|  |  |  |  |
| Parameter | Type | Example | Description |

<table>
  <tr>
    <td>RequestId</td>
    <td>String</td>
    <td>0DFCADBA-7065-42DA-AF17-6868B9C2A8CF</td>
    <td>The ID of the request.</td>
  </tr>
  <tr>
    <td>TotalCount</td>
    <td>Integer</td>
    <td>100</td>
    <td>The total number of entries.</td>
  </tr>
</table>

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribeCheckWarnings
&RiskId=1
&Uuid=d42f938c-d962-48a0-90f9-05e4eaf92e34
&Lang=zh
&SourceIp=127.0.0.1
&CurrentPage=1
&PageSize=20
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<DescribeCheckWarnings>
  <TotalCount>16</TotalCount>
  <CheckWarnings>
        <Status>6</Status>
        <Item>Check accounts without passwords in the system
                            </Item>
        <Type>Identity authentication</Type>
        <Uuid>974af549-3248-44dd-9180-***</Uuid>
        <CheckId>1</CheckId>
        <CheckWarningId>1393768</CheckWarningId>
        <Level>high</Level>
  </CheckWarnings>
  <CheckWarnings>
        <Status>6</Status>
        <Item>Check password complexity</Item>
        <Type>Identity authentication</Type>
        <Uuid>974af549-3248-44dd-9180-***</Uuid>
        <CheckId>52</CheckId>
        <CheckWarningId>1393774</CheckWarningId>
        <Level>high</Level>
  </CheckWarnings>
  <CheckWarnings>
        <Status>6</Status>
        <Item>Make sure that root is the only account whose UID is 0</Item>
        <Type>Identity authentication</Type>
        <Uuid>974af549-3248-44dd-9180-***</Uuid>
        <CheckId>15</CheckId>
        <CheckWarningId>1393773</CheckWarningId>
        <Level>high</Level>
  </CheckWarnings>
  <CheckWarnings>
        <Status>6</Status>
        <Item>Enable address space layout randomization</Item>
        <Type>Intrusion prevention</Type>
        <Uuid>974af549-3248-44dd-9180-***</Uuid>
        <CheckId>14</CheckId>
        <CheckWarningId>1393772</CheckWarningId>
        <Level>high</Level>
  </CheckWarnings>
  <CheckWarnings>
        <Status>6</Status>
        <Item>Specify user permissions on file configurations</Item>
        <Type>File permissions</Type>
        <Uuid>974af549-3248-44dd-9180-***</Uuid>
        <CheckId>13</CheckId>
        <CheckWarningId>1393767</CheckWarningId>
        <Level>high</Level>
  </CheckWarnings>
  <CheckWarnings>
        <Status>6</Status>
        <Item>Specify permissions on the access control configuration file</Item>
        <Type>File permissions</Type>
        <Uuid>974af549-3248-44dd-9180-***</Uuid>
        <CheckId>12</CheckId>
        <CheckWarningId>1393771</CheckWarningId>
        <Level>high</Level>
  </CheckWarnings>
  <CheckWarnings>
        <Status>6</Status>
        <Item>Make sure that SSH LogLevel is set to INFO</Item>
        <Type>Service configuration</Type>
        <Uuid>974af549-3248-44dd-9180-***</Uuid>
        <CheckId>11</CheckId>
        <CheckWarningId>1393766</CheckWarningId>
        <Level>high</Level>
  </CheckWarnings>
  <CheckWarnings>
        <Status>6</Status>
        <Item>Make sure that the rsyslog service is enabled</Item>
        <Type>Security auditing</Type>
        <Uuid>974af549-3248-44dd-9180-***</Uuid>
        <CheckId>10</CheckId>
        <CheckWarningId>1393770</CheckWarningId>
        <Level>high</Level>
  </CheckWarnings>
  <CheckWarnings>
        <Status>6</Status>
        <Item>Specify the timeout period for SSH idle connections</Item>
        <Type>Service configuration</Type>
        <Uuid>974af549-3248-44dd-9180-***</Uuid>
        <CheckId>8</CheckId>
        <CheckWarningId>1393765</CheckWarningId>
        <Level>high</Level>
  </CheckWarnings>
  <CheckWarnings>
        <Status>6</Status>
        <Item>Make sure that SSH V2 is used</Item>
        <Type>Service configuration</Type>
        <Uuid>974af549-3248-44dd-9180-***</Uuid>
        <CheckId>7</CheckId>
        <CheckWarningId>1393764</CheckWarningId>
        <Level>high</Level>
  </CheckWarnings>
  <CheckWarnings>
        <Status>6</Status>
        <Item>Make sure that SSH MaxAuthTries is set to a value from 3 to 6</Item>
        <Type>Service configuration</Type>
        <Uuid>974af549-3248-44dd-9180-***</Uuid>
        <CheckId>6</CheckId>
        <CheckWarningId>1393763</CheckWarningId>
        <Level>high</Level>
  </CheckWarnings>
  <CheckWarnings>
        <Status>6</Status>
        <Item>Make sure that alerts are triggered at least seven days before passwords expire</Item>
        <Type>Identity authentication</Type>
        <Uuid>974af549-3248-44dd-9180-***</Uuid>
        <CheckId>5</CheckId>
        <CheckWarningId>1393769</CheckWarningId>
        <Level>high</Level>
  </CheckWarnings>
  <CheckWarnings>
        <Status>6</Status>
        <Item>Set the shortest interval between password changes</Item>
        <Type>Identity authentication</Type>
        <Uuid>974af549-3248-44dd-9180-***</Uuid>
        <CheckId>4</CheckId>
        <CheckWarningId>1393761</CheckWarningId>
        <Level>high</Level>
  </CheckWarnings>
  <CheckWarnings>
        <Status>6</Status>
        <Item>Set the password validity period</Item>
        <Type>Identity authentication</Type>
        <Uuid>974af549-3248-44dd-9180-***</Uuid>
        <CheckId>3</CheckId>
        <CheckWarningId>1393760</CheckWarningId>
        <Level>high</Level>
  </CheckWarnings>
  <CheckWarnings>
        <Status>6</Status>
        <Item>Disable SSH logon for accounts without specified passwords                   

                            </Item>
        <Type>Service configuration</Type>
        <Uuid>974af549-3248-44dd-9180-***</Uuid>
        <CheckId>2</CheckId>
        <CheckWarningId>1393762</CheckWarningId>
        <Level>high</Level>
  </CheckWarnings>
  <CheckWarnings>
        <Status>6</Status>
        <Item>Check whether password reuse is limited</Item>
        <Type>Identity authentication</Type>
        <Uuid>974af549-3248-44dd-9180-***</Uuid>
        <CheckId>58</CheckId>
        <CheckWarningId>1393775</CheckWarningId>
        <Level>high</Level>
  </CheckWarnings>
  <PageSize>20</PageSize>
  <RequestId>C1E6C4FE-DE00-4B75-A01E-FCAB55A36449</RequestId>
  <CurrentPage>1</CurrentPage>
  <Count>16</Count>
</DescribeCheckWarnings>
```

`JSON`  format

```json
{
 "Count":16,
 "TotalCount":16,
 "PageSize":20,
 "RequestId":"C1E6C4FE-DE00-4B75-A01E-FCAB55A36449",
 "CurrentPage":1,
 "CheckWarnings":[
  {
   "Uuid":"974af549-3248-44dd-9180-***",
   "Status":6,
   "CheckWarningId":1393768,
   "Item":"Check accounts without passwords in the system\r\n                              
\r\n                            ",
   "Type":"Identity authentication",
   "Level":"high",
   "CheckId":1
  },
  {
   "Uuid":"974af549-3248-44dd-9180-***",
   "Status":6,
   "CheckWarningId":1393774,
   "Item":"Check password complexity",
   "Type":"Identity authentication",
   "Level":"high",
   "CheckId":52
  },
  {
   "Uuid":"974af549-3248-44dd-9180-***",
   "Status":6,
   "CheckWarningId":1393773,
   "Item":"Make sure that root is the only account whose UID is 0",
   "Type":"Identity authentication",
   "Level":"high",
   "CheckId":15
  },
  {
   "Uuid":"974af549-3248-44dd-9180-***",
   "Status":6,
   "CheckWarningId":1393772,
   "Item":"Enable address space layout randomization",
   "Type":"Intrusion prevention",
   "Level":"high",
   "CheckId":14
  },
  {
   "Uuid":"974af549-3248-44dd-9180-***",
   "Status":6,
   "CheckWarningId":1393767,
   "Item":"Specify user permissions on file configurations",
   "Type":"File permissions",
   "Level":"high",
   "CheckId":13
  },
  {
   "Uuid":"974af549-3248-44dd-9180-***",
   "Status":6,
   "CheckWarningId":1393771,
   "Item":"Specify the permissions on the access control configuration file",
   "Type":"File permissions",
   "Level":"high",
   "CheckId":12
  },
  {
   "Uuid":"974af549-3248-44dd-9180-***",
   "Status":6,
   "CheckWarningId":1393766,
   "Item":"Make sure that SSH LogLevel is set to INFO",
   "Type":"Service configuration",
   "Level":"high",
   "CheckId":11
  },
  {
   "Uuid":"974af549-3248-44dd-9180-***",
   "Status":6,
   "CheckWarningId":1393770,
   "Item":"Make sure that the rsyslog service is enabled",
   "Type":"Security auditing",
   "Level":"high",
   "CheckId":10
  },
  {
   "Uuid":"974af549-3248-44dd-9180-***",
   "Status":6,
   "CheckWarningId":1393765,
   "Item":"Specify the timeout period for SSH idle connections",
   "Type":"Service configuration",
   "Level":"high",
   "CheckId":8
  },
  {
   "Uuid":"974af549-3248-44dd-9180-***",
   "Status":6,
   "CheckWarningId":1393764,
   "Item":"Make sure that SSH V2 is used",
   "Type":"Service configuration",
   "Level":"high",
   "CheckId":7
  },
  {
   "Uuid":"974af549-3248-44dd-9180-***",
   "Status":6,
   "CheckWarningId":1393763,
   "Item":"Make sure that SSH MaxAuthTries is set to a value from 3 to 6",
   "Type":"Service configuration",
   "Level":"high",
   "CheckId":6
  },
  {
   "Uuid":"974af549-3248-44dd-9180-***",
   "Status":6,
   "CheckWarningId":1393769,
   "Item":"Make sure that alerts are triggered at least seven days before passwords expire",
   "Type":"Identity authentication",
   "Level":"high",
   "CheckId":5
  },
  {
   "Uuid":"974af549-3248-44dd-9180-***",
   "Status":6,
   "CheckWarningId":1393761,
   "Item":"Set the shortest interval between password changes",
   "Type":"Identity authentication",
   "Level":"high",
   "CheckId":4
  },
  {
   "Uuid":"974af549-3248-44dd-9180-***",
   "Status":6,
   "CheckWarningId":1393760,
   "Item":"Set the password validity period",
   "Type":"Identity authentication",
   "Level":"high",
   "CheckId":3
  },
  {
   "Uuid":"974af549-3248-44dd-9180-***",
   "Status":6,
   "CheckWarningId":1393762,
   "Item":"Disable SSH logon for accounts without specified passwords                      
\r\n                            \r\n                                \r\n                   
",
   "Type":"Service configuration",
   "Level":"high",
   "CheckId":2
  },
  {
   "Uuid":"974af549-3248-44dd-9180-***",
   "Status":6,
   "CheckWarningId":1393775,
   "Item":"Check whether password reuse is limited",
   "Type":"Identity authentication",
   "Level":"high",
   "CheckId":58
  }
 ]
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-9-5"></a>

### 3.9.5. DescribeCheckWarningDetail

Queries the details of a specific check item.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeCheckWa rningDetail | The operation that you want to perform.<br>Set the value to DescribeCheckWarningDetail. |
| CheckWarningId | Long | Yes | 1 | The ID of the alert triggered by the check item.<br>Note To query the details of a specific check item, you must specify the ID of the alert triggered by the check item. You can call the DescribeCheckWarnings operation to obtain the alert ID. |
| Lang | String | No | zh | The natural language of the request and response. Valid values:<br>• zh: Chinese<br>• en: English |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| Advice | String | Fix now | The suggestion for the management of the risk item. |
| CheckId | Long | 1 | The ID of the check item. |
| Description | String | Password expiring | The additional details about the risk item. |
| Item | String | Password expiration alert | The name of the check item. |
| Level | String | high | The severity level of the risk item.<br>• high: The item is a high-risk one and highlighted in red.<br>• medium: The item is a medium-risk one and highlighted in orange.<br>• low: The item is a low-risk one and highlighted in gray. |
| Prompt | String | Password expiration alert | The prompt for the risk item. |
| RequestId | String | 09969D2C-4FAD-429E-BFBF-9A60DEF8BF6F | The ID of the request. |
| Type | String | Identity authentication | The type of the check item. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribeCheckWarningDetail
&CheckWarningId=1
&SourceIp=127.0.0.1
&Lang=zh
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<DescribeCheckWarningDetail>
   <Item>Specify user permissions on file configurations</Item>
   <Type>File permissions</Type>
   <Description>Specify user permissions on file configurations</Description>
   <RequestId>9F2361B3-B7C3-4189-8DB5-C6D1F67BC225</RequestId>
   <CheckId>13</CheckId>
   <Prompt></Prompt>
   <Level>high</Level>
   <Advice>Run the following five commands
  chown root:root /etc/passwd /etc/shadow /etc/group /etc/gshadow
  chmod 0644 /etc/group  
  chmod 0644 /etc/passwd  
  chmod 0400 /etc/shadow  
 chmod 0400 /etc/gshadow  </Advice>
</DescribeCheckWarningDetail>
```

`JSON`  format

```json
{
 "Prompt":"",
 "Description":"Specify user permissions on file configurations",
 "Item":"Specify user permissions on file configurations",
 "Type":"File permissions",
 "RequestId":"9F2361B3-B7C3-4189-8DB5-C6D1F67BC225",
 "Advice":"Run the following five commands\r\nchown root:root /etc/passwd /etc/shadow /etc/group /etc/gshadow\r\nchmod 0644 /etc/group  \r\nchmod 0644 /etc/passwd  \r\nchmod 0400 /etc/shadow  \r\nchmod 0400 /etc/gshadow  ",
 "Level":"high",
 "CheckId":13
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-9-6"></a>

### 3.9.6. DescribeWarningMachines

Queries information about servers on which a baseline check is performed. The information includes the statistics and status of risk items and IDs of the servers.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeWarning Machines | The operation that you want to perform.<br>Set the value to DescribeWarningMachines. |
| RiskId | Long | Yes | 1 | The ID of the risk item.<br>Note To query information about servers on which a baseline check is performed, you must specify the ID of the risk item that is related to the baseline check.You can call the DescribeCheckWarningSummary operation to obtain the ID. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Lang | String | No | zh | The natural language of the request and response. Valid values:<br>• zh: Chinese<br>• en: English |
| MachineName | String | No | test_ecs172 | The name of the server on which a baseline check is performed. |
| Uuids | String | No | xxx-aaa-bbb-ccc | The ID of the server on which a baseline check is performed. Separate multiple IDs with commas (,). |
| StrategyId | Long | No | 1 | The ID of the baseline check policy. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. |
| CurrentPage | Integer | No | 1 | The number of the current page. |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| Count | Integer | 10 | The number of entries returned on the current page. |
| CurrentPage | Integer | 1 | The number of the current page. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| RequestId | String | 00BDE2-284A-4534-BD09-FB69836DD750 | The ID of the request. |
| TotalCount | Integer | 100 | The total number of returned entries. |
| WarningMachin es | Array |  | The information about the servers that generate alerts. |
| HighWarningCo unt | Integer | 10 | The number of high-risk check items. |
| InstanceId | String | i-m5ee8b9nr3h30mhb \*\*\*\* | The instance ID of the server. |
| InstanceName | String | aaawebtest | The name of the instance. |
| InternetIp | String | 1.2.3.4 | The public IP address of the server. |
| IntranetIp | String | 1.2.3.5 | The private IP address of the server. |
| LowWarningCo unt | Integer | 3 | The number of low-risk check items. |
| MediumWarnin gCount | Integer | 2 | The number of medium-risk check items. |
| PassCount | Integer | 10 | The number of items that have passed the baseline check. |
| RegionId | String | cn-qingdao | The region ID of the server. |
| Status | Integer | 1 | The verification status of the risk items that are fixed. Valid values:<br>• 1: completed<br>• 2: verifying |
| Uuid | String | xxx-aaa-bbb-ccc | The ID of the server on which a baseline check is performed. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribeWarningMachines
&RiskId=1
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<DescribeWarningMachinesResponse>
      <TotalCount>100</TotalCount>
      <RequestId>00BDE2-284A-4534-BD09-FB69836DD750</RequestId>
      <PageSize>10</PageSize>
      <CurrentPage>1</CurrentPage>
      <WarningMachines>
            <InstanceName>aaawebtest</InstanceName>
            <Status>1</Status>
            <MediumWarningCount>2</MediumWarningCount>
            <Uuid>xxx-aaa-bbb-ccc</Uuid>
            <InternetIp>1.2.3.4</InternetIp>
            <InstanceId>i-m5ee8b9nr3h30mhb****</InstanceId>
            <HighWarningCount>10</HighWarningCount>
            <RegionId>cn-qingdao</RegionId>
            <PassCount>10</PassCount>
            <IntranetIp>1.2.3.5</IntranetIp>
            <LowWarningCount>3</LowWarningCount>
      </WarningMachines>
      <Count>10</Count>
</DescribeWarningMachinesResponse>
```

`JSON`  format

```json
{
    "TotalCount": "100",
    "RequestId": "00BDE2-284A-4534-BD09-FB69836DD750",
    "PageSize": "10",
    "CurrentPage": "1",
    "WarningMachines": [{
        "InstanceName": "aaawebtest",
        "Status": "1",
        "MediumWarningCount": "2",
        "Uuid": "xxx-aaa-bbb-ccc",
        "InternetIp": "1.2.3.4",
        "InstanceId": "i-m5ee8b9nr3h30mhb****",
        "HighWarningCount": "10",
        "RegionId": "cn-qingdao",
        "PassCount": "10",
        "IntranetIp": "1.2.3.5",
        "LowWarningCount": "3"
    }],
    "Count": "10"
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-9-7"></a>

### 3.9.7. DescribeUserBaselineAuthorization

Queries whether Threat Detection Service has the permissions to access a cloud resource.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeUserBase lineAuthorization | The operation that you want to perform.<br>Set the value to DescribeUserBaselineAuthorization. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Lang | String | No | zh | The natural language of the request and response. Valid values:<br>• zh: Chinese<br>• en: English |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | 0AF20EB0-EBBC-4B94-9B84-F3BAFAC53EDE | The ID of the request. |
| UserBaselineAu thorization | Struct |  | The information about whether Threat Detection Service has the permissions to run configuration checks on a cloud resource. |
| Status | Integer | 1 | Indicates whether Threat Detection Service is authorized to run configuration checks on a cloud resource.<br>• 0: permission denied. Threat Detection Service does not have the permissions to run configuration checks on the cloud platform.<br>• 1: permission granted. Threat Detection Service has the permissions to run configuration checks on the cloud platform. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribeUserBaselineAuthorization
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<data>
    <UserBaselineAuthorization>
        <Status>1</Status>
    </UserBaselineAuthorization>
</data>
<requestId>0AF20EB0-EBBC-4B94-9B84-F3BAFAC53EDE</requestId>
```

`JSON`  format

```json
{
  "data": {
    "UserBaselineAuthorization": {
      "Status": 1
    }
  },
  "requestId": "0AF20EB0-EBBC-4B94-9B84-F3BAFAC53EDE"
  }
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-9-8"></a>

### 3.9.8. ValidateHcWarnings

Verifies multiple risk items of the baseline check at a time. The verification operation verifies whether risk items of the baseline check have been fixed. If a risk item is verified, the risk item status is updated to Passed.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | ValidateHcWarnin gs | The operation that you want to perform.<br>Set the value to ValidateHcWarnings. |
| RiskIds | String | Yes | 43 | The ID list of risk items that need to be verified. If the list has multiple risk item IDs, separate them with commas (,). |
| Uuids | String | Yes | 78645c8e-2e89-441b-8eb,a9622a6b-adb5-4dd3-929e,0136460a-1cb5-44e8-\*\*\*\* | The UUID list of servers that contain risk items to be verified. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | 722C4F88-7867-4E7B-8ADE-7451053 | The ID of the request. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=ValidateHcWarnings
&RiskIds=43
&Uuids=78645c8e-2e89-441b-8eb,a9622a6b-adb5-4dd3-929e,0136460a-1cb5-44e8-****
&<Common request parameters>
```

Sample success responses `XML`  format

```xml
<ValidateHcWarningsResponse>
  <RequestId>722C4F88-7867-4E7B-8ADE-7451053</RequestId>
</ValidateHcWarningsResponse>
```

`JSON`  format

```json
{
   "RequestId":"722C4F88-7867-4E7B-8ADE-7451053" 
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-9-9"></a>

### 3.9.9. FixCheckWarnings

Fixes risk items detected in the baseline check.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | FixCheckWarnings | The operation that you want to perform.<br>Set the value to FixCheckWarnings. |
| CheckParams | String | Yes | \[{"checkId":8,"rule s": \[{"ruleId":"rule.ss h_Idle.interval","v alue":1,"paramLis t": \[{"paramName":" range_val","value ":"600"}, {"paramName":"r ange_val","value":"600"}\]}, {"ruleId":"rule.ssh _Idle.count","valu e":1,"paramList": \[{"paramName":" range_val","value ":"3"}\]}\]}\] | The parameters for the risk item to be fixed. Descriptions of the parameters:<br>• checkId: the ID of the check item.<br>• rules: the rules applied to fixes, in the array format.<br>• value: specifies whether the fix method is selected. Valid values:0: not selected.1: selected.<br>• ruleId: specifies the ID of the fix method.<br>• paramList: the list of fix methods, in the array format.<br>paramName: the name of the fix method.<br>value: the value of the fix method. |
| RiskId | Long | Yes | 12 | The ID of the risk item to be fixed. |
| Uuids | String | Yes | uuid-abcd-1234,uuid-abcd-2345 | The UUID list of the servers that have risk items. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Lang | String | No | zh | The natural language of the request and response. Valid values:<br>• zh: Chinese<br>• en: English |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| BatchId | Long | 52370 | The IDs of the returned risk items that have been fixed. |
| RequestId | String | 76C1D7FD-DB1E-45EA-B804-3FBD9A1DD9C0 | The ID of the request. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=FixCheckWarnings
&CheckParams=[{"checkId":8,"rules":[{"ruleId":"rule.ssh_Idle.interval","value":1,"paramList
":[{"paramName":"range_val","value":"600"},{"paramName":"range_val","value":"600"}]},{"rule
Id":"rule.ssh_Idle.count","value":1,"paramList":[{"paramName":"range_val","value":"3"}]}]}]&RiskId=12
&Uuids=uuid-abcd-1234,uuid-abcd-2345
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<FixCheckWarningsResponse>
      <BatchId>52370</BatchId>
      <requestId>76C1D7FD-DB1E-45EA-B804-3FBD9A1DD9C0</requestId>
</FixCheckWarningsResponse>
```

`JSON`  format

```json
{    
    "BatchId": 52370,
    "requestId": "76C1D7FD-DB1E-45EA-B804-3FBD9A1DD9C0"
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-10"></a>

## 3.10. Asset fingerprints

<a id="section-3-10-1"></a>

### 3.10.1. DescribePropertyCount

Queries the statistics of asset fingerprints, including the numbers of processes, ports, software, users, and scheduled tasks.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeProperty Count | The operation that you want to perform. Set the value to DescribePropertyCount. |
| Type | String | No | port | The type of the asset fingerprint. Valid values:<br>• user<br>• software<br>• process<br>• port<br>• cron: scheduled tasks<br>Note If you do not specify a type, all types of asset fingerprints are queried. |
| UuidList | String | No | \[c4678332-ef3\*\*,c46\*\*\*\] | The IDs of the assets, which are unique. |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| Cron | Integer | 261 | The number of scheduled tasks. |
| Port | Integer | 163 | The number of listening ports. |
| Process | Integer | 367 | The number of running processes. |
| RequestId | String | 7E0618A9-D5EF-4220-9471-C42B5E92719F | The ID of the request. |
| Software | Integer | 5073 | The number of software assets. |
| User | Integer | 114 | The number of users. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribePropertyCount
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<DescribePropertyCount>
  <User>340</User>
  <Software>2598</Software>
  <Port>265</Port>
  <Process>395</Process>
  <RequestId>3D93ABAB-0AC2-4A27-A03B-35C0E4AA0443</RequestId>
  <Cron>261</Cron>
</DescribePropertyCount>
```

`JSON`  format

```json
{
 "User":340,
 "Software":2598,
 "Port":265,
 "RequestId":"3D93ABAB-0AC2-4A27-A03B-35C0E4AA0443",
 "Process":395,
 "Cron":261
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-10-2"></a>

### 3.10.2. DescribePropertyPortDetail

Queries the details of a port.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeProperty PortDetail | The operation that you want to perform.<br>Set the value to DescribePropertyPortDetail. |
| Remark | String | No | 1.2.3.4 | The name or IP address of the server. |
| Port | String | No | 22 | The port of the server. |
| ProcName | String | No | sshd | The name of the process. |
| Uuid | String | No | 50d213b4-3a35-427a-b8a5-\*\*\* | The ID of the asset, which is unique. |
| CurrentPage | Integer | No | 1 | The page number of the current page. |
| PageSize | Integer | No | 6 | The number of entries to return on each page. |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | FAA793EF-5B14-4CDD-B3E0-B14D4342C422 | The ID of the request. |
| Propertys | Array |  | Details of the port. |
| BindIp | String | 1.2.3.4 | The IP addresses bound to the port. |
| Port | String | 22 | The port number. |
| InstanceName | String | test-\*\*\* | The name of the asset related to the port. |
| Proto | String | tcp | The network protocol. |
| Ip | String | 1.2.3.1 | The public IP address of the asset. |
| Create | String | 2019-05-13T10:39Z | The time when the data is last collected. |
| CreateTimesta mp | Long | 1557715141000 | The timestamp of last data collection. |
| ProcName | String | sshd | The name of the process that is using the port. |
| Uuid | String | 50d213b4-3a35-427a-b8a5-04b0c7e1f4d2" | The ID of the asset related to the port. |
| InstanceId | String | 50d213b4-3a35-427a-b8a5-04b0c7e1f4d2" | The ID of the asset related to the port. |
| IntranetIp | String | 1.2.3.2 | The private IP address of the asset. |
| InternetIp | String | 1.2.3.1 | The public IP address of the asset. |
| PageInfo | Struct |  | The page information. |
| Count | Integer | 5 | The number of entries returned on the current page. |
| PageSize | Integer | 5 | The number of entries returned per page. |
| TotalCount | Integer | 762 | The total number of returned entries. |
| CurrentPage | Integer | 1 | The page number of the current page. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribePropertyPortDetail
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<DescribePropertyPortDetailResponse>
  <Propertys>
        <InstanceName>centos-xx</InstanceName>
        <Uuid>00274759-73ef-485a-ae40-c2b5972f50cd</Uuid>
        <Proto>tcp</Proto>
        <InternetIp>101.xx.xx.104</InternetIp>
        <InstanceId>i-2ze645t5u9jo4txxx</InstanceId>
        <Create>2020-01-09T13:53Z</Create>
        <Port>22</Port>
        <Ip>101.xx.xx.104</Ip>
        <ProcName>sshd</ProcName>
        <CreateTimestamp>1578549227000</CreateTimestamp>
        <IntranetIp>192.xx.xx.96</IntranetIp>
        <BindIp>0.0.0.0</BindIp>
  </Propertys>
  <Propertys>
        <InstanceName>paas-xxx-test1122</InstanceName>
        <Uuid>007ecd45-e90f-4290-9eac-758407aa1509</Uuid>
        <Proto>tcp</Proto>
        <InternetIp>118.xx.xx.7</InternetIp>
        <InstanceId>i-m5e56ycm6xx7if43xx</InstanceId>
        <Create>2020-02-18T15:52Z</Create>
        <Port>10251</Port>
        <Ip>118.xx.xx.7</Ip>
        <ProcName>kube-scheduler</ProcName>
        <CreateTimestamp>1582012349000</CreateTimestamp>
        <IntranetIp>192.xx.xx.192</IntranetIp>
        <BindIp>::</BindIp>
  </Propertys>
  <Propertys>
        <InstanceName>paas-xx-2</InstanceName>
        <Uuid>007ecd45-e9xx-4290-9eac-758407aa15xx</Uuid>
        <Proto>tcp</Proto>
        <InternetIp>118.xx.xx.7</InternetIp>
        <InstanceId>i-m5e56ycm6s0xxf43maxx</InstanceId>
        <Create>2020-02-18T15:52Z</Create>
        <Port>10252</Port>
        <Ip>118.xx.xx.7</Ip>
        <ProcName>kube-controller-manager</ProcName>
        <CreateTimestamp>1582012349000</CreateTimestamp>
        <IntranetIp>192.xx.xx.192</IntranetIp>
        <BindIp>::</BindIp>
  </Propertys>
  <Propertys>
        <InstanceName>paas-xx-2</InstanceName>
        <Uuid>007ecd45-e90f-42xx-9eac-758407aa15xx</Uuid>
        <Proto>tcp</Proto>
        <InternetIp>118.xx.xx.7</InternetIp>
        <InstanceId>i-m5e56ycmxx07if43maxx</InstanceId>
        <Create>2020-02-18T15:52Z</Create>
        <Port>2379</Port>
        <Ip>118.xx.xx.7</Ip>
        <ProcName>etcd</ProcName>
        <CreateTimestamp>1582012349000</CreateTimestamp>
        <IntranetIp>192.xx.xx.192</IntranetIp>
        <BindIp>::</BindIp>
  </Propertys>
  <Propertys>
        <InstanceName>paas-xx-2</InstanceName>
        <Uuid>007ecd45-e90f-4290-9exx-758407aa15xx</Uuid>
        <Proto>tcp</Proto>
        <InternetIp>118.xx.xx.7</InternetIp>
        <InstanceId>i-m5e56ycm6s07if43maxx</InstanceId>
        <Create>2020-02-18T15:52Z</Create>
        <Port>6443</Port>
        <Ip>118.xx.xx.7</Ip>
        <ProcName>kube-apiserver</ProcName>
        <CreateTimestamp>1582012349000</CreateTimestamp>
        <IntranetIp>192.xx.xx.192</IntranetIp>
        <BindIp>::</BindIp>
  </Propertys>
  <PageInfo>
        <Count>5</Count>
        <PageSize>5</PageSize>
        <TotalCount>762</TotalCount>
        <CurrentPage>1</CurrentPage>
  </PageInfo>
  <requestId>FAA793EF-5B14-4CDD-B3E0-B14D4342C422</requestId>
</DescribePropertyPortDetailResponse>
```

`JSON`  format

```json
{
  "Propertys": [
      {
       "InstanceName": "centos-xx",
              "Uuid": "00274759-73ef-485a-ae40-c2b5972f50cd",
             "Proto": "tcp",
             "InternetIp": "101.xx.xx.104",
             "InstanceId": "i-2ze645t5u9jo4txxx",
             "Create": "2020-01-09T13:53Z",
             "Port": "22",
             "Ip": "101.xx.xx.104",
             "ProcName": "sshd",
             "CreateTimestamp": 1578549227000,
             "IntranetIp": "192.xx.xx.96",
           "BindIp": "0.0.0.0"
      },
      {
       "InstanceName": "paas-xxx-test1122",
             "Uuid": "007ecd45-e90f-4290-9eac-758407aa1509",
             "Proto": "tcp",
              "InternetIp": "118.xx.xx.7",
             "InstanceId": "i-m5e56ycm6xx7if43xx",
             "Create": "2020-02-18T15:52Z",
             "Port": "10251",
             "Ip": "118.xx.xx.7",
             "ProcName": "kube-scheduler",
             "CreateTimestamp": 1582012349000,
             "IntranetIp": "192.xx.xx.192",
             "BindIp": "::"
      },
      {
       "InstanceName": "paas-xx-2",
             "Uuid": "007ecd45-e9xx-4290-9eac-758407aa15xx",
             "Proto": "tcp",
             "InternetIp": "118.xx.xx.7",
             "InstanceId": "i-m5e56ycm6s0xxf43maxx",
             "Create": "2020-02-18T15:52Z",
             "Port": "10252",
             "Ip": "118.xx.xx.7",
             "ProcName": "kube-controller-manager",
             "CreateTimestamp": 1582012349000,
             "IntranetIp": "192.xx.xx.192",
             "BindIp": "::"
        },
        {
            "InstanceName": "paas-xx-2",
            "Uuid": "007ecd45-e90f-42xx-9eac-758407aa15xx",
            "Proto": "tcp",
            "InternetIp": "118.xx.xx.7",
            "InstanceId": "i-m5e56ycmxx07if43maxx",
            "Create": "2020-02-18T15:52Z",
            "Port": "2379",
            "Ip": "118.xx.xx.7",
            "ProcName": "etcd",
            "CreateTimestamp": 1582012349000,
            "IntranetIp": "192.xx.xx.192",
            "BindIp": "::"
        },
        {
            "InstanceName": "paas-xx-2",
            "Uuid": "007ecd45-e90f-4290-9exx-758407aa15xx",
            "Proto": "tcp",
            "InternetIp": "118.xx.xx.7",
            "InstanceId": "i-m5e56ycm6s07if43maxx",
            "Create": "2020-02-18T15:52Z",
            "Port": "6443",
            "Ip": "118.xx.xx.7",
            "ProcName": "kube-apiserver",
            "CreateTimestamp": 1582012349000,
            "IntranetIp": "192.xx.xx.192",
            "BindIp": "::"
         }
    ],
"PageInfo": {
      "Count": 5,
      "PageSize": 5,
      TotalCount: 762,
      "CurrentPage": 1
    },
  "requestId": "FAA793EF-5B14-4CDD-B3E0-B14D4342C422"
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-10-3"></a>

### 3.10.3. DescribePropertyProcDetail

Queries the details of a process.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeProperty ProcDetail | The operation that you want to perform. Set the value to DescribePropertyProcDetail. |
| Cmdline | String | No | . /8888 | The parameter that is used to start the process. |
| CurrentPage | Integer | No | 1 | The page number of the current page. |
| Name | String | No | 8888 | The name of the process. |
| PageSize | Integer | No | 5 | The number of entries to return on each page. |
| Remark | String | No | 1.2.3.4 | The name or IP address of the server. |
| User | String | No | root | The user who runs the process. |
| Uuid | String | No | c4678332-ef35-4ad4-\*\*\* | The ID of the asset related to the process. |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| PageInfo |  |  | The page information. |
| Count | Integer | 1 | The number of entries returned on the current page. |
| CurrentPage | Integer | 1 | The page number of the current page. |
| PageSize | Integer | 5 | The number of entries returned per page. |
| TotalCount | Integer | 1 | The total number of returned entries. |
| Propertys | Array |  | The returned process information. |
| Cmdline | String | . /8888 | The parameter that was used to start the process. |
| Create | String | 2019-05-15T11:08Z | The last time when the data was collected. |
| CreateTimesta mp | Long | 1565686951000 | The timestamp of last data collection. |
| EuidName | String | root | The permission to run the process. |
| InstanceId | String | c4678332-ef35-4ad4-8358-\*\*\* | The ID of the asset. |
| InstanceName | String | test-\*\*\* | The name of the asset. |
| InternetIp | String | 1.2.3.1 | The public IP address of the asset. |
| IntranetIp | String | 1.2.3.2 | The private IP address of the asset. |
| Md5 | String | N/A | The MD5 value of the file. |
| Name | String | 8888 | The name of the process. |
| Path | String | /root/Oracle/Middle ware/\*\*\*/8888 | The path of the process. |
| Pid | String | 12826 | The ID of the process. |
| Pname | String | start\*\*\*.s | The parent name of the process. |
| StartTime | String | 2019-08-07 10:09:05 | The time when the process started. |
| User | String | root | The user who runs the process. |
| Uuid | String | c4678332-ef35-4ad4-8358-6\*\*\* | The ID of the asset related to the process. |
| RequestId | String | 64388374-A309-4191-8606-3346CCA364B0 | The ID of the request. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribePropertyProcDetail
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<DescribePropertyProcDetail>
   <RequestId>64388374-A309-4191-8606-3346CCA364B0</RequestId>
   <PageInfo>
      <Count>2</Count>
      <TotalCount>8184</TotalCount>
      <PageSize>2</PageSize>
      <CurrentPage>1</CurrentPage>
   </PageInfo>
   <Propertys>
      <User>N/A</User>
      <Uuid>90d4cc6a-806f-***</Uuid>
      <Md5>N/A</Md5>
      <CreateTimestamp>1557889713000</CreateTimestamp>
      <InstanceId>i-bp1***</InstanceId>
      <InternetIp></InternetIp>
      <Path>N/A</Path>
      <Name>N/A</Name>
      <IntranetIp>1.2.3.4</IntranetIp>
      <Create>2019-05-15T11:08Z</Create>
      <Pname>N/A</Pname>
      <EuidName>N/A</EuidName>
      <StartTime>N/A</StartTime>
      <Pid>0</Pid>
      <InstanceName>test_***</InstanceName>
      <Cmdline>N/A</Cmdline>
   </Propertys>
   <Propertys>
      <User>N/A</User>
      <Uuid>90d4cc6a-806f-4***</Uuid>
      <Md5>N/A</Md5>
      <CreateTimestamp>1557889713000</CreateTimestamp>
      <InstanceId>i-b***</InstanceId>
      <InternetIp></InternetIp>
      <Path>N/A</Path>
      <Name>N/A</Name>
      <IntranetIp>1.2.3.5</IntranetIp>
      <Create>2019-05-15T11:08Z</Create>
      <Pname>N/A</Pname>
      <EuidName>N/A</EuidName>
      <StartTime>N/A</StartTime>
      <Pid>4</Pid>
      <InstanceName>tsy_***</InstanceName>
      <Cmdline>N/A</Cmdline>
   </Propertys>
</DescribePropertyProcDetail>
```

`JSON`  format

```json
{
 "RequestId":"64388374-A309-4191-8606-3346CCA364B0",
 "PageInfo":{
  "Count":2,
  "TotalCount":8184,
  "PageSize":2,
  "CurrentPage":1
 },
 "Propertys":[
  {
   "User":"N/A",
   "Uuid":"90d4cc6a-806f-***",
   "Md5":"N/A",
   "CreateTimestamp":1557889713000,
   "InstanceId":"i-bp1***",
   "InternetIp":"",
   "Path":"N/A",
   "Name":"N/A",
   "IntranetIp":"1.2.3.4",
   "Create":"2019-05-15T11:08Z",
   "Pname":"N/A",
   "StartTime":"N/A",
   "EuidName":"N/A",
   "Pid":"0",
   "Cmdline":"N/A",
   "InstanceName":"test_***"
  },
  {
   "User":"N/A",
   "Uuid":"90d4cc6a-806f-4***",
   "Md5":"N/A",
   "CreateTimestamp":1557889713000,
   "InstanceId":"i-b***",
   "InternetIp":"",
   "Path":"N/A",
   "Name":"N/A",
   "IntranetIp":"1.2.3.5",
   "Create":"2019-05-15T11:08Z",
   "Pname":"N/A",
   "StartTime":"N/A",
   "EuidName":"N/A",
   "Pid":"4",
   "Cmdline":"N/A",
   "InstanceName":"tsy_***"
  }
 ]
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-10-4"></a>

### 3.10.4. DescribePropertyPortItem

Queries information about ports.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeProperty PortItem | The operation that you want to perform.<br>Set the value to DescribePropertyPortItem. |
| ForceFlush | Boolean | No | true | Specifies whether to force refresh the data that you want to query. |
| Port | String | No | 22 | The port number. |
| CurrentPage | Integer | No | 1 | The page number of the current page. |
| PageSize | Integer | No | 5 | The number of entries to return on each page. |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | 7E0618A9-D5EF-4220-9471-C42B5E92719F | The ID of the request. |
| PropertyItems | Array |  | Details of the port. |
| Port | String | 22 | The number of the listener port. |
| Proto | String | tcp | The network protocol of the port. |
| Count | Integer | 495 | The number of servers that use the port. |
| PageInfo | Struct |  | The page information. |
| Count | Integer | 5 | The number of entries returned on the current page. |
| PageSize | Integer | 5 | The number of entries returned per page. |
| TotalCount | Integer | 163 | The total number of entries. |
| CurrentPage | Integer | 1 | The page number of the current page. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribePropertyPortItem
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<DescribePropertyPortItemResponse>
        <RequestId>7E0618A9-D5EF-4220-9471-C42B5E92719F</RequestId>
        <PropertyItems>
                <Port>22</Port>
                <Proto>tcp</Proto>
                <Count>495</Count>
        </PropertyItems>
        <PropertyItems>
                <Port>111</Port>
                <Proto>tcp</Proto>
                <Count>43</Count>
        </PropertyItems>
        <PropertyItems>
                <Port>6000</Port>
                <Proto>tcp</Proto>
                <Count>2</Count>
        </PropertyItems>
        <PropertyItems>
                <Port>53</Port>
                <Proto>tcp</Proto>
                <Count>1</Count>
        </PropertyItems>
        <PropertyItems>
                <Port>80</Port>
                <Proto>tcp</Proto>
                <Count>38</Count>
        </PropertyItems>
        <PageInfo>
                <Count>5</Count>
                <PageSize>5</PageSize>
                <TotalCount>163</TotalCount>
                <CurrentPage>1</CurrentPage>
        </PageInfo>
</DescribePropertyPortItemResponse>
```

`JSON`  format

```json
{
  "requestId": "7E0618A9-D5EF-4220-9471-C42B5E92719F", 
  "PropertyItems": [
      {
        "Port": "22",
        "Proto": "tcp",
        "Count": 495
      },
      {
        "Port": "111",
        "Proto": "tcp",
        "Count": 43
      },
      {
        "Port": "6000",
        "Proto": "tcp",
        "Count": 2
      },   
      {
        "Port": "53",
        "Proto": "tcp",
        "Count": 1
      },
      {
        "Port": "80",
        "Proto": "tcp",
        "Count": 38
      }
  ],
  "PageInfo": {
      "Count": 5,
      "PageSize": 5,
      "TotalCount": 163,
      "CurrentPage": 1
    }
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-10-5"></a>

### 3.10.5. DescribePropertyProcItem

Queries information about all processes.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeProperty ProcItem | The operation that you want to perform. Set the value to DescribePropertyProcItem. |
| CurrentPage | Integer | No | 1 | The page number of the current page. |
| ForceFlush | Boolean | No | true | Specifies whether to force refresh the data that you want to query. |
| Name | String | No | test | The name of the process. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| PageInfo |  |  | The page information. |
| Count | Integer | 5 | The number of entries returned on the current page. |
| CurrentPage | Integer | 1 | The page number of the current page. |
| PageSize | Integer | 5 | The number of entries returned per page. |
| TotalCount | Integer | 372 | The total number of entries. |
| PropertyItems | Array |  | The process information. |
| Count | Integer | 8888 | The number of servers on which the process runs. |
| Name | String | .ss | The name of the process. |
| RequestId | String | BD8AD4C6-A169-4FA3-BA1F-ED40ED52973B | The ID of the request. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribePropertyProcItem
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<DescribePropertyProcItem>
  <PropertyItems>
        <Name>(sd-**)</Name>
        <Count>7</Count>
  </PropertyItems>
  <PropertyItems>
        <Name>6Cm***</Name>
        <Count>1</Count>
  </PropertyItems>
  <RequestId>BD8AD4C6-A169-4FA3-BA1F-ED40ED52973B</RequestId>
  <PageInfo>
        <Count>2</Count>
        <TotalCount>395</TotalCount>
        <PageSize>2</PageSize>
        <CurrentPage>1</CurrentPage>
  </PageInfo>
</DescribePropertyProcItem>
```

`JSON`  format

```json
{
 "RequestId":"BD8AD4C6-A169-4FA3-BA1F-ED40ED52973B",
 "PropertyItems":[
  {
   "Name":"(sd-**)",
   "Count":7
  },
  {
   "Name":"6Cm***",
   "Count":1
  }
 ],
 "PageInfo":{
  "Count":2,
  "TotalCount":395,
  "PageSize":2,
  "CurrentPage":1
 }
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-10-6"></a>

### 3.10.6. DescribePropertySoftwareDetail

Queries details of a software asset.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeProperty SoftwareDetail | The operation that you want to perform. Set the value to DescribePropertySoftwareDetail. |
| CurrentPage | Integer | No | 1 | The page number of the current page. |
| Name | String | No | tes\*\*\* | The name of the software. |
| PageSize | Integer | No | 5 | The number of entries to return on each page. |
| Path | String | No | /etc/test | The directory where the software is installed. |
| Remark | String | No | 1.2.3.4 | The name or IP address of the server. |
| SoftwareVersion | String | No | 11 | The version of the software. |
| Uuid | String | No | 50d213b4-3a35-427a-b8a5-\*\*\* | The ID of the software asset. |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| PageInfo |  |  | The page information. |
| Count | Integer | 2 | The number of entries returned on the current page. |
| CurrentPage | Integer | 1 | The page number of the current page. |
| PageSize | Integer | 2 | The number of entries returned per page. |
|  |  |  |  |
| Parameter | Type | Example | Description |

<table>
  <tr>
    <td>TotalCount</td>
    <td>Integer</td>
    <td>23</td>
    <td>The total number of entries.</td>
  </tr>
  <tr>
    <td>Propertys</td>
    <td>Array</td>
    <td></td>
    <td>The details of the software.</td>
  </tr>
  <tr>
    <td>Create</td>
    <td>Long</td>
    <td>1565539587000</td>
    <td>The last time when the data was collected.</td>
  </tr>
  <tr>
    <td>CreateTimesta mp</td>
    <td>Long</td>
    <td>1565539587000</td>
    <td>The timestamp of last data collection.</td>
  </tr>
  <tr>
    <td>InstallTime</td>
    <td>String</td>
    <td>2017-09-07 10:54:49</td>
    <td>The time when the software was installed.</td>
  </tr>
  <tr>
    <td>InstanceId</td>
    <td>String</td>
    <td>i-uf***</td>
    <td>The ID of the asset.</td>
  </tr>
  <tr>
    <td>InstanceName</td>
    <td>String</td>
    <td>test</td>
    <td>The name of the asset.</td>
  </tr>
  <tr>
    <td>InternetIp</td>
    <td>String</td>
    <td>1.2.3.1</td>
    <td>The public IP address of the asset.</td>
  </tr>
  <tr>
    <td>IntranetIp</td>
    <td>String</td>
    <td>1.2.3.2</td>
    <td>The private IP address of the asset.</td>
  </tr>
  <tr>
    <td>Ip</td>
    <td>String</td>
    <td>1.2.3.1</td>
    <td>The public IP address of the asset.</td>
  </tr>
  <tr>
    <td>Name</td>
    <td>String</td>
    <td>aaa_base</td>
    <td>The name of the software.</td>
  </tr>
  <tr>
    <td>Path</td>
    <td>String</td>
    <td>/etc/test</td>
    <td>The directory where the software is installed.</td>
  </tr>
  <tr>
    <td>Uuid</td>
    <td>String</td>
    <td>4ef1115b-e423-4b4b-b930-***</td>
    <td>The UUID of the software version.</td>
  </tr>
  <tr>
    <td>Version</td>
    <td>String</td>
    <td>11</td>
    <td>The version of the software.</td>
  </tr>
  <tr>
    <td>RequestId</td>
    <td>String</td>
    <td>9C5AE850-7140-4DE6-B892-055EB0D9F28A</td>
    <td>The ID of the request.</td>
  </tr>
</table>

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribePropertySoftwareDetail
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<DescribePropertySoftwareDetail>
  <RequestId>9C5AE850-7140-4DE6-B892-055EB0D9F28A</RequestId>
  <PageInfo>
        <Count>2</Count>
        <TotalCount>35795</TotalCount>
        <PageSize>2</PageSize>
        <CurrentPage>1</CurrentPage>
  </PageInfo>
  <Propertys>
        <Uuid>04c56617-23fc-***</Uuid>
        <Name>abrt</Name>
        <Ip>1.2.3.1</Ip>
        <CreateTimestamp>1561330240000</CreateTimestamp>
        <IntranetIp>1.2.3.3</IntranetIp>
        <InstanceId>i-bp***</InstanceId>
        <Create>2019-06-24T06:50Z</Create>
        <InternetIp>1.2.3.1</InternetIp>
        <InstallTime>2014-08-14 21:18:50</InstallTime>
        <Version>2.0.8</Version>
        <InstanceName>Test***</InstanceName>
        <Path>/etc/abrt</Path>
  </Propertys>
  <Propertys>
        <Uuid>c038fd42-3151-4***</Uuid>
        <Name>abrt</Name>
        <Ip>1.2.3.5</Ip>
        <CreateTimestamp>1562283761000</CreateTimestamp>
        <IntranetIp>1.2.3.6</IntranetIp>
        <InstanceId>i-b***</InstanceId>
        <Create>2019-07-05T07:42Z</Create>
        <InternetIp>1.2.3.5</InternetIp>
        <InstallTime>2014-11-21 18:23:32</InstallTime>
        <Version>2.1.11</Version>
        <InstanceName>Test***</InstanceName>
        <Path>/etc/abrt</Path>
  </Propertys>
</DescribePropertySoftwareDetail>
```

`JSON`  format

```json
{
 "RequestId":"9C5AE850-7140-4DE6-B892-055EB0D9F28A",
 "PageInfo":{
  "Count":2,
  "TotalCount":35795,
  "PageSize":2,
  "CurrentPage":1
 },
 "Propertys":[
  {
   "Name":"abrt",
   "Uuid":"04c56617-23fc-***",
   "Ip":"1.2.3.1",
   "CreateTimestamp":1561330240000,
   "Create":"2019-06-24T06:50Z",
   "InstanceId":"i-bp***",
   "IntranetIp":"1.2.3.3",
   "InternetIp":"1.2.3.1",
   "InstallTime":"2014-08-14 21:18:50",
   "Version":"2.0.8",
   "InstanceName":"test****",
   "Path":"/etc/abrt"
  },
  {
   "Name":"abrt",
   "Uuid":"c038fd42-3151-4***",
   "Ip":"1.2.3.5",
   "CreateTimestamp":1562283761000,
   "Create":"2019-07-05T07:42Z",
   "InstanceId":"i-b***",
   "IntranetIp":"1.2.3.6",
   "InternetIp":"1.2.3.5",
   "InstallTime":"2014-11-21 18:23:32",
   "Version":"2.1.11",
   "InstanceName":"Test****",
   "Path":"/etc/abrt"
  }
 ]
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-10-7"></a>

### 3.10.7. DescribePropertySoftwareItem

Queries information about all software assets.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeProperty SoftwareItem | The operation that you want to perform.<br>Set the value to DescribePropertySoftwareItem. |
| ForceFlush | Boolean | No | true | Specifies whether to force refresh the data that you want to query. |
| Name | String | No | test | The name of the software. |
| CurrentPage | Integer | No | 1 | The page number of the current page. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | 3A85CFCF-05C8-451A-9E41-C0D5E96BA407 | The ID of the request. |
| PropertyItems | Array |  | The returned software assets. |
| Name | String | aaa_base | The name of the returned software asset. |
| Count | Integer | 23 | The number of servers on which the software is installed. |
| PageInfo | Struct |  | The page information. |
| Count | Integer | 2 | The number of entries returned on the current page. |
| PageSize | Integer | 2 | The number of entries returned per page. |
| TotalCount | Integer | 5037 | The total number of returned entries. |
| CurrentPage | Integer | 1 | The page number of the current page. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribePropertySoftwareItem
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<DescribePropertySoftwareItemResponse>
      <PageInfo>
                <Count>2</Count>
                <PageSize>2</PageSize>
                <TotalCount>5037</TotalCount>
                <CurrentPage>1</CurrentPage>
      </PageInfo>
      <PropertyItems>
                <Name>a11y-profile-manager-indicator</Name>
                <Count>1</Count>
      </PropertyItems>
      <PropertyItems>
                <Name>aaa_base</Name>
                <Count>23</Count>
      </PropertyItems>
      <requestId>3A85CFCF-05C8-451A-9E41-C0D5E96BA407</requestId>
</DescribePropertySoftwareItemResponse>
```

`JSON`  format

```json
{
  "PageInfo": {
      "Count": 2,
      "PageSize": 2,
      "TotalCount": 5037,
      "CurrentPage": 1
    },
    "PropertyItems": [
      {
        "Name": "a11y-profile-manager-indicator",
        "Count": 1
      },
      {
        "Name": "aaa_base",
        "Count": 23
      }
    ],
     "requestId": "3A85CFCF-05C8-451A-9E41-C0D5E96BA407"
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-10-8"></a>

### 3.10.8. DescribePropertyUserDetail

Queries the details of an account in the account list.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeProperty UserDetail | The operation that you want to perform.<br>Set the value to DescribePropertyUserDetail. |
| Remark | String | No | 0.0.0.0 | The name or IP address of the server. |
| User | String | No | test | The name of the account that you want to query. |
| IsRoot | String | No | 0 | Specifies whether the account has root permissions. Valid values:<br>• 0: The account does not have root permissions.<br>• 1: The account has root permissions. |
| Uuid | String | No | 50d213b4-3a35-427a-b8a5-04b0c7e1f4d2 | The UUID of the asset. |
| CurrentPage | Integer | No | 1 | The number of the page to return. |
| PageSize | Integer | No | 2 | The number of entries to return on each page. |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | FAA793EF-5B14-4CDD-B3E0-B14D4342C422 | The ID of the request. |
| Propertys | Array |  | The returned account details. |
| LastLoginTime | String | xxxx | The time of the last logon. |
| IsRoot | String | 0 | Indicates whether the account has root permissions.<br>• 0: The account does not have root permissions.<br>• 1: The account has root permissions. |
| InstanceName | String | null | The name of the asset. |
| AccountsExpira tionDate | String | never | The expiration date of the account. |
| PasswordExpira tionDate | String | never | The expiration date of the account password. |
| Ip | String | null | The IP address of the asset. |
| Create | String | 1565644643000 | The timestamp when the last asset fingerprint was collected. |
| CreateTimesta mp | Long | 1565644643000 | The timestamp generated for the asset fingerprint. |
| User | String | adm | The name of the account. |
| Uuid | String | 02c4a5dc-c2d2-483a-9015-f972b44d2cd9 | The UUID of the asset. |
| LastLoginIp | String | N/A | The source IP address of the last logon. |
| InstanceId | String | 02c4a5dc-c2d2-483a-9015-f972b44d2cd9 | The ID of the asset. |
| IntranetIp | String | 0.0.0.0 | The private IP address of the asset. |
| InternetIp | String | 0.0.0.0 | The public IP address of the asset. |
| Status | String | 0 | The logon status of the account. Valid values:<br>• 0: The account cannot log on.<br>• 1: The account can log on. |
| GroupNames | List | adm | The name of the user group. |
| PageInfo | Struct |  | The page information. |
| Count | Integer | 2 | The number of entries returned on the current page. |
| PageSize | Integer | 2 | The number of entries returned per page. |
| TotalCount | Integer | 384 | The total number of returned entries. |
| CurrentPage | Integer | 1 | The page number of the returned page. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribePropertyUserDetail
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<DescribePropertyUserDetailResponse>
  <requestId>FAA793EF-5B14-4CDD-B3E0-B14D4342C422</requestId>
  <PageInfo>
        <Count>2</Count>
        <PageSize>2</PageSize>
        <TotalCount>384</TotalCount>
        <CurrentPage>1</CurrentPage>
  </PageInfo>
  <Propertys>
        <LastLoginTime>N/A</LastLoginTime>
        <GroupName>adm</GroupName>
        <IsRoot>0</IsRoot>
        <InstanceName></InstanceName>
        <AccountsExpirationDate>never</AccountsExpirationDate>
        <PasswordExpirationDate>never</PasswordExpirationDate>
        <Ip></Ip>
        <Create>1565644643000</Create>
        <Status>0</Status>
        <User>adm</User>
        <Uuid>00ea0155-548e-4f32-bb53-3a000110b30d</Uuid>
        <LastLoginIp>N/A</LastLoginIp>
  </Propertys>
  <Propertys>
        <LastLoginTime>N/A</LastLoginTime>
        <GroupName>adm</GroupName>
        <IsRoot>0</IsRoot>
        <InstanceName></InstanceName>
        <AccountsExpirationDate>never</AccountsExpirationDate>
        <PasswordExpirationDate>never</PasswordExpirationDate>
        <Ip></Ip>
        <Create>1565652008000</Create>
        <Status>0</Status>
        <User>adm</User>
        <Uuid>02c4a5dc-c2d2-483a-9015-f972b44d2cd9</Uuid>
        <LastLoginIp>N/A</LastLoginIp>
  </Propertys>
</DescribePropertyUserDetailResponse>
```

`JSON`  format

```json
{
    "requestId": "FAA793EF-5B14-4CDD-B3E0-B14D4342C422",
    "PageInfo": {
      "Count": 2,
      "PageSize": 2,
      "TotalCount": 384,
      "CurrentPage": 1
    },
    "Propertys": [
      {
        "LastLoginTime": "N/A",
        "GroupName": [
          "adm"
        ],
        "IsRoot": "0",
        "InstanceName": null,
        "AccountsExpirationDate": "never",
        "PasswordExpirationDate": "never",
        "Ip": null,
        "Create": 1565644643000,
        "Status": 0,
        "User": "adm",
        "Uuid": "00ea0155-548e-4f32-bb53-3a000110b30d",
        "LastLoginIp": "N/A"
      },
      {
        "LastLoginTime": "N/A",
        "GroupName": [
          "adm"
        ],
        "IsRoot": "0",
        "InstanceName": null,
        "AccountsExpirationDate": "never",
        "PasswordExpirationDate": "never",
        "Ip": null,
        "Create": 1565652008000,
        "Status": 0,
        "User": "adm",
        "Uuid": "02c4a5dc-c2d2-483a-9015-f972b44d2cd9",
        "LastLoginIp": "N/A"
      }
    ] 
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-10-9"></a>

### 3.10.9. DescribePropertyUserItem

Queries the account information about an asset.

Request parameters Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeProperty UserItem | The operation that you want to perform. Set the value to DescribePropertyUserItem. |
| CurrentPage | Integer | No | 1 | The page number of the current page. |
| ForceFlush | Boolean | No | true | Specifies whether to force refresh the data that you want to query. |
| PageSize | Integer | No | 2 | The number of entries to return on each page. |
| User | String | No | adm | The account information about the asset fingerprint. |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| PageInfo |  |  | The page information. |
| Count | Integer | 2 | The number of entries returned on the current page. |
| CurrentPage | Integer | 1 | The page number of the current page. |
| PageSize | Integer | 2 | The number of entries returned per page. |
| TotalCount | Integer | 114 | The total number of returned entries. |
| PropertyItems | Array |  | The account information. |
| Count | Integer | 384 | The number of servers that belong to the current account. |
| User | String | adm | The name of the account. |
| RequestId | String | 76068BE2-F9C4-4EDD-967B-F503B8CCDD3D | The ID of the request. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribePropertyUserItem
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<DescribePropertyUserItem>
  <PropertyItems>
        <User>a123456</User>
        <Count>1</Count>
  </PropertyItems>
  <PropertyItems>
        <User>aaaa</User>
        <Count>1</Count>
  </PropertyItems>
  <PropertyItems>
        <User>aaaa1</User>
        <Count>1</Count>
  </PropertyItems>
  <RequestId>76068BE2-F9C4-4EDD-967B-F503B8CCDD3D</RequestId>
  <PageInfo>
        <Count>3</Count>
        <TotalCount>340</TotalCount>
        <PageSize>3</PageSize>
        <CurrentPage>1</CurrentPage>
  </PageInfo>
</DescribePropertyUserItem>
```

`JSON`  format

```json
{
 "RequestId":"76068BE2-F9C4-4EDD-967B-F503B8CCDD3D",
 "PropertyItems":[
  {
   "User":"a123456",
   "Count":1
  },
  {
   "User":"aaaa",
   "Count":1
  },
  {
   "User":"aaaa1",
   "Count":1
  }
 ],
 "PageInfo":{
  "Count":3,
  "TotalCount":340,
  "PageSize":3,
  "CurrentPage":1
 }
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-10-10"></a>

### 3.10.10. DescribeModuleConfig

Queries the configurations of asset fingerprint modules.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeModuleC onfig | The operation that you want to perform.<br>Set the value to DescribeModuleConfig. |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | 7E0618A9-D5EF-4220-9471-C42B5E92719F | The ID of the request. |
| Success | Boolean | true | Indicates whether the request is successful. |
| Count | Integer | 2 | The number of module configurations. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |
| ModuleConfigLi st | Array |  | The list of module configurations. |
| ConfigName | String | timescan | The name of the configuration. |
| ModuleName | String | alihids | The name of the template. |
| Items | Array |  | The list of configuration items. |
| InstanceId | String | lb-xxx | The ID of the instance. |
| InstanceName | String | ssxxxxxxxx | The name of the instance. |
| GroupId | Integer | 173 | The ID of the group. |
| Ip | String | 2.2.2.2 | The IP address of the instance. |
| Region | String | outside-of-aliyun | The region where the instance is deployed. |
| Uuid | String | lb-xxxx-xxxx-xxxx-xxxx | The UUID of the server. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribeModuleConfig
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<code>200</code>
<data>
    <Count>2</Count>
    <ModuleConfigList>
        <ConfigName>timescan</ConfigName>
        <ModuleName>alihids</ModuleName>
        <Items>
            <InstanceName>ssxxxxxxxx</InstanceName>
            <Uuid>lb-xxxx-xxxx-xxxx-xxxx</Uuid>
            <InstanceId>lb-xxx</InstanceId>
            <Ip>2.2.2.2</Ip>
            <Region>cn-qingdao</Region>
            <GroupId>173</GroupId>
        </Items>
        <Items>
            <InstanceName>3a04702ca5a0</InstanceName>
            <Uuid>inet-db626549-870c-4d3e-b0b5-4d8a5c7268a6</Uuid>
            <Ip>192.1.2.3</Ip>
            <Region>outside-of-aliyun</Region>
            <GroupId>343</GroupId>
        </Items>
    </ModuleConfigList>
    <ModuleConfigList>
        <ConfigName>sysvulfix</ConfigName>
        <ModuleName>alihids</ModuleName>
        <Items>
            <InstanceName>xx</InstanceName>
            <Uuid>lb-xxx</Uuid>
            <InstanceId>lb-xxx</InstanceId>
            <Ip>2.2.2.2</Ip>
            <Region>cn-qingdao</Region>
            <GroupId>173</GroupId>
        </Items>
        <Items>
            <InstanceName>3a04702ca5a0</InstanceName>
            <Uuid>inet-db626549-870c-4d3e-b0b5-4d8a5c7268a6</Uuid>
            <Ip>192.168.5.3</Ip>
            <Region>outside-of-aliyun</Region>
            <GroupId>343</GroupId>
        </Items>
    </ModuleConfigList>
</data>
<requestId>7E0618A9-D5EF-4220-9471-C42B5E92719F</requestId>
<success>true</success>
```

`JSON`  format

```json
{
  "code": 200,
  "data": {
    "Count": 2,
    "ModuleConfigList": [{
        "ConfigName": "timescan",
        "ModuleName": "alihids",
        "Items": [{
            "InstanceName": "ssxxxxxxxx",
            "Uuid": "lb-xxxx-xxxx-xxxx-xxxx",
            "InstanceId": "lb-xxx",
            "Ip": "2.2.2.2",
            "Region": "cn-qingdao",
            "GroupId": 173
          },
          {
            "InstanceName": "3a04702ca5a0",
            "Uuid": "inet-db626549-870c-4d3e-b0b5-4d8a5c7268a6",
            "Ip": "192.1.2.3",
            "Region": "outside-of-aliyun",
            "GroupId": 343
          }
        ]
      },
      {
        "ConfigName": "sysvulfix",
        "ModuleName": "alihids",
        "Items": [{
            "InstanceName": "xx",
            "Uuid": "lb-xxx",
            "InstanceId": "lb-xxx",
            "Ip": "2.2.2.2",
            "Region": "cn-qingdao",
            "GroupId": 173
          },
          {
            "InstanceName": "3a04702ca5a0",
            "Uuid": "inet-db626549-870c-4d3e-b0b5-4d8a5c7268a6",
            "Ip": "192.168.5.3",
            "Region": "outside-of-aliyun",
            "GroupId": 343
          }
        ]
      }
    ]
  },
  "requestId": "7E0618A9-D5EF-4220-9471-C42B5E92719F",
  "success": true
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-11"></a>

## 3.11. Notifications

<a id="section-3-11-1"></a>

### 3.11.1. DescribeDingTalk

Queries DingTalk notifications.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeDingTalk | The operation that you want to perform.<br>Set the value to DescribeDingTalk. |
| RuleActionName | String | No | Vulnerability notification | The name of the notification. |
| PageSize | Integer | No | 20 | The number of entries to return on each page. |
| CurrentPage | Integer | No | 1 | The page number of the current page. |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | B256A525-7E42-4BB9-A27C-9017FDDFF1A2 | The ID of the request. |
| ActionList | Array |  | The list of notifications. |
| GmtModified | Long | 1550828400000 | The timestamp when the notification was modified. |
| Id | Integer | 1 | The ID of the notification. |
| AliUid | Long | 12312412341 | The UID of the user. |
| GmtCreate | Long | 1550828400000 | The timestamp when the notification was created. |
| Url | String | https://oapi.dingtal k.com/robot/send | The parameters of the notification. |
| IntervalTime | Integer | 1000 | The notification interval. |
| ActionName | String | Alert notification | The name of the notification. |
| Status | Integer | 1 | The status of the notification. Valid values:<br>• 0: disabled<br>• 1: enabled |
| ConfigList | String | \[{\\"type\\":\\"vul\\",\\" configItemList\\": \[{\\"key\\":\\"key\\", \\"valueList\\":\\"123\\ "}\]}\] | The list of notification settings. |
| GroupIdList | String | "123,456" | GroupidList. |
| DingTalkLang | String | zh | The natural language of notifications. Valid values:<br>• zh: Chinese<br>• en: English |
| PageInfo | Struct |  | The page information. |
| PageSize | Integer | 20 | The number of entries returned per page. |
| TotalCount | Integer | 1 | The number of notifications. |
| CurrentPage | Integer | 1 | The page number of the current page. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribeDingTalk
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<data >
    <PageInfo>
        <PageSize>20</PageSize>
        <CurrentPage>1</CurrentPage>
        <TotalCount>1</TotalCount>
    </PageInfo>
    <ActionList>
        <ActionName>Alert notification</ActionName>
        <GmtCreate>1550828400000</GmtCreate>
        <GmtModified>1550828400000</GmtModified>
        <IntervalTime>1000</IntervalTime>
        <Id>1</Id>
        <Url>https://oapi.dingtalk.com/robot/send</Url>
        <AliUid>12312412341</AliUid>
        <configList>[{"type":"vul","configItemList":[{"key":"key", "valueList":"123"}]}]</configList>
        <groupIdList>123,456</groupIdList>
    </ActionList>
</data >
<requestId>B256A525-7E42-4BB9-A27C-9017FDDFF1A2</requestId>
```

`JSON`  format

```json
{
  "data ": {
    "PageInfo": {
      "PageSize": 20,
      "CurrentPage": 1,
      "TotalCount":1
    },
    "ActionList": [{
      "ActionName": "Alert notification",
      "GmtCreate": "1550828400000",
      "GmtModified": "1550828400000",
      "IntervalTime": 1000,
      "Id": 1,
      "Url": "https://oapi.dingtalk.com/robot/send",
      "AliUid": 12312412341,
      "configList":"[{\"type\":\"vul\",\"configItemList\":[{\"key\":\"key\", \"valueList\":
\"123\"}]}]",
      "groupIdList":"123,456"
    }]
  },
  "requestId": "B256A525-7E42-4BB9-A27C-9017FDDFF1A2"
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-11-2"></a>

### 3.11.2. DescribeNoticeConfig

Queries the notification settings.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeNoticeCo nfig | The operation that you want to perform.<br>Set the value to DescribeNoticeConfig. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | D185B7FF-E24C-422D-83D3-C2A25C7A2727 | The ID of the request. |
| NoticeConfigLis t | Array |  | Details of the notification settings. |
| TimeLimit | Integer | 1 | The time period during which notifications can be sent to the recipients. Valid values:<br>• 0: any time<br>• 1: 08:00 to 22:00 |
| Route | Integer | 7 | The notification method. |
| Project | String | sas_suspicious | The project identifier. |
| AliUid | Long | 121234141424 | The UID of the user. |
| CurrentPage | Integer | 1 | The page number of the current page. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribeNoticeConfig
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<code>200</code>
<data>
    <RequestId>D185B7FF-E24C-422D-83D3-C2A25C7A2727</RequestId>
    <NoticeConfigList>
        <Project>sas_suspicious</Project>
        <CurrentPage>1</CurrentPage>
        <TimeLimit>1</TimeLimit>
        <Route>7</Route>
        <AliUid>1049769453489698</AliUid>
    </NoticeConfigList>
    <NoticeConfigList>
        <Project>sas_healthcheck</Project>
        <CurrentPage>1</CurrentPage>
        <TimeLimit>1</TimeLimit>
        <Route>7</Route>
        <AliUid>1049769453489698</AliUid>
    </NoticeConfigList>
</data>
```

`JSON`  format

```json
{
  "code": 200,
  "data": {
  "RequestId":"D185B7FF-E24C-422D-83D3-C2A25C7A2727",
  "NoticeConfigList":[
    {
      "Project":"sas_suspicious",
      "CurrentPage":1,
      "TimeLimit":1,
      "Route":7,
      "AliUid":10497611111111
    },
    {
      "Project":"sas_healthcheck",
      "CurrentPage":1,
      "TimeLimit":1,
      "Route":7,
      "AliUid":10422222222
    }
  ]
}
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-12"></a>

## 3.12. Agent client

<a id="section-3-12-1"></a>

### 3.12.1. SasInstallCode

Queries the verification key used to run the agent installation command.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | SasInstallCode | The operation that you want to perform.<br>Set the value to SasInstallCode. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | B256A525-7E42-4BB9-A27C-9017FDDFF1A2 | The ID of the request. |
| data | String | eDkhGP | The verification key used to run the installation command when you manually install the Threat Detection Service agent. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=SasInstallCode
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<SasInstallCodeResponse>
  <requestId>B256A525-7E42-4BB9-A27C-9017FDDFF1A2</requestId>
  <data>eDkhGP</data>
</SasInstallCodeResponse>
```

`JSON`  format

```json
{
  "requestId": "B256A525-7E42-4BB9-A27C-9017FDDFF1A2",
  "data":"eDkhGP"
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-12-2"></a>

### 3.12.2. PauseClient

Enables or disables the Threat Detection Service agent.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | PauseClient | The operation that you want to perform.<br>Set the value to PauseClient. |
| Uuids | String | Yes | uuid-1211-sadsd-2131 | The UUIDs of servers for which the Threat Detection Service agent needs to be enabled or disabled. |
| Value | String | Yes | 1 | The status of the Threat Detection Service agent. Valid values:<br>• 0: disabled<br>• 1: enabled |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | 6673D49C-A9AB-40DD-B4A2-B92306701AE7 | The ID of the request. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=PauseClient
&Uuids=uuid-1211-sadsd-2131
&Value=1
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<PauseClientResponse>
  <requestId>6673D49C-A9AB-40DD-B4A2-B92306701AE7</requestId>
</PauseClientResponse>
```

`JSON`  format

```json
{
 "requestId": "6673D49C-A9AB-40DD-B4A2-B92306701AE7" 
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-13"></a>

## 3.13. Export check results

<a id="section-3-13-1"></a>

### 3.13.1. ExportRecord

Exports baseline check, asset fingerprint check, and AccessKey leak check results to Excel files.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | ExportRecord | The operation that you want to perform.<br>Set the value to ExportRecord. |
| ExportType | String | Yes | accessKey | The type of the check whose result can be exported. Valid values:<br>• baseline: Alibaba Cloud service baseline<br>• assetInstance: assets<br>• attack: attack analysis<br>• accessKey: AccessKey pair leaks<br>• user: the accounts covered by asset fingerprints<br>• port: the ports covered by asset fingerprints<br>• process: the processes covered by asset fingerprints<br>• software: the software covered by asset fingerprints |
| Lang | String | No | zh | The natural language of the request and response. Valid values:<br>• zh: Chinese<br>• en: English |
| Params | String | No | {"level":"high"} | The conditions to filter check results in the files to which the check results are exported. |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| FileName | String | cms_20171101.xlsx | The name of the exported file. |
| Id | Long | 131231 | The ID of the exported file. |
| RequestId | String | 6673D49C-A9AB-40DD-B4A2-B92306701AE7 | The ID of the request. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=ExportRecord
&ExportType=accessKey
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<ExportRecordResponse>
  <Id>131231</Id>
  <FileName>cms_20171101.xlsx</FileName>
  <requestId>6673D49C-A9AB-40DD-B4A2-B92306701AE7</requestId>
</ExportRecordResponse>
```

`JSON`  format

```json
{
    "Id": 131231,
    "FileName" : "cms_20171101.xlsx",
    "requestId": "6673D49C-A9AB-40DD-B4A2-B92306701AE7"
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-3-14"></a>

## 3.14. Virus detection

<a id="section-3-14-1"></a>

### 3.14.1. OperateSuspiciousTargetConfig

Configures virus detection.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | OperateSuspiciou sTargetConfig | The operation that you want to perform.<br>Set the value to OperateSuspiciousTargetConfig. |
| TargetOperations | String | Yes | " \[{\\"targetType\\": \\"uuid\\",\\"target \\":\\"0585f81a-dd84-4ddf-9971-f59d12345678\\", \\"flag\\":\\"add\\"}, {\\"targetType\\":\\ "uuid\\",\\"target\\ ":\\"01acfd9d-e6a4-4e61-b9eb-aae012345678\\", \\"flag\\":\\"add\\"}, {\\"targetType\\":\\ "uuid\\",\\"target\\ ":\\"04a0e735-ad32-4835-b635-045812345678\\", \\"flag\\":\\"add\\"}\]" | The parameters required to configure virus detection for the server. Set the following parameters:<br>• targetType: the dimension on which viruses are blocked. UUIDs are supported. Set the value to uuid.<br>• target: the UUID of the server on which you want to configure virus detection.<br>• flag: enables or disables virus detection for the server. Valid values: add and del. add specifies to enable the feature and del specifies to disable the feature. |
| TargetType | String | Yes | uuid | The operating dimension on which you manage virus detection. You can manage virus detection only by UUID.<br>Set the value to uuid. |
| Type | String | Yes | auto_breaking | The method of virus detection.<br>Set the value to auto_breaking, which specifies that the system automatically blocks viruses. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Lang | String | No | zh | The natural language of the request and response. Valid values:<br>• zh: Chinese<br>• en: English |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | ABCD-PSD2-5256-1DSA-4222-JHBN | The ID of the request. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=OperateSuspiciousTargetConfig
&TargetOperations="[{\"targetType\":\"uuid\",\"target\":\"0585f81a-dd84-4ddf-9971-f59d12345678\",\"flag\":\"add\"},{\"targetType\":\"uuid\",\"target\":\"01acfd9d-e6a4-4e61-b9eb-aae012345678\",\"flag\":\"add\"},{\"targetType\":\"uuid\",\"target\":\"04a0e735-ad32-4835-b635-045812345678\",\"flag\":\"add\"}]"
&TargetType=uuid
&Type=auto_breaking
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<OperateSuspiciousTargetConfigResponse>
  <RequestId>ABCD-PSD2-5256-1DSA-4222-JHBN</RequestId>
</OperateSuspiciousTargetConfigResponse>
```

`JSON`  format

```json
{
    "RequestId":"ABCD-PSD2-5256-1DSA-4222-JHBN"
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-4"></a>

# 4.Server Guard

<a id="section-4-1"></a>

## 4.1. List of operations

This topic introduces all the Server Guard operations that you can call. For more information, see the corresponding operation description.

Asset management operations

| Operation | Description |
| --- | --- |
| CreateGroup | Creates an asset group. |
| DescribeGroupSummary | Obtains a list of asset groups. |
| DescribeGroupStruct | Queries the structure of an asset group. |
| DeleteGroup | Deletes an asset group. |
| DescribeAllTag | Queries the tag information of all servers. |
| DescribeBetachTag | Queries the tag information of a specified server. |
| ModifyBetachTag | Modifies the tags of multiple specified servers. |
| DeleteTag | Deletes the tag of a server. |
| DescribeAllEntity | Queries information about all servers. |
| DescribeEntityList | Queries a type of servers. |
| ModifyEntityGroup | Modifies the asset group information for a specified server. |
| DescribeMachines | Queries servers that match the specified criteria. |
| DescribeMachineDetail | Queries the detailed information about the specified server. |
| DescribePropertyScheduleConfig | Queries the update cycle of server information. |
| ModifyPropertyScheduleConfig | Modifies the synchronization cycle of host asset information. |
| DescribePropertyStatistic | Queries server statistics. |
| DescribePropertyPortItem | Obtains a list of listener ports on servers. |
| DescribePropertyPortDetail | Queries detailed listening port information. |
| DescribePropertyPortDiff | Queries listening port changes. |
| DescribePropertyProcItem | Obtains a list of server processes. |
| DescribePropertyProcDetail | Queries server process details. |
| DescribePropertyProcDiff | Queries process changes of servers. |
| DescribePropertySoftwareItem | Queries servers that have been installed with the specified application. |
| DescribePropertySoftwareDetail | Obtains the details of application software installed on a server. |
| DescribePropertySoftwareDiff | Queries changes of applications that have been installed on servers. |
| DescribePropertyUserItem | Queries user account information. |
| DescribePropertyUserDetail | Queries user account details. |
| DescribePropertyUserDiff | Queries user account changes. |
| PushAllTask | Performs a quick security check on specified servers. |
| DescribeTopRiskyAssets | Obtains a list of top N vulnerable servers. |
| UnbindAegis | Disables Server Guard for a specified server. |
| UninstallAegis | Uninstalls the Server Guard client from a specified server. |

Vulnerability management operations

| Operation | Description |
| --- | --- |
| DescribeTarget | Queries the servers that are checked for the specified type of risks in vulnerability management. |
| ModifyVulTarget | Modifies the servers for detecting a specified type of vulnerability in the vulnerability management settings. |
| DescribeVulTargetStatistics | Queries the information about target hosts for which vulnerability detection is enabled in the vulnerability management configuration. |
| DescribeTargetConfig | Queries the vulnerability scanning configuration information of a specified server. |
| ModifyTargetConfig | Modifies the vulnerability scanning configuration for a specified server. |
| DescribeVulConfig | Queries the global scanning configuration for each vulnerability type. |
| ModifyVulConfig | Modifies the global vulnerability scanning configuration. |
| DescribeAutoDelConfig | Queries the number of days that an invalid vulnerability is kept for before it is automatically deleted in the vulnerability management settings. |
| ModifyAutoDelConfig | Modifies the number of days that an invalid vulnerability is kept for before it is automatically deleted in the vulnerability management settings. |
| DescribeVulLevel | Queries the vulnerability severities that require attention. |
| ModifyVulLevel | Changes the vulnerability severities that require attention. |
| CreateVulWhitelist | Adds a specified vulnerability to the whitelist. |
| DescribeVulWhitelist | Obtains the whitelist of vulnerabilities. |
| DeleteVulWhitelist | Deletes a specified vulnerability from the vulnerability whitelist. |
| DescribeGroupedVul | Queries information about the specified vulnerability group. |
| DescribeVulList | Obtains a list of application vulnerabilities. |
| DescribeVulDetails | Queries detailed information about a vulnerability. |
| DescribeVulNumStatistics | Queries vulnerability statistics. |
| DescribeVulLevelStatistics | Obtains the statistics on vulnerabilities by vulnerability severity. |
| DescribeVulMachineList | Queries the vulnerability statistics of a specified server. |
| OperateVul | Handles detected vulnerabilities. |
| ModifyBatchIgnoreVul | Ignores multiple vulnerabilities. |
| DeleteVulBatch | Deletes a specified batch of vulnerabilities. |
| ExportVul | Exports vulnerability records that match the specified criteria. |
| DescribeVulExportInfo | Queries the information about vulnerability record export tasks. |

Baseline check operations

| Operation | Description |
| --- | --- |
| DescribeStrategy | Obtains a list of baseline check policies. |
| DescribeStratetyDetail | Queries the details of a specified baseline check policy. |
| ModifyStrategy | Modifies the basic information of a baseline check policy. |
| DeleteStrategy | Deletes a specified baseline check policy. |
| DescribeStrategyTarget | Queries the information about asset groups to which a specified baseline check policy applies. |
| ModifyStrategyTarget | Modifies the information about the asset groups that a specified baseline check policy applies to. |
| DescribeUuidConfig | Checks whether baseline check is enabled for a specified server. |
| ModifyMachineConfig | Configures whether to apply a specified baseline check policy to a specified server. |
| DescribeUserSetting | Queries the number of days an invalid risk is kept for before it is automatically deleted in baseline check. |
| CreateUserSetting | Specifies the number of days an invalid risk is kept for before it is automatically deleted in baseline check. |
| DescribeRiskWhiteList | Obtains the whitelist of risk items that are exempt from the baseline check. |
| BatchDeleteWhiteList | Deletes multiple risks from the whitelist for baseline check. |
| CreateUserWhiteList | Adds a specified risk to the baseline check whitelist. |
| DescribeStratety | Queries the execution details of a specified baseline check policy. |
| DescribeStrategyExecDetail | Queries the execution details of a baseline check policy. |
| DescribeRiskType | Queries all types of risks detected in baseline check and view the number of risks that have been detected by a baseline check policy or on the specified servers for a specific risk type. |
| Describesummary | Queries the risks detected in baseline check by risk type. |
| OperateWarning | Handles the risk alert records detected during the baseline check. |
| ExportWarning | Exports risks that match the specified criteria from baseline check. |
| DescribeExportInfo | Queries export task information, including the export progress and the download link of the exported file. |

Unusual logon detection operations

| Operation | Description |
| --- | --- |
| DescribeBaseConfigs | Queries the logon security settings. |
| ModifyBaseConfig | Modifies logon security settings. |
| DeleteBaseConfig | Deletes a logon security setting, such as an approved logon location or IP address. |
| DescribeSwitchConfigs | Queries the logon security configuration records in the logon security settings. |
| ModifySwitchConfig | Modifies the setting about whether to enable a logon security configuration record to identify a valid logon to a host in the logon security settings. |
| DescribeConfigTarget | Queries the information about host assets to which a specified logon security configuration record applies. |

Webshell detection operations

| Operation | Description |
| --- | --- |
| DescribeWebPath | Queries the Web directories defined in webshell settings. |
| ModifyWebPath | Modifies the Web directory in webshell settings. |
| DescribeCategoryCount | Queries the number of webshells detected by Server Guard. |
| DescribeWebshell | Queries records of webshell files that have been detected by Server Guard, including the detection time and webshell file path. |
| OperateTrojan | Handles the detected webshells. |
| DescribeQuaraFile | Obtains a list of quarantined files. |
| RollbackQuaraFile | Restores a quarantined file. |

Suspicious server detection operations

| Operation | Description |
| --- | --- |
| DescribeSuspEventTypes | Queries the unusual event types. |
| DescribeSuspTrendStatistics | Queries the chart data on different types of unusual server events on each day. |
| OperateSuspiciousEvent | Handles detected unusual events. |
| OperateLoginLog | Labels a detected unusual logon event as handled. |
| CreateSuspiciousExport | Exports the information about server unusual events based on search conditions. |
| DescribeSuspiciousExportInfo | Queries an unusual event export task. |

Server log retrieval operations

| Operation | Description |
| --- | --- |
| CreateLogQuery | Creates or saves server log search conditions. |
| DescribeLogQuery | Queries the saved server log search conditions. |
| DeleteLogQuery | Deletes the saved server log search conditions. |
| DescribeFilterFields | Queries the filter fields of a specified server log search condition. |
| DescribeHistogram | Obtains the statistics on server logs generated within a specified time frame. |
| DescribeLogInfo | Queries the host log fields based on specified query conditions. |
| DescribeLogItems | Queries the server log details that are returned by a query. |

<a id="section-4-2"></a>

## 4.2. Make API requests

<a id="section-4-2-1"></a>

### 4.2.1. Request structure

Apsara Stack Security API is based on Remote Procedure Call (RPC). This topic describes the structure of the API requests.

Description

You can send an HTTP request to call an API operation. The URL of the request must be in the following format:

```text
http://endpoint/?Action=xx&parameters
```

Where:

- `endpoint` : the endpoint used to call a cloud service. The endpoint for the Server Guard service is  `aegis.[ RegionId].example.com` .

- `Action` : the operation that you want to perform.

  For example, you can set this parameter to DescribeFeatures to query the deployed Apsara Stack Security features.

- `parameters` : the request parameters. Request parameters include common request parameters and custom request parameters. Request parameters must be separated with ampersands (&).

  - Common request parameters include information such as the API version and authentication information.

  - For more information about the custom request parameters, see the corresponding operation description.

Example

Call the DescribeFeatures operation to query the deployed Apsara Stack Security features.

```text
https://yundunprivate.[ RegionId].example.com/?Action=DescribeFeatures&AccessKeyId=key-test&Format=JSON&SecureTransport=true&SignatureMethod=HMAC-SHA1&SignatureNonce=15215528852396&SignatureVersion=1.0&SourceIp=1xxxx6&Timestamp=2018-03-02Txxxxxxx&Version=2018-01-16&Signature=xxxx%xxxx%3D
```

API requests are presented in the following easy-to-read format in this document:

```text
https://yundunprivate.[ RegionId].example.com/?Action=DescribeFeatures
&Format=JSON
&Version=2018-01-16
&Signature=xxxx%xxxx%3D
&SignatureMethod=HMAC-SHA1
&SignatureNonce=15215528852396
&SignatureVersion=1.0
&AccessKeyId=key-test
&Timestamp=2012-06-01T12:00:00Z
```

<a id="section-4-2-2"></a>

### 4.2.2. Signature mechanism

Apsara Stack Security authenticates each access request. You need to include a signature for the submitted HTTP or HTTPS request.

API authorization

To ensure the security of your account, we recommend that you use a Resource Access Management (RAM) user to call API operations. Before using a RAM user to call an API operation, you must grant the RAM user the corresponding permission to call the API by creating an authorization policy and attaching the policy to the RAM user.

API signature

To ensure secure calls to the API, Alibaba Cloud authenticates each API request through the signature. When you manually make an API request, you need to use AccessKey Secret to calculate the signature, that is, the hash-based message authentication code (HMAC) value, based on the encoded and sorted request string. For more information, see the definition in RFC 2104.

This topic uses the raw access parameters in the following table to describe how to create an API signature.

| Parameter | Description |
| --- | --- |
| Access point | <code>http://semawaf.[ RegionId].example.com/?</code> |
| API-specific parameters | <code>Action=DescribeFeatures</code> |
| Common parameters (excluding the Signature parameter) | <code>&amp;Timestamp=2016-02-23T12:46:24Z</code><br><code>&amp;Format=JSON</code><br><code>&amp;AccessKeyId=&lt;yourAccessKeyId&gt;</code><br><code>&amp;SignatureMethod=HMAC-SHA1</code><br><code>&amp;SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf</code><br><code>&amp;Version=2018-01-16</code><br><code>&amp;SignatureVersion=1.0</code> |
| AccessKey secret | <code>&lt;yourAccessKeySecret&gt;</code> |

1. Use the request parameters to construct a canonicalized query string.

   Note

   The request parameters include common request parameters (excluding the

   Signature parameter) and API-specific parameters.

   <ol type="i">

   <li>

   Sort the parameters.

   </li>

   </ol>

   Sort the request parameters in alphabetical order.

   <ol type="i" start="2">

   <li>

   Encode the parameters.

   </li>

   </ol>

   Use UTF-8 to URL-encode the parameter names and values. The encoding rules are as follows:

   - Letters, digits, hyphens (-), underscores (_), periods (.), and tildes (~) are not encoded.

   - Other characters are encoded in the %XY format, where XY is the hexadecimal representation of the character in ASCII. For example, the double quotation mark (") is encoded as %22.

   - Extended UTF-8 characters are encoded in the %XY%ZA… format.

   - Note that a space is encoded as %20, instead of a plus sign (+).

   <ol type="i" start="3">

   <li>

   Connect the encoded parameter names and values with equal signs (=).

   </li>

   <li>

   Then, sort the parameter name and value pairs connected by equal signs in alphabetical order,

   </li>

   </ol>

   and connect them with ampersands (&) to produce the canonicalized query string.

2. Use the canonicalized query string to construct the string for signature calculation based on the following rules:

   ```text
   StringToSign=HTTPMethod + “&” + percentEncode(“/”) + ”&” +
   percentEncode(CanonicalizedQueryString)
   ```

3. Calculate the HMAC value of the StringToSign string according to the definition in RFC 2104.

   Note

   The key used for signature calculation is your AccessKey secret adding the

   ampersand (&) (ASCII 38). Secure Hash Algorithm 1 (SHA1) is used as the hash algorithm.

4. Encode the preceding HMAC value into a string based on Base64 encoding rules to obtain the signature value.

   ```text
   LEW8N4y7Uasop******
   ```

5. Set the Signature parameter in the request parameters to this signature value to sign the request.

<a id="section-4-2-3"></a>

### 4.2.3. Common request parameters

The following table describes the common request parameters that are used to indicate information such as the API version and authentication information.

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Version | String | Yes | The API version in the format of YYYY-MM-DD.<br>Set the value to <em>2016-11-11</em>. |
| AccessKeyId | String | Yes | The key ID that Alibaba Cloud assigns to a user for service access. |
| Signature | String | Yes | The signature string. |
| SignatureMethod | String | Yes | The signature method.<br>Set the value to <em>HMAC-SHA1</em>. |
| Timestamp | String | Yes | The timestamp of the request. Follow the ISO 8601 standard to specify the date and use the offset from Coordinated Universal Time (UTC) to specify the time zone.<br>The format is <code> YYYY-MM-</code><code>DDThh:mm:ssZ </code>.<br>For example, 2014-05-26T12:00:00Z indicates 20:00:00 on May 26, 2014, Beijing time. |
| SignatureVersion | String | Yes | The signature algorithm version.<br>Set the value to <em>1.0</em>. |
| SignatureNonce | String | Yes | The unique random number used to prevent network replay attacks. You must use different random numbers for different requests. |
| ResourceOwnerAc count | String | No | The owner account of the resource to be accessed through this API request, that is, the logon username. |
| Format | String | No | The format of the response.<br>Set the value to <em>JSON or XML</em>.<br>Note Default value: XML. |

<a id="section-4-2-4"></a>

### 4.2.4. Response structure

Apsara Stack Security API responses support both the XML and JSON formats. The system always returns a unique identification code RequestId each time you send a request to call an operation, no matter whether the call is successful or not.

Sample responses (XML format)

```xml
<? xml version="1.0" encoding="UTF-8"? >
<! -- The root node of the result -->
<Operation name+Response>
    <! -- Returned request ID -->
    <RequestId>4C467B38-3910-447D-87BC-AC049166F216</RequestId>
    <! -- Returned data -->
</Operation name+Response>
```

Sample responses (JSON format)

```json
{
"RequestId": "4C467B38-3910-447D-87BC-AC049166F216",
/* Returned data */
}
```

<a id="section-4-3"></a>

## 4.3. Asset management

<a id="section-4-3-1"></a>

### 4.3.1. CreateGroup

Description

You can call this operation to create an asset group.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>CreateGroup</em>. |
| GroupFather | Long | Yes | The parent asset group ID. |
| GroupFlag | Integer | Yes | The asset group type. Valid values:<br>• <em>0</em>: indicates a default group.<br>• <em>1</em>: indicates a custom group. |
| GroupIndex | Integer | Yes | The sequence number of the asset group. |
| GroupName | String | Yes | The name of the asset group. |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=CreateGroup
  &GroupFather=0
  &GroupFlag=1
  &GroupIndex=1
  &GroupName=Web group
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
   "RequestId":"415AE1FC-3C11-4AA9-A06F-DE13D3430366"
  }
  ```

<a id="section-4-3-2"></a>

### 4.3.2. DescribeGroupSummary

Description

You can call this operation to obtain a list of asset groups.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>DescribeGroupSummary</em>. |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| Count | Integer | The number of asset groups. |
| Groups | List | The information about asset groups. For more information, see the following parameter descriptions. |
| GroupId | Long | The asset group ID. |
| GroupIndex | Integer | The sequence number of the asset group. |
| GroupLevel | Integer | The level of the asset group. |
| GroupName | String | The name of the asset group. |
| GroupFather | Integer | The ID of the parent asset group. |
| GroupFlag | Integer | The type of the asset group. Valid values:<br>• <em>1</em>: indicates a non-leaf node group that contains child asset groups.<br>• <em>0</em>: indicates a leaf node group. |
| MachineNum | Integer | The number of ECS instances contained in the group. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=DescribeGroupSummary
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
   "Groups":[
    {
     "GroupFlag":1,
     "GroupName":"Test group 21",
     "GroupIndex":1,
     "MachineNum":0,
     "GroupId":346
    },
    {
     "GroupFlag":1,
     "GroupName":"Test group 1",
     "GroupIndex":2,
     "MachineNum":0,
     "GroupId":343
    },
    {
     "GroupFlag":1,
     "GroupName":"Test group 2",
     "GroupIndex":3,
     "MachineNum":0,
     "GroupId":345
    },
    {
     "GroupFlag":0,
     "GroupName":"Not grouped",
     "GroupIndex":100,
     "MachineNum":1,
     "GroupId":336
    }
   ],
   "Count":4,
   "RequestId":"B9FB5483-3CA6-4520-9F89-068ED6AAC6EE"
  }
  ```

<a id="section-4-3-3"></a>

### 4.3.3. DescribeGroupStruct

Description

You can call this operation to query the asset group structure.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set this parameter to <em>DescribeGroupStruct</em>. |
| Mark | String | No | The IP address or instance name of the server. |
| TagIdList | String | No | The server tag ID. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| GroupFather | Integer | The ID of the parent asset group. |
| GroupId | Long | The ID of the asset group. |
| Groups | List | The asset groups. For more information, see the following descriptions. |
| GroupId | Long | The ID of the asset group. |
| GroupIndex | Integer | The sequence number of the asset group. |
| GroupLevel | Integer | The level of the asset group. |
| GroupName | String | The name of the asset group. |
| GroupFather | Integer | The ID of the parent asset group. |
| GroupFlag | Integer | The type of the asset group. Valid values:<br>• <em>1</em>: indicates a non-leaf node group that contains child asset groups.<br>• <em>0</em>: indicates a leaf node group. |
| ChildGroups | List | The child asset groups. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample request

  ```text
  https://aegis.[ RegionId].example.com/?Action=DescribeGroupStruct
  &remark=x.x.x.x
  &tagIdList=123
  &<Common request parameters>
  ```

- Sample response (JSON format)

  ```json
  {
      "Groups":[
          {
              "groupIndex":2,
              "groupFather":0,
              "groupId":343,
              "groupName":"****",
              "groupLevel":1,
              "groupFlag":1,
              "childGroups":[]
          },
          {
              "groupIndex":3,
              "groupFather":0,
              "groupId":345,
              "groupName":"****",
              "groupLevel":1,
              "groupFlag":1,
              "childGroups":[
                  {
                      "groupIndex":1,
                      "groupFather":345,
                      "groupId":346,
                      "groupName":"****",
                      "groupLevel":2,
                      "groupFlag":1,
                      "childGroups":[]
                  }
              ]
          },
          {
              "groupIndex":100,
              "groupFather":0,
              "groupId":336,
              "groupName":"****",
              "groupFlag":0,
              "childGroups":[]
          }
      ],
      "RequestId":"C4490A16-DDE4-4351-A366-57F9FCDC188F",
      "GroupFather":0,
      "GroupId":0
  }
       
  ```

<a id="section-4-3-4"></a>

### 4.3.4. DeleteGroup

Description

You can call this operation to delete a specified asset group.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>DeleteGroup</em>. |
| GroupFlag | Integer | Yes | The type of the asset group. Valid values:<br>• <em>0</em>: indicates a default group.<br>• <em>1</em>: indicates a custom group. |
| GroupId | Long | Yes | The ID of the asset group. |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=DeleteGroup
  &GroupFlag=1
  &GroupId=123
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
   "RequestId":"415AE1FC-3C11-4AA9-A06F-DE13D3430366"
  }
  ```

<a id="section-4-3-5"></a>

### 4.3.5. DescribeAllTag

Description

You can call this operation to query the tag information of all servers.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>DescribeAllTag</em>. |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| EntityList | Array | The tag information of all servers. For more information, see the following parameter descriptions. |
| AliUid | Long | The Alibaba Cloud account ID. |
| GmtCreate | Long | The creation time of the asset tag. |
| GmtModified | Long | The last modification time of the asset tag. |
| Id | Long | The ID of the asset tag. |
| TagName | String | The name of the asset tag. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=DescribeAllTag
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
   "RequestId":"09D7C349-5306-4335-849A-10916F89E769",
   "EntityList":[
    {
     "AliUid":"123",
     "GmtCreate":"1508897933000",
     "GmtModified":"1508897933000",
     "Id":"1",
     "TagName":"test"
    },
   ]
  }
  ```

<a id="section-4-3-6"></a>

### 4.3.6. DescribeBetachTag

Description

You can call this operation to query the tag information of a specified server.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>DescribeBetachTag</em>. |
| UuidList | String | No | The UUID of the server. |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| TagInfoList | Array | The tag information of the specified server. For more information, see the following parameter descriptions. |
| AliUid | Long | The Alibaba Cloud account ID. |
| GmtCreate | Long | The creation time of the asset tag. |
| GmtModified | Long | The last modification time of the asset tag. |
| Id | Long | The ID of the asset tag. |
| TagName | String | The name of the asset tag. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=DescribeBetachTag
  &UuidList=inet-00f20b1a-e2dd-408b-b38e-6a6e1ed5d818
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
   "RequestId":"09D7C349-5306-4335-849A-10916F89E769",
   "EntityList":[
    {
     "AliUid":"123",
     "GmtCreate":"1508897933000",
     "GmtModified":"1508897933000",
     "Id":"1",
     "TagName":"test"
    },
   ]
  }
  ```

<a id="section-4-3-7"></a>

### 4.3.7. ModifyBetachTag

Description

You can call this operation to modify the tags of multiple specified servers.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>ModifyBetachTag</em>. |
| TagList | String | Yes | The server tag. Separate multiple tags with commas (,). |
| UuidList | String | Yes | The UUID of the server. |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=ModifyBetachTag
  &UuidList=inet-00f20b1a-e2dd-408b-b38e-6a6e1ed5d818
  &TagList=test,test2
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
   "RequestId":"09D7C349-5306-4335-849A-10916F89E769",
  }
  ```

<a id="section-4-3-8"></a>

### 4.3.8. DeleteTag

Description

You can call this operation to delete a server tag.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>DeleteTag</em>. |
| Id | Long | No | The ID of the server tag. |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=DeleteTag
  &Id=123
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
   "RequestId":"415AE1FC-3C11-4AA9-A06F-DE13D3430366"
  }
  ```

<a id="section-4-3-9"></a>

### 4.3.9. DescribeAllEntity

Description

You can call this operation to query information about all servers.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set this parameter to <em>DescribeAllEntity</em>. |
| GroupId | Long | No | The ID of the asset group. |
| Os | String | No | The operating system of the server.Valid values:<br>• <em>win</em>: indicates the Windows operating system.<br>• <em>linux</em>: indicates the Linux operating system. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| Count | Integer | The number of returned records. |
| EntityList | Array | The servers. For more information, see the following descriptions. |
| GroupId | Integer | The ID of the asset group. |
| Uuid | String | The universally unique identifier (UUID) of the server. |
| InstanceName | String | The instance name of the server. |
| Ip | String | The IP address of the server.<br>Note The public IP address of the server is displayed preferentially. If no public IP address is assigned to the server, the private IP address of the server is displayed. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample request

  ```text
  https://aegis.[ RegionId].example.com/?Action=DescribeAllEntity
  &GroupId=123
  &Os=win
  &<Common request parameters>
        
  ```

- Sample response (JSON format)

  ```json
  {
      "Count":2,
      "RequestId":"09D7C349-5306-4335-849A-10916F89E769",
      "EntityList":[
          {
              "Uuid":"inet-00f20b1a-e2dd-408b-b38e-6a6e1ed5d818",
              "Ip":"x.x.x.x",
              "GroupId":336,
              "InstanceName":"****"
          },
          ......
      ]
  }
        
  ```

<a id="section-4-3-10"></a>

### 4.3.10. DescribeEntityList

Description

You can call this operation to query servers of a specified type. For example, you can query servers by security event type.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set this parameter to <em>DescribeEntityList</em>. |
| PageSize | Integer | No | The number of records to return on each page.<br>Default value: <em>20</em>. |
| CurrentPage | Integer | No | The number of the page to return.<br>Default value: <em>1</em>. |
| RegionNo | String | No | The ID of the region. |
| GroupId | Long | No | The ID of the asset group. |
| Os | String | No | The operating system of the server.Valid values:<br>• <em>win</em>: indicates the Windows operating system.<br>• <em>linux</em>: indicates the Linux operating system. |
| Account | String | No | Queries servers with unusual logons detected.<br>Set this parameter to <em>remoteLogin</em>. |
| Health | String | No | Queries servers with baseline check issues detected.<br>Set this parameter to <em>exception</em>. |
| Patch | String | No | Queries servers with vulnerabilities detected.<br>Set this parameter to <em>vul</em>. |
| Suspicious | String | No | Queries servers with unusual events detected.<br>Set this parameter to <em>exception</em>. |
| Trojan | String | No | Queries servers with webshells detected.<br>Valid values:<br>• <em>webshell</em>: indicates trojan files.<br>• <em>process</em>: indicates trojan processes. |
| Status | String | No | The status of the Server Guard Agent.<br>Valid values:<br>• <em>offline</em>: indicates that the Server Guard Agent is offline.<br>• <em>pause</em>: indicates that the Server Guard Agent is disabled. |
| TagIdList | String | No | The server tag ID. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| CurrentPage | Integer | The number of the current page returned. |
| PageSize | Integer | The number of records returned on each page. |
| TotalCount | Integer | The number of returned records. |
| EntityList | Array | The servers. For more information, see the following descriptions. |
| AegisOnline | Boolean | Indicates whether the Server Guard Agent is online. |
| AegisVersion | String | The version of the Server Guard Agent. |
| BuyVersion | String | The version of the Server Guard package. |
| GroupId | Integer | The ID of the asset group. |
| ClientStatus | Boolean | Indicates whether the server is protected. A value of false indicates that the protection for the server is paused. |
| Flag | Integer | The type of the server. Valid values:<br>• <em>0</em>: indicates an Alibaba Cloud ECS instance.<br>• <em>1</em>: indicates an external server. |
| Uuid | String | The universally unique identifier (UUID) of the server. |
| InstanceName | String | The instance name of the server. |
| Os | String | The type of the operating system. |
| Region | String | The ID of the region. |
| Ip | String | The IP address of the server.<br>Note The public IP address of the server is displayed preferentially. If no public IP address is assigned to the server, the private IP address of the server is displayed. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample request

  ```text
  https://aegis.[ RegionId].example.com/?Action=DescribeEntityList
  &Account=remoteLogin
  &CurrentPage=1
  &GroupId=1
  &Health=exception
  &Os=windows
  &PageSize=20
  &Patch=vul
  &RegionNo=****
  &Remark=x.x.x.x
  &Status=offline
  &Suspicious=exception
  &TagIdList=1,2,3
  &Trojan=webshell
  &<Common request parameters>
        
  ```

- Sample response (JSON format)

  ```json
  {
      "TotalCount":1,
      "PageSize":1,
      "RequestId":"8BFB5273-6582-446A-9E0B-BAC0A1A468EA",
      "CurrentPage":1,
      "EntityList":[
          {
              "Uuid":"inet-00f20b1a-e2dd-408b-b38e-6a6e1ed5d818",
              "Os":"linux",
              "ClientStatus":false,
              "Ip":"x.x.x.x",
              "Region":"****",
              "Flag":0,
              "BuyVersion":"4",
              "GroupId":336,
              "InstanceName":"****"
          }
      ]
  }
        
  ```

<a id="section-4-3-11"></a>

### 4.3.11. ModifyEntityGroup

Description

You can call this operation to modify the asset group information for a specified server.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>ModifyEntityGroup</em>. |
|  |  |  |  |
| Name | Type | Required | Description |

<table>
  <tr>
    <td>GroupId</td>
    <td>Long</td>
    <td>No</td>
    <td>The modified asset group ID.</td>
  </tr>
  <tr>
    <td>Uuids</td>
    <td>String</td>
    <td>No</td>
    <td>The UUID of the server. Separate multiple UUIDs with commas (,).</td>
  </tr>
</table>

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=ModifyEntityGroup
  &GroupId=11
  &Uuids=inet-db626549-870c-4d3e-b0b5-4d8a5c7268a6,inet-db626549-870c-4d3e-b0b5-4d8a5c7268a7
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
   "RequestId":"C4490A16-DDE4-4351-A366-57F9FCDC188F",
  }
  ```

<a id="section-4-3-12"></a>

### 4.3.12. DescribeMachines

Description

You can call this operation to query servers that match the specified criteria. For example, you can query all servers in an asset group.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set this parameter to <em>DescribeMachines</em>. |
| GroupId | Long | No | The ID of the asset group. |
| TagIdList | String | No | The server tag ID. |
| Mark | String | No | The IP address or instance name of the server. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| Count | Integer | The number of returned records. |
| Machines | Array | The servers. For more information, see the following descriptions. |
| GroupId | Integer | The ID of the asset group. |
| InstanceName | String | The instance name of the server. |
| Os | String | The type of the operating system. |
| Ip | String | The IP address of the server.<br>Note The public IP address of the server is displayed preferentially. If no public IP address is assigned to the server, the private IP address of the server is displayed. |
| Uuid | String | The universally unique identifier (UUID) of the server. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample request

  ```text
  https://aegis.[ RegionId].example.com/?Action=DescribeMachines
  &GroupId=123
  &<Common request parameters>
  ```

- Sample response (JSON format)

  ```json
  {
      "Count":1,
      "Machines":[
          {
              "groupId":336,
              "os":"linux",
              "instanceName":"****",
              "uuid":"inet-db626549-870c-4d3e-b0b5-4d8a5c7268a6",
              "ip":"192.168.x.x"
          }
      ],
      "RequestId":"C984123D-C8E0-4974-9CEE-ADD0596C46DB"
  }
        
  ```

<a id="section-4-3-13"></a>

### 4.3.13. DescribeMachineDetail

Description

You can call this operation to query the detailed information about a specified server.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set this parameter to <em>DescribeMachineDetail</em>. |
| Uuid | String | No | The universally unique identifier (UUID) of the server. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| MachineDetail | Array | The detailed information about the server. For more information, see the following descriptions. |
| AegisOnline | Boolean | Indicates whether the Server Guard Agent is online. |
| AegisVersion | String | The version of the Server Guard Agent. |
| BuyVersion | String | The version of the Server Guard package. |
| GroupId | Integer | The ID of the asset group. |
| ClientStatus | Boolean | Indicates whether the server is protected. A value of false indicates that the protection for the server is paused. |
| Flag | Integer | The type of the server. Valid values:<br>• <em>0</em>: indicates an Alibaba Cloud ECS instance.<br>• <em>1</em>: indicates an external server. |
| GroupId | Long | The ID of the asset group. |
| GroupTrace | String | The full path of the asset group. |
| InstanceId | String | The instance ID of the server. |
| InstanceName | String | The instance name of the server. |
| Os | String | The type of the operating system. |
| Region | String | The ID of the region. |
| Ip | String | The IP address of the server.<br>Note The public IP address of the server is displayed preferentially. If no public IP address is assigned to the server, the private IP address of the server is displayed. |
| IntranetIp | String | The private IP address of the server. |
| Uuid | String | The UUID of the server. |
| Tag | String | The server tag ID. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample request

  ```text
  https://aegis.[ RegionId].example.com/?Action=DescribeMachineDetail
  &Uuid=6dbdbfe7-06fa-4d9a-8268-ce2dc6d673ac
  &<Common request parameters>
        
  ```

- Sample response (JSON format)

  ```json
  {
      "RequestId":"5D5D6F8F-6986-4996-9321-8EEA9FC048D1",
      "MachineDetail":{
          "Uuid":"inet-db626549-870c-4d3e-b0b5-4d8a5c7268a6",
          "Ip":"192.168.x.x",
          "GroupTrace":"Not grouped",
          "Os":"linux",
          "ClientStatus":true,
          "Region":"outside-of-aliyun",
          "Tag":"",
          "AegisOnline":false,
          "InstanceName":"****"
      }
  }
        
  ```

<a id="section-4-3-14"></a>

### 4.3.14. DescribePropertyScheduleConfig

Description

You can call this operation to query the update cycle of server information.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>DescribePropertyScheduleConfig</em>. |
| Type | String | No | The type of the server information. Valid values:<br>• <em>scheduler_account_period</em>: indicates the user information.<br>• <em>scheduler_port_period</em>: indicates the port information.<br>• <em>scheduler_process_period</em>: indicates the process information.<br>• <em>scheduler_software_period</em>: indicates the application software information. |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| Config | String | The update cycle in hours. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=DescribePropertyScheduleConfig
  &Type=scheduler_account_period
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
   "RequestId":"C528C153-33E6-4CF5-8C90-A2E6FFD6191C",
   "Config": "2"
  }
  ```

<a id="section-4-3-15"></a>

### 4.3.15. ModifyPropertyScheduleConfig

Description

You can call this operation to modify the synchronization cycle of server information.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>ModifyPropertyScheduleConfig</em>. |
| Type | String | Yes | The type of asset information whose synchronization cycle is to be modified.Valid values:<br>• <em>scheduler_software_period</em>: indicates the synchronization cycle of application software information.<br>• <em>scheduler_account_period</em>: indicates the synchronization cycle of user account information.<br>• <em>scheduler_port_period</em>: indicates the synchronization cycle of port information.<br>• <em>scheduler_process_period</em>: indicates the synchronization cycle of process information. |
| ScheduleTime | String | Yes | The new synchronization cycle. Unit: hours. |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| ModifyResult | Boolean | Indicates whether the modification is successful. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=ModifyPropertyScheduleConfig
  &Type=scheduler_software_period
  &ScheduleTime=24
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
   "ModifyResult":true,
   "RequestId":"2932CB78-51FB-459C-A3E8-76BE2968069A"
  }
  ```

<a id="section-4-3-16"></a>

### 4.3.16. DescribePropertyStatistic

Description

You can call this operation to query the server statistics.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>DescribePropertyStatistic</em>. |
| Uuids | String | No | The UUID of the server. Separate multiple UUIDs with commas (,). |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| PropertyStatistics | Array | The list of server statistics. For more information, see the following parameter descriptions. |
| PortCount | String | The number of enabled ports. |
| PortGetDate | String | The port information update time. |
| ProcCount | String | The number of running processes. |
| ProcGetDate | String | The process information update time. |
| RootUserCount | String | The number of user accounts with root permission. |
| UserCount | String | The total number of user accounts. |
| UserGetDate | String | The user account information update time. |
| Uuid | String | The UUID of the server. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=DescribePropertyStatistic
  &Uuids=inet-00f20b1a-e2dd-408b-b38e-6a6e1ed5d818
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
   "PropertyStatistics":[
    {
     "UserGetDate":1514373155000,
     "Uuid":"inet-00f20b1a-e2dd-408b-b38e-6a6e1ed5d818",
     "RootUserCount":1,
     "UserCount":33,
     "ProcCount":89,
     "PortGetDate":1514115614000,
     "PortCount":6,
     "ProcGetDate":1514373133000
    }
   ],
   "RequestId":"C1CACE7E-E868-4E44-A52E-4CB1463B62BB"
  }
  ```

<a id="section-4-3-17"></a>

### 4.3.17. DescribePropertyPortItem

Description Description

You can call this operation to obtain a list of listener ports on hosts.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>DescribePropertyPortItem</em>. |
| PageSize | Integer | No | The maximum number of records to be displayed on each page of the query output.<br>Default value: <em>20</em>. |
| CurrentPage | Integer | No | The current page number.<br>Default value: <em>1</em>. |
| Port | String | No | The port number. |
| ProcName | String | No | The process name. |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| TotalCount | Integer | The total number of returned records. |
| Count | Integer | The number of records on the current page. |
| CurrentPage | Integer | The current page number. |
| PageSize | Integer | The maximum number of records displayed on a page. |
| PropertyPortItems | Array | The list of listener ports on hosts. For more information, see the following parameter descriptions. |
| Count | Integer | The number of hosts that have enabled the specified port. |
| Port | String | The port number. |
| Proto | String | The network protocol, such as TCP or UDP. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=DescribePropertyPortItem
  &Port=22
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
   "TotalCount":1,
   "PageSize":20,
   "RequestId":"9D38986A-F145-4FA8-AE1C-1DB1C2BDF4C0",
   "CurrentPage":1,
   "PropertyPortItems":[
    {
     "Proto":"tcp",
     "Port":"22",
     "Count":2
    }
   ],
   "Count":1
  }
  ```

<a id="section-4-3-18"></a>

### 4.3.18. DescribePropertyPortDetail

Description

You can call this operation to query detailed information about a listening port.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set this parameter to <em>DescribePropertyPortDetail</em>. |
| PageSize | Integer | No | The number of records to return on each page.<br>Default value: <em>20</em>. |
| CurrentPage | Integer | No | The number of the page to return.<br>Default value: <em>1</em>. |
| GroupId | Long | No | The ID of the asset group. |
| Ip | String | No | The IP address of the server. |
| Port | String | No | The port number. |
| Extend | String | No | Indicates whether fuzzy match is enabled to search for port numbers.Valid values:<br>• <em>1</em>: indicates that fuzzy match is enabled.<br>• <em>0</em>: indicates that fuzzy match is disabled. |
| ProcName | String | No | The name of the process. |
| Mark | String | No | The IP address or instance name of the server.<br>Note Fuzzy match is supported. |
| TagIdListString | String | No | The server tag ID. |
| Uuid | String | No | The universally unique identifier (UUID) of the server. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| TotalCount | Integer | The number of returned records. |
| Count | Integer | The number of records returned on the current page. |
| CurrentPage | Integer | The number of the current page returned. |
| PageSize | Integer | The number of records returned on each page. |
| PropertyPorts | Array | The information about the listening port. For more information, see the following descriptions. |
| BindIp | String | The IP address bound to the port. |
| Create | String | The time when the port was enabled. |
| InstanceName | String | The instance name of the server. |
| Ip | String | The IP address of the server. |
| Port | String | The port number. |
| ProcName | String | The name of the process. |
| Proto | String | The network protocol, such as TCP and UDP. |
| Uuid | String | The UUID of the server. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample request

  ```text
  https://aegis.[ RegionId].example.com/?Action=DescribePropertyPortDetail
  &Uuid=inet-f6ac9a93-0818-4052-90e2-d24f18ee198b
  &<Common request parameters>
        
  ```

- Sample response (JSON format)

  ```json
  {
      "TotalCount":1,
      "PageSize":20,
      "RequestId":"D85484BB-4DC2-44EC-AD67-0B3765EC9213",
      "CurrentPage":1,
      "PropertyPorts":[
          {
              "InstanceName":"****",
              "Uuid":"inet-f6ac9a93-0818-4052-90e2-d24f18ee198b",
              "Proto":"tcp",
              "Create":1514373168000,
              "Ip":"x.x.x.x",
              "Port":"22",
              "ProcName":"sshd",
              "BindIp":"0.0.0.0"
          }
      ],
      "Count":1
  }
        
  ```

<a id="section-4-3-19"></a>

### 4.3.19. DescribePropertyPortDiff

Description

You can call this operation to query listening port changes.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set this parameter to <em>DescribePropertyPortDiff</em>. |
| PageSize | Integer | No | The number of records to return on each page.<br>Default value: <em>20</em>. |
| CurrentPage | Integer | No | The number of the page to return.<br>Default value: <em>1</em>. |
| DiffStatus | String | No | The type of the listening port change.Valid values:<br>• <em>start</em>: indicates that the listening port is enabled.<br>• <em>stop</em>: indicates that the listening port is disabled. |
| Ip | String | No | The IP address of the server. |
| Port | String | No | The port number. |
| Extend | String | No | Indicates whether fuzzy match is enabled to search for port numbers.Valid values:<br>• <em>1</em>: indicates that fuzzy match is enabled.<br>• <em>0</em>: indicates that fuzzy match is disabled. |
| ProcName | String | No | The name of the process. |
| Mark | String | No | The IP address or instance name of the server.<br>Note Fuzzy match is supported. |
| TagIdListString | String | No | The server tag ID. |
| Uuid | String | No | The universally unique identifier (UUID) of the server. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| TotalCount | Integer | The number of returned records. |
| CurrentPage | Integer | The number of the current page returned. |
| PageSize | Integer | The number of records returned on each page. |
| PropertyPortDiffs | Array | The listening port changes. For more information, see the following descriptions. |
| BindIp | String | The IP address bound to the port. |
| Create | String | The time when the port was enabled. |
| DiffKeyList | String | The port fields that have been changed, including Proto, ProcName, and BindIp. |
| DiffStatus | String | The type of the listening port change. Valid values:<br>• <em>start</em>: indicates that the listening port is enabled.<br>• <em>stop</em>: indicates that the listening port is disabled. |
| InstanceName | String | The instance name of the server. |
| Ip | String | The IP address of the server. |
| ProcName | String | The name of the process. |
| Port | String | The port number. |
| Proto | String | The network protocol, such as TCP and UDP. |
| Uuid | String | The UUID of the server. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample request

  ```text
  https://aegis.[ RegionId].example.com/?Action=DescribePropertyPortDiff
  &Uuid=inet-f6ac9a93-0818-4052-90e2-d24f18ee198b
  &<Common request parameters>
        
  ```

- Sample response (JSON format)

  ```json
  {
      "TotalCount":1,
      "PageSize":20,
      "RequestId":"AFC431E3-F8E3-4652-91CB-9FF4053F282A",
      "CurrentPage":1,
      "PropertyPortDiffs":[
          {
              "InstanceName":"****",
              "Uuid":"inet-f6ac9a93-0818-4052-90e2-d24f18ee198b",
              "Proto":"tcp",
              "Create":1514366856000,
              "Ip":"x.x.x.x",
              "Port":"22",
              "ProcName":"sshd",
              "DiffKeyList":"proto,procName,bindIp",
              "DiffStatus":"stop",
              "BindIp":"0.0.0.0"
          }
      ]
  }
        
  ```

<a id="section-4-3-20"></a>

### 4.3.20. DescribePropertyProcItem

Description

You can call this operation to obtain a list of server processes.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>DescribePropertyProcItem</em>. |
| PageSize | Integer | No | The maximum number of records to be displayed on each page of the query output.<br>Default value: <em>20</em>. |
| CurrentPage | Integer | No | The current page number.<br>Default value: <em>1</em>. |
| Name | String | No | The process name. |
| User | String | No | The user who started the process. |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| TotalCount | Integer | The total number of returned records. |
| Count | Integer | The number of records on the current page. |
| CurrentPage | Integer | The current page number. |
| PageSize | Integer | The maximum number of records displayed on a page. |
| PropertyProcItems | Array | The list of server processes. For more information, see the following parameter descriptions. |
| Count | Integer | The number of servers on which the process is running. |
| Name | String | The process name. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=DescribePropertyProcItem
  &Name=init
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
   "TotalCount":1,
   "PropertyProcItems":[
    {
     "Count":2,
     "Name":"init"
    }
   ],
   "PageSize":20,
   "RequestId":"8BE95FB1-66B7-4509-AF82-3AA67368A5D8",
   "CurrentPage":1,
   "Count":1
  }
  ```

<a id="section-4-3-21"></a>

### 4.3.21. DescribePropertyProcDetail

Description

You can call this operation to query server process details.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set this parameter to <em>DescribePropertyProcDetail</em>. |
| PageSize | Integer | No | The number of records to return on each page.<br>Default value: <em>20</em>. |
| CurrentPage | Integer | No | The number of the page to return.<br>Default value: <em>1</em>. |
| GroupId | Long | No | The ID of the asset group. |
| Ip | String | No | The IP address of the server. |
| Name | String | No | The name of the process. |
| Extend | String | No | Indicates whether fuzzy match is enabled to search for process names.Valid values:<br>• <em>1</em>: indicates that fuzzy match is enabled.<br>• <em>0</em>: indicates that fuzzy match is disabled. |
| User | String | No | The user who started the process. |
| Mark | String | No | The IP address or instance name of the server.<br>Note Fuzzy match is supported. |
| Cmdline | String | No | The process parameter. |
| TagIdListString | String | No | The server tag ID. |
| Uuid | String | No | The universally unique identifier (UUID) of the server. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| TotalCount | Integer | The number of returned records. |
| Count | Integer | The number of records returned on the current page. |
| CurrentPage | Integer | The number of the current page returned. |
| PageSize | Integer | The number of records returned on each page. |
| PropertyProcs | Array | The details of the server process. For more information, see the following descriptions. |
| Cmdline | String | The process parameter. |
| Create | String | The time when the information was reported. |
| EuidName | String | The permissions that the process has to access resources and files. |
| InstanceName | String | The instance name of the server. |
| Md5 | String | The MD5 value of the executable file. |
| Name | String | The name of the process. |
| Path | String | The path of the process. |
| Pid | String | The ID of the process. |
| ProcName | String | The name of the process. |
| Pname | String | The name of the parent process. |
| StartTime | String | The time when the process was started. |
| User | String | The user who started the process. |
| Uuid | String | The UUID of the server. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample request

  ```text
  https://aegis.[ RegionId].example.com/?Action=DescribePropertyProcDetail
  &Uuid=inet-00f20b1a-e2dd-408b-b38e-6a6e1ed5d818
  &<Common request parameters>
        
  ```

- Sample response (JSON format)

  ```json
  {
      "PropertyProcs":[
          {
              "InstanceName":"****",
              "Path":"/sbin/init",
              "Pname":"N/A",
              "Uuid":"inet-00f20b1a-e2dd-408b-b38e-6a6e1ed5d818",
              "User":"root",
              "Create":1514373133000,
              "StartTime":"2017-12-26 22:34:45",
              "Pid":"1",
              "EuidName":"root",
              "Cmdline":"/sbin/init",
              "Name":"init",
              "Md5":"70023aaf3f480d198d3b078d8c39****"
          }
      ],
      "TotalCount":1,
      "PageSize":20,
      "RequestId":"AB20A6D4-43EB-44E2-AD64-E03EAC1C14D9",
      "CurrentPage":1,
      "Count":1
  }
        
  ```

<a id="section-4-3-22"></a>

### 4.3.22. DescribePropertyProcDiff

Description

You can call this operation to query process changes of a server.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set this parameter to <em>DescribePropertyProcDiff</em>. |
| PageSize | Integer | No | The number of records to return on each page.<br>Default value: <em>20</em>. |
| CurrentPage | Integer | No | The number of the page to return.<br>Default value: <em>1</em>. |
| DiffStatus | String | No | The type of the process change. Valid values:<br>• <em>start</em>: indicates that the process is started.<br>• <em>stop</em>: indicates that the process is stopped. |
| Ip | String | No | The IP address of the server. |
| Name | String | No | The name of the process. |
| User | String | No | The user who started the process. |
| Mark | String | No | The IP address or instance name of the server.<br>Note Fuzzy match is supported. |
| Uuid | String | No | The universally unique identifier (UUID) of the server. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| TotalCount | Integer | The number of returned records. |
| CurrentPage | Integer | The number of the current page returned. |
| PageSize | Integer | The number of records returned on each page. |
| PropertyProcDiffs | Array | The server process changes. For more information, see the following descriptions. |
| Cmdline | String | The process parameter. |
| Create | String | The time when the information was reported. |
| DiffKeyList | String | The names of the fields that have been changed. |
| DiffStatus | String | The type of the process change. |
| EuidName | String | The permissions that the process has to access resources and files. |
| InstanceName | String | The instance name of the server. |
| Ip | String | The IP address of the server. |
| Md5 | String | The MD5 value of the executable file. |
| Name | String | The name of the process. |
| Path | String | The path of the process. |
| Pid | String | The ID of the process. |
| Pname | String | The name of the parent process. |
| StartTime | String | The time when the process was started. |
| Uuid | String | The UUID of the server. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample request

  ```text
  https://aegis.[ RegionId].example.com/?Action=DescribePropertyProcDiff
  &Uuid=inet-00f20b1a-e2dd-408b-b38e-6a6e1ed5d818
  &<Common request parameters>
        
  ```

- Sample response (JSON format)

  ```json
  {
      "TotalCount":1,
      "PageSize":20,
      "RequestId":"D0951162-E933-4E2B-BDE2-B8FD806CEF9F",
      "CurrentPage":1,
      "PropertyProcDiffs":[
          {
              "Pname":"N/A",
              "Ip":"x.x.x.x",
              "StartTime":"2017-12-26 22:34:45",
              "Pid":"1",
              "DiffKeyList":"startTime,path,user,pid,pname,md5,uid,cmdline,euidName",
              "DiffStatus":"start",
              "Name":"init",
              "InstanceName":"****",
              "Uuid":"inet-00f20b1a-e2dd-408b-b38e-6a6e1ed5d818",
              "Create":1514366744000,
              "Cmdline":"/sbin/init",
              "Euidname":"root",
              "Md5":"70023aaf3f480d198d3b078d8c39****"
          },
      ]
  }
        
  ```

<a id="section-4-3-23"></a>

### 4.3.23. DescribePropertySoftwareItem

Description

You can call this operation to query servers that have been installed with the specified application.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>DescribePropertySoftwareItem</em>. |
| PageSize | Integer | No | The maximum number of records displayed on a page.<br>Default value: <em>20</em>. |
| CurrentPage | Integer | No | The current page number.<br>Default value: <em>1</em>. |
| Name | String | No | The name of the application. |
| Path | String | No | The application installation path. |
| SoftwareVersion | String | No | The version of the application. |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| TotalCount | Integer | The number of returned records. |
| Count | Integer | The number of records on the current page. |
| CurrentPage | Integer | The current page number. |
| PageSize | Integer | The maximum number of records displayed on a page. |
| PropertySoftwareItems | Array | A list of servers that have been installed with the application. For more information, see the following parameter descriptions. |
| Count | Integer | The number of servers that have been installed with the application. |
| Name | String | The name of the application. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=DescribePropertySoftwareItem
  &Name=spice-vdagent
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
   "TotalCount":1,
   "PropertySoftwareItems":[
    {
     "count":2,
     "Name":"spice-vdagent"
    }
   ],
   "PageSize":20,
   "RequestId":"0F2A3DEA-A5B3-4C2A-8BFC-4724A205E28B",
   "CurrentPage":1,
   "count": 1,
  }
  ```

<a id="section-4-3-24"></a>

### 4.3.24. DescribePropertySoftwareDetail

Description

You can call this operation to query the details of software installed on a server.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set this parameter to <em>DescribePropertySoftwareDetail</em>. |
| PageSize | Integer | No | The number of records to return on each page.<br>Default value: <em>20</em>. |
| CurrentPage | Integer | No | The number of the page to return.<br>Default value: <em>1</em>. |
| Ip | String | No | The IP address of the server. |
| Name | String | No | The name of the software. |
| Extend | String | No | Indicates whether fuzzy match is enabled to search for software names..Valid values:<br>• <em>1</em>: indicates that fuzzy match is enabled.<br>• <em>0</em>: indicates that fuzzy match is disabled. |
| Path | String | No | The installation path of the software. |
| Remark | String | No | The IP address or instance name of the server.<br>Note Fuzzy match is supported. |
| SoftwareVersion | String | No | The version of the software. |
| Uuid | String | No | The universally unique identifier (UUID) of the server. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| TotalCount | Integer | The number of returned records. |
| Count | Integer | The number of records returned on the current page. |
| CurrentPage | Integer | The number of the current page returned. |
| PageSize | Integer | The number of records returned on each page. |
| PropertySoftwares | Array | The details of software installed on the server. For more information, see the following descriptions. |
| Create | String | The time when the information was reported. |
| InstallTime | String | The time when the software was installed. |
| InstanceName | String | The instance name of the server. |
| Ip | String | The IP address of the server. |
| Path | String | The installation path of the software. |
| Version | String | The version of the software. |
| Uuid | String | The UUID of the server. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample request

  ```text
  https://aegis.[ RegionId].example.com/?Action=DescribePropertySoftwareDetail
  &Uuid=inet-00f20b1a-e2dd-408b-b38e-6a6e1ed5d818
  &<Common request parameters>
        
  ```

- Sample response (JSON format)

  ```json
  {
      "TotalCount":1,
      "PropertySoftwares":[
          {
              "InstanceName":"****",
              "Path":"/usr/libexec/gvfs-gphoto2-volume-monitor",
              "Uuid":"inet-00f20b1a-e2dd-408b-b38e-6a6e1ed5d818",
              "InstallTime":"2016-06-29 06:55:22",
              "Version":"1.4.3",
              "Create":1514172615000,
              "Ip":"x.x.x.x"
          }
      ],
      "PageSize":20,
      "RequestId":"31409246-AB88-4B36-A2B8-16D21BA9E170",
      "CurrentPage":1,
      "Count":1
  }
        
  ```

<a id="section-4-3-25"></a>

### 4.3.25. DescribePropertySoftwareDiff

Description

You can call this operation to query changes of applications that have been installed on servers.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>DescribePropertySoftwareDiff</em>. |
| PageSize | Integer | No | The maximum number of records displayed on a page.<br>Default value: <em>20</em>. |
| CurrentPage | Integer | No | The current page number.<br>Default value: <em>1</em>. |
| DiffStatus | String | No | The type of the application changes.Valid values:<br>• <em>create</em>: indicates an installation.<br>• <em>delete</em>: indicates an uninstallation.<br>• <em>modified</em>: indicates a modification. |
| Ip | String | No | The IP address of the server. |
| Name | String | No | The name of the application. |
| Path | String | No | The path where the application is installed. |
| SoftwareVersion | String | No | The version of the application. |
| Mark | String | No | The IP address or instance name of the server.<br>Note Fuzzy match is supported. |
| Uuid | String | No | The UUID of the server. |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| TotalCount | Integer | The number of returned records. |
| CurrentPage | Integer | The current page number. |
| PageSize | Integer | The maximum number of records displayed on a page. |
| PropertySoftwareDiffs | Array | The application changes. For more information, see the following parameter descriptions. |
| Create | String | The time when the application change was reported. |
| DiffKeyList | String | The name of the fields that have been changed. |
| DiffStatus | String | The type of the changes. |
| InstanceName | String | The instance name of the server. |
| Ip | String | The IP address of the server. |
| Name | String | The name of the application. |
| Path | String | The path where the application is installed. |
| Version | String | The version of the application. |
| Uuid | String | The UUID of the server. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=DescribePropertySoftwareDiff
  &Uuid=inet-f6ac9a93-0818-4052-90e2-d24f18ee198b
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
   "TotalCount":1398,
   "PageSize":2,
   "RequestId":"3A0814BA-1A5D-43DC-A6E9-3B52EDD3700E",
   "CurrentPage":1,
   "PropertySoftwareDiffs":[
    {
     "Path":"/etc/ghostscript",
     "Uuid":"inet-f6ac9a93-0818-4052-90e2-d24f18ee198b",
     "Version":"8.70",
     "Create":1514172428000,
     "DiffKeyList":"version,path",
     "DiffStatus":"create",
     "Name":"ghostscript"
    },
    {
     "Path":"/usr/sbin/brctl",
     "Uuid":"inet-f6ac9a93-0818-4052-90e2-d24f18ee198b",
     "Version":"1.2",
     "Create":1514172428000,
     "DiffKeyList":"version,path",
     "DiffStatus":"create",
     "Name":"bridge-utils"
    }
   ]
  }
  ```

<a id="section-4-3-26"></a>

### 4.3.26. DescribePropertyUserItem

Description

You can call this operation to query user account information.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>DescribePropertyUserItem</em>. |
| PageSize | Integer | No | The maximum number of records displayed on a page.<br>Default value: <em>20</em>. |
| CurrentPage | Integer | No | The current page number.<br>Default value: <em>1</em>. |
| User | String | No | The username of the account. |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| TotalCount | Integer | The number of returned records. |
| Count | Integer | The number of records on the current page. |
| CurrentPage | Integer | The current page number. |
| PageSize | Integer | The maximum number of records displayed on a page. |
| PropertyUserItems | Array | The returned user account information. For more information, see the following parameter descriptions. |
| Count | Integer | The number of servers under the account. |
| Name | String | The username of the account. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=DescribePropertyUserItem
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
   "TotalCount":2,
   "PropertyUserItems":[
    {
     "User":"abrt",
     "Count": 2
    },
    {
     "User":"adm",
     "Count": 2
    }
   ],
   "PageSize":20,
   "RequestId":"E80981C2-AD12-4C60-9976-6927C1FE449B",
   "CurrentPage":1,
   "Count": 2
  }
  ```

<a id="section-4-3-27"></a>

### 4.3.27. DescribePropertyUserDetail

Description

You can call this operation to query user account details.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set this parameter to <em>DescribePropertyUserDetail</em>. |
| PageSize | Integer | No | The number of records to return on each page.<br>Default value: <em>20</em>. |
| CurrentPage | Integer | No | The number of the page to return.<br>Default value: <em>1</em>. |
| GroupId | Long | No | The ID of the asset group. |
| Ip | String | No | The IP address of the server. |
| IsRoot | String | No | Indicates whether the user account is a root account. Valid values:<br>• <em>1</em>: indicates yes.<br>• <em>0</em>: indicates no. |
| User | String | No | The name of the user account. |
| Extend | String | No | Indicates whether fuzzy match is enabled to search for user accounts.Valid values:<br>• <em>1</em>: indicates that fuzzy match is enabled.<br>• <em>0</em>: indicates that fuzzy match is disabled. |
| Mark | String | No | The IP address or instance name of the server.<br>Note Fuzzy match is supported. |
| TagIdListString | String | No | The server tag ID. |
| Uuid | String | No | The universally unique identifier (UUID) of the server. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| TotalCount | Integer | The number of returned records. |
| Count | Integer | The number of records returned on the current page. |
| CurrentPage | Integer | The number of the current page returned. |
| PageSize | Integer | The number of records returned on each page. |
| PropertyUsers | Array | The details of the user account. For more information, see the following descriptions. |
| AccountsExpirationDate | String | The time when the user account expires. |
| Create | String | The time when the information was reported. |
| GroupName | String | The information about the user group. |
| InstanceName | String | The instance name of the server. |
| Ip | String | The IP address of the server. |
| IsRoot | String | Indicates whether the user account is a root account. |
| LastLoginIp | String | The last IP address that is used by the user account to log on to the server. |
| LastLoginTime | String | The last logon time of the user account. |
| PasswordExpirationDate | String | The time when the password of the user account expires. |
| User | String | The name of the user account. |
| Uuid | String | The UUID of the server. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample request

  ```text
  https://aegis.[ RegionId].example.com/?Action=DescribePropertyUserDetail
  &Uuid=inet-00f20b1a-e2dd-408b-b38e-6a6e1ed5d818
  &<Common request parameters>
        
  ```

- Sample response (JSON format)

  ```json
  {
      "TotalCount":66,
      "PageSize":2,
      "RequestId":"2EEAE2A6-1662-471C-A5E5-8A6190B01AFF",
      "CurrentPage":1,
      "Count":1,
      "PropertyUsers":[
          {
              "GroupName":[
                  "root"
              ],
              "InstanceName":"****",
              "IsRoot":"1",
              "LastLoginTime":"2017-12-27 10:22:25",
              "Uuid":"inet-00f20b1a-e2dd-408b-b38e-6a6e1ed5d818",
              "User":"root",
              "LastLoginIp":"192.168.x.x",
              "Create":1514373155000,
              "Ip":"x.x.x.x",
              "AccountsExpirationDate":"never",
              "PasswordExpirationDate":"never"
          }
      ]
  }
        
  ```

<a id="section-4-3-28"></a>

### 4.3.28. DescribePropertyUserDiff

Description

You can call this operation to query user account changes.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set this parameter to <em>DescribePropertyUserDiff</em>. |
| PageSize | Integer | No | The number of records to return on each page.<br>Default value: <em>20</em>. |
| CurrentPage | Integer | No | The number of the page to return.<br>Default value: <em>1</em>. |
| DiffStatus | String | No | The type of the user account change.Valid values:<br>• <em>create</em>: indicates that a new account has been added.<br>• <em>delete</em>: indicates that an account has been deleted.<br>• <em>modified</em>: indicates that an account has been modified. |
| IsRoot | String | No | Indicates whether the user account is a root account. Valid values:<br>• <em>1</em>: indicates yes.<br>• <em>0</em>: indicates no. |
| User | String | No | The name of the user account. |
| Mark | String | No | The IP address or instance name of the server.<br>Note Fuzzy match is supported. |
| Uuid | String | No | The universally unique identifier (UUID) of the server. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| TotalCount | Integer | The number of returned records. |
| CurrentPage | Integer | The number of the current page returned. |
| PageSize | Integer | The number of records returned on each page. |
| PropertyUserDiffs | Array | The user account changes. For more information, see the following descriptions. |
| AccountsExpirationDate | String | The time when the user account expires. |
| Create | String | The time when the information was reported. |
| DiffKeyList | String | The names of the fields that have been changed. |
| DiffStatus | String | The type of the user account change. |
| GroupName | String | The information about the user group. |
| InstanceName | String | The instance name of the server. |
| Ip | String | The IP address of the server. |
| IsRoot | String | Indicates whether the user account is a root account. |
| PasswordExpirationDate | String | The time when the password of the user account expires. |
| User | String | The name of the user account. |
| Uuid | String | The UUID of the server. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample request

  ```text
  https://aegis.[ RegionId].example.com/?Action=DescribePropertyUserDiff
  &Uuid=inet-00f20b1a-e2dd-408b-b38e-6a6e1ed5d818
  &<Common request parameters>
  ```

- Sample response (JSON format)

  ```json
  {
      "TotalCount":1,
      "PageSize":20,
      "RequestId":"20903EB6-E695-44A4-85C2-B9DFE4376F1F",
      "CurrentPage":1,
      "PropertyUserDiffs":[
          {
              "GroupName":[
                  "root"
              ],
              "InstanceName":"****",
              "IsRoot":"0",
              "User":"****",
              "Uuid":"inet-00f20b1a-e2dd-408b-b38e-6a6e1ed5d818",
              "Create":1514020942000,
              "Ip":"x.x.x.x",
              "AccountsExpirationDate":"never",
              "DiffKeyList":"isRoot,groupName,accountsExpirationDate,passwordExpirationDate
  ",
              "DiffStatus":"create",
              "PasswordExpirationDate":"never"
          }
      ]
  }
        
  ```

<a id="section-4-3-29"></a>

### 4.3.29. PushAllTask

Description

You can call this operation to perform a quick security check on specified servers.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set this parameter to <em>PushAllTask</em>. |
| Uuids | String | No | The universally unique identifier (UUID) of the server. Separate multiple UUIDs with commas (,). |
| Tasks | String | No | The type of the security check task. Valid values:<br>• <em>OVAL_ENTITY</em>: indicates all security check tasks.<br>• <em>CMS</em>: indicates a check for CMS vulnerabilities.<br>• <em>SYSVUL</em>: indicates a check for system software vulnerabilities.<br>• <em>HEALTH_CHECK</em>: indicates a baseline check.<br>• <em>WEBSHELL</em>: indicates a check for webshells.<br>• <em>PROC_SNAPSHOT</em>: indicates a check on process data.<br>• <em>PORT_SNAPSHOT</em>: indicates a check on port data.<br>• <em>ACCOUNT_SNAPSHOT</em>: indicates a check on account data.<br>• <em>SOFTWARE_SNAPSHOT</em>: indicates a check on application data. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| PushTaskRsp | Struct | The task delivery result. For more information, see the following descriptions. |
| PushTaskResultList | Array | The tasks that fail to be delivered. For more information, see the following descriptions. |
| GroupId | String | The ID of the asset group. |
| InstanceId | String | The instance ID of the server. |
| InstanceName | String | The instance name of the server. |
| Ip | String | The IP address of the server. |
| Message | String | The details of the task delivery result. |
| Online | String | Indicates whether the Server Guard client is online. |
| OsVersion | String | The version of the operating system. |
| Region | String | The region where the server resides. |
| Success | String | The task delivery result. |
| Uuid | String | The UUID of the server. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample request

  ```text
  https://aegis.[ RegionId].example.com/?Action=PushAllTask
  &Tasks=OVAL_ENTITY
  &Uuids=inet-00f20b1a-e2dd-408b-b38e-6a6e1ed5****
  &<Common request parameters>
        
  ```

- Sample response (JSON format)

  ```json
  {
      "RequestId":"8A773295-DB9C-423D-979E-C0E8B9F88FEA",
      "PushTaskRsp":{
          "PushTaskResultList":[
              {
                  "InstanceName":"****",
                  "Uuid":"inet-00f20b1a-e2dd-408b-b38e-6a6e1ed5****",
                  "Message":"{\"code\":\"clinent_offline\",\"message\":\"The client is offline\",\"success\":false}",
                  "InstanceId":"i-25l6r****",
                  "Ip":"x.x.x.x",
                  "OsVersion":"linux",
                  "Region":"cn-****-a01",
                  "Online":false,
                  "Success":false,
                  "GroupId":336
              }
          ]
      }
  }
        
  ```

<a id="section-4-3-30"></a>

### 4.3.30. DescribeTopRiskyAssets

Description

You can call this operation to query top N vulnerable servers.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set this parameter to <em>DescribeTopRiskyAssets</em>. |
| PageSize | Integer | No | The number of records to return, that is, the top N vulnerable servers. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| TotalCount | Integer | The number of returned records. |
| TopRiskyAssets | Array | The top N vulnerable servers. For more information, see the following descriptions. |
| HcCount | String | The number of at-risk items detected in the baseline check. |
| Ip | String | The IP address of the server. |
| Uuid | String | The universally unique identifier (UUID) of the server. |
| VulCount | String | The number of detected vulnerabilities. |
| WarningCount | String | The number of detected security events. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample request

  ```text
  https://aegis.[ RegionId].example.com/?Action=DescribeTopRiskyAssets
  &PageSize=1
  &<Common request parameters>
        
  ```

- Sample response (JSON format)

  ```json
  {
      "TotalCount": 1,
      "RequestId": "5D8D4058-2EE3-4599-9951-BDAA3340AD4D",
      "TopRiskyAssets": [
          {
              "Ip": "192.168.x.x",
              "Uuid": "inet-dsljaoe-jjdsklaj****",
              "VulCount": 2,
              "HcCount": 1,
              "WarningCount": 2
          }
      ]
  }
        
  ```

<a id="section-4-3-31"></a>

### 4.3.31. UnbindAegis

Description

You can call this operation to disable Server Guard for a specified server.

Note

After this operation, Server Guard is not able to detect any security events on this

server.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>UnbindAegis</em>. |
| Uuids | String | Yes | The UUID of the server. Separate multiple UUIDs with commas (,). |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=UnbindAegis
  &Uuids=6dbdbfe7-06fa-4d9a-8268-ce2dc6d673ac,6dbdbfe7-06fa-4d9a-8268-ce2dc6d673ac
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
   "RequestId":"8BFB5273-6582-446A-9E0B-BAC0A1A468EA"
  }
  ```

<a id="section-4-3-32"></a>

### 4.3.32. UninstallAegis

Description

You can call this operation to uninstall the Server Guard client from a specified server.

Note

After the client is uninstalled, Server Guard is not able to detect the security events on

this server.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>UninstallAegis</em>. |
| Uuids | String | Yes | The UUID of the server. Separate multiple UUIDs with commas (,). |
| Reason | String | No | The reason for uninstalling the client. |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=UninstallAegis
  &Reason=Suspend the feature
  &Uuids=6dbdbfe7-06fa-4d9a-8268-ce2dc6d673ac,6dbdbfe7-06fa-4d9a-8268-ce2dc6d673ac
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
   "RequestId":"8BFB5273-6582-446A-9E0B-BAC0A1A468EA"
  }
  ```

<a id="section-4-4"></a>

## 4.4. Vulnerability management

<a id="section-4-4-1"></a>

### 4.4.1. DescribeTarget

Description

You can call this operation to query the servers that are checked for the specified type of risks in vulnerability management.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>DescribeTarget</em>. |
| Type | String | No | The type of the risks. For example, <em>vul</em> represents vulnerabilities. |
| Config | String | No | The type of the vulnerabilities in JSON format. For example, {"vulType":"cve"} represents Linux software vulnerabilities. |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| TotalCount | Integer | The number of returned records. |
| Targets | Array | A list of servers that are checked for the specified type of risks. For more information, see the following parameter descriptions. |
| TargetType | String | Valid values:<br>• <em>groupId</em>: indicates the ID of an asset group.<br>• <em>uuid</em>: indicates the UUID of a server. |
| Target | String | The asset group ID or server UUID. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=DescribeTarget
  &Config={"vulType":"cve"}
  &Type=vul
  &<Common request parameters>
        
  ```

- Sample responses (JSON format)

  ```json
  {
      "TotalCount":2,
      "RequestId":"1FF54D56-47ED-47FB-B4DB-2BDF3857D526",
      "Targets":[
          {
              "Target":"inet-00f20b1a-e2dd-408b-b38e-6a6e1ed5d818",
              "TargetType":"uuid"
          },
          {
              "Target":"336",
              "TargetType":"groupId"
          }
      ]
  }
        
  ```

<a id="section-4-4-2"></a>

### 4.4.2. ModifyVulTarget

Description

You can call this operation to modify the servers for detecting a specified type of vulnerability in the vulnerability management settings.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>ModifyVulTarget</em>. |
| Config | String | No | The vulnerability type information, in JSON format. For example, <code> {"vulType":"cve"} </code> indicates Linux software vulnerabilities. |
| Target | String | No | The specified server, in JSON format. For more information, see the sample request. |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=ModifyVulTarget
  &Config={"vulType":"cve"}
  &Target={"target":"inet-00f20b1a-e2dd-408b-b38e-6a6e1ed5d818","targetType":"uuid","flag":
  "add"}
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
   "RequestId":"1FF54D56-47ED-47FB-B4DB-2BDF3857D526"
  }
  ```

<a id="section-4-4-3"></a>

### 4.4.3. DescribeVulTargetStatistics

Description

You can call this operation to query the information about target hosts for which vulnerability detection is enabled in the vulnerability management configuration.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>DescribeVulTargetStatistics</em>. |
| Type | String | No | The vulnerability type. |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| CurrentPage | Integer | The current page number. |
| PageSize | Integer | The maximum number of records displayed on a page. |
| TotalCount | Integer | The total number of returned records. |
| TargetStats | Array | The list of target hosts for which vulnerability detection is enabled. For more information, see the following parameter descriptions. |
| VulType | String | The vulnerability type. |
| Targets | Array | The information about target hosts. For more information, see the following parameter descriptions. |
| Flag | String | Indicates whether vulnerability detection is enabled. |
| TargetType | String | The type of the Target parameter value. Valid values:<br>• <em>groupId</em>: indicates an asset group ID.<br>• <em>uuid</em>: indicates a host asset UUID. |
| Target | String | The asset group ID or host asset UUID. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=DescribeVulTargetStatistics
  &Type=cve
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
   "TotalCount":1,
   "TargetStats":[
    {
     "VulType":"cve","Targets":[]
    },
   "PageSize":10,
   "RequestId":"89DD84B4-B592-476C-A6C0-51D56B3E8EAC",
   "CurrentPage":1
  }
  ```

<a id="section-4-4-4"></a>

### 4.4.4. DescribeTargetConfig

Description

You can call this operation to query the vulnerability scanning configuration information of a specified server.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>DescribeTargetConfig</em>. |
| Type | String | No | The type of the vulnerability. |
| Uuid | String | No | The UUID of the server. |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| TotalCount | Integer | The total number of the returned records. |
| TargetConfigs | Array | The list of vulnerability scanning configuration information. For more information, see the following parameter descriptions. |
| Type | String | The type of the vulnerability. |
| Config | String | Whether vulnerability scanning is enabled. Valid values: on and off. |
| OverAllConfig | String | Whether global vulnerability scanning is enabled.Valid values: on and off.<br>Note The global vulnerability scanning configuration overrides the vulnerability scanning configuration for a single server. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=DescribeTargetConfig
  &Type=cve
  &Uuid=inet-00f20b1a-e2dd-408b-b38e-6a6e1ed5d818
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
   "TotalCount":1,
   "RequestId":"092094BF-910F-4CE6-BE93-C3989B607977",
   "TargetConfigs":[
    {
     "Config":"off",
     "Type":"cve",
     "OverAllConfig":"off"
    }
   ]
  }
  ```

<a id="section-4-4-5"></a>

### 4.4.5. ModifyTargetConfig

Description

You can call this operation to modify the vulnerability scanning configuration for a specified server.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>ModifyTargetConfig</em>. |
| Type | String | No | The type of the vulnerability. |
| Uuid | String | No | The UUID of the server. |
| Config | String | No | The vulnerability scanning configuration.Valid values:<br>• <em>on</em>: indicates enabled.<br>• <em>off</em>: indicates disabled. |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=ModifyTargetConfig
  &Config=on
  &Type=cms
  &Uuid=46ef7c05-0c53-486c-b446-ef6ff972551c
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
   "RequestId":"092094BF-910F-4CE6-BE93-C3989B607977"
  }
  ```

<a id="section-4-4-6"></a>

### 4.4.6. DescribeVulConfig

Description

You can call this operation to query the global scanning configuration for each vulnerability type.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>DescribeVulConfig</em>. |
| Type | String | No | The type of the vulnerability. |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| TotalCount | Integer | The total number of returned records. |
| TargetConfigs | Array | The list of global vulnerability scanning configurations. For more information, see the following parameter descriptions. |
| Type | String | The type of the vulnerability. |
| Config | String | The global scanning configuration for the vulnerability type. Valid values: on and off. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=DescribeVulConfig
  &Type=cve
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
   "TotalCount":1,
   "RequestId":"A8E09216-31DF-45B6-A76B-E3F053752C07",
   "TargetConfigs":[
    {
     "Config":"off",
     "Type":"cve"
    }
  }
  ```

<a id="section-4-4-7"></a>

### 4.4.7. ModifyVulConfig

Description

You can call this operation to modify the global vulnerability scanning configuration.

Note

The global vulnerability scanning configuration overrides the vulnerability scanning

configuration for a single server.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>ModifyVulConfig</em>. |
| Type | String | No | The type of the vulnerability. |
| Config | String | No | The vulnerability scanning configuration.Valid values:<br>• <em>on</em>: indicates enabled.<br>• <em>off</em>: indicates disabled. |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=ModifyVulConfig
  &Config=on
  &Type=cms
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
   "RequestId":"A8E09216-31DF-45B6-A76B-E3F053752C07"
  }
  ```

<a id="section-4-4-8"></a>

### 4.4.8. DescribeAutoDelConfig

Description

You can call this operation to query the number of days that an invalid vulnerability is kept for before it is automatically deleted in the vulnerability management settings.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>DescribeAutoDelConfig</em>. |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| Days | Integer | The number of days that an invalid vulnerability is kept for. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=DescribeAutoDelConfig
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
   "RequestId":"E3785090-CFF4-4C53-82E4-08F902586053",
   "Days":7
  }
  ```

<a id="section-4-4-9"></a>

### 4.4.9. ModifyAutoDelConfig

Description

You can call this operation to modify the number of days that an invalid vulnerability is kept for before it is automatically deleted in the vulnerability management settings.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>ModifyAutoDelConfig</em>. |
| Days | Integer | No | The number of days that an invalid vulnerability is kept for. |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=ModifyAutoDelConfig
  &Days=7
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
   "RequestId":"E3785090-CFF4-4C53-82E4-08F902586053"
  }
  ```

<a id="section-4-4-10"></a>

### 4.4.10. DescribeVulLevel

Description Description

You can call this operation to query the vulnerability severities that require attention.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>DescribeVulLevel</em>. |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| ConcernLevels | List | The list of vulnerability severities that require attention. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=DescribeVulLevel
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
   "RequestId":"7935CB7A-D1B7-4EE6-93D0-FF3D040CF19B",
   "ConcernLevels":["high","medium"]
  }
  ```

<a id="section-4-4-11"></a>

### 4.4.11. ModifyVulLevel

Description

You can call this operation to change the vulnerability severities that require attention.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>ModifyVulLevel</em>. |
| ConcernLevels | String | No | The vulnerability severities that require attention. Separate multiple severities with commas (,). |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=ModifyVulLevel
  &ConcernLevel=high,medium
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
   "RequestId":"7935CB7A-D1B7-4EE6-93D0-FF3D040CF19B"
  }
  ```

<a id="section-4-4-12"></a>

### 4.4.12. CreateVulWhitelist

Description

You can call this operation to add a specified vulnerability to the whitelist. Server Guard does not report the vulnerabilities on the whitelist.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>CreateVulWhitelist</em>. |
| Reason | String | No | The reason for adding the vulnerability to the whitelist. |
| Whitelist | String | No | The vulnerability to be whitelisted, in JSON format. For more information, see the sample request. |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=CreateVulWhitelist
  &Reason=The vulnerability is not harmful.
  &Whitelist=[{"name":"oval:com.redhat.rhsa:def:20173263","type":"cve","aliasName":"RHSA-2017:3263: curl security update"}]
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
   "RequestId":"E3785090-CFF4-4C53-82E4-08F902586053"
  }
  ```

<a id="section-4-4-13"></a>

### 4.4.13. DescribeVulWhitelist

Description

You can call this operation to obtain the whitelist of vulnerabilities.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>DescribeVulWhitelist</em>. |
| PageSize | Integer | No | The maximum number of records to be displayed on each page of the query output.<br>Default value: <em>20</em>. |
| CurrentPage | Integer | No | The current page number.<br>Default value: <em>1</em>. |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| CurrentPage | Integer | The current page number. |
| PageSize | Integer | The maximum number of records displayed on a page. |
| TotalCount | Integer | The total number of returned records. |
| VulWhitelists | Array | The vulnerability whitelist. For more information, see the following parameter descriptions. |
| AliasName | String | The alias of the vulnerability. |
| Name | String | The name of the vulnerability. |
| Reason | String | The reason for adding the vulnerability to the whitelist. |
| Type | String | The vulnerability type. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=DescribeVulWhitelist
  &CurrentPage=1
  &PageSize=20
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
   "TotalCount":1,
   "VulWhitelists":[
    {
     "Name":"oval:com.redhat.rhsa:def:20173263",
     "AliasName":"RHSA-2017:3263: curl security update",
     "Type":"cve",
     "Reason":"Not fixed at present"
    }
   ],
   "PageSize":3,
   "RequestId":"74F97EF7-B543-43FD-A4E9-18456731F9C5",
   "CurrentPage":1
  }
  ```

<a id="section-4-4-14"></a>

### 4.4.14. DeleteVulWhitelist

Description

You can call this operation to delete a specified vulnerability from the vulnerability whitelist. After this operation, Server Guard re-detects and reports the vulnerability.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set this parameter to <em>DeleteVulWhitelist</em>. |
| Whitelist | String | No | The vulnerability to be deleted from the whitelist, in JSON format. For more information, see the sample request. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample request

  ```text
  https://aegis.[ RegionId].example.com/?Action=DeleteVulWhitelist
  &Whitelist=[{"name":"oval:com.redhat.rhsa:def:20173263","type":"cve","aliasName":"RHSA-2017:3263: curl security update"}]
  &<Common request parameters>
  ```

- Sample response (JSON format)

  ```json
  {
   "RequestId":"E3785090-CFF4-4C53-82E4-08F902586053"
  }
  ```

<a id="section-4-4-15"></a>

### 4.4.15. DescribeGroupedVul

Description

You can call this operation to query information about the specified vulnerability group. The vulnerability management feature can display detected vulnerability records by group. A vulnerability group contains all servers with a specific vulnerability detected by Server Guard.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>DescribeGroupedVul</em>. |
| PageSize | Integer | No | The maximum number of records to be displayed on each page of the query output.<br>Default value: <em>20</em>. |
| CurrentPage | Integer | No | The current page number.<br>Default value: <em>1</em>. |
| Dealed | String | No | Indicates whether the vulnerability has been handled. Valid values:<br>• <em>Y</em>: indicates that the vulnerability has been handled.<br>• <em>N</em>: indicates that the vulnerability has not been handled. |
| Direction | String | No | The sorting mode of vulnerabilities in the vulnerability group. Valid values:<br>• <em>asc</em>: indicates sorting in ascending order.<br>• <em>desc</em>: indicates sorting in descending order. |
| LastTsEnd | Long | No | The end time of the last detection of the vulnerability. |
| LastTsStart | Long | No | The start time of the last detection of the vulnerability. |
| Level | String | No | The severity of the vulnerability. Valid values:<br>• <em>serious</em>: critical<br>• <em>high</em>: important<br>• <em>medium</em>: moderate<br>• <em>low</em>: low |
| Name | String | No | The name of the vulnerability. |
| Necessity | String | No | The necessity for fixing the vulnerability.Valid values:<br>• <em>asap</em>: indicates that the vulnerability must be fixed as soon as possible.<br>• <em>later</em>: indicates that the vulnerability can be fixed later.<br>• <em>nntf</em>: indicates that the vulnerability can be ignored. |
| OrderBy | String | No | The field based on which the vulnerabilities in the vulnerability group are sorted. You can specify other request parameters for sorting order. |
| PatchId | Long | No | The ID of the patch used to fix the vulnerability. |
| Product | String | No | The product where the vulnerability exists. |
| StatusList | String | No | The status of the vulnerability. Valid values:<br>• <em>1</em>: indicates that the vulnerability has not been fixed.<br>• <em>2</em>: indicates that the vulnerability fix failed.<br>• <em>3</em>: indicates that the server has failed to be rolled back to the version before the vulnerability fix.<br>• <em>4</em>: indicates that the vulnerability is being fixed.<br>• <em>5</em>: indicates that the server is being rolled back to the version before the vulnerability fix.<br>• <em>6</em>: indicates that the vulnerability fix is being verified.<br>• <em>7</em>: indicates that the vulnerability has been fixed successfully.<br>• <em>8</em>: indicates that the vulnerability has been fixed successfully, and that the server is waiting for restart.<br>• <em>9</em>: indicates that the server has been rolled back to the version before the vulnerability fix.<br>• <em>10</em>: indicates that the vulnerability has been ignored.<br>• <em>11</em>: indicates that the server has been rolled back to the version before the vulnerability fix, and that the server is waiting for restart.<br>• <em>12</em>: indicates that the vulnerability does not exist.<br>• <em>20</em>: indicates that the vulnerability is invalid.<br>Note The statuses are specified in a single parameter, separated with commas (,). |
| Type | String | No | The type of the vulnerability. |
| Uuids | String | No | The UUID of the server. Separate multiple UUIDs with commas (,). |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| CurrentPage | Integer | The current page number. |
| PageSize | Integer | The maximum number of records displayed on a page. |
| TotalCount | Integer | The total number of returned records. |
| GroupedVulItems | Array | The information about the vulnerability group. For more information, see the following parameter descriptions. |
| AliasName | String | The alias of the vulnerability. |
| AsapCount | Integer | The number of assets to be fixed as soon as possible. |
| Count | Integer | The total number of vulnerabilities. |
| GmtLast | Long | The last time when the vulnerability was detected. |
| HandledCount | Integer | The total number of vulnerabilities handled. |
| Level | String | The severity of the vulnerability. |
| Name | String | The name of the vulnerability. |
| PendingCount | Integer | The number of vulnerabilities that have not been handled. |
| Product | String | The product affected by the vulnerability. |
| Status | Integer | The status of the vulnerability. |
| TotalCount | Integer | The total number of vulnerabilities. |
| Type | String | The type of the vulnerability. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=DescribeGroupedVul
  &CurrentPage=1
  &Dealed=y
  &Direction=asc
  &LastTsEnd=1517414400000
  &LastTsStart=1517414500000
  &Level=high
  &Name=oval:com.redhat.rhsa:def:20170817
  &Necessity=asap
  &OrderBy=name
  &PageSize=20
  &PatchId=27001
  &Product=redhat
  &SourceIp=
  &StatusList=1,2
  &Type=cve
  &Uuids=46ef7c05-0c53-486c-b446-ef6ff972551c,b688bf9f-1fd9-42c8-bb34-28697f562dc5
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
   "GroupedVulItems":[
    {
     "Name":"oval:com.redhat.rhsa:def:20170817",
     "Status":7,
     "Count":0,
     "TotalCount":1,
     "PendingCount":0,
     "AliasName":"RHSA-2017:0817: kernel security, bug fix, and enhancement update",
     "AsapCount":0,
     "Type":"cve",
     "GmtLast":1513695612000,
     "Level":"high",
     "HandledCount":1
    },
   ],
   "TotalCount":1,
   "PageSize":10,
   "RequestId":"6FCF95BE-7A78-4AD8-811C-BF12FC34AC34",
   "CurrentPage":1
  }
  ```

<a id="section-4-4-16"></a>

### 4.4.16. DescribeVulList

Description

You can call this operation to obtain the vulnerability list of the specified host asset.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>DescribeVulList</em>. |
| PageSize | Integer | No | The maximum number of records to be displayed on each page of the query output.<br>Default value: <em>20</em>. |
| CurrentPage | Integer | No | The current page number.<br>Default value: <em>1</em>. |
| Dealed | String | No | Indicates whether the vulnerability has been handled. Valid values:<br>• <em>Y</em>: indicates that the vulnerability has been handled.<br>• <em>N</em>: indicates that the vulnerability has not been handled. |
| Level | String | No | The severity of the vulnerability. Valid values:<br>• <em>serious</em>: critical<br>• <em>high</em>: important<br>• <em>medium</em>: moderate<br>• <em>low</em>: low |
| Name | String | No | The name of the vulnerability. |
| Necessity | String | No | The necessity for fixing the vulnerability.Valid values:<br>• <em>asap</em>: indicates that the vulnerability must be fixed as soon as possible.<br>• <em>later</em>: indicates that the vulnerability can be fixed later.<br>• <em>nntf</em>: indicates that the vulnerability can be ignored. |
| Type | String | No | The type of the vulnerability. |
| StatusList | String | No | The status of the vulnerability. Valid values:<br>• <em>1</em>: indicates that the vulnerability has not been fixed.<br>• <em>2</em>: indicates that the vulnerability fix failed.<br>• <em>3</em>: indicates that the host has failed to be rolled back to the version before the vulnerability fix.<br>• <em>4</em>: indicates that the vulnerability is being fixed.<br>• <em>5</em>: indicates that the host is being rolled back to the version before the vulnerability fix.<br>• <em>6</em>: indicates that the vulnerability fix is being verified.<br>• <em>7</em>: indicates that the vulnerability has been fixed successfully.<br>• <em>8</em>: indicates that the vulnerability has been fixed successfully, and that the host is waiting for restart.<br>• <em>9</em>: indicates that the host has been rolled back to the version before the vulnerability fix.<br>• <em>10</em>: indicates that the vulnerability has been ignored.<br>• <em>11</em>: indicates that the host has been rolled back to the version before the vulnerability fix, and that the host is waiting for restart.<br>• <em>12</em>: indicates that the vulnerability does not exist.<br>• <em>20</em>: indicates that the vulnerability is invalid.<br>Note Note: The statuses are specified in a single parameter, separated with commas (,). |
| Uuids | String | No | The UUID of the host asset. Separate multiple host asset UUIDs with commas (,). |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| CurrentPage | Integer | The current page number. |
| PageSize | Integer | The maximum number of records displayed on a page. |
| TotalCount | Integer | The total number of records returned from the query. |
| VulRecords | Array | The list of vulnerabilities. For more information, see the following parameter descriptions. |
| AliasName | String | The alias of the vulnerability. |
| ExtendContent | String | The extended information of the vulnerability. |
| ExtendContentJson | String | The extended information of the vulnerability (JSON format). |
| FirstTs | Long | The first time when the vulnerability was detected. |
| ModifyTs | Long | The last time when the vulnerability was updated. |
| LastTs | Long | The last time when the vulnerability was detected. |
| Level | String | The severity of the vulnerability. |
| Name | String | The name of the vulnerability. |
| Necessity | String | The necessity for fixing the vulnerability. Valid values:<br>• <em>asap</em>: indicates that the vulnerability must be fixed as soon as possible.<br>• <em>later</em>: indicates that the vulnerability can be fixed later.<br>• <em>nntf</em>: indicates that the vulnerability can be ignored. |
| PrimaryId | Long | The ID of the primary key. |
| Product | String | The product affected by the vulnerability. |
| RecordId | Long | The ID of the vulnerability record. |
| Related | String | The CVE ID of the vulnerability. |
| RepairTs | Long | The time when the vulnerability was fixed. |
| ResultCode | String | The code of the vulnerability handling result. |
| ResultMessage | String | The message of the vulnerability handling result. |
| RiskDesc | String | The risk description of the vulnerability. |
| RiskLevel | Integer | The risk level of the vulnerability. |
| Status | Integer | The status of the vulnerability. Valid values:<br>• <em>1</em>: indicates that the vulnerability is to be handled.<br>• <em>2</em>: indicates that the vulnerability has been ignored.<br>• <em>3</em>: indicates that the vulnerability has been confirmed.<br>• <em>8</em>: indicates that the vulnerability has been marked as a false positive.<br>• <em>16</em>: indicates that the vulnerability is being handled.<br>• <em>32</em>: indicates that the vulnerability has been handled. |
| Tag | String | The tag of the vulnerability. |
| Type | String | The type of the vulnerability. |
| Uuid | String | The UUID of the host asset. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=DescribeVulList
  &CurrentPage=1
  &Dealed=n
  &Level=serious
  &Name=RHSA-2017:1100: nss and nss-util security update
  &Necessity=asap
  &PageSize=20
  &StatusList=1
  &Type=cve
  &Uuids=f293ade2-e5b1-4cc0-99a6-cc993a4158cc
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
   "TotalCount":1,
   "PageSize":20,
   "RequestId":"2E35F7F7-DA6D-46A5-BA9D-8751BDAE7710",
   "CurrentPage":1,
   "VulRecords":[
    {
     "Uuid":"b688bf9f-1fd9-42c8-bb34-28697f562dc5",
     "Necessity":"nntf",
     "ModifyTs":1512949391000,
     "Type":"cve",
     "FirstTs":1499321694000,
     "Related":"CVE-2016-1248",
     "ExtendContentJson":{"Necessity":{"Cvss_factor":"6.8","Total_score":"6.799999965526585
  ","Status":"normal","Enviroment_factor":"1.0","Time_factor":"0.9999999949303802","Assets_factor":"1","Gmt_create":"20171210","Is_calc":"1"},"Os":"centos","cveList":["CVE-2016-1248"],"RpmEntityList":[{"Name":"vim-minimal","Version":"7.4.160","FullVersion":"7.4.160-1.el7","MatchDetail":"vim-minimal version less than 2:7.4.160-1.el7_3.1","UpdateCmd":"yum update vim-minimal","Path":"/etc/virc"}],"OsRelease":"7"},
     "Name":"oval:com.redhat.rhsa:def:20162972",
     "Status":1,
     "LastTs":1512949391000,
     "AliasName":"RHSA-2016:2972: vim security update (Moderate)",
     "Tag":"oval",
     "PrimaryId":281156,
     "Level":"high"
    }
   ]
  }
  ```

<a id="section-4-4-17"></a>

### 4.4.17. DescribeVulDetails

Description

You can call this operation to query detailed information about a vulnerability.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>DescribeVulDetails</em>. |
| Type | Integer | Yes | The type of the vulnerability. |
| Name | String | Yes | The name of the vulnerability. |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| Cves | Array | The vulnerability details. For more information, see the following parameter descriptions. |
| Classify | String | The vulnerability type code. |
| Classifys | Array | The detailed vulnerability information. For more information, see the following parameter descriptions. |
| Classify | String | The vulnerability type code. |
| Description | String | The description of the vulnerability type. |
| DemoVideoUrl | String | The URL of the vulnerability video demo. |
| CnvdId | String | The CNVD ID. |
| Complexity | String | The complexity. |
| Content | String | The vulnerability details. |
| ExtendContentJson | String | The additional information about the vulnerability (JSON format). |
| CveId | String | The CVE ID. |
| CvssScore | String | The CVSS score. |
| CvssVector | String | The CVSS score string. |
| OtherId | String | The ID of the vulnerability. |
| Poc | String | The proof of concept (POC) method. |
| PocCreateTime | Long | The time when the POC method was created. |
| PocDisclosureTime | Long | The time when the POC method was revealed. |
| Service | String | The products that are affected by the vulnerability. |
| Reference | String | The corresponding reference. |
| ReleaseTime | Long | The time when the vulnerability was revealed. |
| Solution | String | The solution for fixing the vulnerability. |
| Summary | String | The vulnerability summary. |
| Title | String | The title of the vulnerability. |
| Vendor | String | The vendors that are affected by the vulnerability. |
| VulLevel | String | The severity level of the vulnerability. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=DescribeVulDetails
  &Name=oval:com.redhat.rhsa:def:20170036
  &Type=cve
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
   "Cves": [{
    "CvssVector": "CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H",
    "OtherId": "CVE-2016-7117",
    "Classifys": [],
    "Vendor": "Linux",
    "CvssScore": "10.0",
    "CnvdId": "CNVD-2016-09362",
    "Reference": "http://www.securityfocus.com/bid/93304",
    "Solution": "<p>The vendor has released a patch to fix this vulnerability. Download thepatch from: \n<br  />https://bugzilla.redhat.com/show_bug.cgi?id=1382268</p>\n",
    "CveId": "CVE-2016-7117",
    "ReleaseTime": 1476028800000,
    "VulLevel": "serious",
    "Title": "The use-after-free vulnerability in __sys_recvmmsg function in the Linux kernel",
    "Summary": "The Linux kernel is released by the Linux Foundation of the United States for Linux operating systems. The use-after-free vulnerability is found in the net/socket.cfile in \n\nLinux kernel 4.5.2 and earlier versions. It allows remote attackers to execute arbitrary code."
   }],
   "RequestId": "70DEE6B7-A167-4B5D-ADAA-3631443D5190"
  }
  ```

<a id="section-4-4-18"></a>

### 4.4.18. DescribeVulNumStatistics

Description

You can call this operation to query vulnerability statistics.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>DescribeVulNumStatistics</em>. |
| StartTs | Long | No | The start time for statistics collection. |
| EndTs | Long | No | The end time for statistics collection. |
| Uuids | String | No | The UUID of the server. Separate multiple UUIDs with commas (,). |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| CmsDealedTotalNum | Integer | The number of CMS vulnerabilities handled. |
| CmsNum | Integer | The number of CMS vulnerabilities. |
| CveNum | Integer | The number of CVE vulnerabilities. |
| EmgNum | Integer | The number of other vulnerabilities. |
| SysNum | Integer | The number of Windows OS vulnerabilities. |
| VulAsapSum | Integer | The number of vulnerabilities that need to be handled as soon as possible. |
| VulDealedTotalNum | Integer | The total number of vulnerabilities handled. |
| VulSeriousTotal | Integer | The total number of critical vulnerabilities. |
| VulHighTotal | Integer | The total number of important vulnerabilities. |
| VulMediumTotal | Integer | The total number of moderate vulnerabilities. |
| VulLowTotal | Integer | The total number of low vulnerabilities. |
| VulLaterSum | Integer | The number of vulnerabilities that can be handled later. |
| VulNntfSum | Integer | The number of vulnerabilities that do not need to be fixed temporarily. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=DescribeVulNumStatistics
  &EndTs=1514736000000
  &StartTs=1514736000000
  &Uuids=46ef7c05-0c53-486c-b446-ef6ff972551c
  &<Common request parameters>
        
  ```

- Sample responses (JSON format)

  ```json
  {
      "VulHighTotal":0,
      "CveNum":1,
      "VulMediumTotal":0,
      "EmgNum":0,
      "VulLowTotal":0,
      "VulNntfSum":1,
      "VulAsapSum":0,
      "SysNum":0,
      "VulDealedTotalNum":1,
      "RequestId":"093C121C-2981-4E69-8309-CD1BDD8C872A",
      "CmsNum":0,
      "VulSeriousTotal":0,
      "CmsDealedTotalNum":0,
      "VulLaterSum":0
  }
        
  ```

<a id="section-4-4-19"></a>

### 4.4.19. DescribeVulLevelStatistics

Description

You can call this operation to obtain the statistics on vulnerabilities by vulnerability severity.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>DescribeVulLevelStatistics</em>. |
| StartTs | Long | No | The start time of the time frame specified for query. |
| EndTs | Long | No | The end time of the time frame specified for query. |
| Uuids | String | No | The UUID of the server. Separate multiple UUIDs with commas (,). |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| TotalCount | Integer | The total number of returned records. |
| LevelStatistics | Array | The vulnerability statistics. For more information, see the following parameter descriptions. |
| CmsDealedTotalNum | Integer | The number of handled CMS vulnerabilities. |
| CmsNum | Integer | The number of CMS vulnerabilities. |
| CveNum | Integer | The number of CVE vulnerabilities. |
| EmgNum | Integer | The number of other vulnerabilities. |
| Level | String | The severity of the vulnerability. |
| SysNum | Integer | The number of Windows vulnerabilities. |
| VulAsapSum | Integer | The number of high-priority vulnerabilities. |
| VulDealedTotalNum | Integer | The total number of handled vulnerabilities. |
| VulSeriousTotal | Integer | The total number of critical-risk vulnerabilities. |
| VulHighTotal | Integer | The total number of important-risk vulnerabilities. |
| VulMediumTotal | Integer | The total number of moderate-risk vulnerabilities. |
| VulLowTotal | Integer | The total number of low-risk vulnerabilities. |
| VulLaterSum | Integer | The number of medium-priority vulnerabilities. |
| VulNntfSum | Integer | The number of low-priority vulnerabilities. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=DescribeVulLevelStatistics
  &EndTs=1514736000000
  &StartTs=1514736000000
  &Uuids=46ef7c05-0c53-486c-b446-ef6ff972551c,b688bf9f-1fd9-42c8-bb34-28697f562dc5
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
   "TotalCount":0,
   "LevelStatistics":[
    {
     "VulHighTotal":0,
     "CveNum":0,
     "VulMediumTotal":0,
     "EmgNum":0,
     "VulLowTotal":0,
     "VulNntfSum":0,
     "VulAsapSum":0,
     "SysNum":0,
     "VulDealedTotalNum":0,
     "CmsNum":0,
     "Level":"high",
     "VulSeriousTotal":0,
     "CmsDealedTotalNum":0,
     "VulLaterSum":0
    },
    {
     "VulHighTotal":0,
     "CveNum":0,
     "VulMediumTotal":0,
     "EmgNum":0,
     "VulLowTotal":0,
     "VulNntfSum":0,
     "VulAsapSum":0,
     "SysNum":0,
     "VulDealedTotalNum":0,
     "CmsNum":0,
     "Level":"low",
     "VulSeriousTotal":0,
     "CmsDealedTotalNum":0,
     "VulLaterSum":0
    }
   ],
   "RequestId":"9B062D3F-AD5A-4D3E-9A7A-45CAC2713FC0"
  }
  ```

<a id="section-4-4-20"></a>

### 4.4.20. DescribeVulMachineList

Description

You can call this operation to query the vulnerability statistics of a specified server.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>DescribeVulMachineList</em>. |
| StartTs | Long | No | The start time of the time frame during which the statistics were collected. |
| EndTs | Long | No | The end time of the time frame during which the statistics were collected. |
| Uuids | String | No | The UUID of the server. Separate multiple UUIDs with commas (,). |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| TotalCount | Integer | The total number of the returned records. |
| MachineStatistics | Array | The vulnerability statistics. For more information, see the following parameter descriptions. |
| CmsDealedTotalNum | Integer | The number of CMS vulnerabilities that have been handled. |
| CmsNum | Integer | The number of CMS vulnerabilities. |
| CveNum | Integer | The number of CVE vulnerabilities. |
| EmgNum | Integer | The number of other vulnerabilities. |
| SysNum | Integer | The number of Windows vulnerabilities. |
| VulAsapSum | Integer | The number of high-priority vulnerabilities. |
| VulDealedTotalNum | Integer | The total number of vulnerabilities that have been handled. |
| VulSeriousTotal | Integer | The total number of critical-risk vulnerabilities. |
| VulHighTotal | Integer | The total number of important-risk vulnerabilities. |
| VulMediumTotal | Integer | The total number of moderate-risk vulnerabilities. |
| VulLowTotal | Integer | The total number of low-risk vulnerabilities. |
| VulLaterSum | Integer | The number of medium-priority vulnerabilities. |
| VulNntfSum | Integer | The number of low-priority vulnerabilities. |
| Uuid | String | The UUID of the server. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=DescribeVulMachineList
  &EndTs=1514736000000
  &StartTs=1514736000000
  &Uuids=46ef7c05-0c53-486c-b446-ef6ff972551c
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
   "TotalCount":0,
   "MachineStatistics":[
    {
     "Uuid":"577f9886-bf66-4c3c-88ac-28c938cb527b",
     "VulHighTotal":0,
     "CveNum":1,
     "VulMediumTotal":0,
     "EmgNum":0,
     "VulLowTotal":0,
     "VulNntfSum":0,
     "VulAsapSum":0,
     "SysNum":0,
     "VulDealedTotalNum":0,
     "CmsNum":0,
     "VulSeriousTotal":0,
     "CmsDealedTotalNum":0,
     "VulLaterSum":0
    }
   ],
   "RequestId":"A3F8BE63-9BA1-450D-BB5D-CE9205E6645D"
  }
  ```

<a id="section-4-4-21"></a>

### 4.4.21. OperateVul

Description

You can call this operation to handle detected vulnerabilities.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>OperateVul</em>. |
| Info | String | No | The vulnerability information, in JSON format. For more information, see the sample request. |
| OperateType | String | No | The type of the operation. Valid values:<br>• <em>vul_fix</em>: indicates an operation to fix the vulnerability.<br>• <em>vul_verify</em>: indicates an operation to verify the vulnerability fix.<br>• <em>vul_rebooted</em>: indicates an operation to verify the vulnerability fix after the server is restarted.<br>• <em>vul_rollback</em>: indicates an operation to undo the vulnerability fix.<br>• <em>vul_ignore</em>: indicates an operation to ignore the vulnerability.<br>• <em>vul_undo_ignore</em>: indicates an operation to unignore the vulnerability.<br>• <em>vul_delete</em>: indicates an operation to delete the vulnerability record. |
| Reason | String | No | The reason why the vulnerability is ignored if the OperateType parameter is set to vul_ignore. |
| Type | String | No | The type of the vulnerability. |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=OperateVul
  &Info=[{"name":"oval:com.redhat.rhsa:def:20171100","uuid":"e49fb179-bbe7-4b6c-ab65-e106fb58d235","tag":"oval"}]
  &OperateType=vul_ignore
  &Reason=Postpone the fix
  &Type=cve
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
   "RequestId":"A3F8BE63-9BA1-450D-BB5D-CE9205E6645D"
  }
  ```

<a id="section-4-4-22"></a>

### 4.4.22. ModifyBatchIgnoreVul

Description

You can call this operation to ignore multiple vulnerabilities.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>ModifyBatchIgnoreVul</em>. |
| Info | String | No | The vulnerabilities to be ignored, in JSON format. For more information, see the sample request. |
| Reason | String | No | The reason for ignoring the vulnerabilities. |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=ModifyBatchIgnoreVul
  &Info=[{"name":"oval:com.redhat.rhsa:def:20162972","type":"cve","aliasName":"RHSA-2016:2972: vim security update (Moderate)"}]
  &Reason=Postpone handling
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
   "RequestId":"E3785090-CFF4-4C53-82E4-08F902586053"
  }
  ```

<a id="section-4-4-23"></a>

### 4.4.23. DeleteVulBatch

Description

You can call this operation to delete a specified batch of vulnerabilities.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>DeleteVulBatch</em>. |
| BatchName | String | No | The name of the vulnerability batch. |
| Resource | String | No | The scenario of the vulnerability batch. |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=DeleteVulBatch
  &BatchName=Vulnerabilities managed by network security team
  &Resource=vulnerability
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
   "RequestId":"E3785090-CFF4-4C53-82E4-08F902586053"
  }
  ```

<a id="section-4-4-24"></a>

### 4.4.24. ExportVul

Description

You can call this operation to export vulnerability records that match the specified criteria.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>ExportVul</em>. |
| AliasName | String | No | The alias of the vulnerability. |
| BatchName | String | No | The name of the vulnerability fix batch. |
| Dealed | String | No | Indicates whether the vulnerability has been handled. Valid values:<br>• <em>Y</em>: indicates that the vulnerability has been handled.<br>• <em>N</em>: indicates that the vulnerability has not been handled. |
| Level | String | No | The severity of the vulnerability. |
| Name | String | No | The name of the vulnerability. |
| Necessity | String | No | The priority of the vulnerability. Valid values:<br>• <em>asap</em>: indicates that the vulnerability must be fixed as soon as possible.<br>• <em>later</em>: indicates that the vulnerability can be fixed later.<br>• <em>nntf</em>: indicates that the vulnerability can be ignored. |
| Resource | String | No | The source of the vulnerability fixing batch. |
| StatusList | String | No | The status of the vulnerability. Valid values:<br>• <em>1</em>: indicates that the vulnerability is pending.<br>• <em>2</em>: indicates that the vulnerability has been ignored.<br>• <em>3</em>: indicates that the vulnerability has been confirmed.<br>• <em>8</em>: indicates that the vulnerability has been marked as a false positive.<br>• <em>16</em>: indicates that the vulnerability is being handled.<br>• <em>32</em>: indicates that the vulnerability has been handled.You can specify multiple statuses and separate them with commas (,). |
| Type | String | No | The type of the vulnerability. |
| Uuids | String | No | The UUID of the server. Separate multiple UUIDs with commas (,). |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| CurrentCount | Integer | The number of records that have been exported. |
| ExportStatus | String | The status of the export task. Valid values:<br>• <em>init</em>: indicates that the export task is being initialized.<br>• <em>pending</em>: indicates that the export task is pending for summarization.<br>• <em>exporting</em>: indicates that the export task is being executed.<br>• <em>success</em>: indicates that the export task has been completed.<br>• <em>fail</em>: indicates that the export task has failed. |
| Message | String | The status description or failure information of the export task. |
| FileName | String | The name of the exported file. |
| Id | Integer | The ID of the export task. |
| Link | String | The download link of the exported file. |
| Progress | Integer | The export progress. |
| TotalCount | Integer | The total number of records that have been exported. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=ExportVul
  for example, RHSA-2016:2972: vim security update (Moderate), and trigger another vulnerability scan.
  &BatchName=Security group test
  &Dealed=y
  &Level=low
  &Name=oval:com.redhat.rhsa:def:20162972
  &Necessity=later
  &Resource=vulnerability
  &StatusList=1
  &Type=cve
  &Uuids=46ef7c05-0c53-486c-b446-ef6ff972551c
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
   "FileName":"cve_20180303",
   "RequestId":"3B3C79B1-617E-4081-903B-86EA4AC0213F",
   "Id":36
  }
  ```

<a id="section-4-4-25"></a>

### 4.4.25. DescribeVulExportInfo

Description

You can call this operation to query a vulnerability record export task.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set this parameter to <em>DescribeVulExportInfo</em>. |
| ExportId | Long | No | The ID of the vulnerability record export task. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| CurrentCount | Integer | The number of records that have been exported. |
| ExportStatus | String | The status of the export task. Valid values:<br>• <em>init</em>: indicates that the export task is being initialized.<br>• <em>pending</em>: indicates that the export task is pending.<br>• <em>exporting</em>: indicates that the export task is being executed.<br>• <em>success</em>: indicates that the export task has been completed.<br>• <em>fail</em>: indicates that the export task has failed. |
| Message | String | The status description or failure information of the export task. |
| FileName | String | The name of the exported file. |
| Id | Integer | The ID of the export task. |
| Link | String | The download link of the exported file. |
| Progress | Integer | The export progress. |
| TotalCount | Integer | The total number of records that have been exported. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample request

  ```text
  https://aegis.[ RegionId].example.com/?Action=DescribeVulExportInfo
  &ExportId=10
  &<Common request parameters>
  ```

- Sample response (JSON format)

  ```json
  {
   "Status":"success",
   "Link":"http://jiangzhi.oss-cn-shanghai.example.com/export/sys_20171124_1511510709277.zip?Expires=1511514309&OSSAccessKeyId=<yourAccessKeyId>&Signature=xxxx%xxxx%3D",
   "TotalCount":2,
   "Message":"success",
   "FileName":"sys_20171124",
   "RequestId":"9C689776-0F8B-4290-8C11-D9242A86C75B",
   "CurrentCount":1,
   "Id":17,
   "Progress":100
  }
  ```

<a id="section-4-5"></a>

## 4.5. Baseline check

<a id="section-4-5-1"></a>

### 4.5.1. DescribeStrategy

Description

You can call this operation to obtain a list of baseline check policies.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>DescribeStrategy</em>. |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| Count | Integer | The total number of the returned records. |
| Strategies | Array | The list of baseline check policies. For more information, see the following parameter descriptions. |
| CycleDays | Integer | The cycle of policy execution. |
| CycleStartTime | Integer | The start time of policy execution. Valid values:<br>• <em>0</em>: indicates the period from 00:00 to 06:00.<br>• <em>6</em>: indicates the period from 06:00 to 12:00.<br>• <em>12</em>: indicates the period from 12:00 to 18:00.<br>• <em>18</em>: indicates the period from 18:00 to 24:00. |
| EcsCount | Integer | The number of hosts using the policy. |
| Id | Integer | The ID of the policy. |
| Name | String | The name of the policy. |
| RiskCount | Integer | The number of at-risk items contained in the policy. |
| Type | Integer | The policy type. Valid values:<br>• <em>1</em>: indicates a system default policy.<br>• <em>2</em>: indicates a custom policy. |
| ConfigTargets | Array | The information about asset groups using the policy. For more information, see the following parameter descriptions. |
| Flag | String | A flag that indicates whether the policy applies to the specified asset group. Valid values:<br>• <em>add</em>: indicates the whitelist mode, that is, the policy applies to the asset group.<br>• <em>del</em>: indicates the blacklist mode, that is, the policy does not apply to the asset group.<br>Note Generally, the blacklist mode is used for system default policies, and the whitelist mode is used for custom policies. |
| TargetType | String | The return value is fixed to groupId, which indicates that the value of the Target parameter is an asset group ID. |
| Target | String | The ID of the asset group. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=DescribeStrategy
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
      "Count": 2,
      "RequestId": "4F914046-4358-4BA9-BE42-83AA1FD1FF52",
      "Strategies": [
          {
              "Name": "test",
              "RiskCount": 2,
              "CycleDays": 3,
              "Type": 2,
              "CycleStartTime": 6,
              "ConfigTargets": [
                  {
                      "Target": "4361221",
                      "Flag": "add",
                      "TargetType": "groupId"
                  }
              ],
              "Id": 15161,
              "EcsCount": 0
          },
          {
              "Name": "Default policy",
              "RiskCount": 14,
              "CycleDays": 1,
              "Type": 1,
              "CycleStartTime": 0,
              "ConfigTargets": [
                  {
                      "Target": "none",
                      "Flag": "del",
                      "TargetType": "flag_item"
                  }
              ],
              "Id": 20,
              "EcsCount": 48
          }
      ]
  }
  ```

<a id="section-4-5-2"></a>

### 4.5.2. DescribeStratetyDetail

Description

You can call this operation to query the details of a specified baseline check policy.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>DescribeStratetyDetail</em>. |
| Id | String | No | The ID of the baseline check policy. |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| Strategy | Array | The details of the baseline check policy. For more information, see the following parameter descriptions. |
| CycleDays | Integer | The cycle of policy execution. |
| CycleStartTime | Integer | The start time of policy execution. Valid values:<br>• <em>0</em>: indicates the period from 00:00 to 06:00.<br>• <em>6</em>: indicates the period from 06:00 to 12:00.<br>• <em>12</em>: indicates the period from 12:00 to 18:00.<br>• <em>18</em>: indicates the period from 18:00 to 24:00. |
| Id | Integer | The ID of the policy. |
| Name | String | The name of the policy. |
| Type | Integer | The type of the policy. Valid values:<br>• <em>1</em>: indicates a system default policy.<br>• <em>2</em>: indicates a custom policy. |
| RiskTypeWhiteListQuery ResultList | Array | The risk information contained in the policy. For more information, see the following parameter descriptions. |
| Alias | String | The name of the risk category. |
| On | Boolean | Indicates whether to check for risks of the specified category. |
| TypeName | String | The code of the risk category. |
| SubTypes | Array | The list of risk subcategories. For more information, see the following parameter descriptions. |
| Alias | String | The name of the risk subcategory. |
| TypeName | String | The code of the risk subcategory. |
| On | Boolean | Indicates whether to check for risks of the specified subcategory. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=DescribeStratetyDetail
  &Id=1
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
       "RequestId": "99F17C4B-2E23-4B41-BBEB-C03963B06EB4",
       "Strategy": {
    "Name": "Yunwu testing",
               "CycleDays": 1,
               "CycleStartTime": 18,
               "Type": 2,
               "Id": 12,
               "RiskTypeWhiteListQueryResultList": [
                   {
                       "On": false,
                       "Alias": "Compliance with Security Standards",
                       "TypeName": "cis",
                       "SubTypes": [
                            {
                                "On": true,
                                "Alias": "Memcached",
                                "TypeName": "memcached-check"
                            },
                            {
                                "On": true,
                                "Alias": "CentOS 7",
                                "TypeName": "centos7"
                            },
                            {
                                "On": false,
                                "Alias": "Tomcat 7",
                                "TypeName": "tomcat7"
                            },
                            {
                                "On": false,
                                "Alias": "MongoDB",
                                "TypeName": "mongodb-check"
                            }
                       ]
                   }
    ]
   }
  }
  ```

<a id="section-4-5-3"></a>

### 4.5.3. ModifyStrategy

Description

You can call this operation to modify the basic information of a baseline check policy.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>ModifyStrategy</em>. |
| CycleDays | String | No | The baseline check cycle. |
| CycleStartTime | String | No | The time when the baseline check starts.Valid values:<br>• <em>0</em>: starts at 00:00 and ends at 06:00.<br>• <em>6</em>: starts at 06:00 and ends at 12:00.<br>• <em>12</em>: starts at 12:00 and ends at 18:00.<br>• <em>18</em>: starts at 18:00 and ends at 24:00. |
| Id | String | No | The ID of the baseline check policy.<br>Note If this parameter is set to null, a baseline check policy is added. |
| Name | String | No | The name of the baseline check policy. |
| RiskSubTypeName | String | No | The sub-risk types in the baseline check policy. Separate multiple sub-risk types with commas (,). |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| Result | Struct | The returned information. For more information, see the following parameter descriptions. |
| StrategyId | Integer | The ID of the baseline check policy. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=ModifyStrategy
  &CycleDays=1
  &CycleStartTime=8
  &Id=52
  &Name=Web server
  &RiskSubTypeName=redis_check,linux_password
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
   "RequestId":"161F1BEE-5268-4935-9763-C39A2F7F65DD",
   "Result":2
    "StrategyId":52
   }
  }
  ```

<a id="section-4-5-4"></a>

### 4.5.4. DeleteStrategy

Description

You can call this operation to delete a specified baseline check policy.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>DeleteStrategy</em>. |
| Id | String | No | The ID of the baseline check policy. |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=DeleteStrategy
  &Id=123456
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
      "RequestId": "43F670F3-AB40-4E91-BC7D-C57468834F67"
  }
  ```

<a id="section-4-5-5"></a>

### 4.5.5. DescribeStrategyTarget

Description

You can call this operation to query the information about asset groups to which a specified baseline check policy applies.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>DescribeStrategyTarget</em>. |
| Config | String | No | The policy configuration information.The baseline check policy ID is specified in JSON format, for example, <code> {"strategyId":15161} </code>. |
| Type | String | No | The configuration type.<br>Set the value to <em>hc_strategy</em>. |
| Target | String | No | The ID of the asset group to which the baseline check policy applies. |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| Count | Integer | The total number of returned records. |
| StrategyTargets | Array | The information about asset groups to which the policy applies. For more information, see the following parameter descriptions. |
| Flag | String | Indicates whether the policy applies to the specified asset group. Valid values:<br>• <em>add</em>: indicates the whitelist mode, that is, the policy applies to the asset group.<br>• <em>del</em>: indicates the blacklist mode, that is, the policy does not apply to the asset group.<br>Note Generally, the blacklist mode is used for system default policies, and the whitelist mode is used for custom policies. |
| TargetType | String | The return value is fixed to groupId, indicating that the value of the Target parameter is the ID of the asset group. |
| Target | String | The asset group ID. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=DescribeStrategyTarget
  &Config={"strategyId":15161}
  &Type=hc_strategy
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
          "Count": 1,
          "StrategyTargets":[
              {
                  "Flag": "del",
                  "Target": "281801",
                  "TargetType": "groupId"
              }
          ]
   "requestId": "B44F545D-15CF-4A57-B8BF-4340D15D0507"
  }
  ```

<a id="section-4-5-6"></a>

### 4.5.6. ModifyStrategyTarget

Description

You can call this operation to modify the information about the asset groups that a specified baseline check policy applies to.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>ModifyStrategyTarget</em>. |
| Config | String | No | The policy configuration information.The baseline check policy ID is specified in JSON format, for example, <code> {"strategyId":15161} </code>. |
| Type | String | No | The configuration type.<br>Set the value to <em>hc_strategy</em>. |
| Target | String | No | The information about asset groups that the baseline check policy applies to. For more information, see the sample request. |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=ModifyStrategyTarget
  &Type=hc_strategy
  &Config={"strategyId":36071}
  &Target=[{"targetType":"groupId","target":"1111","flag":"add"}]
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
   "RequestId": "B44F545D-15CF-4A57-B8BF-4340D15D0507"
  }
  ```

<a id="section-4-5-7"></a>

### 4.5.7. DescribeUuidConfig

Description

You can call this operation to check whether baseline check is enabled for a specified server.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>DescribeUuidConfig</em>. |
| Uuid | String | No | The UUID of the server. |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| Data | Struct | The baseline check configuration. For more information, see the following parameter descriptions. |
| Flag | String | Indicates whether baseline check is enabled. Valid values:<br>• <em>add</em>: indicates enabled.<br>• <em>del</em>: indicates disabled. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=DescribeUuidConfig
  &uuid=4bc19998-e100-4b04-ab11-1e677418d311
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
      "Data": {
          "Flag": "del"
      },
      "RequestId": "A89978FE-BC35-427E-A4B1-7AEEAE741CC2",
  }
  ```

<a id="section-4-5-8"></a>

### 4.5.8. ModifyMachineConfig

Description

You can call this operation to configure whether to apply a specified baseline check policy to a specified server.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>ModifyMachineConfig</em>. |
| Type | String | No | The configuration type.<br>Set the value to <em>hc_switch</em>, indicating the baseline check policy switch. |
| Target | String | No | The specified server, in JSON format. For more information, see the sample request. |
| Config | String | No | The policy configuration information.The baseline check policy ID is specified in JSON format, for example, <code> {"strategyId":15161} </code>. |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=ModifyMachineConfig
  &target={"targetType":"uuid","target":"2738e842-7d46-42f7-acb4-e6796b051ddc","ip":"x.x.x.x","flag":"del"}
  &type=hc_switch
  &config={"strategyId":15161}
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
      "RequestId": "A89978FE-BC35-427E-A4B1-7AEEAE741CC2",
  }
  ```

<a id="section-4-5-9"></a>

### 4.5.9. DescribeUserSetting

Description

You can call this operation to query the number of days an invalid risk is kept for before it is automatically deleted in baseline check.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>DescribeUserSetting</em>. |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| InvalidWarningKeepDays | Integer | The number of days that an invalid risk is kept for. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=DescribeUserSetting
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
   "InvalidWarningKeepDays":90,
   "RequestId":"0A079FE2-0D1B-4A4D-A4EF-D02B5DDE12A7"
  }
  ```

<a id="section-4-5-10"></a>

### 4.5.10. CreateUserSetting

Description

You can call this operation to specify the number of days an invalid risk is kept for before it is automatically deleted in baseline check.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>CreateUserSetting</em>. |
| InvalidWarningKee pDays | Integer | No | The number of days an invalid risk is kept for. Valid values:<br>• <em>7</em>: indicates that the invalid risk item is to be deleted in seven days.<br>• <em>30</em>: indicates that the invalid risk item is to be deleted in 30 days.<br>• <em>90</em>: indicates that the invalid risk item is to be deleted in 90 days. |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=CreateUserSetting
  &InvalidWarningKeepDays=90
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
      "RequestId": "43F670F3-AB40-4E91-BC7D-C57468834F67",
  }
  ```

<a id="section-4-5-11"></a>

### 4.5.11. DescribeRiskWhiteList

Description

You can call this operation to obtain the whitelist of risk items that are exempt from the baseline check.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>DescribeRiskWhiteList</em>. |
| PageSize | Integer | No | The maximum number of records to be displayed on each page of the query output.<br>Default value: <em>20</em>. |
| CurrentPage | Integer | No | The current page number.<br>Default value: <em>1</em>. |
| RiskName | String | No | The name of the risk item. This parameter supports fuzzy match. |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| TotalCount | Integer | The total number of returned records. |
| Count | Integer | The number of records on the current page. |
| CurrentPage | Integer | The current page number. |
| PageSize | Integer | The maximum number of records displayed on a page. |
| WhiteLists | Array | The risk item whitelist. For more information, see the following parameter descriptions. |
| Reason | String | The reason for adding the risk item to the whitelist. |
| RiskId | Long | The ID of the risk item. |
| RiskName | String | The name of the risk item. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=DescribeRiskWhiteList
  &RiskName=SSH logon baseline check
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
   "TotalCount":1,
   "PageSize":20,
   "RequestId":"B452E97A-7DFA-44FC-915D-5D590A702846",
   "CurrentPage":1,
   "WhiteLists":[
    {
     "RiskName":"SSH logon baseline check",
     "RiskId":1
    }
   ],
   "Count":1
  }
  ```

<a id="section-4-5-12"></a>

### 4.5.12. BatchDeleteWhiteList

Description

You can call this operation to delete multiple risks from the whitelist for baseline check.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>BatchDeleteWhiteList</em>. |
| RiskIdList | String | No | The ID of the risk to be deleted from the whitelist. Separate multiple IDs with commas (,). |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=BatchDeleteWhiteList
  &RiskIdList=1,2,3
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
   "RequestId":"E3785090-CFF4-4C53-82E4-08F902586053"
  }
  ```

<a id="section-4-5-13"></a>

### 4.5.13. CreateUserWhiteList

Description

You can call this operation to add a specified risk to the baseline check whitelist. After this operation, the risk is not reported during baseline check.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>CreateUserWhiteList</em>. |
| RiskIdList | String | No | The ID of the risk to be added to the whitelist. Separate multiple IDs with commas (,). |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=CreateUserWhiteList
  &RiskIdList=1,2,3
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
   "RequestId":"E3785090-CFF4-4C53-82E4-08F902586053"
  }
  ```

<a id="section-4-5-14"></a>

### 4.5.14. DescribeStratety

Description

You can call this operation to query the execution details of a specified baseline check policy.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>DescribeStratety</em>. |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| Strategies | Array | The list of baseline check policies. For more information, see the following parameter descriptions. |
| CycleDays | Integer | The execution cycle of the policy. |
| CycleStartTime | Integer | The start time of policy execution. |
| EcsCount | Integer | The number of hosts to which the policy applies. |
| ExecStatus | Integer | The current execution status of the policy. Valid values:<br>• <em>1</em>: indicates that the policy has been executed.<br>• <em>2</em>: indicates that the policy is being executed. |
| Id | Integer | The ID of the policy. |
| Name | String | The name of the policy. |
| ProcessRate | Integer | The progress of policy execution. Unit: percentage. |
| RiskCount | Integer | The number of risk items contained in the policy. |
| ConfigTargets | Array | The asset group to which the policy applies. For more information, see the following parameter descriptions. |
| Flag | String | Indicates whether the policy applies to the specified asset group. Valid values:<br>• <em>add</em>: indicates the whitelist mode, that is, the policy applies to the asset group.<br>• <em>del</em>: indicates the blacklist mode, that is, the policy does not apply to the asset group.<br>Note Generally, the blacklist mode is used for system default policies, and the whitelist mode is used for custom policies. |
| TargetType | String | The return value is fixed to groupId, indicating that the value of the Target parameter is the ID of the asset group. |
| Target | String | The asset group ID. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=DescribeStratety
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
          "requestId": "751BEDD8-A16F-49CE-A3C4-605849645D79",
      "Strategies": [
              {
                  "Name": "Threat Detection Service No. 12345",
                  "RiskCount": 4,
                  "CycleDays": 1,
                  "CycleStartTime": 6,
                  "Type": 2,
                  "ProcessRate": 0,
                  "ConfigTargets": [
                      {
                          "Flag": "add",
                          "Target": "5078483",
                          "TargetType": "groupId"
                      }
                  ],
                  "Id": 36071,
                  "ExecStatus": 1,
                  "EcsCount": 2
              }  
      ]
  }                    
  ```

<a id="section-4-5-15"></a>

### 4.5.15. DescribeStrategyExecDetail

Description

You can call this operation to query the execution details of a baseline check policy.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>DescribeStrategyExecDetail</em>. |
| StrategyId | Integer | No | The ID of the baseline check policy. |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| EndTime | String | The time when the baseline check was complete. |
| FailCount | Integer | The number of servers that failed to pass the check. |
| FailedEcsList | Array | A list of servers that failed to pass the check. For more information, see the following parameter descriptions. |
| Ip | String | The IP address of the server. |
| InstanceName | String | The instance name of the server. |
| IntranetIp | String | The private IP address of the server. |
| Reason | String | The reason that causes the baseline check failure. |
| InProcessCount | Integer | The number of servers that are being checked. |
| percent | String | The baseline check progress in percentage. |
| Source | String | The baseline check mode: automatic or manual. |
| StartTime | String | The time when the baseline check started. |
| SuccessCount | Integer | The number of servers that have passed the check. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=DescribeStrategyExecDetail
  &StrategyId=1
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
       "requestId": "751BEDD8-A16F-49CE-A3C4-605849645D79",
         "Source": "Schedule",
         "InProcessCount": 0,
         "SuccessCount": 1,
         "Percent": 100,
         "EndTime": "2018-04-08 12:15:20",
         "FailedEcsList": [],
         "StartTime": "2018-04-08 12:15:10",
         "FailCount": 0,
  }
  ```

<a id="section-4-5-16"></a>

### 4.5.16. DescribeRiskType

Description

You can call this operation to query all types of risks detected in baseline check and view the number of risks that have been detected by a baseline check policy or on the specified servers for a specific risk type.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>DescribeRiskType</em>. |
| StrategyId | Long | No | The ID of the baseline check policy. |
| Uuids | String | No | The UUID of the server. Multiple UUIDs are separated with commas (,). |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| Count | Integer | The number of risk types. |
| RiskTypes | Array | A list of risk types. For more information, see the following parameter descriptions. |
| Alias | String | The name of the risk type. |
| TypeName | String | The code of the risk type. |
| WarnCount | String | The number of risks that have been detected. |
| SubTypes | Array | A list of sub-risk types. For more information, see the following parameter descriptions. |
| Alias | String | The name of the sub-risk type. |
| TypeName | String | The code of the sub-risk type. |
| WarnCount | String | The number of risks that have been detected. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=DescribeRiskType
  &StrategyId=10
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
   "RequestId":"11D3993A-02B8-4FD9-9116-922BCDE53A80",
   "RiskTypes":[
    {
     "TypeName":"system",
     "SubTypes":[
      {
       "TypeName":"group_policy",
       "Alias":"Group policy",
       "WarnCount":0
      },
      {
       "TypeName":"baseline",
       "Alias":"Baseline policy",
       "WarnCount":0
      },
      {
       "TypeName":"register",
       "Alias":"Registry",
       "WarnCount":0
      }
     ],
     "Alias":"System",
     "WarnCount":0
    }
   ],
   "count": 1,
  }
  ```

<a id="section-4-5-17"></a>

### 4.5.17. Describesummary

Description

You can call this operation to query the risks detected in baseline check by risk type.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>Describesummary</em>. |
| PageSize | Integer | No | The number of records displayed on a page. Default value: <em>20</em>. |
| CurrentPage | Integer | No | The current page number.<br>Default value: <em>1</em>. |
| Dealed | String | No | Indicates whether the risk has been handled. Valid values:<br>• <em>Y</em>: indicates that the risk has been handled.<br>• <em>N</em>: indicates that the risk has not been handled. |
| RiskLevels | String | No | The risk level. Separate multiple risk levels with commas (,). |
| RiskName | String | No | The name of the risk.<br>Note Fuzzy match is supported. |
| StatusList | String | No | The status of the risk. Valid values:<br>• <em>1</em>: indicates that the risk is pending.<br>• <em>2</em>: indicates that the risk has been ignored.<br>• <em>3</em>: indicates that the risk has been confirmed.<br>• <em>8</em>: indicates that the risk has been marked as a false positive.<br>• <em>16</em>: indicates that the risk is being handled.<br>• <em>32</em>: indicates that the risk has been handled.You can specify multiple statuses and separate them with commas (,). |
| StrategyId | Long | No | The ID of the baseline check policy. |
| TypeNames | String | No | The type of the risk. Separate multiple risk types with commas (,). |
| SubTypeNames | String | No | The type of the sub-risk. Separate multiple sub-risk types with commas (,). |
| Uuids | String | No | The UUID of the server. Separate multiple UUIDs with commas (,). |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| TotalCount | Integer | The number of returned records. |
| Count | Integer | The number of returned risk records. |
| CurrentPage | Integer | The current page number. |
| PageSize | Integer | The maximum number of records displayed on a page. |
| WarningSummarys | Array | A list of risks. For more information, see the following parameter descriptions. |
| LastFoundTime | String | The latest time when the risk was detected. |
| Level | String | The risk level. |
| PendingCount | Integer | The number of pending risks. |
| RiskDetail | String | The risk details. |
| RiskId | Long | The ID of the risk. |
| RiskName | String | The name of the risk. |
| TypeAlias | String | The type of the risk. |
| SubTypeAlias | String | The type of the sub-risk. |
| TotalCount | Integer | The total number of risks. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=Describesummary
  &CurrentPage=20
  &Dealed=Y
  &PageSize=10
  &StrategyId=1
  &Uuid=2738e842-7d46-42f7-acb4-e6796b051ddc
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
   "TotalCount":1,
   "PageSize":20,
   "RequestId":"38AAFEEE-F52F-4B2E-9F28-FC4A35F8D432",
   "CurrentPage":1,
   "count": 1,
   "WarningSummarys":[
    {
     "RiskId":1,
     "LastFoundTime":"2018-04-08 16:51:26",
     "RiskDetail":"The SSH logon security policy checks the following configurations: \n1. 
  Checks whether the logon port is the default port 22\n2 and whether the root account is allowed\n3. Checks whether the SSH V1 protocol is used\n4. Checks whether the RSH protocolis used\n5. Checks whether authentication-based logon is performed\n Solution: \n Edit /etc/ssh/sshd_config\n1. Port (not 22)\n2. PermitRootLogin (no)\n3. Protocol (2)\n4. Ignore
  Rhosts (yes)\n5. e) HostbasedAuthentication (no)
     "Level":"low",
     "TypeAlias":"System",
     "SubTypeAlias":"Baseline check policy",
     "RiskName":"SSH logon baseline check"
    }
   ]
  }
  ```

<a id="section-4-5-18"></a>

### 4.5.18. OperateWarning

Description

You can call this operation to handle the risk alert records detected during the baseline check.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>OperateWarning</em>. |
| RiskWarningIds | String | No | The risk alert record ID. Separate multiple risk alert record IDs with commas (,). |
| OperateType | String | No | The type of the operation. Valid values:<br>• <em>verify</em>: indicates an operation to verify the risk alert.<br>• <em>ignore</em>: indicates an operation to ignore the risk alert.<br>• <em>cancelIgnore</em>: indicates an operation to cancel the ignore operation on the risk alert.<br>• <em>delete</em>: indicates an operation to delete the risk alert record. |
| Reason | String | No | The reason why the risk alert record is ignored if the OperateType parameter is set to ignore. |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=OperateWarning
  &OperateType=verify
  &RiskWarningIds=22,45
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
   "RequestId":"38AAFEEE-F52F-4B2E-9F28-FC4A35F8D432"
  }
  ```

<a id="section-4-5-19"></a>

### 4.5.19. ExportWarning

Description

You can call this operation to export risks that match the specified criteria from baseline check.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>ExportWarning</em>. |
| IsSummaryExport | String | No | Indicates whether to export the summary page. Valid values:<br>• <em>1</em>: exports the summary page.<br>• <em>0</em>: does not export the summary page. |
| Dealed | String | No | Indicates whether the risk has been handled. Valid values:<br>• <em>Y</em>: indicates that the risk has been handled.<br>• <em>N</em>: indicates that the risk has not been handled. |
| RiskLevels | String | No | The risk level. Multiple risk levels are separated with commas (,). |
| RiskName | String | No | The name of the risk.<br>Note Fuzzy match is supported. |
| StrategyId | Integer | No | The ID of the baseline check policy. |
| TypeNames | String | No | The risk type. |
| SubTypeNames | String | No | The sub-risk type. |
| Uuids | String | No | The UUID of the server. Multiple UUIDs are separated with commas (,). |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| FileName | String | The name of the exported file. |
| Id | Integer | The ID of the export task. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=ExportWarning
  &Dealed=n
  &RiskLevels=serious,high,medium,low
  &RiskName=Weak FTP password
  &StrategyId=15161
  &SubTypeNames=centos7
  &TypeNames=cis
  &Uuids=6dbdbfe7-06fa-4d9a-8268-ce2dc6d673ac
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
       "FileName": "health_check_export_20180306",
       "RequestId": "F2F08DED-C788-430F-91F2-11991818BE2D",
       "Id": 16719
  }
  ```

<a id="section-4-5-20"></a>

### 4.5.20. DescribeExportInfo

Description

You can call this operation to query the export task information, including the export progress and the download link of the exported file.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set this parameter to <em>DescribeExportInfo</em>. |
| ExportId | Long | No | The ID of the export task. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| CurrentCount | Integer | The number of records that have been exported. |
| FileName | String | The name of the exported file. |
| Id | Integer | The ID of the export task. |
| GmtCreate | Long | The time when the export task was created. |
| Link | String | The download link of the exported file. |
| Progress | Integer | The export progress. |
| TotalCount | Integer | The total number of records that have been exported. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample request

  ```text
  https://aegis.[ RegionId].example.com/?Action=DescribeExportInfo
  &ExportId=1
  &<Common request parameters>
  ```

- Sample response (JSON format)

  ```json
  {
      "Link": "http://hc-export.oss-cn-shanghai.example.com/export_hc/health_check_export_20180303_1520065303578.zip?Expires=1520670103&OSSAccessKeyId=<yourAccessKeyId>&Signature=xxxx%xxxx%3D",
      "TotalCount": 82,
      "FileName": "health_check_export_20180303",
      "RequestId": "00F89798-3370-4C20-8506-B2BC3970EC5A",
      "CurrentCount": 82,
      "Id": 16678,
      "GmtCreate": 1520065302000,
      "Progress": 100
  }
  ```

<a id="section-4-6"></a>

## 4.6. Unusual logon detection

<a id="section-4-6-1"></a>

### 4.6.1. DescribeBaseConfigs

Description

You can call this operation to query the logon security settings.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>DescribeBaseConfigs</em>. |
| Type | String | Yes | The type of the logon security configuration record. Valid values:<br>• <em>login_common_location</em>: indicates an approved logon location.<br>• <em>login_common_ip</em>: indicates an approved logon IP address.<br>• <em>login_common_time</em>: indicates an approved logon time period.<br>• <em>login_common_account</em>: indicates an approved logon account. |
| Target | String | No | The specified server.<br>Note You must specify this parameter to query the logon security settings of a specified server. For more information about the format, see the sample request. |
| PageSize | Integer | No | The maximum number of records to be displayed on each page.<br>Default value: <em>20</em>. |
| CurrentPage | Integer | No | The current page number.<br>Default value: <em>1</em>. |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| CurrentPage | Integer | The current page number. |
| PageSize | Integer | The maximum number of records displayed on a page. |
| TotalCount | Integer | The total number of the returned records. |
| BaseConfigs | Array | The logon security settings. For more information, see the following parameter descriptions. |
| Account | String | The approved logon account. |
| EndTime | String | The end time of the approved logon time period. |
| Ip | String | The approved logon IP address. |
| Location | String | The approved logon location. |
| StartTime | String | The start time of the approved logon time period. |
| TotalCount | Integer | The total number of servers. |
| UuidCount | Integer | The number of servers to which the specified configuration record applies. |
| TargetList | Array | The information about servers to which the specified configuration record applies. For more information, see the following parameter descriptions. |
| TargetType | String | The type of the Target parameter value. Valid values:<br>• <em>groupId</em>: indicates an asset group ID.<br>• <em>uuid</em>: indicates a server UUID. |
| Target | String | The asset group ID or server UUID. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=DescribeBaseConfigs
  &CurrentPage=1
  &PageSize=20
  &Target=[{"targetType":"uuid","target":"6dbdbfe7-06fa-4d9a-8268-ce2dc6d673ac"}]
  &Type=login_common_location
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
   "BaseConfigs": [{
    "totalCount": 9,
    "location": "United States",
    "uuidCount": 1,
    "targetList": [{
     "target": "6dbdbfe7-06fa-4d9a-8268-ce2dc6d673ac",
     "targetType": "uuid"
    }]
   }],
   "TotalCount": 1,
   "PageSize": 5,
   "RequestId": "485ABE58-4E27-4416-997C-F8F3B8748EB6",
   "CurrentPage": 1
  }
  ```

<a id="section-4-6-2"></a>

### 4.6.2. ModifyBaseConfig

Description

You can call this operation to modify logon security settings.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>ModifyBaseConfig</em>. |
| Type | String | Yes | The type of the logon security settings.Valid values:<br>• <em>login_common_location</em>: indicates approved logon locations.<br>• <em>login_common_ip</em>: indicates approved logon IP addresses.<br>• <em>login_common_time</em>: indicates approved logon time periods.<br>• <em>login_common_account</em>: indicates approved logon accounts. |
| Target | String | No | The target server.<br>Note You must set this parameter when you need to query the logon security settings for a server. For more information about the format, see the following sample request. |
| Config | String | No | The logon security settings. The formats for all the settings are as follows:<br>• Approved logon locations: <code> {"locat</code> <code>ion":"Ganzhou City"}</code><br>• Approved logon IP addresses: <code> {"ip"</code><code>:"x.x.x.x"}</code><br>• Approved logon time periods: <code> {"st</code> <code>artTime":"16:18","endTime":"16:1</code><br><code>8"}</code><br>• Approved logon accounts: <code> {"accou</code> <code>nt":"dbaadmin"}</code> |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=ModifyBaseConfig
  &Config={"startTime":"16:18","endTime":"16:18"}
  &Target=[{"targetType":"uuid","target":"0c797eb1-e6b9-4b5a-8917-a7e6cbbb4b2e","flag":"add
  "},{"targetType":"uuid","target":"1759b0ea-6dd7-438b-b60d-c90179bd9ebc","flag":"del"}]
  &Type=login_common_location
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
   "RequestId":"BB8F5902-BD50-49AB-B124-18E9CA92BB99"
  }
  ```

<a id="section-4-6-3"></a>

### 4.6.3. DeleteBaseConfig

Description

You can call this operation to delete a logon security setting, such as an approved logon location or IP address.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set this parameter to <em>DeleteBaseConfig</em>. |
| Config | String | Yes | The logon security setting. The formats of the logon security settings and examples are as follows:<br>• Approved logon location: <code> {"locati</code> <code>on":"Ganzhou City"}</code><br>• Approved logon IP address: <code> {"ip":</code> <code>" x.x.x.x"}</code><br>• Approved logon time range: <code> {"star</code> <code>tTime":"16:18","endTime":"16:18"</code><br><code>}</code><br>• Approved logon account: <code> {"accoun</code> <code>t":"dbaa****"}</code> |
| Type | String | Yes | The type of the logon security setting.Valid values:<br>• <em>login_common_location</em>: indicates an approved logon location.<br>• <em>login_common_ip</em>: indicates an approved logon IP address.<br>• <em>login_common_time</em>: indicates an approved logon time range.<br>• <em>login_common_account</em>: indicates an approved logon account. |
| Target | String | No | The target server.<br>Note You must set this parameter if you want to delete a logon security setting for a server.For more information about the format, see the following sample request. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample request

  ```text
  https://aegis.[ RegionId].example.com/?Action=DeleteBaseConfig
  &Config={"location":"Ganzhou City"}
  &Target=[{"targetType":"uuid","target":"6dbdbfe7-06fa-4d9a-8268-ce2dc6d673ac"}]
  &Type=login_common_location
  &<Common request parameters>
        
  ```

- Sample response (JSON format)

  ```json
  {
      "RequestId":"E3785090-CFF4-4C53-82E4-08F902586053"
  }
        
  ```

<a id="section-4-6-4"></a>

### 4.6.4. DescribeSwitchConfigs

Description

You can call this operation to query the logon security configuration records in the logon security settings.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>DescribeSwitchConfigs</em>. |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| Count | Integer | The total number of returned records. |
| ConfigList | Array | The statuses of the logon security configuration items. For more information, see the following parameter descriptions. |
| Item | String | The logon security configuration items. Valid values:<br>• <em>login_common_location</em>: indicates an approved logon location.<br>• <em>login_common_ip</em>: indicates an approved logon IP address.<br>• <em>login_common_time</em>: indicates an approved logon time range.<br>• <em>login_common_account</em>: indicates an approved logon account. |
| Status | Integer | The status of the configuration item. Valid values:<br>• <em>1</em>: indicates enabled.<br>• <em>0</em>: indicates disabled. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=DescribeSwitchConfigs
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
   "Count":3,
   "RequestId":"3F2C126D-870B-4AE4-8604-58BDECF873F4",
   "ConfigList":[
    {
     "Status":1,
     "Item":"login_common_ip"
    },
    {
     "Status":0,
     "Item":"login_common_account"
    },
    {
     "Status":0,"Item":"login_common_time"
    }
   ]
  }
  ```

<a id="section-4-6-5"></a>

### 4.6.5. ModifySwitchConfig

Description

You can call this operation to modify the setting about whether to enable a logon security configuration record to identify a valid logon to a server in the logon security settings.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>ModifySwitchConfig</em>. |
| Item | String | Yes | The logon security configuration items.Valid values:<br>• <em>login_common_location</em>: indicates an approved logon location.<br>• <em>login_common_ip</em>: indicates an approved logon IP address.<br>• <em>login_common_time</em>: indicates an approved logon time range.<br>• <em>login_common_account</em>: indicates an approved logon account. |
| Status | Integer | Yes | The status of the logon security configuration switch. Valid values:<br>• <em>1</em>: indicates enabled.<br>• <em>0</em>: indicates disabled. |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| Count | Integer | The total number of returned records. |
| ConfigList | Array | The status of the logon security configuration switch. For more information, see the following parameter descriptions. |
| Item | String | The logon security configuration items. Valid values:<br>• <em>login_common_location</em>: indicates an approved logon location.<br>• <em>login_common_ip</em>: indicates an approved logon IP address.<br>• <em>login_common_time</em>: indicates an approved logon time range.<br>• <em>login_common_account</em>: indicates an approved logon account. |
| Status | Integer | The status of the logon security configuration switch. Valid values:<br>• <em>1</em>: indicates enabled.<br>• <em>0</em>: indicates disabled. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=ModifySwitchConfig
  &Item=login_common_location
  &Status=1
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
   "RequestId":"3F2C126D-870B-4AE4-8604-58BDECF873F4"
  }
  ```

<a id="section-4-6-6"></a>

### 4.6.6. DescribeConfigTarget

Description

You can call this operation to query the information about servers to which a specified logon security configuration record applies.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>DescribeConfigTarget</em>. |
| Type | String | Yes | The logon security configuration record used to identify a valid logon to a server.Valid values:<br>• <em>login_common_location</em>: indicates an approved logon location.<br>• <em>login_common_ip</em>: indicates an approved logon IP address.<br>• <em>login_common_time</em>: indicates an approved logon time range.<br>• <em>login_common_account</em>: indicates an approved logon account. |
| Target | String | No | The specified server.<br>Note You need to specify this parameter to query the logon security configuration records of a specified server. For more information about the format, see the sample request. |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| Count | Integer | The total number of returned records. |
| TargetList | Array | The information about server to which the specified configuration record applies. For more information, see the following parameter descriptions. |
| TargetType | String | The type of the Target parameter value. Valid values:<br>• <em>groupId</em>: indicates an asset group ID.<br>• <em>uuid</em>: indicates a server UUID. |
| Target | String | The asset group ID or server UUID. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=DescribeConfigTarget
  &Config={"uuidCount":1,"location":"Ganzhou"}
  &Target=[{"targetType":"uuid","target":"6dbdbfe7-06fa-4d9a-8268-ce2dc6d673ac"}]
  &Type=login_common_location
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
    "TargetList": [{
     "Target": "inet-e53455ec-a134-4d46-9ff5-c4f3a5fe0f02",
     "TargetType": "uuid"
    }, {
     "Target": "inet-25f4ef74-29c7-49fd-85cc-b4543a2489a8",
     "TargetType": "uuid"
    }
   "Count": 2,
   "RequestId": "B8064EA4-9472-4D03-B7D1-6684DB5CD0BE",
  }
  ```

<a id="section-4-7"></a>

## 4.7. Webshell detection

<a id="section-4-7-1"></a>

### 4.7.1. DescribeWebPath

Description

You can call this operation to query the Web directories defined in webshell settings.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set this parameter to <em>DescribeWebPath</em>. |
| PageSize | Integer | No | The number of records to return on each page.<br>Default value: <em>20</em>. |
| CurrentPage | Integer | No | The number of the page to return.<br>Default value: <em>1</em>. |
| Type | String | No | The type of the settings.<br>Set this parameter to <em>web_path</em> to specify the Web directory settings. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| TotalCount | Integer | The number of returned records. |
| CurrentPage | Integer | The number of the current page returned. |
| PageSize | Integer | The number of records returned on each page. |
| Count | Integer | The number of Web directories. |
| ConfigList | Array | The Web directories. For more information, see the following descriptions. |
| WebPath | String | The path of the Web directory. |
| TargetList | Array | The servers that the Web directory has been applied to. For more information, see the following descriptions. |
| TargetType | String | This parameter always returns a value of uuid, which means that the Target parameter returns the universally unique identifier (UUID) of the server. |
| Target | String | The UUID of the server. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample request

  ```text
  https://aegis.[ RegionId].example.com/?Action=DescribeWebPath
  &<Common request parameters>
  ```

- Sample response (JSON format)

  ```json
  {
   "TotalCount":1,
   "PageSize":5,
   "RequestId":"7B6AD7C9-0F8D-4126-B8AA-6DC308B0B534",
   "CurrentPage":1,
   "Count":1,
   "ConfigList":[
    {
     "TargetList":[
      {
       "Target":"inet-f6ac9a93-0818-4052-90e2-d24f18ee198b",
       "TargetType":"uuid"
      }
     ],
     "WebPath":"/usr/local/tomcat/webroot18"
    }
   ]
  }
  ```

<a id="section-4-7-2"></a>

### 4.7.2. ModifyWebPath

Description

You can call this operation to modify the Web directory in webshell settings.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>ModifyWebPath</em>. |
| Type | String | No | The configuration type.<br>Set the value to <em>web_path</em>, indicating the web directory configuration. |
| Config | String | No | The Web directory configuration, in JSON format. For more information, see the sample request. |
| Target | String | No | The list of target servers to which the Web directory configuration applies, in JSON format. For more information, see the sample request. |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=ModifyWebPath
  &Type=web_path
  &Config={"webPath":"/test"}
  &Target={"targetType":"uuid","target":"0c797eb1-e6b9-4b5a-8917-a7e6cbbb4b2e","flag":"add"
  }
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
   "RequestId":"7B6AD7C9-0F8D-4126-B8AA-6DC308B0B534"
  }
  ```

<a id="section-4-7-3"></a>

### 4.7.3. DescribeCategoryCount

Description

You can call this operation to query the number of webshells detected by Server Guard.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>DescribeCategoryCount</em>. |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| Webshell | Integer | The number of webshells. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=DescribeCategoryCount
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
      "RequestId": "43F670F3-AB40-4E91-BC7D-C57468834F67",
      "Webshell": 2
  }
  ```

<a id="section-4-7-4"></a>

### 4.7.4. DescribeWebshell

Description

You can call this operation to query records of webshell files that have been detected by Server Guard, including the detection time and webshell file path.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set this parameter to <em>DescribeWebshell</em>. |
| GroupId | Integer | No | The ID of the asset group. |
| Mark | String | No | The IP address or instance name of the server. |
| Tag | Integer | No | The server tag ID. |
| Dealed | String | No | The status of the webshell event. Valid values:<br>• <em>n</em>: indicates that the event is pending.<br>• <em>y</em>: indicates that the event has been handled. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| WebshellList | Array | The webshell events. For more information, see the following descriptions. |
| Os | String | The operating system of the server. |
| InstanceName | String | The instance name of the server. |
| GroupId | Long | The ID of the asset group. |
| Ip | String | The IP address of the server.<br>Note The public IP address of the server is displayed preferentially. If no public IP address is assigned to the server, the private IP address of the server is displayed. |
| Uuid | String | The universally unique identifier (UUID) of the server. |
| FoundTime | String | The time when the webshell file was detected. |
| InstanceId | String | The instance ID of the server. |
| TrojanType | String | The type of the webshell file. |
| FirstFoundTime | String | The time when the webshell file was detected for the first time. |
| TrojanSize | Long | The size of the webshell file. |
| Domain | String | The domain name associated with the server. |
| TrojanPath | String | The path of the webshell file. |
| Region | String | The region where the server resides. |
| Status | Integer | The status of the webshell event. Valid values:<br>• <em>1</em>: indicates that the event is pending.<br>• <em>2</em>: indicates that the event has been ignored.<br>• <em>3</em>: indicates that the event has been confirmed.<br>• <em>8</em>: indicates that the event has been labeled as a false positive.<br>• <em>16</em>: indicates that the event is being handled.<br>• <em>32</em>: indicates that the event has been handled. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample request

  ```text
  https://aegis.[ RegionId].example.com/?Action=DescribeWebshell
  &Dealed=n
  &GroupId=1
  &Remark=xx.xx.xx.xx
  &Tag=11
  &<Common request parameters>
  ```

- Sample response (JSON format)

  ```json
  {
      "WebshellList": [{
          "Uuid": "aa46dbe9-d35d-4b77-a4d9-10bc6b1b****",
          "FoundTime": "2018-02-27 03:23:18",
          "Ip": "xx.xx.xx.xx",
          "FirstFoundTime": "2017-12-24 03:36:03",
          "Domain": "",
          "TrojanType": "Webshell",
          "InstanceId": "i-bp15xtqydmbujgep****",
          "TrojanPath": "c:/zhb/wamp/wamp/www/My.php",
          "GroupId": 3259405,
          "Os": "windows",
          "Status": 1,
          "Region": "cn-hangzhou-dg-a01",
          "TrojanSize": 0,
          "InstanceName": "win08****"
      }, {
          "Uuid": "aa46dbe9-d35d-4b77-a4d9-10bc6b1bb610",
          "FoundTime": "2017-12-25 03:53:22",
          "Ip": "x.x.x.x",
          "FirstFoundTime": "2017-12-24 03:36:01",
          "Domain": "",
          "TrojanType": "Webshell",
          "InstanceId": "i-bp15xtqydmbujgepdbev",
          "TrojanPath": "c:/zhb/wamp/../wamp/wamp/www/abc/My.php",
          "GroupId": 3259405,
          "Os": "windows",
          "Status": 9,
          "Region": "cn-hangzhou-dg-a01",
          "TrojanSize": 0,
          "InstanceName": "win08-zhb"
      }],
      "RequestId": "E4B254AE-5CB1-4810-8B51-A08DF5697F25"
  }
        
  ```

<a id="section-4-7-5"></a>

### 4.7.5. OperateTrojan

Description

You can call this operation to handle detected webshells.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>OperateTrojan</em>. |
| Info | String | No | The webshell information, in JSON format. For more information, see the sample request. |
| OperateType | String | No | The type of the operation. Valid values:<br>• <em>isolate</em>: indicates an operation to quarantine the file.<br>• <em>trust</em>: indicates an operation to trust the file.<br>• <em>untrust</em>: indicates an operation to cancel trusting the file.<br>• <em>restore</em>: indicates an operation to restore the file. |
| Type | Integer | No | The type of the trojan.<br>Set the value to <em>1</em>. |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| FailedCount | Integer | The number of failed operations. |
| SuccessCount | Integer | The number of successful operations. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=OperateTrojan
  &Info=[{"uuid":"97988c2b-de9d-4159-90ab-7cc73561c64c","filePath":"/home/test/Z02.php","webshellId":""}]
  &OperateType=trust
  &Type=1
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
      "RequestId": "43F670F3-AB40-4E91-BC7D-C57468834F67",
      "FailedCount": 0,
      "SuccessCount": 1
  }
  ```

<a id="section-4-7-6"></a>

### 4.7.6. DescribeQuaraFile

Description

You can call this operation to obtain the list of quarantined files.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>DescribeQuaraFile</em>. |
| PageSize | Integer | No | The maximum number of records to be displayed on each page of the query result.<br>Default value: <em>20</em>. |
| CurrentPage | Integer | No | The current page number.<br>Default value: <em>1</em>. |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| TotalCount | Integer | The total number of returned records. |
| CurrentPage | Integer | The current page number. |
| PageSize | Integer | The maximum number of records displayed on a page. |
| QuaraFiles | Array | The list of quarantined files. For more information, see the following parameter descriptions. |
| EventName | String | The name of the unusual event. |
| EventType | String | The type of the unusual event. |
| FileStatus | String | The status of the quarantined file. Valid values:<br>• <em>quaraFailed</em>("0"): indicates that the file failed to be quarantined.<br>• <em>rollbackFailed</em>("1"): indicates that the file failed to be rolled back to a previous version.<br>• <em>quaraDone</em>("2"): indicates that the file has been quarantined.<br>• <em>rollbackDone</em>("3"): indicates that the file has been rolled back to a previous version.<br>• <em>quaraing</em>("4"): indicates that the file is being quarantined.<br>• <em>rollbacking</em>("5"): indicates that the file is being rolled back to a previous version. |
| Md5 | String | The MD5 value of the file. |
| Online | Boolean | Indicates whether the Server Guard agent on the server is online. |
| Path | String | The file path. |
| Tag | String | The unique identifier of the unusual event. |
| Uuid | String | The UUID of the server. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=DescribeQuaraFile
  &<Common request parameters>
        
  ```

- Sample responses (JSON format)

  ```json
  {
      "TotalCount":1,
      "PageSize":20,
      "RequestId":"0C7FAD74-83FA-4671-9250-A5F2A64F437A",
      "CurrentPage":1,
      "QuaraFiles":[
          {
              "Path":"/bin/ping",
              "Uuid":"9b0c4d55-2f1f-4766-a90a-2c9d8a0b7642",
              "FileStatus":"quaraDone",
              "EventType":"Parent class of cloud scanning events (test ping)",
              "EventName":"Sub-class of cloud scanning events (test ping)",
              "Tag":"1d791175ad0bffd973b039248d6086e0",
              "Online":false,
              "Md5":"1421d9ad2b0031483f396154d48161f1"
          }
      ]
  }
        
  ```

<a id="section-4-7-7"></a>

### 4.7.7. RollbackQuaraFile

Description

You can call this operation to restore a specified quarantined file.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>RollbackQuaraFile</em>. |
| EventName | String | No | The name of the unusual event. |
| EventType | String | No | The type of the unusual event. |
| Tag | String | No | The GUID of the unusual event. |
| Uuid | String | No | The UUID of the server. |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=RollbackQuaraFile
  &EventName=DDoS trojan
  &EventType=Malicious process
  &Tag=a50f96f958fbd59f68e4bca4d90679d6
  &Uuid=00f11fcb-1a9a-4fd5-a48a-e0e5bd12a6a4
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
   "RequestId":"0C7FAD74-83FA-4671-9250-A5F2A64F437A",
  }
  ```

<a id="section-4-8"></a>

## 4.8. Exception detection on hosts

<a id="section-4-8-1"></a>

### 4.8.1. DescribeSuspEventTypes

Description

You can call this operation to query the unusual event types.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>DescribeSuspEventTypes</em>. |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| TotalCount | Integer | The total number of returned records. |
| EventTypes | Array | The list of unusual event types. For more information, see the following parameter descriptions. |
| AliseEventType | String | The name of the unusual event type. |
| EventType | String | The identifier of the unusual event type. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=DescribeSuspEventTypes
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
   "TotalCount":1,
   "RequestId":"66BE7091-BC00-4943-8A0D-B3DCE90AD7B5",
   "EventTypes":[
    {
     "EventType":"Suspicious process",
     "AliseEventType":"Suspicious process"
    }
   ]
  }
  ```

<a id="section-4-8-2"></a>

### 4.8.2. DescribeSuspTrendStatistics

Description

You can call this operation to query the chart data on different types of unusual server events on each day.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>DescribeSuspTrendStatistics</em>. |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| Interval | Integer | The time length of the the time frame specified for query. |
| StartTime | Integer | The start time of the time frame specified for query. |
| SuspiciousItems | List | The statistics on numbers of different types of suspicious events. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=DescribeSuspTrendStatistics
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
   "RequestId":"66BE7091-BC00-4943-8A0D-B3DCE90AD7B5",
   "Start":-28800000,
   "Interval":86400000,
   "SuspiciousItems":[ ]
  }
  ```

<a id="section-4-8-3"></a>

### 4.8.3. OperateSuspiciousEvent

Description

You can call this operation to handle detected unusual events.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>OperateSuspiciousEvent</em>. |
| Data | String | No | The unusual event to be handled, in JSON format. For more information, see the sample request. |
| OperateType | String | No | The type of the operation. Valid values:<br>• <em>deal</em>: indicates an operation to handle the unusual event.<br>• <em>confirm</em>: indicates an operation to mark the unusual event as handled.<br>• <em>mark_misinformation</em>: indicates an operation to mark the unusual event as false positive.<br>• <em>unmark_misinformation</em>: indicates an operation to remove the false positive mark of the unusual event.<br>• <em>ignore</em>: indicates an operation to ignore the unusual event. |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=OperateSuspiciousEvent
  &OperateType=ignore
  &Data={"uuid":"97988c2b-de9d-4159-90ab-7cc73561c64c","tag":"f87eb0ee5934f6f65343ec601ce71c2f","eventType":"Malicious processes (malware checking)","eventName":"DDoS Trojan},{"uuid":"97988c2b-de9d-4159-90ab-7cc73561c64c","tag":"95347a77b8c0d6dae99a23ab69aa90f4","event
  Type":"Malicious processes (malware checking)","eventName":"GateDDoS Trojan"}
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
   "RequestId":"654A6FD8-B55D-4D6B-AAFF-4122503D108B"
  }
  ```

<a id="section-4-8-4"></a>

### 4.8.4. OperateLoginLog

Description

You can call this operation to label a detected unusual logon event as handled.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>OperateLoginLog</em>. |
| Ids | String | Yes | The ID of the unusual logon log.Separate multiple log IDs with commas (,). |
| OperateType | String | Yes | The type of the operation.<br>Set the value to <em>confirm</em>, indicating that the event has been handled. |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=OperateLoginLog
  &Ids=2006434
  &OperateType=confirm
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
   "RequestId":"BE391ABB-6B7C-4C41-9F6C-862C1DEE3905"
  }
  ```

<a id="section-4-8-5"></a>

### 4.8.5. CreateSuspiciousExport

Description

You can call this operation to export the information about unusual events on servers based on search conditions.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>CreateSuspiciousExport</em>. |
| Dealed | String | No | Indicates whether the unusual event has been handled. Valid values:<br>• <em>Y</em>: indicates that the event has been handled.<br>• <em>N</em>: indicates that the event has not been handled. |
| EventNameRemark | String | No | The name of the event. Fuzzy matching is supported. |
| EventType | String | No | The name of the event type. Valid values:<br>• <em>Unusual logon</em><br>• <em>Suspicious process</em><br>• <em>Suspicious account</em><br>• <em>Sensitive file tampering</em><br>• <em>Suspicious network connection</em><br>• <em>Unusual event</em><br>• <em>Suspicious file</em><br>• <em>Malicious process</em> |
| GroupId | String | No | The ID of the asset group. |
| Level | String | No | The risk level of the event. Valid values:<br>• <em>Critical</em>: indicates a critical-risk event.<br>• <em>Important</em>: indicates an important-risk event.<br>• <em>Moderate</em>: indicates a moderate-risk event.<br>• <em>low</em>: indicates a low-risk event.You can specify multiple event levels and separate them with commas (,). |
| Remark | String | No | The name or IP address of the server.Fuzzy matching is supported. |
| StatusList | String | No | The handling status of the event. Valid values:<br>• <em>1</em>: indicates that the event is to be handled.<br>• <em>2</em>: indicates that the event has been ignored.<br>• <em>3</em>: indicates that the event has been confirmed.<br>• <em>8</em>: indicates that the event has been labeled as a false positive.<br>• <em>16</em>: indicates that the event is being handled.<br>• <em>32</em>: indicates that the event has been handled.You can specify multiple statuses and separate them with commas (,). |
| Tag | String | No | The tag of the server. |
| Uuids | String | No | The UUID of the server. Separate multiple UUIDs with commas (,). |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| FileName | String | The name of the exported file. |
| Id | Long | The ID of the export task. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=CreateSuspiciousExport
  &Remark=23
  &EventType=Suspicious process
  &Level=serious,high,medium,low
  &Dealed=n
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
      "RequestId": "43F670F3-AB40-4E91-BC7D-C57468834F67",
      "FileName": "suspicious_20180408",
      "Id": 387
  }
  ```

<a id="section-4-8-6"></a>

### 4.8.6. DescribeSuspiciousExportInfo

Description

You can call this operation to query an unusual event export task.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set this parameter to <em>DescribeSuspiciousExportInfo</em>. |
| ExportId | Long | No | The ID of the export task. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| CurrentCount | Integer | The number of records that have been exported. |
| ExportStatus | String | The status of the export task. Valid values:<br>• <em>init</em>: indicates that the export task is being initialized.<br>• <em>pending</em>: indicates that the export task is pending.<br>• <em>exporting</em>: indicates that the export task is being executed.<br>• <em>success</em>: indicates that the export task has been completed.<br>• <em>fail</em>: indicates that the export task has failed. |
| Message | String | The status description or failure information of the export task. |
| FileName | String | The name of the exported file. |
| Id | Integer | The ID of the export task. |
| GmtCreate | Long | The time when the export task was created. |
| Link | String | The download link of the exported file. |
| Progress | Integer | The export progress. |
| TotalCount | Integer | The total number of records that have been exported. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample request

  ```text
  https://aegis.[ RegionId].example.com/?Action=DescribeSuspiciousExportInfo
  &ExportId=1
  &<Common request parameters>
  ```

- Sample response (JSON format)

  ```json
  {
   "TotalCount":30,
   "GmtCreate":1518071546000,
   "Progress":100,
   "Message":"success",
   "RequestId":"654A6FD8-B55D-4D6B-AAFF-4122503D108B",
   "FileName":"suspicious_20180208",
   "ExportStatus":"success",
   "CurrentCount":30,
   "Id":11,
   "Link":"http://suspicious-export.oss-cn-shanghai.example.com/export/suspicious_20180208_1518071576098.zip?Expires=1518075176&OSSAccessKeyId=<yourAccessKeyId>&Signature=xxxx%xxxx%3D"
  }
  ```

<a id="section-4-8-7"></a>

### 4.8.7. DescribeVirusInfo

Description

You can call this operation to upload the MD5 values of files and use Alibaba Cloud Antivirus to determine whether the files are malicious programs.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>DescribeVirusInfo</em>. |
| Md5 | String | Yes | The MD5 value of the file. |
| Lang | String | No | The language attribute of the file, such as <em>zh</em>. |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| Data | Boolean | Indicates whether the file is malicious. Valid values:<br>• True: Indicates that the file is malicious.<br>• False: Indicates that the file is not malicious. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].aliyuncs.com/?Action= DescribeVirusInfo
  &Md5=6f6628d923f9018b28acc5f905e03244
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
   "RequestId": "A2423F39-3272-4491-804E-D0EBDE3E894D",
   "Data": true
  }
  ```

<a id="section-4-9"></a>

## 4.9. Retrieval of host logs

<a id="section-4-9-1"></a>

### 4.9.1. CreateLogQuery

Description

You can call this operation to create or save server log search conditions.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>CreateLogQuery</em>. |
| Conditions | String | No | The log search condition. |
| QueryDetail | String | No | The log search sub-conditions. |
| QueryName | String | No | The saved search name. |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=CreateLogQuery
  &Conditions=aegis-log-login@warn_port:22
  &QueryDetail=[[{"itemForm":{},"d":{"name":"Logons","id":"aegis-log-login","fields":[{"name":"ip","type":"string","desc":"IP address","text":"IP(IP address)"}]]
  &QueryName=test
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
   "RequestId":"415AE1FC-3C11-4AA9-A06F-DE13D3430366"
  }
  ```

<a id="section-4-9-2"></a>

### 4.9.2. DescribeLogQuery

Description

You can call this operation to query the saved server log search conditions.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>DescribeLogQuery</em>. |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| ListTotal | Integer | The total number of returned records. |
| QueryItems | Array | The details of log search conditions. For more information, see the following parameter descriptions. |
| Conditions | String | The log search conditions. |
| QueryDetail | String | The log search sub-conditions. |
| QueryName | String | The name of the log search task. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=DescribeLogQuery
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
   "RequestId":"65802B9B-4D30-40F0-8691-F126652DBEBE",
   "ListTotal":1,
   "QueryItems":[
    {
     "QueryDetail":"[[{\"itemForm\":{},\"d\":{\"name\":\"Account snapshot\",\"id\":\"aegis-snapshot-host\",\"fields\":[{\"name\":\"ip\",\"type\":\"string\",\"desc\":\"IP address\"}
  ,{\"name\":\"uuid\",\"type\":\"string\",\"desc\":\"Client ID\"},{\"name\":\"perm\",\"type
  \":\"string\",\"desc\":\"Root permission availability\"},{\"name\":\"home_dir\",\"type\":
  \"string\",\"desc\":\"Home directory\"},{\"name\":\"warn_time\",\"type\":\"string\",\"desc\":\"Password expiration reminder time\"},{\"name\":\"groups\",\"type\":\"array\",\"desc
  \":\"User group\"},{\"name\":\"login_ip\",\"type\":\"string\",\"desc\":\"Last logon IP\"}
  ,{\"name\":\"last_chg\",\"type\":\"string\",\"desc\":\"Last password change time\"},{\"name\":\"shell\",\"type\":\"string\",\"desc\":\"Linux shell command\"},{\"name\":\"domain\",\"type\":\"string\",\"desc\":\"Windows domain\"},{\"name\":\"tty\",\"type\":\"string\",\
  "desc\":\"Logon terminal\"},{\"name\":\"account_expire\",\"type\":\"string\",\"desc\":\"Account expiration time\"},{\"name\":\"passwd_expire\",\"type\":\"string\",\"desc\":\"Password expiration time\"},{\"name\":\"last_logon\",\"type\":\"string\",\"desc\":\"Last logon time\"},{\"name\":\"user\",\"type\":\"string\",\"desc\":\"User\"},{\"name\":\"status\",
  \"type\":\"string\",\"desc\":\"User status: 0-disabled, 1-enabled\"}]},\"searchFields\":[
  {\"name\":\"ip\",\"type\":\"string\",\"desc\":\"IP address\"},{\"name\":\"uuid\",\"type\":\"string\",\"desc\":\"Client ID\"},{\"name\":\"perm\",\"type\":\"string\",\"desc\":\"Root permission availability\"},{\"name\":\"home_dir\",\"type\":\"string\",\"desc\":\"Home directory\"},{\"name\":\"warn_time\",\"type\":\"string\",\"desc\":\"Password expiration reminder time\"},{\"name\":\"groups\",\"type\":\"array\",\"desc\":\"User group\"},{\"name\":\"login_ip\",\"type\":\"string\",\"desc\":\"Last logon IP\"},{\"name\":\"last_chg\",\"type\":\"string\",\"desc\":\"Last password change time\"},{\"name\":\"shell\",\"type\":\"string\",\"desc\":\"Linux shell command\"},{\"name\":\"domain\",\"type\":\"string\",\"desc\
  ":\"Windows domain\"},{\"name\":\"tty\",\"type\":\"string\",\"desc\":\"Logon terminal\"},
  {\"name\":\"account_expire\",\"type\":\"string\",\"desc\":\"Account expiration time\"},{\
  "name\":\"passwd_expire\",\"type\":\"string\",\"desc\":\"Password expiration time\"},{\"name\":\"last_logon\",\"type\":\"string\",\"desc\":\"Last logon time\"},{\"name\":\"user\",\"type\":\"string\",\"desc\":\"User\"},{\"name\":\"status\",\"type\":\"string\",\"desc\":\"User status: 0-disabled, 1-enabled\"}],\"f\":{\"name\":\"ip\",\"type\":\"string\",\"desc\":\"IP address\"},\"searchLimit\":[{\"name\":\"Including\",\"value\":\":\"}],\"l\":\":
  \",\"kw\":\"string\"}]]",
     "Conditions":"aegis-snapshot-host@ip:string",
     "QueryName":"aa"
    }
   ]
  }
  ```

<a id="section-4-9-3"></a>

### 4.9.3. DeleteLogQuery

Description

You can call this operation to delete the saved server log search conditions.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>DeleteLogQuery</em>. |
| QueryName | String | No | The name of the saved search. |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=DeleteLogQuery
  &QueryName=test
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
   "RequestId":"415AE1FC-3C11-4AA9-A06F-DE13D3430366"
  }
  ```

<a id="section-4-9-4"></a>

### 4.9.4. DescribeFilterFields

Description

You can call this operation to query the filter fields of a specified server log search condition.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>DescribeFilterFields</em>. |
| Query | String | No | The log search condition. |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| Total | String | The total number of search conditions. |
| LogFilterList | Array | The filter field information. For more information, see the following parameter descriptions. |
| Fields | String | The filter fields. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=DescribeFilterFields
  &Query=aegis-log-login@warn_port:22
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
   "LogFilterList":[
    {
     "Fields":"IP;IP address,UUID;Client ID","fieldsName":"default"
    }
   ],
   "Total":"20",
   "RequestID":"883e1e3d-4443-4206-871c-6c0625c01332"
  }
  ```

<a id="section-4-9-5"></a>

### 4.9.5. DescribeHistogram

Description

You can call this operation to obtain the statistics on server logs generated within a specified time frame.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>DescribeHistogram</em>. |
| Query | String | Yes | The log query conditions. |
| EndTime | String | Yes | The end time of the time frame specified for query. |
| StartTime | String | Yes | The start time of the time frame specified for query. |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| Categories | String | The timeline information. |
| Items | Array | The log quantity statistics. For more information, see the following parameter descriptions. |
| Data | List | The number of logs. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=DescribeHistogram
  &EndTime=2018-03-03 17:41:03
  &Query=aegis-log-login@warn_port:22
  &StartTime=2018-03-02 17:41:03
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
   "RequestId":"82D245FB-7A5D-4155-B59F-5B084CE93B6B",
   "Categories":[
    "1519983663000,1519984800000",
    "1519984800000,1519986600000",
    "1519986600000,1519988400000",
    "1519988400000,1519990200000",
    "1519990200000,1519992000000",
    "1519992000000,1519993800000",
    "1519993800000,1519995600000"
   ],
   "Items":[
    {
     "Data":[
      0,
      0,
      0,
      0,
      0,
      0,
      0
     ]
    }
   ]
  }
  ```

<a id="section-4-9-6"></a>

### 4.9.6. DescribeLogInfo

Description

You can call this operation to query the server log fields based on specified query conditions.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>DescribeLogInfo</em>. |
| PageSize | Integer | No | The maximum number of records to be displayed on each page of the query result.<br>Default value: <em>20</em>. |
| CurrentPage | Integer | No | The current page number.<br>Default value: <em>1</em>. |
| Query | String | Yes | The log query conditions. |
| EndTime | String | Yes | The end time of the query. |
| StartTime | String | Yes | The start time of the query. |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| TotalCount | Integer | The total number of returned records. |
| LogInfoItems | Array | The information about server log fields. For more information, see the following parameter descriptions. |
| Id | String | The ID of the log source. |
| Name | String | The name of the log source. |
| Fields | Array | The list of server log fields. For more information, see the following parameter descriptions. |
| Name | String | The ID of the log field. |
| Desc | String | The name of the log field. |
| Type | String | The type of the log field. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=DescribeLogInfo
  &CurrentPage=1
  &EndTime=2018-03-03 17:41:03
  &PageSize=20
  &Query=aegis-log-login@warn_port:22
  &StartTime=2018-03-02 17:41:03
  &<Common request parameters>
        
  ```

- Sample responses (JSON format)

  ```json
  {
      "TotalCount":1,
      "RequestId":"3A7CFB73-C24C-4711-B7D9-2BE74EBFFE78",
      "LogInfoItems":[
          {
              "Fields":[
                  {
                      "Desc":"IP address",
                      "Type":"string",
                      "Name":"ip"
                  },
                  {
                      "Desc":"Client number",
                      "Type":"string",
                      "Name":"uuid"
                  },
                  {
                      "Desc":"Logon source IP address",
                      "Type":"string",
                      "Name":"warn_ip"
                  },
                  {
                      "Desc":"Logon port",
                      "Type":"string",
                      "Name":"warn_port"
                  },
                  {
                      "Desc":"Logon username",
                      "Type":"string",
                      "Name":"warn_user"
                  },
                  {
                      "Desc":"Logon type",
                      "Type":"string",
                      "Name":"warn_type"
                  },
                  {
                      "Desc":"Logon count",
                      "Type":"string",
                      "Name":"warn_count"
                  }
              ],
              "Id":"aegis-log-login",
              "Name":"Logon serial number"
          },
      ]
  }
        
  ```

<a id="section-4-9-7"></a>

### 4.9.7. DescribeLogItems

Description

You can call this operation to query the server log details that are returned by a query.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>DescribeLogItems</em>. |
| PageSize | Integer | No | The number of records displayed on a page.<br>Default value: <em>20</em>. |
| CurrentPage | Integer | No | The current page number.<br>Default value: <em>1</em>. |
| Query | String | No | The log query criterion. |
| AccountSnapshot Offset | Integer | No | The offset of the account snapshot log. |
| CrackOffset | Integer | No | The offset of the brute force password cracking log. |
| LoginOffset | Integer | No | The offset of the logon log. |
| NetworkOffset | Integer | No | The offset of the network connection log. |
| PortSnapshotOffs et | Integer | No | The offset of the listening port snapshot log. |
| ProcessOffset | Integer | No | The offset of the process startup log. |
| ProcessSnapshotO ffset | Integer | No | The offset of the process snapshot log. |
| EndTime | String | Yes | The end time of the time frame specified for query. |
| StartTime | String | Yes | The start time of the time frame specified for query. |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| TotalCount | Integer | The number of returned records. |
| CurrentPage | Integer | The current page number. |
| SetPageSize | Integer | The maximum number of records displayed on a page. |
| AccountSnapshotOffset | Integer | The offset of the account snapshot log. |
| AccountSnapshotTotalC ount | Integer | The total number of account snapshot log entries. |
| CrackOffset | Integer | The offset of the brute force password cracking log. |
| CrackTotalCount | Integer | The total number of brute force password cracking log entries. |
| LoginTotalCount | Integer | The total number of logon log entries. |
| NetworkOffset | Integer | The offset of the network connection log. |
| NetworkTotalCount | Integer | The total number of network connection log entries. |
| PortSnapshotOffset | Integer | The offset of the listening port snapshot log. |
| PortSnapshotTotalCoun t | Integer | The total number of listening port snapshot log entries. |
| ProcessOffset | Integer | The offset of the process startup log. |
| ProcessTotalCount | Integer | The total number of process startup log entries. |
| ProcessSnapshotOffset | Integer | The offset of the process snapshot log. |
| ProcessSnapshotTotalC ount | Integer | The total number of process snapshot log entries. |
| LogsList | Array | A list of host log details. For more information, see the following parameter descriptions. |
| LogSourceID | String | The ID of the log source. |
| LogSource | String | The name of the log source. |
| MLogTime | String | The time when the log entry was created. |
| MContents | Array | A list of host log entries. For more information, see the following parameter descriptions. |
| MKey | String | The log entry. |
| MValue | String | The value of the log entry. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://aegis.[ RegionId].example.com/?Action=DescribeLogItems
  &CurrentPage=1
  &PageSize=100
  &AccountSnapshotOffset=1000
  &CrackOffset=1000
  &EndTime=2018-03-05 11:46:07
  &LoginOffset=1000
  &NetworkOffset=1000
  &PortSnapshotOffset=1000
  &ProcessOffset=1000
  &ProcessSnapshotOffset=1000
  &Query=aegis-log-login@warn_port:22
  &StartTime=2018-03-02 17:41:03
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
   "RequestId":"BE391ABB-6B7C-4C41-9F6C-862C1DEE3905",
   "PageSize":100,
   "AccountSnapshotTotalCount":0,
   "LogsList":[],
   "CrackOffset":0,
   "ProcessOffset":0,
   "NetworkOffset":0,
   "ProcessSnapshotOffset":0,
   "LoginTotalCount":0,
   "CurrentPage":1,
   "PortSnapshotOffset":0,
   "NetworkTotalCount":0,
   "AccountSnapshotOffset":0,
   "CrackTotalCount":0,
   "PortSnapshotTotalCount":0,
   "ProcessSnapshotTotalCount":0,
   "ProcessTotalCount":0
  }
  ```

<a id="section-5"></a>

# 5.Anti-DDoS

<a id="section-5-1"></a>

## 5.1. List of operations

This topic introduces all the Apsara Stack Security Anti-DDoS operations that you can call. For more information, see the corresponding operation description.

| Operation | Description |
| --- | --- |
| CheckIpSegment | Checks whether a CIDR block to be added for monitoring is valid. |
| DescribeRegionName | Queries the regions of the CIDR blocks where traffic data collection and analysis is performed. |
| CreateIpSegment | Adds a specified CIDR block to be monitored. |
| DescribeIpSegment | Obtains a list of CIDR blocks under traffic monitoring. |
| DeleteIpSegment | Deletes a CIDR block whose traffic is collected and monitored based on the CIDR block record ID. |
| ModifyIpSegment | Modifies a monitored CIDR block with a specified record ID. |
| CreateDdosPolicy | Adds an anti-DDoS policy for a specified IP address or CIDR block. |
| DescribeDdosPolicies | Queries the configured DDoS protection policies. |
| DeleteDdosPolicy | Deletes an anti-DDoS policy for a specified CIDR block. |
| ModifyDdosPolicy | Modifies a specified anti-DDoS policy. |
| DescribeBlockSwitchs | Queries the status of the traffic block switch in anti-DDoS. |
| ModifyBlockSwitchs | Changes the status of the block switch in DDoS settings. |
| DescribeDdosEvents | Obtains the list of DDoS events that meet the specified search criteria. |
| DescribeFlowAnalysisResult | Queries the analysis result of the traffic sent to an IP address. |
| DescribeFlowDetails | Queries the detailed traffic information for a specified IP address. |
| CancelCleanStatus | Disables DDoS traffic scrubbing for a specified IP address. |
| CreateWhiteList | Adds a whitelist of trusted IP addresses that are exempt from traffic security monitoring. |
| DescribeWhiteList | Queries the IP addresses that have been added to a whitelist. |
| DeleteWhiteList | Deletes multiple risks from the whitelist for baseline check. |
| DescribeConsoleDdosPolicies | Obtains the records of anti-DDoS policies, including the system default policies. |

<a id="section-5-2"></a>

## 5.2. Make API requests

<a id="section-5-2-1"></a>

### 5.2.1. Request structure

Apsara Stack Security API is based on Remote Procedure Call (RPC). This topic describes the structure of the API requests.

Description

You can send an HTTP request to call an API operation. The URL of the request must be in the following format:

```text
http://endpoint/?Action=xx&parameters
```

Where:

- `endpoint` : the endpoint used to call a cloud service. The endpoint for the Anti-DDoS service is  `dd osprivate.[ RegionId].example.com` .

- `Action` : the operation that you want to perform.

  For example, you can set this parameter to DescribeFeatures to query the deployed Apsara Stack Security features.

- `parameters` : the request parameters. Request parameters include common request parameters and custom request parameters. Request parameters must be separated with ampersands (&).

  - Common request parameters include information such as the API version and authentication information.

  - For more information about the custom request parameters, see the corresponding operation description.

Example

Call the DescribeFeatures operation to query the deployed Apsara Stack Security features.

```text
https://yundunprivate.[ RegionId].example.com/?Action=DescribeFeatures&AccessKeyId=key-test&Format=JSON&SecureTransport=true&SignatureMethod=HMAC-SHA1&SignatureNonce=15215528852396&SignatureVersion=1.0&SourceIp=1xxxx6&Timestamp=2018-03-02Txxxxxxx&Version=2018-01-16&Signature=xxxx%xxxx%3D
```

API requests are presented in the following easy-to-read format in this document:

```text
https://yundunprivate.[ RegionId].example.com/?Action=DescribeFeatures
&Format=JSON
&Version=2018-01-16
&Signature=xxxx%xxxx%3D
&SignatureMethod=HMAC-SHA1
&SignatureNonce=15215528852396
&SignatureVersion=1.0
&AccessKeyId=key-test
&Timestamp=2012-06-01T12:00:00Z
```

<a id="section-5-2-2"></a>

### 5.2.2. Signature mechanism

Apsara Stack Security authenticates each access request. You need to include a signature for the submitted HTTP or HTTPS request.

API authorization

To ensure the security of your account, we recommend that you use a Resource Access Management (RAM) user to call API operations. Before using a RAM user to call an API operation, you must grant the RAM user the corresponding permission to call the API by creating an authorization policy and attaching the policy to the RAM user.

API signature

To ensure secure calls to the API, Alibaba Cloud authenticates each API request through the signature. When you manually make an API request, you need to use AccessKey Secret to calculate the signature, that is, the hash-based message authentication code (HMAC) value, based on the encoded and sorted request string. For more information, see the definition in RFC 2104.

This topic uses the raw access parameters in the following table to describe how to create an API signature.

| Parameter | Description |
| --- | --- |
| Access point | <code>http://semawaf.[ RegionId].example.com/?</code> |
| API-specific parameters | <code>Action=DescribeFeatures</code> |
| Common parameters (excluding the Signature parameter) | <code>&amp;Timestamp=2016-02-23T12:46:24Z</code><br><code>&amp;Format=JSON</code><br><code>&amp;AccessKeyId=&lt;yourAccessKeyId&gt;</code><br><code>&amp;SignatureMethod=HMAC-SHA1</code><br><code>&amp;SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf</code><br><code>&amp;Version=2018-01-16</code><br><code>&amp;SignatureVersion=1.0</code> |
| AccessKey secret | <code>&lt;yourAccessKeySecret&gt;</code> |

1. Use the request parameters to construct a canonicalized query string.

   Note

   The request parameters include common request parameters (excluding the

   Signature parameter) and API-specific parameters.

   <ol type="i">

   <li>

   Sort the parameters.

   </li>

   </ol>

   Sort the request parameters in alphabetical order.

   <ol type="i" start="2">

   <li>

   Encode the parameters.

   </li>

   </ol>

   Use UTF-8 to URL-encode the parameter names and values. The encoding rules are as follows:

   - Letters, digits, hyphens (-), underscores (_), periods (.), and tildes (~) are not encoded.

   - Other characters are encoded in the %XY format, where XY is the hexadecimal representation of the character in ASCII. For example, the double quotation mark (") is encoded as %22.

   - Extended UTF-8 characters are encoded in the %XY%ZA… format.

   - Note that a space is encoded as %20, instead of a plus sign (+).

   <ol type="i" start="3">

   <li>

   Connect the encoded parameter names and values with equal signs (=).

   </li>

   <li>

   Then, sort the parameter name and value pairs connected by equal signs in alphabetical order,

   </li>

   </ol>

   and connect them with ampersands (&) to produce the canonicalized query string.

2. Use the canonicalized query string to construct the string for signature calculation based on the following rules:

   ```text
   StringToSign=HTTPMethod + “&” + percentEncode(“/”) + ”&” +
   percentEncode(CanonicalizedQueryString)
   ```

3. Calculate the HMAC value of the StringToSign string according to the definition in RFC 2104.

   Note

   The key used for signature calculation is your AccessKey secret adding the

   ampersand (&) (ASCII 38). Secure Hash Algorithm 1 (SHA1) is used as the hash algorithm.

4. Encode the preceding HMAC value into a string based on Base64 encoding rules to obtain the signature value.

   ```text
   LEW8N4y7Uasop******
   ```

5. Set the Signature parameter in the request parameters to this signature value to sign the request.

<a id="section-5-2-3"></a>

### 5.2.3. Common request parameters

The following table describes the common request parameters that are used to indicate information such as the API version and authentication information.

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Version | String | Yes | The API version in the format of YYYY-MM-DD.<br>Set the value to <em>2018-01-16</em>. |
| AccessKeyId | String | Yes | The key ID that Alibaba Cloud assigns to a user for service access. |
| Signature | String | Yes | The signature string. |
| SignatureMethod | String | Yes | The signature method.<br>Set the value to <em>HMAC-SHA1</em>. |
| Timestamp | String | Yes | The timestamp of the request. Follow the ISO 8601 standard to specify the date and use the offset from Coordinated Universal Time (UTC) to specify the time zone.<br>The format is <code> YYYY-MM-</code><code>DDThh:mm:ssZ </code>.<br>For example, 2014-05-26T12:00:00Z indicates 20:00:00 on May 26, 2014, Beijing time. |
| SignatureVersion | String | Yes | The signature algorithm version.<br>Set the value to <em>1.0</em>. |
| SignatureNonce | String | Yes | The unique random number used to prevent network replay attacks. You must use different random numbers for different requests. |
| ResourceOwnerAc count | String | No | The owner account of the resource to be accessed through this API request, that is, the logon username. |
| Format | String | No | The format of the response.<br>Set the value to <em>JSON or XML</em>.<br>Note Default value: XML. |

<a id="section-5-2-4"></a>

### 5.2.4. Response structure

Apsara Stack Security API responses support both the XML and JSON formats. The system always returns a unique identification code RequestId each time you send a request to call an operation, no matter whether the call is successful or not.

Sample responses (XML format)

```xml
<? xml version="1.0" encoding="UTF-8"? >
<! -- The root node of the result -->
<Operation name+Response>
    <! -- Returned request ID -->
    <RequestId>4C467B38-3910-447D-87BC-AC049166F216</RequestId>
    <! -- Returned data -->
</Operation name+Response>
```

Sample responses (JSON format)

```json
{
"RequestId": "4C467B38-3910-447D-87BC-AC049166F216",
/* Returned data */
}
```

<a id="section-5-3"></a>

## 5.3. APIs

<a id="section-5-3-1"></a>

### 5.3.1. CheckIpSegment

Description

You can call this operation to check whether a CIDR block to be added for monitoring is valid. If a success result is returned through this API, the CIDR block specified in the request can be added.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>CheckIpSegment</em>. |
| IpSegmentName | String | Yes | The CIDR block to be checked, in x.x.x.x/x format. For example, 172.21.23.222/24. |
| InfoType | String | No | The CIDR block information type. For example, a value of distribution indicates the region information. |
| InfoName | String | No | The information describing the CIDR block based on the value of the InfoType parameter. For example, if the InfoType parameter is set to distribution, you can set the InfoName parameter to DXJF, indicating that the CIDR block belongs to the region where the Daxing IDC is located. |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://ddosprivate.[ RegionId].example.com/?Action=CheckIpSegment
  &IpSegmentName=192.1.1.1/24
  &InfoType=distribution
  &InfoName=DXJF
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
   "RequestId":"71064826-726F-4ADA-B879-05D8055476FB"
  }
  ```

<a id="section-5-3-2"></a>

### 5.3.2. DescribeRegionName

Description

You can call this operation to query the regions of the CIDR blocks where traffic data collection and analysis is performed.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>DescribeRegionName</em>. |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| RegionNameList | Array | A list of regions. For more information, see the following parameter descriptions. |
| Id | Integer | The ID of the region. |
| Description | String | The region of the CIDR block. |
| CodeType | String | The type of the CIDR block information. For example, distribution indicates the region information. |
| Code | String | This parameter is used with the CodeType parameter to specify the code of the corresponding information. For example, if the CodeType parameter is set to distribution and the Code parameter is set to DXJF, this indicates that the CIDR block belongs to the region where the Daxing data center is located. |
| CodeName | String | This parameter is used with the CodeType parameter to specify the name of the corresponding information. |
| GmtCreate | String | The time when the CIDR block was created. |
| GmtModified | String | The latest time when the CIDR block was modified. |
| Seq | Integer | The sequence number of the region record. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://ddosprivate.[ RegionId].example.com/?Action=DescribeRegionName
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
   "RegionNameList":[
    {
     "GmtCreate":1463367238000,
     "Description":"Hybrid cloud data center list",
     "CodeName":"Daxing data center",
     "GmtModified":1463367238000,
     "CodeType":"distribution",
     "Id":17,
     "Code":"am1",
     "Seq":1
    },
    {
     "GmtCreate":1463367238000,
     "Description":"Hybrid cloud data center list",
     "CodeName":"Not specified",
     "GmtModified":1463367238000,
     "CodeType":"distribution",
     "Id":32,
     "Code":"UNKNOWN",
     "Seq":4
    },
    {
     "GmtCreate":1485069049000,
     "Description": "Data center list",
     "CodeName":"Beijing data center",
     "GmtModified":1485069049000,
     "CodeType":"distribution",
     "Id":50,
     "RegionId": "cn-beijing-btc-a01",
     "Seq":2
    },
    {
     "GmtCreate":1485069106000,
     "Description": "Data center list",
     "CodeName":"Hangzhou data center",
     "GmtModified":1485069104000,
     "CodeType":"distribution",
     "Id":51,
     "Code":"cn-hangzhou-dg-a01",
     "Seq":3
    },
    {
     "GmtCreate":1463367238000,
     "Description":"Hybrid cloud data center list",
     "CodeName":"Daxing data center",
     "GmtModified":1463367238000,
     "CodeType":"distribution",
     "Id":52,
     "Code":"DD_DXJF",
     "Seq":1
    }
   ],
   "RequestId":"26738B34-6680-4BD7-BBF8-EF8DE53D52F6"
  }
  ```

<a id="section-5-3-3"></a>

### 5.3.3. CreateIpSegment

Description

You can call this operation to add a specified CIDR block to be monitored.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>CreateIpSegment</em>. |
| IpSegmentName | String | Yes | The CIDR block to be added for monitoring, in x.x.x.x/x format. For example, 172.21.23.222/24. |
| InfoType | String | No | The CIDR block information type. For example, a value of distribution indicates the region information. |
| InfoName | String | No | The information describing the CIDR block based on the value of the InfoType parameter. For example, if the InfoType parameter is set to distribution, you can set the InfoName parameter to DXJF, indicating that the CIDR block belongs to the region where the Daxing data center is located. |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://ddosprivate.[ RegionId].example.com/?Action=CreateIpSegment
  &IpSegmentName=172.21.13.222/24
  &InfoType=distribution
  &InfoName=DXJF
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
   "RequestId":"6C91B447-DAA5-40DB-B818-E10820D99DEC"
  }
  ```

<a id="section-5-3-4"></a>

### 5.3.4. DescribeIpSegment

Description

You can call this operation to query Classless Inter-Domain Routing (CIDR) blocks under traffic monitoring.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set this parameter to <em>DescribeIpSegment</em>. |
| CurrentPage | Integer | No | The number of the page to return. |
| PageSize | Integer | No | The number of records to return on each page. |
| InfoType | String | No | The type of the CIDR block information.For example, a value of distribution indicates the region information. |
| Distribution | String | No | The ID of the region. For example, a value of DXJF indicates the region where the Daxing IDC is located. |
| IpSegment | String | No | The CIDR block, in x.x.x.x/x format. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| CurrentPage | Integer | The number of the current page returned. |
| PageSize | Integer | The number of records returned on each page. |
| TotalCount | Integer | The total number of returned pages. |
| IpSegmentList | Array | The CIDR blocks for traffic collection. For more information, see the following descriptions. |
| GmtCreate | Long | The time when the CIDR block for traffic collection was created. |
| GmtModified | Long | The time when the CIDR block for traffic collection was last modified. |
| Id | Integer | The ID of the CIDR block for traffic collection. |
| RegionName | String | The region name of the CIDR block. |
| InfoType | String | The type of the CIDR block information. For example, a value of distribution indicates the region information. |
| InfoName | String | The information describing the CIDR block based on the value of the InfoType parameter. For example, if the value of the InfoType parameter is distribution, the value of the InfoName parameter can be DXJF, indicating that the CIDR block belongs to the region where the Daxing IDC is located. |
| IpExpressions | String | The CIDR block for traffic collection, in x.x.x.x/x format. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample request

  ```text
  https://ddosprivate.[ RegionId].example.com/?Action=DescribeIpSegment
  &CurrentPage=1
  &Distribution=DXJF
  &InfoType=distribution
  &IpSegment=x.x.x.x/x
  &PageSize=20
  &<Common request parameters>
        
  ```

- Sample response (JSON format)

  ```json
  {
      "TotalCount":1,
      "PageSize":20,
      "RequestId":"AC51224B-3730-4C6B-B444-2307C7F73E84",
      "IpSegmentList":[
          {
              "IpExpressions":"192.168.x.x/24",
              "GmtCreate":1520565939000,
              "RegionName":"Daxing IDC",
              "GmtModified":1520565939000,
              "InfoName":"****",
              "Id":9,
              "InfoType":"distribution1"
          }
      ],
      "CurrentPage":1
  }
        
  ```

<a id="section-5-3-5"></a>

### 5.3.5. DeleteIpSegment

Description

You can call this operation to delete a CIDR block whose traffic is collected and monitored based on the CIDR block record ID.

Note

You must obtain the record ID of the monitored CIDR block to be deleted before calling

this operation.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>DeleteIpSegment</em>. |
| IpId | String | Yes | The record ID of the monitored CIDR block to be deleted. |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://ddosprivate.[ RegionId].example.com/?Action=DeleteIpSegment
  &IpId=1
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
   "RequestId":"9C40FE9D-EE39-4162-8E94-7C0A32F276D8"
  }
  ```

<a id="section-5-3-6"></a>

### 5.3.6. ModifyIpSegment

Description

You can call this operation to modify a monitored Classless Inter-Domain Routing (CIDR) block with a specified record ID.

Note

You must know the record ID of the monitored CIDR block to be modified before calling

this operation.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set this parameter to <em>ModifyIpSegment</em>. |
| IpId | Integer | Yes | The record ID of the monitored CIDR block to be modified. |
| InfoName | String | Yes | The region to which the CIDR block belongs. For example, a value of DXJF indicates that the CIDR block belongs to the region where the Daxing IDC is located. |
| IpSegmentName | String | Yes | The CIDR block, in x.x.x.x/x format. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample request

  ```text
  https://ddosprivate.[ RegionId].example.com/?Action=ModifyIpSegment
  &InfoName=****
  &InfoType=distribution
  &IpId=11
  &IpSegmentName=192.168.x.x/24
  &<Common request parameters>
        
  ```

- Sample response (JSON format)

  ```json
  {
      "RequestId":"5FFE58AA-355B-4E0E-A742-0BB5554BA959"
  }
        
  ```

<a id="section-5-3-7"></a>

### 5.3.7. CreateDdosPolicy

Description

You can call this operation to add an anti-DDoS policy for a specified IP address or Classless Inter-Domain Routing (CIDR) block.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set this parameter to <em>CreateDdosPolicy</em>. |
| ExternalServiceIP | String | Yes | The IP address or CIDR block to which the anti-DDoS policy applies, in x.x.x.x or x.x.x.x/x format. |
| FlowRate | Integer | Yes | The traffic rate threshold. Unit: Mbit/s.<br>Note The value of this parameter must be greater than 0. |
| HttpRate | Integer | Yes | The HTTP request rate threshold. Unit: queries per second (QPS).<br>Note The value of this parameter must be greater than 50. |
| PackageRate | Integer | Yes | The packet rate threshold. Unit: packets per second (PPS).<br>Note The value of this parameter must be greater than 0. |
| UserId | Long | No | The user ID of the request sender. The parameter is automatically set by the system. |
| UserName | String | Yes | The username of the request sender.The parameter is automatically set by the system. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample request

  ```text
  https://ddosprivate.[ RegionId].example.com/?Action=CreateDdosPolicy
  &ExternalServiceIP=192.168.x.x/32
  &FlowRate=1
  &HttpRate=60
  &PackageRate=1
  &<Common request parameters>
        
  ```

- Sample response (JSON format)

  ```json
  {
      "RequestId":"CA179B61-DD6D-4FE3-A410-CC16AC705DF4"
  }
        
  ```

<a id="section-5-3-8"></a>

### 5.3.8. DescribeDdosPolicies

Description

You can call this operation to query the configured DDoS protection policies.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>DescribeDdosPolicies</em>. |
| CurrentPage | Integer | No | The current page number. |
| PageSize | Integer | No | The maximum number of records displayed on a page. |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| CurrentPage | Integer | The current page number. |
| PageSize | Integer | The maximum number of records displayed on a page. |
| TotalCount | Integer | The total number of pages returned. |
| DdosPolicies | Array | A list of DDoS protection policies. For more information, see the following parameter descriptions. |
| Code | String | The region code of the CIDR block that the DDoS protection policy is applied to. |
| CodeName | String | The region name of the CIDR block that the DDoS protection policy is applied to. |
| DepartmentName | String | The department of the user AliUID that created the DDoS protection policy. |
| ExternalServiceIP | String | The IP address or CIDR block that the DDoS protection policy is applied to. |
| FlowRate | Integer | The bandwidth threshold. Unit: Mbit/s. |
| HttpRate | Integer | The HTTP request threshold. Unit: QPS. |
| PackageRate | Integer | The packet threshold. Unit: PPS. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://ddosprivate.[ RegionId].example.com/?Action=DescribeDdosPolicies
  &CurrentPage=1
  &PageSize=10
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
      "TotalCount":1,
      "PageSize": 10,
      "RequestId": "179E1AA9-1BC2-4A66-9E4B-1640EDDE7D1C",
      "CurrentPage": 1,
      "DdosPolicies": [
          {
              "PackageRate": 200,
              "HttpRate": 0,
              "CodeName":"Daxing data center",
              "ExternalServiceIP": "x.x.x.x/x",
              "DepartmentName": "Department 1",
              "Code": "DD_DXJF",
              "FlowRate": 900,
              "AliUid": 0
          }
      ]
  }
  ```

<a id="section-5-3-9"></a>

### 5.3.9. DeleteDdosPolicy

Description

You can call this operation to delete an anti-DDoS policy for a specified Classless Inter-Domain Routing (CIDR) block.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set this parameter to <em>DeleteDdosPolicy</em>. |
| RegionCode | String | Yes | The ID of the region. For example, cn-hangzhou-env6-d01. |
| ExternalServiceIP | String | Yes | The IP address or CIDR block to which the anti-DDoS policy applies, in x.x.x.x or x.x.x.x/x format. |
| FlowRate | Integer | No | The traffic rate threshold. Unit: Mbit/s.<br>Note The value of this parameter must be greater than 0. |
| HttpRate | Integer | No | The HTTP request rate threshold. Unit: queries per second (QPS).<br>Note The value of this parameter must be greater than 50. |
| PackageRate | Integer | No | The packet rate threshold. Unit: packets per second (PPS).<br>Note The value of this parameter must be greater than 0. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample request

  ```text
  https://ddosprivate.[ RegionId].example.com/?Action=DeleteDdosPolicy
  &ExternalServiceIP=192.168.x.x/24
  &RegionCode=cn-****-env6-d01
  &FlowRate=55
  &HttpRate=55
  &PackageRate=55
  &<Common request parameters>
        
  ```

- Sample response (JSON format)

  ```json
  {
      "RequestId":"8C9B8735-18BA-451B-AE9D-1428554CA360"
  }
        
  ```

<a id="section-5-3-10"></a>

### 5.3.10. ModifyDdosPolicy

Description

You can call this operation to modify a specified anti-DDoS policy.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set this parameter to <em>ModifyDdosPolicy</em>. |
| Distribution | String | Yes | The ID of the region. For example, a value of DXJF indicates the region where the Daxing IDC is located. |
| ExternalServiceIP | String | Yes | The IP address or Classless Inter-Domain Routing (CIDR) block to which the anti-DDoS policy applies, in x.x.x.x or x.x.x.x/x format. |
| FlowRate | Integer | Yes | The traffic rate threshold. Unit: Mbit/s.<br>Note The value of this parameter must be greater than 0. |
| HttpRate | Integer | Yes | The HTTP request rate threshold. Unit: queries per second (QPS).<br>Note The value of this parameter must be greater than 50. |
| PackageRate | Integer | Yes | The packet rate threshold. Unit: packets per second (PPS).<br>Note The value of this parameter must be greater than 0. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample request

  ```text
  https://ddosprivate.[ RegionId].example.com/?Action=ModifyDdosPolicy
  &Distribution=****
  &ExternalServiceIP=192.168.x.x/32
  &FlowRate=1
  &HttpRate=60
  &PackageRate=1
  &<Common request parameters>
        
  ```

- Sample response (JSON format)

  ```json
  {
      "RequestId":"CA179B61-DD6D-4FE3-A410-CC16AC705DF4"
  }
        
  ```

<a id="section-5-3-11"></a>

### 5.3.11. DescribeBlockSwitchs

Description

You can call this operation to query the status of the traffic block switch in anti-DDoS.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>DescribeBlockSwitchs</em>. |
| CurrentPage | Integer | No | The current page number. |
| PageSize | Integer | No | The maximum number of records displayed on a page. |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |
| CurrentPage | Integer | The current page number. |
| PageSize | Integer | The maximum number of records displayed on a page. |
| TotalCount | Integer | The total number of pages returned. |
| BlockSwitchs | Array | The traffic block switch information. For more information, see the following parameter descriptions. |
| Code | String | The code of the block switch, which uniquely identifies a block switch. |
| Description | String | The brief description of the block switch. |
| Id | Integer | The ID of the block switch. |
| Mode | Integer | The status of the block switch. Valid values:<br>• <em>0</em>: indicates disabled.<br>• <em>1</em>: indicates enabled. |
| ModeName | String | The status name of the block switch. Valid values:<br>• <em>Disabled</em><br>• <em>Enabled</em> |
| Name | String | The name of the block switch. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://ddosprivate.[ RegionId].example.com/?Action=DescribeBlockSwitchs
  &CurrentPage=1
  &PageSize=20
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
   "PageSize": 10,
   "RequestId":"95F2F4C8-7623-48B7-A976-30B48F3A25EB",
   "CurrentPage":1,
   "BlockSwitchs":[
    {
     "Description": "test",
     "Mode":0,
     "ModeName":"Disabled",
     "id": 1,
     "Code":"UPGRADE_SWITCH",
     "Name":"Upgrade channel switch"
    },
    {
     "Description":"Automatic upgrade switch",
     "Mode":1,
     "ModeName":"Enabled",
     "Id":2,
     "Code":"AUTO_UPGRADE_SWITH",
     "Name":"Automatic upgrade switch"
    }
   ]
  }
  ```

<a id="section-5-3-12"></a>

### 5.3.12. ModifyBlockSwitchs

Description

You can call this operation to change the status of the block switch in DDoS settings.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>ModifyBlockSwitch</em>. |
| Id | Integer | Yes | The ID of the block switch. |
| Mode | Integer | Yes | The status of the block switch. Valid values:<br>• <em>0</em>: indicates disabled.<br>• <em>1</em>: indicates enabled. |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://ddosprivate.[ RegionId].example.com/?Action=ModifyBlockSwitch
  &Id=1
  &Mode=1
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
   "RequestId":"B7FA97F0-082D-4611-A3C4-867011E2A106" 
  }
  ```

<a id="section-5-3-13"></a>

### 5.3.13. DescribeDdosEvents

Description

You can call this operation to query distributed denial of service (DDoS) events that meet the specified search criteria.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set this parameter to <em>DescribeDdosEvents</em>. |
| CurrentPage | Integer | No | The number of the page to return. |
| PageSize | Integer | No | The number of records to return on each page. |
| StartRow | Integer | No | The sequence number of the first record to return on the current page. |
| Distribution | String | No | The ID of the region. For example, a value of DXJF indicates the region where the Daxing IDC is located. |
| VmIP | String | No | The IP address of the victim server. |
| StartDay | Long | No | The beginning of the time range where data is queried. |
| EndDay | Long | No | The end of the time range where data is queried. |
| SearchReason | String | No | The reason why the DDoS event is triggered. Valid values: <em>bps</em>, <em>pps</em>, and <em>qps</em>.<br>You can query events triggered by multiple reasons. For example, you can enter "bps,pps" to query the DDoS events that are triggered when the traffic rate threshold or the packet transmission rate threshold is exceeded. |
| SelectStatus | String | No | The status of the DDoS event. Valid values:<br>• <em>Scrubbing</em><br>• <em>Scrubbing completed</em> |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| CurrentPage | Integer | The number of the current page returned. |
| PageSize | Integer | The number of records returned on each page. |
| TotalCount | Integer | The total number of returned pages. |
| DdosEvents | Array | The DDoS events. For more information, see the following descriptions. |
| Id | Long | The ID of the event. |
| GmtCreate | Long | The time when the event was created. |
| GmtModified | Long | The time when the event was updated. |
| Aliuid | Long | The AliUid of the asset owner. |
| AttackType | String | The type of the attack.<br>Note In the current version, only the value of <em>defence</em> is supported. |
| Caller | String | The name of the system that calls the operation.<br>Note Currently, the fixed value is <em>beaver_dj</em>, indicating Network Traffic Monitoring System. |
| Category | Integer | The number of the security event category. |
| CategoryName | String | The name of the security event category. |
| VmIp | String | The IP address of the victim server. |
| Code | String | The scrubbing status of the event. Valid values:<br>• <em>Scrubbing</em><br>• <em>Scrubbing completed</em> |
| Bps | Long | The traffic rate threshold. Unit: Mbit/s. |
| Pps | Long | The packet rate threshold. Unit: packets per second (PPS). |
| Qps | Long | The HTTP request rate threshold. Unit: queries per second (QPS). |
| Conn | Integer | The threshold of concurrent connections.<br>Note This response parameter has been deprecated. |
| NewConn | Integer | The threshold of new connections.<br>Note This response parameter has been deprecated. |
| Reason | String | The reason why the event was reported. |
| Distribution | String | The ID of the region. |
| DistributionDisplay | String | The name of the region. |
| IsFinished | Boolean | Indicates whether the attack has finished. Valid values:<br>• <em>true</em>: indicates that the attack has finished.<br>• <em>false</em>: indicates that the attack has not finished. |
| OccurrenceTime | Long | The time when the event occurred. |
| EndTime | Long | The time when the attack finished. |
| LocationAdd | String | The location where the event was added.<br>Note This response parameter is invalid in Apsara Stack. |
| LocationDel | String | The location where the event was canceled.<br>Note This response parameter is invalid in Apsara Stack. |
| Status | Integer | The status of the IP address where the DDoS event occurred. Valid values:<br>• <em>0</em>: indicates that the IP address has not expired.<br>• <em>1</em>: indicates that the IP address has expired. |
| Successful | Integer | Indicates whether the attack succeeds. Valid values:<br>• <em>0</em>: indicates that the attack has failed.<br>• <em>1</em>: indicates that the attack succeeded. |
| NeedIgnore | Integer | Indicates whether you need to ignore the event.Valid values:<br>• <em>0</em>: indicates that you do not need to ignore the event.<br>• <em>1</em>: indicates that the event has been reported repeatedly and you need to ignore the event. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample request

  ```text
  https://ddosprivate.[ RegionId].example.com/?Action=DescribeDdosEvents
  &CurrentPage=1
  &Distribution=DXJF
  $StartDay=1381079107176
  $EndDay=1481079107176
  &PageSize=10
  &<Common request parameters>
  ```

- Sample response (JSON format)

  ```json
  {
   "TotalCount":1,
   "RequestId":"AD525B06-F5F7-4319-94F4-45154D5B0750",
   "DdosEvents":[
    {
     "NewConn":0,
     "Status":0,
     "LocationDel":"nulllocal",
     "Category":21,
     "Bps":5,
     "EndTime":1573233588000,
     "Zone":"default",
     "GmtModified":1484372333000,
     "AttackType":"0",
     "Conn":0,
     "Code":"Scrubbing",
     "DistributionDisplay":"Daxing IDC",
     "Reason":"bps",
     "OccurrenceTime":1473233588000,
     "GmtCreate":1484369068000,
     "Pps":450,
     "Caller":"beaver_dj",
     "Qps":0,
     "Distribution":"am1",
     "LocationAdd":"local",
     "CategoryName":"DDOS_DEFENSE",
     "Id":3,
     "IsFinished":false,
     "NeedIgnore":0
    }
   ],
   "CurrentPage":1
  }
  ```

<a id="section-5-3-14"></a>

### 5.3.14. DescribeFlowAnalysisResult

Description

You can call this operation to query the analysis result of the traffic sent to an IP address.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set this parameter to <em>DescribeFlowAnalysisResult</em>. |
| Distribution | String | Yes | The ID of the region. For example, a value of DXJF indicates the region where the Daxing IDC is located. |
| VmIP | String | Yes | The IP address of the victim server. |
| StartDate | Long | Yes | The beginning of the time range where traffic is analyzed. |
| SearchReason | String | No | The reason why the distributed denial of service (DDoS) event is triggered. Valid values: <em>bps</em>, <em>pps</em>, and <em>qps</em>.<br>You can query events triggered by multiple reasons. For example, you can enter "bps,pps" to query the DDoS events that are triggered when the traffic rate threshold or the packet transmission rate threshold is exceeded. |
| SelectStatus | String | No | The status of the DDoS event. Valid values:<br>• <em>Scrubbing</em><br>• <em>Scrubbing completed</em> |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| TopAttackers | Array | The analysis on the top 10 attackers. For more information, see the following descriptions. |
| Ip | String | The IP address of the attacker. |
| Count | Float | The percentage of attacks launched to the IP address compared to the total attacks. |
| TopProtocols | Array | The analysis on the composition of the attack traffic. For more information, see the following descriptions.<br>Note The traffic composition analysis shows traffic of different protocols, including TCP, ICMP, and UDP. |
| Protocol | String | The protocol. |
| Count | Float | The percentage of the traffic of the specified protocol compared to the total amount of traffic. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample request

  ```text
  https://ddosprivate.[ RegionId].example.com/?Action=DescribeFlowAnalysisResult
  &Distribution=DD_DXJF
  &startDate=123123312000
  &VmIp=x.x.x.x
  &<Common request parameters>
        
  ```

- Sample response (JSON format)

  ```json
  {
      "TopAttackers":["Ip":"x.x.x.x","Count":"1.00"],
      "RequestId":"B2488F1F-930D-4906-AC76-61045B4F1EF2",
      "TopProtocols":["Protocol":"tcp","Count":"1.00"] 
  }
        
  ```

<a id="section-5-3-15"></a>

### 5.3.15. DescribeFlowDetails

Description

You can call this operation to query the detailed traffic information for a specified IP address.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set this parameter to <em>DescribeFlowDetails</em>. |
| Distribution | String | Yes | The ID of the region. For example, a value of DXJF indicates the region where the Daxing IDC is located. |
| VmIP | String | Yes | The IP address of the victim server. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| HttpStatusCode | Integer | The HTTP status code. |
| FlowDetail | Struct | The detailed traffic information. For more information, see the following descriptions. |
| AliUid | Long | The ID of the Alibaba Cloud account. |
| Distribution | String | The ID of the region. |
| DistributionDisplay | String | The name of the region. |
| ExternalServiceIp | String | The IP address or Classless Inter-Domain Routing (CIDR) block. |
| FlowRate | Integer | The flow rate. Unit: Mbit/s. |
| HttpRate | Integer | The HTTP request rate. Unit: queries per second (QPS). |
| PackageRate | Integer | The packet rate. Unit: packets per second (PPS). |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample request

  ```text
  https://ddosprivate.[ RegionId].example.com/?Action=DescribeFlowDetails
  &Distribution=****
  &VmIp=10.0.x.x
  &<Common request parameters>
        
  ```

- Sample response (JSON format)

  ```json
  {
      "RequestId":"8491DBFD-48C0-4E11-B6FC-6F38921244A9",
      "FlowDetail":{
          "PackageRate":200,
          "HttpRate":0,
          "ExternalServiceIP":"10.0.x.x/32",
          "Distribution":"DXJF",
          "DistributionDisplay":"Daxing IDC",
          "FlowRate":900,
          "AliUid":0
      },
      "HttpStatusCode":200 
  }
        
  ```

<a id="section-5-3-16"></a>

### 5.3.16. CancelCleanStatus

Description

You can call this operation to disable DDoS traffic scrubbing for a specified IP address.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set this parameter to <em>CancelCleanStatus</em>. |
| Distribution | String | Yes | The ID of the region. For example, a value of DXJF indicates the region where the Daxing IDC is located. |
| VmIp | String | Yes | The IP address of the instance, in x.x.x.x format. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample request

  ```text
  https://ddosprivate.[ RegionId].example.com/?Action=CancelCleanStatus
  &Distribution=DXJF
  &SourceIp=10.0.x.x
  &VmIp=172.16.x.x
  &<Common request parameters>
        
  ```

- Sample response (JSON format)

  ```json
  {
      "RequestId":"208B016D-4CB9-4A85-96A5-0B8ED1EBF271"
  }
        
  ```

<a id="section-5-3-17"></a>

### 5.3.17. CreateWhiteList

Description

You can call this operation to add a whitelist of trusted IP addresses that are exempt from traffic security monitoring.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set this parameter to <em>CreateWhiteList</em>. |
| Type | Integer | Yes | The type of the whitelist. Valid values:<br>• <em>6</em>: indicates a server brute-force attack whitelist.<br>• <em>12</em>: indicates a BWAF source IP address whitelist.<br>• <em>15</em>: indicates an application attack whitelist. |
| Username | String | No | The username used to add the whitelist. |
| DestinationIp | String | No | The destination IP address.<br>Note When you add a BWAF source IP address whitelist (that is, the Type parameter is set to 12), the DestinationIp parameter must be set to the default value 0.0.0.0. |
| SourceIpStr | String | No | The source IP address. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample request

  ```text
  https://ddosprivate.[ RegionId].example.com/?Action=CreateWhiteList
  &Type=15
  &DestinationIp=192.168.xx.xx
  &SourceIpStr=192.168.xx.xx
  &Username=test
  &<Common request parameters>
  ```

- Sample response (JSON format)

  ```json
  {
      "RequestId":"208B016D-4CB9-4A85-96A5-0B8ED1EBF271"
  }
  ```

<a id="section-5-3-18"></a>

### 5.3.18. DescribeWhiteList

Description

You can call this operation to query the IP addresses that have been added to a whitelist.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set this parameter to <em>DescribeWhiteList</em>. |
| DestinationIp | String | No | The destination IP address. |
| SourceIpStr | String | No | The source IP address. |
| Type | Integer | No | The type of the whitelist. Valid values:<br>• <em>6</em>: indicates a server brute-force attack whitelist.<br>• <em>12</em>: indicates a BWAF source IP address whitelist.<br>• <em>15</em>: indicates an application attack whitelist. |
| Username | String | No | The username. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| CurrentPage | Integer | The number of the current page returned. |
| PageSize | Integer | The number of records returned on each page. |
| TotalCount | Integer | The total number of returned pages. |
| WhiteLists | List | The whitelist records. For more information, see the following descriptions. |
| SourceIp | String | The source IP address. |
| Id | Integer | The ID of the whitelist record. |
| Type | Integer | The type of the whitelist. Valid values:<br>• <em>6</em>: indicates a server brute-force attack whitelist.<br>• <em>12</em>: indicates a BWAF source IP address whitelist.<br>• <em>15</em>: indicates an application attack whitelist. |
| Username | String | The username. |
| DestinationIp | String | The destination IP address. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample request

  ```text
  https://ddosprivate.[ RegionId].example.com/?Action=DescribeWhiteList
  &Type=15
  &DestinationIp=172.16.xx.xx
  &SourceIpStr=172.17.xx.xx
  &Username=test
  &<Common request parameters>
  ```

- Sample response (JSON format)

  ```json
  {
      "CurrentPage":1,
      "PageSize":20,
      "RequestId":"430A3687-B9EC-4F71-B472-EE24ED609863",
      "Success":true,
      "TotalCount":0,
      "WhiteLists":[{
          "DestinationIp":"172.16.xx.xx",
          "Id":6,
          "SourceIp":"172.17.xx.xx",
          "Type":15,
          "Username":"****"
      }]
  }
  ```

<a id="section-5-3-19"></a>

### 5.3.19. DeleteWhiteList

Description

You can call this operation to delete a specified whitelist entry.

Request parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>DeleteWhiteList</em>. |
| Id | Integer | Yes | The ID of the whitelist entry. |

Response parameters

| Name | Type | Description |
| --- | --- | --- |
| RequestId | String | The GUID generated by Alibaba Cloud for the request. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample requests

  ```text
  https://ddosprivate.[ RegionId].example.com/?Action=DeleteWhiteList
  &Id=15
  &<Common request parameters>
  ```

- Sample responses (JSON format)

  ```json
  {
   "RequestId":"208B016D-4CB9-4A85-96A5-0B8ED1EBF271"
  }
  ```

<a id="section-5-3-20"></a>

### 5.3.20. DescribeConsoleDdosPolicies

Description

You can call this operation to obtain the records of anti-DDoS policies, including the system default policies.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set this parameter to <em>DescribeConsoleDdosPolicies</em>. |
| AliUid | Long | Yes | The ID of the Alibaba Cloud account. |
| CurrentPage | Integer | No | The number of the page to return. |
| PageSize | Integer | No | The number of records to return on each page. |
| StartRow | Integer | No | The start row to return. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| CurrentPage | Integer | The number of the current page returned. |
| PageSize | Integer | The number of records returned on each page. |
| TotalCount | Integer | The total number of returned pages. |
| ThresholdList | List | The anti-DDoS policies. For more information, see the following descriptions. |
| DepartmentName | String | The department name of the current user. |
| ExternalServiceIP | String | The IP address or Classless Inter-Domain Routing (CIDR) block.<br>Note A value of default is returned if the system default policy is used. |
| Code | String | The IDC ID corresponding to the CIDR block. |
| CodeName | Sting | The IDC name corresponding to the CIDR block. |
| FlowRate | Integer | The threshold for the traffic rate. Unit: Mbit/s. |
| HttpRate | Integer | The threshold for the HTTP request rate. Unit: queries per second (QPS). |
| PackageRate | Integer | The threshold for the packet rate. Unit: packets per second (PPS). |
| AliUid | Long | The Alibaba Cloud account ID corresponding to the policy. |

Error codes

For more information about the error codes that this operation can return, see Error codes.

Examples

- Sample request

  ```text
  https://ddosprivate.[ RegionId].example.com/?Action=DescribeConsoleDdosPolicies
  &AliUid=****
  &CurrentPage=1
  &PageSize=10
  &SourceIp=xx.xx.xx.xx
  &<Common request parameters>
  ```

- Sample response (JSON format)

  ```json
  {
      "CurrentPage":1,
      "HttpStatusCode":200,
      "PageSize":20,
      "RequestId":"7C3AC882-E5A8-4855-BE77-B6837B695EF1",
      "ThresholdList":[
          {
              "AliUid":151971404963****,
              "Code":"DD_DXJF",
              "CodeName":"DD_DXJF",
              "DepartmentName":"****Cloud",
              "ExternalServiceIP":"1.1.xx.xx/32",
              "FlowRate":1,
              "HttpRate":52,
              "PackageRate":1
          },
          {
              "AliUid":151971404963****,
              "Code":"DD_DXJF",
              "CodeName":"DD_DXJF",
              "DepartmentName":"****Cloud",
              "ExternalServiceIP":"2.2.xx.xx/32",
              "FlowRate":1,
              "HttpRate":51,
              "PackageRate":1
          },
          {
              "AliUid":-1,
              "Code":"DD_DXJF",
              "CodeName":"DD_DXJF",
              "ExternalServiceIP":"default",
              "FlowRate":900,
              "HttpRate":0,
              "PackageRate":200
          }
      ],
      "TotalCount":3
  }
  ```

<a id="section-6"></a>

# 6.Cloud Firewall

<a id="section-6-1"></a>

## 6.1. List of operations by function

The following tables list API operations available for use in Cloud Firewall.

Access control

| API operation | Description |
| --- | --- |
| DescribePolicyPriorUsed | Queries the priority range of access control policies that match specific query conditions. |
| ModifyControlPolicyPosition | Modifies the priority of an access control policy. |
| DescribeControlPolicy | Queries information about all the access control policies that match specific query conditions. |
| AddControlPolic | Creates an access control policy. |
| DeleteControlPolicy | Deletes an access control policy. |
| ModifyControlPolicy | Modifies the configurations of an access control policy. |

Address book

| API operation | Description |
| --- | --- |
| AddAddressBook | Creates an access control address book. Supported address book types are IP address books, Elastic Compute Service (ECS) tag address books, port address books, and domain address books. |
| DeleteAddressBook | Deletes an access control address book. |
| ModifyAddressBook | Modifies an access control address book. |
| DescribeAddressBook | Queries detailed information about access control address books. |

<a id="section-6-2"></a>

## 6.2. Make API requests

<a id="section-6-2-1"></a>

### 6.2.1. Request structure

Apsara Stack Security APIs are based on RPC. This chapter describes the structure of the API requests.

Request structure description

You can send an HTTP request to call an API. The URL of the request must be in the following format:

```text
http://endpoint/?Action=xx&parameters
```

Where:

- `endpoint` : An endpoint is used to call a cloud service. The endpoint for the Web Application Firewall (WAF) service is  `wafprivate.[ RegionId].example.com` .

- `Action` : The operation that you want to perform.

  For example, you can set the value to DescribeFeatures to query the deployed Apsara Stack Security features.

- `parameters` : The request parameters that are contained in the request. Request parameters include common request parameters and custom request parameters. Request parameters must be separated with ampersands (&).

  - Common request parameters are used to indicate information such as the API version and authentication information. For more information, see Common request parameters.

  - For more information about the custom request parameters, see the corresponding operation description.

Example

Call the DescribeFeatures operation to query the deployed Apsara Stack Security features.

```text
https://yundunprivate.[ RegionId].example.com/?Action=DescribeFeatures&AccessKeyId=key-test&Format=JSON&SecureTransport=true&SignatureMethod=HMAC-SHA1&SignatureNonce=15215528852396&SignatureVersion=1.0&SourceIp=1xxxx6&Timestamp=2018-03-02Txxxxxxx&Version=2018-01-16&Signature=xxxx%xxxx%3D
```

API requests are presented in the following easy-to-read form in this document:

```text
https://yundunprivate.[ RegionId].example.com/?Action=DescribeFeatures
&Format=JSON
&Version=2018-05-01
&Signature=xxxx%xxxx%3D
&SignatureMethod=HMAC-SHA1
&SignatureNonce=15215528852396
&SignatureVersion=1.0
&AccessKeyId=key-test
&Timestamp=2012-06-01T12:00:00Z
```

<a id="section-6-2-2"></a>

### 6.2.2. Signature mechanism

Apsara Stack Security authenticates each access request. You need to include a signature for the submitted HTTP or HTTPS request.

API authorization

To ensure the security of your account, we recommend that you use a Resource Access Management (RAM) user to call API operations. Before using a RAM user to call an API operation, you must grant the RAM user the corresponding permission to call the API by creating an authorization policy and attaching the policy to the RAM user.

API signature

To ensure secure calls to the API, Alibaba Cloud authenticates each API request through the signature. When you manually make an API request, you need to use AccessKey Secret to calculate the signature, that is, the hash-based message authentication code (HMAC) value, based on the encoded and sorted request string. For more information, see the definition in RFC 2104.

This topic uses the raw access parameters in the following table to describe how to create an API signature.

| Parameter | Description |
| --- | --- |
| Access point | <code>http://semawaf.[ RegionId].example.com/?</code> |
| API-specific parameters | <code>Action=DescribeFeatures</code> |
| Common parameters (excluding the Signature parameter) | <code>&amp;Timestamp=2016-02-23T12:46:24Z</code><br><code>&amp;Format=JSON</code><br><code>&amp;AccessKeyId=&lt;yourAccessKeyId&gt;</code><br><code>&amp;SignatureMethod=HMAC-SHA1</code><br><code>&amp;SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf</code><br><code>&amp;Version=2018-01-16</code><br><code>&amp;SignatureVersion=1.0</code> |
| AccessKey secret | <code>&lt;yourAccessKeySecret&gt;</code> |

1. Use the request parameters to construct a canonicalized query string.

   Note

   The request parameters include common request parameters (excluding the

   Signature parameter) and API-specific parameters.

   <ol type="i">

   <li>

   Sort the parameters.

   </li>

   </ol>

   Sort the request parameters in alphabetical order.

   <ol type="i" start="2">

   <li>

   Encode the parameters.

   </li>

   </ol>

   Use UTF-8 to URL-encode the parameter names and values. The encoding rules are as follows:

   - Letters, digits, hyphens (-), underscores (_), periods (.), and tildes (~) are not encoded.

   - Other characters are encoded in the %XY format, where XY is the hexadecimal representation of the character in ASCII. For example, the double quotation mark (") is encoded as %22.

   - Extended UTF-8 characters are encoded in the %XY%ZA… format.

   - Note that a space is encoded as %20, instead of a plus sign (+).

   <ol type="i" start="3">

   <li>

   Connect the encoded parameter names and values with equal signs (=).

   </li>

   <li>

   Then, sort the parameter name and value pairs connected by equal signs in alphabetical order,

   </li>

   </ol>

   and connect them with ampersands (&) to produce the canonicalized query string.

2. Use the canonicalized query string to construct the string for signature calculation based on the following rules:

   ```text
   StringToSign=HTTPMethod + “&” + percentEncode(“/”) + ”&” +
   percentEncode(CanonicalizedQueryString)
   ```

3. Calculate the HMAC value of the StringToSign string according to the definition in RFC 2104.

   Note

   The key used for signature calculation is your AccessKey secret adding the

   ampersand (&) (ASCII 38). Secure Hash Algorithm 1 (SHA1) is used as the hash algorithm.

4. Encode the preceding HMAC value into a string based on Base64 encoding rules to obtain the signature value.

   ```text
   LEW8N4y7Uasop******
   ```

5. Set the Signature parameter in the request parameters to this signature value to sign the request.

<a id="section-6-2-3"></a>

### 6.2.3. Common request parameters

The following table describes the common request parameters that are used to indicate information such as the API version and authentication information.

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Version | String | Yes | The API version in the format of YYYY-MM-DD.<br>Set the value to <em>2018-01-16</em>. |
| AccessKeyId | String | Yes | The key ID that Alibaba Cloud assigns to a user for service access. |
| Signature | String | Yes | The signature string. |
| SignatureMethod | String | Yes | The signature method.<br>Set the value to <em>HMAC-SHA1</em>. |
| Timestamp | String | Yes | The timestamp of the request. Follow the ISO 8601 standard to specify the date and use the offset from Coordinated Universal Time (UTC) to specify the time zone.<br>The format is <code> YYYY-MM-</code><code>DDThh:mm:ssZ </code>.<br>For example, 2014-05-26T12:00:00Z indicates 20:00:00 on May 26, 2014, Beijing time. |
| SignatureVersion | String | Yes | The signature algorithm version.<br>Set the value to <em>1.0</em>. |
| SignatureNonce | String | Yes | The unique random number used to prevent network replay attacks. You must use different random numbers for different requests. |
| ResourceOwnerAc count | String | No | The owner account of the resource to be accessed through this API request, that is, the logon username. |
| Format | String | No | The format of the response.<br>Set the value to <em>JSON or XML</em>.<br>Note Default value: XML. |

<a id="section-6-2-4"></a>

### 6.2.4. Response structure

Apsara Stack Security API responses support both the XML and JSON formats. The system always returns a unique identification code RequestId each time you send a request to call an operation, no matter whether the call is successful or not.

Sample responses (XML format)

```xml
<? xml version="1.0" encoding="UTF-8"? >
<! -- The root node of the result -->
<Operation name+Response>
    <! -- Returned request ID -->
    <RequestId>4C467B38-3910-447D-87BC-AC049166F216</RequestId>
    <! -- Returned data -->
</Operation name+Response>
```

Sample responses (JSON format)

```json
{
"RequestId": "4C467B38-3910-447D-87BC-AC049166F216",
/* Returned data */
}
```

<a id="section-6-3"></a>

## 6.3. Access control

<a id="section-6-3-1"></a>

### 6.3.1. DescribePolicyPriorUsed

Queries the priority range of access control policies that match specific query conditions.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribePolicyPri orUsed | The operation that you want to perform. Set the value to DescribePolicyPriorUsed. |
| Direction | String | Yes | in | The traffic direction to which the access control policy applies.<br>Valid values:<br>• in: inbound traffic<br>• out: outbound traffic |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Lang | String | No | zh | The natural language of the request and response.<br>Valid values:<br>• zh: Chinese<br>• en: English |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| End | Integer | 150 | The lowest priority of the access control policy. |
| RequestId | String | CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2837D | The ID of the request. |
| Start | Integer | 1 | The highest priority of the access control policy. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribePolicyPriorUsed
&Direction=in
&<Common request parameters>
```

Sample success responses `XML`  format

```xml
<DescribePolicyPriorUsedResponse>
      <RequestId>CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2837D</RequestId>
      <Start>1</Start>
      <End>150</End>
</DescribePolicyPriorUsedResponse>
```

`JSON`  format

```json
{
    "RequestId": "CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2837D",
    "Start": 1,
    "End": 150
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-6-3-2"></a>

### 6.3.2. ModifyControlPolicyPosition

Modifies the priority of an access control policy.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | ModifyControlPoli cyPosition | The operation that you want to perform. Set the value to ModifyControlPolicyPosition. |
| Direction | String | Yes | in | The direction of the traffic to which the access control policy applies. Valid values:<br>• in: inbound traffic<br>• out: outbound traffic |
| NewOrder | String | Yes | 1 | The new priority of the access control policy. |
| OldOrder | String | Yes | 5 | The original priority of the access control policy. |
| Lang | String | No | zh | The natural language of the request and response. Valid values:<br>• zh: Chinese<br>• en: English |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | 850A84D6-0DE4-4797-A1E8-00090125EEB1 | The ID of the request. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=ModifyControlPolicyPosition
&Direction=in
&NewOrder=1
&OldOrder=5
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<ModifyControlPolicyPosition>
   <RequestId>850A84D6-0DE4-4797-A1E8-00090125EEB1</RequestId>
</ModifyControlPolicyPosition>
```

`JSON`  format

```json
{
 "RequestId":"850A84D6-0DE4-4797-A1E8-00090125EEB1"
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-6-3-3"></a>

### 6.3.3. DescribeControlPolicy

Queries information about all the access control policies.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeControlP olicy | The operation that you want to perform.<br>Set the value to DescribeControlPolicy. |
| CurrentPage | String | Yes | 1 | The page number of the current page.<br>Default value: 1. |
| Direction | String | Yes | in | The direction of the traffic to which the access control policy applies.<br>Valid values:<br>• in: inbound traffic<br>• out: outbound traffic |
| PageSize | String | Yes | 10 | The number of entries to return on each page.<br>Maximum value: 50. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Lang | String | No | zh | The natural language of the request and response.<br>Valid values:<br>• zh: Chinese<br>• en: English |
| Source | String | No | 1.2.3.5 | The source address in the access control policy. Fuzzy match is supported.<br>Valid values:<br>• If the SourceType parameter is set to <code> net </code>, the value of this parameter is the source CIDR block.<br>Example: 10.0.1.0/24.<br>• If the SourceType parameter is set to <code> group </code>, the value of this parameter is the name of the source address book.<br>Example: db_group.<br>• If the SourceType parameter is set to <code> location </code>, the value of this parameter is the source location.<br>Example: beijing.<br>• If the SourceType parameter is not specified, all source addresses are queried.<br>Note The valid values of this parameter depend on the value of the SourceType parameter. |
| Destination | String | No | 1.2.3.0 | The destination address in the access control policy. Fuzzy match is supported.<br>Valid values:<br>• If the DestinationType parameter is set to <code> net </code>, the value of this parameter is the destination CIDR block.<br>Example: 10.0.3.0/24.<br>• If the DestinationType parameter is set to <code> domain </code>, the value of this parameter is the destination domain.<br>Example: aliyun.<br>• If the DestinationType parameter is set to <code> group </code>, the value of this parameter is the name of the destination address book.<br>Example: db_group.<br>• If the DestinationType parameter is set to <code> location </code>, the value of this parameter is the destination location.<br>Example: beijing.<br>• If the DestinationType parameter is not specified, all destination addresses are queried.<br>Note The valid values of this parameter depend on the value of the DestinationType parameter. |
| Description | String | No | test | The description of the access control policy. Fuzzy match is supported.<br>Note If this parameter is not specified, the descriptions of all access control policies are queried. |
| Proto | String | No | TCP | The type of protocol in the access control policy.<br>Valid values:<br>• TCP<br>• UDP<br>• ICMP<br>• ANY, which indicates all types of protocols |
| AclAction | String | No | accept | The action that Cloud Firewall performs on the traffic.<br>Valid values:<br>• accept: allows the traffic.<br>• drop: denies the traffic.<br>• log: monitors the traffic.<br>• If this parameter is not specified, access control policies that specify the preceding actions are queried. |
| Release | String | No | true | Specifies whether the access control policy is enabled. By default, an access control policy is enabled after it is created.<br>Valid values:<br>• true: The access control policy is enabled.<br>• false: The access control policy is disabled. |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| PageNo | String | 1 | The page number of the current page. |
| PageSize | String | 10 | The number of entries returned per page. |
| Policys | Array |  | The information about the access control policy. |
| AclAction | String | accept | The action that Cloud Firewall performs on the traffic.<br>Valid values:<br>• accept: allows the traffic.<br>• drop: denies the traffic.<br>• log: monitors the traffic. |
| AclUuid | String | 00281255-d220-4db1-8f4f-c4df221ad84c | The ID of the access control policy. |
| ApplicationId | String | 10\*\*\* | The application ID in the access control policy. |
| ApplicationNa me | String | HTTP | The type of the application that the access control policy supports.<br>Valid values:<br>• FTP<br>• HTTP<br>• HTTPS<br>• Memcache<br>• MongoDB<br>• MQTT<br>• MySQL<br>• RDP<br>• Redis<br>• SMTP<br>• SMTPS<br>• SSH<br>• SSL<br>• VNC<br>• ANY, which indicates all types of applications |
| Description | String | test | The description of the access control policy. |
| DestPort | String | 80 | The destination port in the access control policy. |
| DestPortGroup | String | my_port_group | The name of the destination port address book in the access control policy. |
| DestPortGroup Ports | List | \[80,443\] | The ports in the destination port address book. |
| DestPortType | String | port | The type of the destination port in the access control policy.<br>Valid values:<br>• port<br>• group: port address book |
| Destination | String | 1.2.3.4/24 | The destination address in the access control policy.<br>Valid values:<br>• If the DestinationType parameter is set to net, the value of this parameter is the destination IP address or CIDR block.<br>Example: 10.0.3.0/24.<br>• If the DestinationType parameter is set to domain, the value of this parameter is the destination domain.<br>Example: aliyuncs.com.<br>• If the DestinationType parameter is set to group, the value of this parameter is the name of the destination address book.<br>Example: db_group.<br>• If the DestinationType parameter is set to location, the value of this parameter is the destination location. For more information about location codes, see AddControlPolicy.<br>Example: \["BJ11", "ZB"\].<br>Note The valid values of this parameter depend on the value of the DestinationType parameter. |
| DestinationGro upCidrs | List | \["1.2.3.0/24", "1.2.3.1/32"\] | The CIDR blocks in the destination address book. |
| DestinationGro upType | String | ip | The type of the destination address book in the access control policy.<br>Valid values:<br>• ip: an address book that includes one or more IP addresses<br>• tag: an address book that includes one or more IP addresses with Elastic Compute Service (ECS) tags<br>• domain: an address book that includes one or more domain names<br>• threat: an address book that includes one or more malicious IP addresses or domain names<br>• backsrc: an address book that includes one or more back-to-origin addresses of Anti-DDoS Pro or Anti-DDoS Premium instances or WAF instances |
| DestinationTyp e | String | net | The type of the destination address in the access control policy.<br>Valid values:<br>• net: destination CIDR block<br>• group: destination address book<br>• domain: destination domain name<br>• location: destination location |
| Direction | String | in | The direction of the traffic to which the access control policy applies.<br>Valid values:<br>• in: inbound traffic<br>• out: outbound traffic |
| DnsResult | String | 1.1.1.1,2.2.2.2 | The DNS resolution result. |
| DnsResultTime | Long | 1579261141 | The timestamp of the DNS resolution result. |
| HitTimes | Integer | 100 | The number of hits for the access control policy. |
| Order | Integer | 1 | The priority of the access control policy.<br>The priority value starts from 1. A smaller value indicates a higher priority.<br>Note The value -1 indicates the lowest priority. |
| Proto | String | TCP | The type of the security protocol in the access control policy.<br>Valid values:<br>• ANY<br>• TCP<br>• UDP<br>• ICMP |
| Release | String | true | Indicates whether the access control policy is enabled. By default, an access control policy is enabled after it is created.<br>Valid values:<br>• true: The access control policy is enabled.<br>• false: The access control policy is disabled. |
| Source | String | 1.2.3.0/24 | The source address in the access control policy.<br>Valid values:<br>• If the SourceType parameter is set to <code> ne</code> <code>t </code>, the value of this parameter is the source CIDR block.<br>Example: 10.0.1.0/24.<br>• If the SourceType parameter is set to <code> gr</code> <code>oup </code>, the value of this parameter is the name of the source address book.<br>Example: db_group.<br>• If the SourcetType parameter is set to location, the value of this parameter is the source location. For more information about location codes, see AddControlPolicy.Example: \["BJ11", "ZB"\]. |
| SourceGroupCid rs | List | \["10.0.0.0/24", "10.0.0.1/32"\] | The CIDR blocks in the source address book. |
| SourceGroupTy pe | String | ip | The type of the source address book in the access control policy.<br>Valid values:<br>• ip: an address book that includes one or more IP addresses<br>• tag: an address book that includes one or more IP addresses with ECS tags<br>• domain: an address book that includes one or more domain names<br>• threat: an address book that includes one or more malicious IP addresses or domain names<br>• backsrc: an address book that includes one or more back-to-origin addresses of Anti-DDoS Pro or Anti-DDoS Premium instances or WAF instances |
| SourceType | String | net | The type of the source address in the access control policy.<br>Valid values:<br>• net: source CIDR block<br>• group: source address book<br>• location: source location |
| RequestId | String | CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2837D | The ID of the request. |
| TotalCount | String | 100 | The total number of the returned access control policies. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribeControlPolicy
&CurrentPage=1
&Direction=in
&PageSize=10
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<DescribeControlPolicyResponse>
  <TotalCount>58</TotalCount>
  <PageNo>1</PageNo>
  <PageSize>10</PageSize>
  <RequestId>A08BC58F-A83D-43EB-BC31-2F0D723929CC</RequestId>
  <Policys>
        <ApplicationName>RDP</ApplicationName>
        <Description>11</Description>
        <HitTimes>0</HitTimes>
        <DestinationType>net</DestinationType>
        <SourceType>net</SourceType>
        <Proto>TCP</Proto>
        <Order>5</Order>
        <ApplicationId>27</ApplicationId>
        <Direction>in</Direction>
        <DestPortType>port</DestPortType>
        <Source>1.1.1.1/32</Source>
        <DestPort>1/1</DestPort>
        <AclAction>accept</AclAction>
        <AclUuid>53d82f0e-9bf1-4761-ab3b-a070b4811234</AclUuid>
        <Destination>1.1.1.1/32</Destination>
        <DnsResult>1.1.1.1,2.2.2.2</DnsResult>
        <DnsResultTime>1579261141</DnsResultTime>
  </Policys>
</DescribeControlPolicyResponse>
```

`JSON`  format

```json
{
    "TotalCount":58,
    "PageNo":1,
    "PageSize":10,
    "RequestId":"A08BC58F-A83D-43EB-BC31-2F0D723929CC",
    "Policys":[
        {
            "DestinationGroupCidrs":[
            ],
            "SourceGroupCidrs":[
            ],
            "ApplicationName":"RDP",
            "Description":"11",
            "HitTimes":0,
            "DestinationType":"net",
            "SourceType":"net",
            "Proto":"TCP",
            "Order":5,
            "ApplicationId":"27",
            "Direction":"in",
            "DestPortType":"port",
            "Source":"1.1.1.1/32",
            "DestPort":"1/1",
            "AclAction":"accept",
            "DestPortGroupPorts":[
            ],
            "AclUuid":"53d82f0e-9bf1-4761-ab3b-a070b4811234",
            "Destination":"1.1.1.1/32",
            "DnsResult": "1.1.1.1,2.2.2.2",
            "DnsResultTime": 1579261141
        }
    ]
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-6-3-4"></a>

### 6.3.4. AddControlPolicy

Creates an access control policy.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| AclAction | String | Yes | accept | The action that Cloud Firewall performs on the traffic. Valid values:<br>• accept: allows the traffic.<br>• drop: denies the traffic.<br>• log: monitors the traffic. |
| Action | String | Yes | AddControlPolicy | The operation that you want to perform. Set the value to AddControlPolicy. |
| ApplicationName | String | Yes | HTTP | The type of applications to which the policy is applied.<br>Valid values:<br>• ANY<br>• HTTP<br>• HTTPS<br>• MySQL<br>• SMTP<br>• SMTPS<br>• RDP<br>• VNC<br>• SSH<br>• Redis<br>• MQTT<br>• MongoDB<br>• Memcache<br>• SSL<br>Note ANY, which indicates all types of applications |
| Description | String | Yes | test | The description of the access control policy. |
| Destination | String | Yes | 1.2.3.4/24 | The destination address in the access control policy.<br>• If the DestinationType parameter is set to net, the value of this parameter is the destination CIDR block. Example: 1.2.3.4/24.<br>• If the DestinationType parameter is set to group, the value of this parameter is the name of the destination address book. Example: db_group.<br>• If the DestinationType parameter is set to domain, the value of this parameter is the destination domain name. Example: \*.aliyuncs.com.<br>• If the DestinationType parameter is set to location, the value of this parameter is the destination location. For more information about the location codes, see the following section. Example: \["BJ11", "ZB"\]. |
| DestinationType | String | Yes | net | The type of the destination address in the access control policy.<br>• net: CIDR block<br>• group: destination address book<br>• domain: destination domain name<br>• location: destination location |
| Direction | String | Yes | in | The direction of the traffic to which the access control policy applies. Valid values:<br>• in: inbound traffic<br>• out: outbound traffic |
| NewOrder | String | Yes | -1 | The priority of the access control policy. The priority value starts from 1.A smaller value indicates a higher priority.<br>Note The value -1 indicates the lowest priority. |
| Proto | String | Yes | TCP | The type of the security protocol in the access control policy. If you are not sure about the protocol type, you can set this parameter to ANY.<br>• ANY<br>• TCP<br>• UDP<br>• ICMP |
| Source | String | Yes | 1.2.3.0/24 | The source address in the access control policy.<br>• If the SourceType parameter is set to net, the value of this parameter is the source CIDR block. Example: 1.2.3.0/24.<br>• If the SourceType parameter is set to group, the value of this parameter is the name of the source address book. Example: db_group.<br>• If the SourceType parameter is set to location, the value of this parameter is the source location. For more information about the location codes, see the following section.Example: \["BJ11", "ZB"\]. |
| SourceType | String | Yes | net | The type of the source address in the access control policy. Valid values:<br>• net: source CIDR block<br>• group: source address book<br>• location: source location |
| DestPort | String | No | 80 | The destination port in the access control policy.<br>Note If the DestPortType parameter is set to port, you must specify this parameter. |
| DestPortGroup | String | No | my_port_group | The name of the destination port address book in the access control policy.<br>Note If the DestPortType parameter is set to group, you must specify this parameter. |
| DestPortType | String | No | port | The type of the destination port in the access control policy. Valid values:<br>• port<br>• group: port address book |
| Lang | String | No | zh | The natural language of the request and response. Valid values:<br>• zh: Chinese<br>• en: English |
| SourceIp | String | No | 1.2.3.5 | The source IP address of the request. |

The following section lists the location codes.

- China: ZD

- Beijing: BJ11

- Tianjin: TJ12

- Hebei: HB13

- Shanxi: SX14

- Liaoning: LN21

- Jilin Province: JL22

- Shanghai: SH31

- Jiangsu: JS32

- Zhejiang: ZJ33

- Anhui: AH34

- Fujian: FJ35

- Jiangxi: JX36

- Shandong: SD37

- Henan: HN41

- Hubei: HB42

- Hunan: HN43

- Guangdong: GD44

- Hainan: HN46

- Chongqing: CQ50

- Sichuan: SC51

- Guizhou: GZ52

- Yunnan: YN53

- Shaanxi: SX61

- Gansu: GS62

- Qinghai: QH63

- Heilongjiang: HLJ23

- Xizang: XZ54

- Guangxi: GX45

- Nei Mongol: NMG15

- Ningxia: NX64

- Xinjiang: XJ65

- Taiwan: TW

- Hong Kong S.A.R: HK

- Macao S.A.R: MO

- Areas outside China: ZB

- Asia (excluding China): ZC

- Europe: EU

- Africa: AF

- North America: NA

- South America: LA

- Oceania: OA

- Antarctica: AQ

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| AclUuid | String | 00281255-d220-4db1-8f4f-c4df221ad84c | The ID of the access control policy. |
| RequestId | String | CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2837D | The ID of the request. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=AddControlPolicy
&AclAction=accept
&ApplicationName=ANY
&Description=demo_rule_1
&Destination=1.2.3.4/24
&DestinationType=net
&Direction=in
&NewOrder=-1
&Proto=TCP
&Source=1.2.3.0/24
&SourceType=net
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<AddControlPolicy>
   <RequestId>CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2837D</RequestId>
   <AclUuid>00281255-d220-4db1-8f4f-c4df221ad84c</AclUuid>
</AddControlPolicy>
```

`JSON`  format

```json
{
 "RequestId":"CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2837D",
 "AclUuid":"00281255-d220-4db1-8f4f-c4df221ad84c"
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-6-3-5"></a>

### 6.3.5. DeleteControlPolicy

Deletes an access control policy.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DeleteControlPoli cy | The operation that you want to perform. Set the value to DeleteControlPolicy. |
| AclUuid | String | Yes | 00281255-d220-4db1-8f4f-c4df221ad84c | The ID of the access control policy.<br>To delete an access control policy, you must specify the ID of the policy. You can call the DescribeControlPolicy operation to obtain the ID. |
| Direction | String | Yes | in | The direction of the traffic to which the access control policy applies.<br>Valid values:<br>• in: inbound traffic<br>• out: outbound traffic |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the traffic. |
| Lang | String | No | zh | The natural language of the request and response.<br>Valid values:<br>• zh: Chinese<br>• en: English |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2837D | The ID of the request. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=DeleteControlPolicy
&AclUuid=00281255-d220-4db1-8f4f-c4df221ad84c
&Direction=in
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<DeleteControlPolicyResponse>
  <RequestId>CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2837D</RequestId>
</DeleteControlPolicyResponse>
```

`JSON`  format

```json
{
    "RequestId": "CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2837D"
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-6-3-6"></a>

### 6.3.6. ModifyControlPolicy

Modifies the configuration of an access control policy.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| AclAction | String | Yes | accept | The action that Cloud Firewall performs on the traffic. Valid values:<br>• accept: allows the traffic.<br>• drop: denies the traffic.<br>• log: monitors the traffic. |
| AclUuid | String | Yes | 00281255-d220-4db1-8f4f-c4df221ad84c | The ID of the access control policy.<br>To modify the access control policy, you must specify the ID of the policy.You can call the DescribeControlPolicy operation to obtain the ID. |
| Action | String | Yes | ModifyControlPoli cy | The operation that you want to perform. Set the value to ModifyControlPolicy. |
| ApplicationName | String | Yes | HTTP | The type of the application that the access control policy supports.<br>Valid values:<br>• ANY<br>• HTTP<br>• HTTPS<br>• MySQL<br>• SMTP<br>• SMTPS<br>• RDP<br>• VNC<br>• SSH<br>• Redis<br>• MQTT<br>• MongoDB<br>• Memcache<br>• SSL<br>Note ANY, which all types of applications |
| Description | String | Yes | test | The description of the access control policy. |
| Destination | String | Yes | 1.2.3.4/24 | The destination address in the access control policy.<br>• If the DestinationType parameter is set to net, this parameter specifies the destination CIDR block. Example: 1.2.3.4/24.<br>• If the DestinationType parameter is set to group, this parameter specifies the name of the destination address book. Example: db_group.<br>• If the DestinationType parameter is set to domain, this parameter specifies the destination domain name. Example: \*.aliyuncs.com.<br>• If the DestinationType parameter is set to location, the value of this parameter is the destination location. Example: \["BJ11", "ZB"\]. |
| DestinationType | String | Yes | net | The type of the destination address in the access control policy. Valid values:<br>• net: destination CIDR block<br>• group: destination address book<br>• domain: destination domain name<br>• location: destination location |
| Direction | String | Yes | in | The direction of the traffic to which the access control policy applies. Valid values:<br>• in: inbound traffic<br>• out: outbound traffic |
| Proto | String | Yes | TCP | The type of the security protocol in the access control policy. If you are not sure about the protocol type, you can set this parameter to ANY. Valid values:<br>• ANY<br>• TCP<br>• UDP<br>• ICMP |
| Source | String | Yes | 1.2.3.0/24 | The source address in the access control policy.<br>• If the SourceType parameter is set to net, the value of this parameter is the source CIDR block. Example: 1.2.3.0/24.<br>• If the SourceType parameter is set to group, the value of this parameter is the name of the source address book. Example: db_group.<br>• If the SourceType parameter is set to location, the value of this parameter is the source location.Example: \["BJ11", "ZB"\]. |
| SourceType | String | Yes | net | The type of the source address in the access control policy. Valid values:<br>• net: source CIDR block<br>• group: source address book<br>• location: source location |
| DestPort | String | No | 80 | The destination port in the access control policy. |
| DestPortGroup | String | No | my_port_group | The name of the destination port address book in the access control policy. |
| DestPortType | String | No | port | The type of the destination port in the access control policy. Valid values:<br>• port<br>• group: port address book |
| Lang | String | No | zh | The natural language of the request and response. Valid values:<br>• zh: Chinese<br>• en: English |
| SourceIp | String | No | 1.2.3.5 | The source IP address of the request. |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2837D | The ID of the request. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=ModifyControlPolicy
&AclAction=accept
&AclUuid=00281255-d220-4db1-8f4f-c4df221ad84c
&ApplicationName=ANY
&Description=demo_rule_1
&Destination=1.2.3.4/24
&DestinationType=net
&Direction=in
&Proto=TCP
&Source=1.2.3.0/24
&SourceType=net
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<ModifyControlPolicy>
   <RequestId>CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2837D</RequestId>
</ModifyControlPolicy>
```

`JSON`  format

```json
{
 "RequestId":"CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2837D"
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-6-3-7"></a>

### 6.3.7. VPC firewalls

<a id="section-6-3-7-1"></a>

#### 6.3.7.1. CreateVpcFirewallControlPolicy

Creates an access control policy to a specific policy group for a VPC firewall.

Note

The VPC firewall instances that are used to protect each Cloud Enterprise Network

(CEN) instance and each Express Connect use different access control policies.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | CreateVpcFirewal lControlPolicy | The operation that you want to perform.<br>Set the value to CreateVpcFirewallControlPolicy. |
| AclAction | String | Yes | accept | The action that the VPC firewall performs on the traffic.<br>Valid values:<br>• accept: allows the traffic.<br>• drop: denies the traffic.<br>• log: monitors the traffic. |
| ApplicationName | String | Yes | HTTP | The type of the application to which the access control policy applies.<br>Valid values:<br>• FTP<br>• HTTP<br>• HTTPS<br>• MySQL<br>• SMTP<br>• SMTPS<br>• RDP<br>• VNC<br>• SSH<br>• Redis<br>• MQTT<br>• MongoDB<br>• Memcache<br>• SSL<br>• ANY, which indicates all types of applications |
| Description | String | Yes | test | The description of the access control policy. |
| Destination | String | Yes | 80 | The destination port in the access control policy.<br>Note If the DestPortType parameter is set to port, you must specify this parameter. |
| DestinationType | String | Yes | net | The type of the destination address in the access control policy.<br>• net: CIDR block<br>• group: destination address book<br>• domain: destination domain name |
| NewOrder | String | Yes | -1 | The priority of the access control policy.<br>The priority value starts from 1. A smaller value indicates a higher priority.<br>Note The value -1 indicates the lowest priority. |
| Proto | String | Yes | TCP | The type of the security protocol in the access control policy.<br>• If you are not sure about the protocol type, you can set this parameter to ANY.<br>• TCP<br>• UDP<br>• ICMP |
| Source | String | Yes | 10.2.3.0/24 | The source address in the access control policy.<br>• If the SourceType parameter is set to <code> net </code>, the value of this parameter is the source CIDR block.<br>Example: 10.2.3.0/24.<br>• If the SourceType parameter is set to <code> group </code>, the value of this parameter is the name of the source address book.<br>Example: db_group. |
| SourceType | String | Yes | net | The type of the source address in the access control policy.<br>Valid values:<br>• net: source CIDR block<br>• group: source address book |
| VpcFirewallId | String | Yes | vfw-a42bbb7b887148 c9\*\*\*\* | The ID of the access control policy group. You can call the DescribeVpcFirewallAclGroupList operation to obtain the ID.<br>Valid values:<br>• If the VPC firewall is used to protect a Cloud Enterprise Network (CEN) instance, the ID of the CEN instance is used. Example: cen-ervw5jbw1234\*\*\*\*\*.<br>• If the VPC firewall is used to protect an Express Connect, the ID of the VPC firewall instance is used.Example: vfw-a42bbb748c91234\*\*\*\*\*. |
| Lang | String | No | zh | The natural language of the request and response. Valid values:<br>• zh: Chinese<br>• en: English |
| DestPort | String | No | 80 | The destination port in the access control policy.<br>Note If the DestPortType parameter is set to <code> port </code>, you must specify this parameter. |
| DestPortType | String | No | net | The type of the destination port in the access control policy.<br>• port<br>• group: port address book |
| DestPortGroup | String | No | my_port_group | The name of the destination port address book in the access control policy.<br>Note If the DestPortType parameter is set to <code> group </code>, you must specify this parameter. |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| AclUuid | String | CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2837D | The ID of the request. |
| RequestId | String | 00281255-d220-4db1-8f4f-c4df221ad84c | The ID of the access control policy. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=CreateVpcFirewallControlPolicy
&VpcFirewallId=vfw-a42bbb7b887148c9****
&AclAction=accept
&ApplicationName=ANY
&Description=demo_rule_1
&Destination=10.2.3.0/24
&DestinationType=net
&NewOrder=-1
&Proto=TCP
&Source=10.2.3.0/24
&SourceType=net
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<CreateVpcFirewallControlPolicyResponse>
  <RequestId>CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2837D</RequestId>
  <AclUuid>00281255-d220-4db1-8f4f-c4d*********</AclUuid>
</CreateVpcFirewallControlPolicyResponse>
```

`JSON`  format

```json
{
    "RequestId": "CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2837D",
    "AclUuid": "00281255-d220-4db1-8f4f-c4d*********"
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-6-3-7-2"></a>

#### 6.3.7.2. DescribeVpcFirewallControlPolicy

Queries the information of the access control policies for a specific VPC firewall.

Note

The VPC firewall instances that are used to protect each Cloud Enterprise Network

(CEN) instance and each Express Connect use different access control policies.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeVpcFirew allControlPolicy | The operation that you want to perform.<br>Set the value to DescribeVpcFirewallControlPolicy. |
| CurrentPage | String | Yes | 1 | The page number of the current page.<br>Default value: 1. |
| PageSize | String | Yes | 10 | The number of entries to return on each page.<br>Maximum value: 50. |
| VpcFirewallId | String | Yes | vfw-a42bbb7b887148 c9\*\*\*\* | The ID of the access control policy group. You can call the DescribeVpcFirewallAclGroupList operation to obtain the ID.<br>Valid values:<br>• If the VPC firewall is used to protect a CEN instance, the ID of the CEN instance is used.<br>Example: cen-ervw0g12b5jbw\*\*\*\*.<br>• If the VPC firewall is used to protect an Express Connect, the ID of the VPC firewall instance is used.<br>Example: vfw-a42bbb7b887148c9\*\*\*\*. |
| Lang | String | No | zh | The natural language of the request and response.<br>Valid values:<br>• zh: Chinese<br>• en: English |
| Source | String | No | 10.0.1.0/24 | The source address in the access control policy. Fuzzy match is supported.<br>Valid values:<br>• If the SourceType parameter is set to <code> net </code>, the value of this parameter is the source CIDR block.<br>Example: 10.0.1.0/24.<br>• If the SourceType parameter is set to <code> group </code>, the value of this parameter is the name of the source address book.<br>Example: db_group.<br>• If the SourceType parameter is not specified, all sources are queried.<br>Note The valid values of this parameter depend on the value of the SourceType parameter. |
| Destination | String | No | 10.0.3.0 | The destination address in the access control policy. Fuzzy match is supported.<br>Valid values:<br>• If the DestinationType parameter is set to <code> net </code>, the value of this parameter is the destination CIDR block.<br>Example: 10.0.3.0/24.<br>• If the DestinationType is set to <code> d</code> <code>omain </code>, the value of this parameter is the destination domain name.<br>Example: aliyun.com.<br>• If the DestinationType parameter is set to <code> group </code>, the value of this parameter is the name of the destination address book.<br>Example: db_group.<br>• If the DestinationType parameter is not specified, all destination addresses are queried.<br>Note The valid values of this parameter depend on the value of the DestinationType parameter. |
| Description | String | No | test | The description of the access control policy. Fuzzy match is supported.<br>Note If this parameter is not specified, the descriptions of all access control policies are queried. |
| Proto | String | No | TCP | The type of the protocol in the access control policy.<br>Valid values:<br>• TCP<br>• UDP<br>• ICMP<br>• ANY, which indicates all types of protocols |
| AclAction | String | No | accept | The action that Cloud Firewall performs on the traffic.<br>Valid values:<br>• accept: allows the traffic.<br>• drop: denies the traffic.<br>• log: monitors the traffic.<br>• If this parameter is not specified, access control policies that specify all the preceding actions are queried. |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| Policys | Array |  | The information of the access control policy. |
| AclAction | String | accept | The action that Cloud Firewall performs on the traffic.<br>Valid values:<br>• accept: allows the traffic.<br>• drop: denies the traffic.<br>• log: monitors the traffic. |
| AclUuid | String | 00281255-d220-4db1-8f4f-c4df221a\*\*\*\* | The ID of the access control policy. |
| ApplicationId | String | 10\*\* | The application ID in the access control policy. |
| ApplicationNa me | String | HTTP | The type of the application that the access control policy supports.<br>Valid values:<br>• HTTP<br>• HTTPS<br>• MySQL<br>• SMTP<br>• SMTPS<br>• RDP<br>• VNC<br>• SSH<br>• Redis<br>• MQTT<br>• MongoDB<br>• Memcache<br>• SSL<br>• ANY, which indicates all types of applications |
| Description | String | test | The description of the access control policy. |
| DestPort | String | 80 | The destination port in the access control policy. |
| DestPortGroup | String | my_port_group | The name of the destination port address book in the access control policy. |
| DestPortGroup Ports | List | \[80,443\] | The ports in the destination port address book. |
| DestPortType | String | port | The type of the destination port in the access control policy.<br>Valid values:<br>• port<br>• group: port address book |
| Destination | String | 10.0.3.0/24 | The destination address in the access control policy.<br>Valid values:<br>• If the DestinationType parameter is set to <code> net </code>, the value of this parameter is the destination CIDR block.<br>Example: 10.0.3.0/24.<br>• If the DestinationType parameter is set to <code> domain </code>, the value of this parameter is the destination domain name.<br>Example: aliyuncs.com.<br>• If the DestinationType parameter is set to <code> group </code>, the value of this parameter is the name of the destination address book.<br>Example: db_group.<br>Note The valid values of this parameter depend on the value of the DestinationType parameter. |
| DestinationGro upCidrs | List | \["10.0.4.0/24", "10.0.0.1/32"\] | The CIDR blocks in the destination address book. |
| DestinationTyp e | String | net | The type of the destination address in the access control policy.<br>Valid values:<br>• net: destination CIDR block<br>• group: destination address book<br>• domain: destination domain name |
| Direction | String | in | The direction of traffic to which the access control policy applies.<br>Valid values:<br>• in: inbound traffic<br>• out: outbound traffic |
| HitTimes | Integer | 100 | The number of hits for the access control policy. |
| Order | Integer | 1 | The priority of the access control policy.<br>The priority value starts from 1. A smaller value indicates a higher priority. The value -1 indicates the lowest priority. |
| Proto | String | TCP | The type of the protocol in the access control policy.<br>Valid values:<br>• TCP<br>• UDP<br>• ICMP<br>• ANY, which indicates all types of protocols |
| Source | String | 10.0.6.0/24 | The source address in the access control policy.<br>Valid values:<br>• If the SourceType parameter is set to <code> n</code> <code>et </code>, the value of this parameter is the source CIDR block.<br>Example: 10.0.6.0/24.<br>• If the SourceType parameter is set to <code> g</code> <code>roup </code>, the value of this parameter is the name of the source address book.<br>Example: db_group.<br>Note The valid values of this parameter depend on the value of the SourceType parameter. |
| SourceGroupCid rs | List | \["10.0.6.0/24", "10.0.0.2/32"\] | The CIDR blocks in the source address book of the access control policy. |
| SourceType | String | net | The type of the source address in the access control policy.<br>Valid values:<br>• net: source CIDR block<br>• group: source address book |
| RequestId | String | CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2837D | The ID of the request. |
| TotalCount | String | 20 | The total number of the access control policies. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribeVpcFirewallControlPolicy
&VpcFirewallId=vfw-a42bbb7b887148c9****
&CurrentPage=1
&PageSize=10
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<DescribeVpcFirewallControlPolicyResponse>
  <TotalCount>1</TotalCount>
  <PageNo>1</PageNo>
  <PageSize>10</PageSize>
  <RequestId>A08BC58F-A83D-43EB-BC31-2F0D723929CC</RequestId>
  <Policys>
        <ApplicationName>HTTP</ApplicationName>
        <Description>11</Description>
        <HitTimes>0</HitTimes>
        <DestinationType>net</DestinationType>
        <SourceType>net</SourceType>
        <Proto>TCP</Proto>
        <Order>5</Order>
        <ApplicationId>27</ApplicationId>
        <DestPortType>port</DestPortType>
        <Source>10.1.1.1/32</Source>
        <DestPort>80/80</DestPort>
        <AclAction>accept</AclAction>
        <AclUuid>53d82f0e-9bf1-4761-ab3b-a070b4811234</AclUuid>
        <Destination>10.2.1.1/32</Destination>
  </Policys>
</DescribeVpcFirewallControlPolicyResponse>
```

`JSON`  format

```json
{
    "TotalCount":1,
    "PageNo":1,
    "PageSize":10,
    "RequestId":"A08BC58F-A83D-43EB-BC31-2F0D723929CC",
    "Policys":[
        {
            "DestinationGroupCidrs":[
            ],
            "SourceGroupCidrs":[
            ],
            "ApplicationName":"HTTP",
            "Description":"11",
            "HitTimes":0,
            "DestinationType":"net",
            "SourceType":"net",
            "Proto":"TCP",
            "Order":5,
            "ApplicationId":"27",
            "DestPortType":"port",
            "Source":"10.1.1.1/32",
            "DestPort":"80/80",
            "AclAction":"accept",
            "DestPortGroupPorts":[
            ],
            "AclUuid":"53d82f0e-9bf1-4761-ab3b-a070b4811234",
            "Destination":"10.2.1.1/32"
        }
    ]
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-6-3-7-3"></a>

#### 6.3.7.3. ModifyVpcFirewallControlPolicy

Modifies the configuration of an access control policy in a specific policy group for a VPC firewall.

Note

The VPC firewall instances that are used to protect each Cloud Enterprise Network

(CEN) instance and each Express Connect use different access control policies.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | ModifyVpcFirewal lControlPolicy | The operation that you want to perform.<br>Set the value to ModifyVpcFirewallControlPolicy. |
| AclAction | String | Yes | accept | The action that Cloud Firewall performs on the traffic.<br>Valid values:<br>• accept: allows the traffic.<br>• drop: denies the traffic.<br>• log: monitors the traffic. |
| AclUuid | String | Yes | 00281255-d220-4db1-8f4f-c4df221ad84c | The ID of the access control policy.<br>To modify the configuration of an access control policy, you must provide the ID of the policy. You can call the DescribeVpcFirewallControlPolicy operation to obtain the ID. |
| ApplicationName | String | Yes | HTTP | The type of applications to which the access control policy applies.<br>Valid values:<br>• ANY<br>• FTP<br>• HTTP<br>• HTTPS<br>• MySQL<br>• SMTP<br>• SMTPS<br>• RDP<br>• VNC<br>• SSH<br>• Redis<br>• MQTT<br>• MongoDB<br>• Memcache<br>• SSL<br>• ANY, which indicates all types of applications |
| Description | String | Yes | test | The description of the access control policy. |
| Destination | String | Yes | 10.2.3.0/24 | The destination address in the access control policy.<br>• If the DestinationType parameter is set to <code> net </code>, the value of this parameter is the destination CIDR block.<br>Example: 10.2.3.0/24.<br>• If the DestinationType parameter is set to <code> group </code>, the value of this parameter is the name of the destination address book.<br>Example: db_group.<br>• If the DestinationType parameter is set to <code> domain </code>, the value of this parameter is the destination domain name.<br>Example: \*.aliyuncs.com. |
| DestinationType | String | Yes | net | The type of the destination address in the access control policy.<br>Valid values:<br>• net: CIDR block<br>• group: destination address book<br>• domain: destination domain name |
| Proto | String | Yes | TCP | The type of the security protocol in the access control policy.<br>Valid values:<br>• ANY, which indicates all types of protocols<br>• TCP<br>• UDP<br>• ICMP |
| Source | String | Yes | 10.2.4.0/24 | The source address in the access control policy.<br>Valid values:<br>• If the SourceType parameter is set to <code> net </code>, the value of this parameter is the source CIDR block.<br>Example: 10.2.4.0/24<br>• If the SourceType parameter is set to <code> group </code>, the value of this parameter is the name of the source address book.<br>Example: db_group |
| SourceType | String | Yes | net | The type of the source address in the access control policy.<br>Valid values:<br>• net: source CIDR block.<br>• group: source address book |
| VpcFirewallId | String | Yes | vfw-a42bbb7b887148 c9\*\*\*\* | The ID of the access control policy group. You can call the DescribeVpcFirewallAclGroupList operation to obtain the ID.<br>• If the VPC firewall is used to protect a Cloud Enterprise Network (CEN) instance, the ID of the CEN instance is used.<br>Example: cen-ervw0g12b5jbw\*\*\*\*.<br>• If the VPC firewall is used to protect an Express Connect, the ID of the VPC firewall instance is used.<br>Example: vfw-a42bbb7b887148c9\*\*\*\*. |
| Lang | String | No | zh | The natural language of the request and response.<br>Valid values:<br>• zh: Chinese<br>• en: English |
| DestPort | String | No | 80 | The destination port in the access control policy. |
| DestPortType | String | No | port | The type of the destination port in the access control policy.<br>• port<br>• group: port address book |
| DestPortGroup | String | No | my_port_group | The name of the destination port address book in the access control policy. |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2837D | The ID of the request. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=ModifyVpcFirewallControlPolicy
&VpcFirewallId=vfw-a42bbb7b887148c9****
&AclAction=accept
&AclUuid=00281255-d220-4db1-8f4f-c4df221ad84c
&ApplicationName=ANY
&Description=demo_rule_1
&Destination=10.2.3.0/24
&DestinationType=net
&Proto=TCP
&Source=10.2.4.0/24
&SourceType=net
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<ModifyVpcFirewallControlPolicyResponse>
  <RequestId>CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2837D</RequestId>
</ModifyVpcFirewallControlPolicyResponse>
```

`JSON`  format

```json
{
    "RequestId": "CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2837D"
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-6-3-7-4"></a>

#### 6.3.7.4. ModifyVpcFirewallControlPolicyPosition

Modifies the priority of an access control policy in a specific policy group for a VPC firewall.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | ModifyVpcFirewal lControlPolicyPosi tion | The operation that you want to perform.<br>Set the value to ModifyVpcFirewallControlPolicyPo sition. |
| NewOrder | String | Yes | 1 | The new priority of the access control policy. |
| OldOrder | String | Yes | 5 | The original priority of the access control policy. |
| VpcFirewallId | String | Yes | vfw-a42bbb7b887148 c9\*\*\*\* | The ID of the access control policy group. You can call the DescribeVpcFirewallAclGroupList operation to obtain the ID.<br>Valid values:<br>• If the VPC firewall is used to protect a Cloud Enterprise Network (CEN) instance, the ID of the CEN instance is used.<br>Example: cen-ervw0g12b5jbw\*\*\*\*.<br>• If the VPC firewall is used to protect an Express Connect, the ID of the VPC firewall instance is used.<br>Example: vfw-a42bbb7b887148c9\*\*\*\*. |
| Lang | String | No | zh | The natural language of the request and response.<br>Valid values:<br>• zh: Chinese<br>• en: English |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | 850A84D6-0DE4-4797-A1E8-00090125EEB1 | The ID of the request. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=ModifyVpcFirewallControlPolicyPosition
&VpcFirewallId=vfw-a42bbb7b887148c9****
&NewOrder=1
&OldOrder=5
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<ModifyVpcFirewallControlPolicyPositionResponse>
  <RequestId>850A84D6-0DE4-4797-A1E8-00090125EEB1</RequestId>
</ModifyVpcFirewallControlPolicyPositionResponse>
```

`JSON`  format

```json
{
    "RequestId": "850A84D6-0DE4-4797-A1E8-00090125EEB1"
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-6-3-7-5"></a>

#### 6.3.7.5. DeleteVpcFirewallControlPolicy

Deletes an access control policy from a specific policy group for a VPC firewall.

Note

The VPC firewall instances that are used to protect each Cloud Enterprise Network

(CEN) instance and each Express Connect use different access control policies.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DeleteVpcFirewal lControlPolicy | The operation that you want to perform.<br>Set the value to DeleteVpcFirewallControlPolicy. |
| AclUuid | String | Yes | 00281255-d220-4db1-8f4f-c4df2214\*\*\*\* | The ID of the access control policy.<br>To delete an access control policy, you must specify the ID of the policy. You can call the DescribeVpcFirewallControlPolicy operation to obtain the ID. |
| VpcFirewallId | String | Yes | vfw-a42bbb7b887148 c91\*\*\*\* | The ID of the access control policy group. You can call the DescribeVpcFirewallAclGroupList operation to obtain the ID.<br>Valid values:<br>• If the VPC firewall is used to protect a CEN instance, the ID of the CEN instance is used.<br>Example: cen-ervw0g12b5jbw\*\*\*\*.<br>• If the VPC firewall is used to protect an Express Connect, the ID of the VPC firewall instance is used.<br>Example: vfw-a42bbb7b887148c9\*\*\*\*. |
| Lang | String | No | zh | The natural language of the request and response. Valid values:<br>• zh: Chinese<br>• en: English |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2837D | The ID of the request. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=DeleteVpcFirewallControlPolicy
&VpcFirewallId=vfw-a42bbb7b887148c9****
&AclUuid=00281255-d220-4db1-8f4f-c4df221ad84c
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<DeleteVpcFirewallControlPolicyResponse>
  <RequestId>CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2837D</RequestId>
</DeleteVpcFirewallControlPolicyResponse>
```

`JSON`  format

```json
{
    "RequestId": "CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2837D"
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-6-3-7-6"></a>

#### 6.3.7.6. DescribeVpcFirewallPolicyPriorUsed

Queries the priority range of the access control policies in a specific policy group for a VPC firewall.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeVpcFirew allPolicyPriorUsed | The operation that you want to perform.<br>Set the value to DescribeVpcFirewallPolicyPriorUse d. |
| VpcFirewallId | String | Yes | vfw-a42bbb7b887148 c9\*\*\*\* | The ID of the access control policy group. You can call the DescribeVpcFirewallAclGroupList operation to obtain the ID.<br>Valid values:<br>• If the VPC firewall is used to protect a Cloud Enterprise Network (CEN) instance, the ID of the CEN instance is used.<br>Example: cen-ervw0g12b5jbw\*\*\*\*.<br>• If the VPC firewall is used to protect an Express Connect, the ID of the VPC firewall instance is used.<br>Example: vfw-a42bbb7b887148c9\*\*\*\*. |
| Lang | String | No | zh | The natural language of the request and response.<br>Valid values:<br>• zh: Chinese<br>• en: English |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| End | Integer | 150 | The lowest priority for the access control policy. |
| RequestId | String | CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2837D | The ID of the request. |
| Start | Integer | 1 | The highest priority for the access control policy. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribeVpcFirewallPolicyPriorUsed
&VpcFirewallId=vfw-a42bbb7b887148c9****
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<DescribeVpcFirewallPolicyPriorUsedResponse>
  <RequestId>CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2837D</RequestId>
  <Start>1</Start>
  <End>150</End>
</DescribeVpcFirewallPolicyPriorUsedResponse>
```

`JSON`  format

```json
{
    "RequestId": "CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2837D",
    "Start": 1,
    "End": 150
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-6-3-7-7"></a>

#### 6.3.7.7. DescribeVpcFirewallAclGroupList

Queries information about all access control policy groups for a VPC firewall.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeVpcFirew allAclGroupList | The operation that you want to perform.<br>Set the value to DescribeVpcFirewallAclGroupList. |
| Lang | String | No | zh | The natural language of the request and response. Valid values:<br>• zh: Chinese<br>• en: English |
| FirewallConfigure Status | String | No | configured | Specifies whether VPC firewalls are configured.<br>• notconfigured: VPC firewalls are not configured.<br>• configured: VPC firewalls are configured.<br>• If you do not specify this parameter, all access control policy groups are queried. |
| CurrentPage | String | No | 1 | The page number of the current page.<br>Default value: 1 |
| PageSize | String | No | 10 | The number of entries to return on each page.<br>Maximum value: 50. |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| AclGroupList | Array |  | The information about the access control policy group. |
| AclGroupId | String | vfw-a42bbb7b887148c9\* \*\*\* | The ID of the access control policy group.You can call the DescribeVpcFirewallAclGroupList operation to obtain the ID.<br>Valid values:<br>• If the VPC firewall is used to protect a Cloud Enterprise Network (CEN) instance, the ID of the CEN instance is used.<br>Example: cen-ervw0g12b5jbw\*\*\*\*.<br>• If the VPC firewall is used to protect an Express Connect, the ID of the VPC firewall instance is used.<br>Example: vfw-a42bbb7b887148c9\*\*\*\*. |
| AclGroupName | String | group_test | The name of the access control policy group.<br>• If the VPC firewall is used to protect a CEN instance, the name of the CEN instance is used.<br>• If the VPC firewall is used to protect an Express Connect, the name of the VPC firewall is used. |
| RequestId | String | CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2837D | The ID of the request. |
| TotalCount | Integer | 1 | The total number of access control policy groups. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribeVpcFirewallAclGroupList
&FirewallConfigureStatus=configured
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<DescribeVpcFirewallAclGroupListResponse>
  <TotalCount>1</TotalCount>
  <AclGroupList>
        <AclGroupId>vfw-a42bbb7b887148c9****</AclGroupId>
        <AclGroupName>group_test</AclGroupName>
  </AclGroupList>
</DescribeVpcFirewallAclGroupListResponse>
```

`JSON`  format

```json
{"TotalCount":1,"AclGroupList":[{"AclGroupId":"vfw-a42bbb7b887148c9****","AclGroupName":"group_test"}]}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-6-3-7-8"></a>

#### 6.3.7.8. ResetVpcFirewallRuleHitCount

Resets the count on hits of an access control policy in a specific policy group for a VPC firewall.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | ResetVpcFirewall RuleHitCount | The operation that you want to perform.<br>Set the value to ResetVpcFirewallRuleHitCount. |
| AclUuid | String | Yes | 00281255-d220-4db1-8f4f-c4df221ad84c | The ID of the access control policy.<br>To delete an access control policy, you must specify the ID of the policy. You can call the DescribeVpcFirewallControlPolicy operation to obtain the ID. |
| Lang | String | No | zh | The natural language of the request and response.<br>Valid values:<br>• zh: Chinese<br>• en: English |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2837D | The ID of the request. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=ResetVpcFirewallRuleHitCount
&AclUuid=00281255-d220-4db1-8f4f-c4df221a1234
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<ResetVpcFirewallRuleHitCountResponse>
  <RequestId>CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2837D</RequestId>
</ResetVpcFirewallRuleHitCountResponse>
```

`JSON`  format

```json
{
    "RequestId": "CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2837D"
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-6-4"></a>

## 6.4. Firewall switch

<a id="section-6-4-1"></a>

### 6.4.1. PutEnableFwSwitch

Turns on a firewall switch.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | PutEnableFwSwit ch | The operation that you want to perform.<br>Set the value to PutEnableFwSwitch. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Lang | String | No | zh | The natural language of the request and response. Valid values:<br>• zh: Chinese<br>• en: English |
| IpaddrList.N | RepeatLi st | No | \["1.2.3.4","5.6.7.8 "\] | The list of IP addresses. |
| RegionList.N | RepeatLi st | No | \["cn-hangzhou","cn-shanghai"\] | The list of regions. |
| ResourceTypeList.N | RepeatLi st | No | \["EcsPublicIp","Na tEip"\] | The list of asset types.<br>Valid values:<br>• BastionHostIP: the IP address of a bastion host<br>• EcsEIP: the EIP of an ECS instance<br>• EcsPublicIP: the public IP address of an ECS instance<br>• EIP<br>• EniEIP: the EIP of an ENI<br>• NatEIP: the EIP of a NAT gateway<br>• SlbEIP: the EIP of an SLB instance<br>• SlbPublicIP: the public IP address of an SLB instance<br>• NatPublicIP: the public IP address of a NAT gateway<br>• HAVIP: the HA VIP |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | B2841452-CB8D-4F7D-B247-38E1CF7334F8 | The ID of the request. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=PutEnableFwSwitch&IpaddrList=["1.2.3.4","5.6.7.8"]
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<RequestId>B2841452-CB8D-4F7D-B247-38E1CF7334F8</RequestId>
```

`JSON`  format

```json
{
    "RequestId":"B2841452-CB8D-4F7D-B247-38E1CF7334F8"
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-6-4-2"></a>

### 6.4.2. PutDisableFwSwitch

Turns off a firewall switch.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | PutDisableFwSwit ch | The operation that you want to perform.<br>Set the value to PutDisableFwSwitch. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Lang | String | No | zh | The natural language of the request and response. Valid values:<br>• zh: Chinese<br>• en: English |
| IpaddrList.N | RepeatLi st | No | \["1.2.3.4","5.6.7.8 "\] | The list of IP addresses. |
| RegionList.N | RepeatLi st | No | \["cn-hangzhou","cn-shanghai"\] | The list of regions. |
| ResourceTypeList.N | RepeatLi st | No | \["EcsPublicIp","Na tEip"\] | The list of asset types.<br>Valid values:<br>• BastionHostIP: the IP address of a bastion host<br>• EcsEIP: the EIP of an ECS instance<br>• EcsPublicIP: the public IP address of an ECS instance<br>• EIP<br>• EniEIP: the EIP of an ENI<br>• NatEIP: the EIP of a NAT gateway<br>• SlbEIP: the EIP of an SLB instance<br>• SlbPublicIP: the public IP address of an SLB instance<br>• NatPublicIP: the public IP address of a NAT gateway<br>• HAVIP: the HA VIP |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | B2841452-CB8D-4F7D-B247-38E1CF7334F8 | The ID of the request. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=PutDisableFwSwitch&IpaddrList=["1.2.3.4","5.6.7.8"]
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<RequestId>B2841452-CB8D-4F7D-B247-38E1CF7334F8</RequestId>
```

`JSON`  format

```json
{
    "RequestId":"B2841452-CB8D-4F7D-B247-38E1CF7334F8"
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-6-4-3"></a>

### 6.4.3. PutEnableAllFwSwitch

Turns on all firewall switches.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | PutEnableAllFwS witch | The operation that you want to perform.<br>Set the value to PutEnableAllFwSwitch. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Lang | String | No | zh | The natural language of the request and response. Valid values:<br>• zh: Chinese<br>• en: English |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | B2841452-CB8D-4F7D-B247-38E1CF7334F8 | The ID of the request. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=PutEnableAllFwSwitch
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<RequestId>B2841452-CB8D-4F7D-B247-38E1CF7334F8</RequestId>
```

`JSON`  format

```json
{
    "RequestId":"B2841452-CB8D-4F7D-B247-38E1CF7334F8"
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-6-4-4"></a>

### 6.4.4. PutDisableAllFwSwitch

Turns off all firewall switches.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | PutDisableAllFwS witch | The operation that you want to perform.<br>Set the value to PutDisableAllFwSwitch. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| Lang | String | No | zh | The natural language of the request and response. Valid values:<br>• zh: Chinese<br>• en: English |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | B2841452-CB8D-4F7D-B247-38E1CF7334F8 | The ID of the request. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=PutDisableAllFwSwitch
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<RequestId>B2841452-CB8D-4F7D-B247-38E1CF7334F8</RequestId>
```

`JSON`  format

```json
{
    "RequestId":"B2841452-CB8D-4F7D-B247-38E1CF7334F8"
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-6-5"></a>

## 6.5. Address books

<a id="section-6-5-1"></a>

### 6.5.1. AddAddressBook

Creates an address book for access control. Supported address book types are IP address books, Elastic Compute Service (ECS) tag address books, port address books, and domain address books.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | AddAddressBook | The operation that you want to perform. Set the value to AddAddressBook. |
| Description | String | Yes | DEMO address book | The description of the address book. |
| GroupName | String | Yes | demo_address_b ook | The name of the address book. |
| GroupType | String | Yes | ip | The type of the address book. Valid values:<br>• ip: IP address book<br>• domain: domain address book<br>• port: port address book<br>• tag: ECS tag address book |
| AddressList | String | No | 1.2.3.4/32, 1.2.3.0/24 | The addresses you want to add to the address book. Separate multiple addresses with commas (,).<br>Note If the GroupType parameter is set to ip, port or domain, this parameter is required.<br>• If the GroupType parameter is set to ip, the value of this parameter is the IP addresses. Example: 1.2.3.4/32,1.2.3.0/24.<br>• If the GroupType parameter is set to port, the value of this parameter is the ports or port ranges. Example: 80,100/200.<br>• If the GroupType parameter is set to domain, the value of this parameter is the domain names. Example: demo1.aliyun.com,demo2.aliyun.co m. |
| AutoAddTagEcs | String | No | 1 | Specifies whether to automatically add public IP addresses of ECS instances to the address book if they match the specific tags. Valid values:<br>• 1: yes<br>• 0: no |
| Lang | String | No | zh | The natural language of the request and response. Valid values:<br>• zh: Chinese<br>• en: English |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| TagList.N.TagKey | String | No | key1 | The key of ECS tag N you want to match. |
| TagList.N.TagVal ue | String | No | value1 | The value of ECS tag N you want to match. |
| TagRelation | String | No | and | The logical relation among ECS tags you want to mach. Valid values:<br>• and: Only the public IP addresses of ECS instances that match all the specific tags can be added to the address book.<br>• or: The public IP addresses of ECS instances that match any of the specific tags can be added to the address book. |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| GroupUuid | String | f04ac7ce-628b-4cb7-be61-310222b718e8 | The ID of the returned address book |
| RequestId | String | CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2837D | The ID of the request. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=AddAddressBook
&Description=DEMO address book
&GroupName=demo_address_book
&GroupType=ip
&AddressList=1.2.3.4/32,1.2.3.0/24
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<AddAddressBook>
      <RequestId>B2841452-CB8D-4F7D-B247-38E1CF7334F8</RequestId>
      <GroupUuid>0580bbd0-24cd-47ae-9e5a-f5a099251e32</GroupUuid>
    </AddAddressBook>
```

`JSON`  format

```json
{
    "RequestId":"B2841452-CB8D-4F7D-B247-38E1CF7334F8",
    "GroupUuid":"0580bbd0-24cd-47ae-9e5a-f5a099251e32"
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-6-5-2"></a>

### 6.5.2. DeleteAddressBook

Deletes an address book for access control.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DeleteAddressBo ok | The operation that you want to perform. Set the value to DeleteAddressBook. |
| GroupUuid | String | Yes | 0657ab9d-fe8b-4174-b2a6-6baf358ea4ad | The ID of the address book.<br>To delete the address book, you must specify the ID of the address book. You can call the DescribeAddressBook operation to obtain the ID. |
| Lang | String | No | zh | The natural language of the request and response. Valid values:<br>• zh: Chinese<br>• en: English |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2837D | The ID of the request. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=DeleteAddressBook
&GroupUuid=0657ab9d-fe8b-4174-b2a6-6baf358ea4ad
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<DeleteAddressBook>
   <RequestId>850A84D6-0DE4-4797-A1E8-00090125EEB1</RequestId>
</DeleteAddressBook>
```

`JSON`  format

```json
{
 "RequestId":"850A84D6-0DE4-4797-A1E8-00090125EEB1"
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-6-5-3"></a>

### 6.5.3. ModifyAddressBook

Modifies an address book for the access control.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | ModifyAddressBo ok | The operation that you want to perform. Set the value to ModifyAddressBook. |
| Description | String | Yes | DEMO address book | The description of the address book. |
| GroupName | String | Yes | demo_address_b ook | The name of the address book. |
| GroupUuid | String | Yes | 0657ab9d-fe8b-4174-b2a6-6baf358ea4ad | The ID of the address book.<br>To modify the address book, you must specify the ID of the address book. You can call the DescribeAddressBook operation to obtain the ID. |
| AddressList | String | No | 1.1.1.1/32, 2.2.2.0/24 | The addresses you want to add to the address book. Separate multiple addresses with commas (,).<br>Note If the GroupType parameter is set to ip, port, or domain, this parameter is required.<br>• If the GroupType parameter is set to ip, the value of this parameter is the IP addresses. Example: 1.2.3.4/32,1.2.3.0/24.<br>• If the GroupType parameter is set to port, the value of this parameter is the ports or port ranges. Example: 80,100/200.<br>• If the GroupType parameter is set to domain, the value of this parameter is the domain names. Example: demo1.aliyun.com,demo2.aliyun.co m. |
| AutoAddTagEcs | String | No | 1 | Specifies whether to automatically add the public IP addresses of ECS instances to the address book if they match the specific tags. Valid values:<br>• 1: yes<br>• 0: no |
| Lang | String | No | zh | The natural language of the request and response. Valid values:<br>• zh: Chinese<br>• en: English |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| TagList.N.TagKey | String | No | key1 | The key of ECS tag N you want to match. |
| TagList.N.TagVal ue | String | No | value1 | The value of ECS tag N you want to match. |
| TagRelation | String | No | and | The logical relation among ECS tags.Valid values:<br>• and: Only the public IP addresses of ECS instances that match all the specific tags can be added to the address book.<br>• or: The public IP addresses of ECS instances that match any of the specific tags can be added to the address book. |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| RequestId | String | CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2837D | The ID of the request. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=ModifyAddressBook
&GroupUuid=0657ab9d-fe8b-4174-b2a6-6baf358ea4ad
&Description=DEMO address book
&GroupName=demo_address_book
&GroupType=ip
&AddressList=1.1.1.1/32,2.2.2.0/24
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<ModifyAddressBook>
      <RequestId>CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2837D</RequestId>
</ModifyAddressBook>
```

`JSON`  format

```json
{
    "RequestId":"CBF1E9B7-D6A0-4E9E-AD3E-2B47E6C2837D"
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-6-5-4"></a>

### 6.5.4. DescribeAddressBook

Queries the details of an address book for the access control.

Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Action | String | Yes | DescribeAddressB ook | The operation that you want to perform. Set the value to DescribeAddressBook. |
| ContainPort | String | No | 80 | Details about the address book that contains ports.This parameter only takes effect when the GroupType parameter is set to port. |
| CurrentPage | String | No | 1 | The number of the page to return.Default value: 1. |
| GroupType | String | No | ip | The type of the address book. Valid values:<br>• ip: IP address book<br>• domain: domain address book<br>• port: port address book<br>• tag: ECS tag address book |
| Lang | String | No | zh | The natural language of the request and response. Valid values:<br>• zh: Chinese<br>• en: English |
| PageSize | String | No | 50 | The number of entries to return on each page. Maximum value: 50. |
| Query | String | No | 1.2.3.0 | The query condition that specifies the address book. |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |

Response parameters

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| Acls | Array |  | The information about the address book. |
| AddressList | List | \[ "1.2.3.4/32", "0.0.0.0/0" \] | The addresses in the address book. |
| AddressListCou nt | Integer | 2 | The number of addresses in the address book. |
| AutoAddTagEc s | Integer | 1 | Indicates whether to automatically add the public IP addresses of ECS instances to the address book if they match the specific tags.Valid values:<br>• 1: yes<br>• 0: no |
| Description | String | DEMO address book | The description of the address book. |
| Global | Integer | 0 | Indicates whether the address book is global. Valid values:<br>• 1: yes<br>• 0: no |
| GroupName | String | demo_address_boo k | The name of the address book. |
| GroupType | String | ip | The type of the address book. Valid values:<br>• ip: IP address book<br>• domain: domain address book<br>• port: port address book<br>• tag: ECS tag address book |
| GroupUuid | String | f04ac7ce-628b-4cb7-be61-310222b718e8 | The ID of the address book. |
| ReferenceCount | Integer | 3 | The number of times the address book is referenced. |
| TagList | Array |  | Details about the ECS tags that can be automatically added to the address book. |
| TagKey | String | key1 | The key of ECS tag N you want to match. |
| TagValue | String | value1 | The value of ECS tag N you want to match. |
| TagRelation | String | and | The logical relation among ECS tags. Valid values:<br>• and: Only the public IP addresses of ECS instances that match all the specific tags can be added to the address book.<br>• or: The public IP addresses of ECS instances that match any of the specific tags can be added to the address book. |
| PageNo | String | 1 | The number of the current page. |
| PageSize | String | 10 | The number of entries returned per page. |
| RequestId | String | B36F150A-1E27-43AA-B72C-D2AC712F09DA | The ID of the request. |
| TotalCount | String | 100 | The number of address books. |

Examples

Sample requests

```text
http(s)://[Endpoint]/?Action=DescribeAddressBook
&<Common request parameters>
```

Sample success responses

`XML`  format

```xml
<DescribeAddressBook>
   <TotalCount>123</TotalCount>
   <PageSiNo>1</PageSiNo>
   <PageSize>1</PageSize>
   <RequestId>B36F150A-1E27-43AA-B72C-D2AC712F09DA</RequestId>
   <Acls>
      <Description>9-3 IP address book</Description>
      <GroupType>ip</GroupType>
      <AddressList>1.2.3.4/32</AddressList>
      <AddressList>0.0.0.0/0</AddressList>
      <GroupName>9-3 IP address book</GroupName>
      <AutoAddTagEcs>0</AutoAddTagEcs>
      <TagValue></TagValue>
      <TagRelation></TagRelation>
      <ReferenceCount>0</ReferenceCount>
      <TagKey></TagKey>
      <AddressListCount>2</AddressListCount>
      <GroupUuid>a3c5e-018e-4c08-bea8-eafc95d1a54e</GroupUuid>
      <Global>0</Global>
   </Acls>
</DescribeAddressBook>
```

`JSON`  format

```json
{
 "TotalCount":123,
 "PageSize":1,
 "RequestId":"B36F150A-1E27-43AA-B72C-D2AC712F09DA",
 "Acls":[
  {
   "Description":"9-3 IP address book",
   "GroupType":"ip",
   "AddressList":[
    "1.2.3.4/32",
    "0.0.0.0/0"
   ],
   "GroupName":"9-3 IP address book",
   "AutoAddTagEcs":0,
   "TagValue":"",
   "TagRelation":"",
   "TagList":[],
   "ReferenceCount":0,
   "TagKey":"",
   "AddressListCount":2,
   "GroupUuid":"a3c5e-018e-4c08-bea8-eafc95d1a54e",
   "Global":0
  }
 ],
 "PageSiNo":1
}
```

Error codes

For a list of error codes, see Error codes.

<a id="section-7"></a>

# 7.Sensitive Data Discovery and Protection

<a id="section-7-1"></a>

## 7.1. List of operations by function

The following tables lists API operations available for use in Sensitive Data Discovery and Protection (SDDP).

| Operation | Description |
| --- | --- |
| DescribeDataAssets |  |
| DescribeInstances |  |
| DescribeTables |  |
| DescribePackages |  |
| DescribeColumns |  |
| DescribeOssObjects |  |
| DescribeOssObjectDetail |  |
| DescribeDeparts |  |
| DescribeAccounts |  |
| DescribeAccountDetail |  |
| DescribePrivileges |  |
| DescribeEventTypes |  |
| DescribeEvents |  |
| DescribeEventDetail |  |
| ModifyEventStatus |  |
| ModifyEventTypeStatus |  |
| ModifyDefaultLevel |  |
| DescribeRules |  |
| CreateRule |  |
| ModifyRule |  |
| ModifyRuleStatus |  |
| DeleteRule |  |
| DescribeDataLimitSet |  |
| CreateDataLimit |  |
| DeleteDataLimit |  |

<a id="section-7-2"></a>

## 7.2. Make API requests

<a id="section-7-2-1"></a>

### 7.2.1. Request structure

Apsara Stack Security API operations use the Remote Procedure Call (RPC) protocol. This topic describes the API request syntax.

Description

You can call API operations by sending HTTP requests. The request syntax is as follows:

```text
http://endpoint/?Action=xx&parameters
```

Where:

- `endpoint` : the endpoint of the Sensitive Data Discovery and Protection (SDDP) API is  `sddp-api.[ RegionId].example.com` .

- `Action` : the name of the operation being performed.

  For example, to query data assets, you must set the Action parameter to DescribeDataAssets.

- `parameters` : the request parameters for the operation. Separate multiple parameters with ampersands ( `&` ). Request parameters include both common parameters and operation-specific parameters.

  - Common parameters include information such as the API version and authentication information.

  - For more information about operation-specific parameters, see the corresponding operation description.

Example

The following example demonstrates how to call the DescribeDataAssets operation to query data assets:

```text
https://sddp-api.[ RegionId].example.com/?Action=DescribeDataAssets&CurrentPage=1&PageSize=10&AccessKeyId=key-test&Format=JSON&SecureTransport=true&SignatureMethod=HMAC-SHA1&SignatureNonce=15215528852396&SignatureVersion=1.0&SourceIp=1xxxx6&Timestamp=2019-04-19Txxxxxxx&Version=2019-01-03&Signature=xxxx%xxxx%3D
```

API requests are presented in the following easy-to-read format in this document:

```text
https://sddp-api.[ RegionId].example.com/?Action=DescribeDataAssets
&CurrentPage=1
&PageSize=10
&Format=JSON
&Version=2019-01-03
&Signature=xxxx%xxxx%3D
&SignatureMethod=HMAC-SHA1
&SignatureNonce=15215528852396
&SignatureVersion=1.0
&AccessKeyId=key-test
&Timestamp=2019-04-19T12:00:00Z
```

<a id="section-7-2-2"></a>

### 7.2.2. Request signatures

Apsara Stack Security authenticates each access request. Therefore, each request must contain signature information, regardless of whether it is sent through HTTP or HTTPS.

API authorization

To ensure the security of your account, we recommend that you use a Resource Access Management (RAM) user to call API operations. Before using a RAM user to call an API operation, you must grant the RAM user the corresponding permission to call the operation by creating an authorization policy and attaching the policy to the RAM user.

API signature

To ensure security, Apsara Stack authenticates each API request through the signature. When you manually make an API request, you must use the AccessKey secret to calculate the signature, that is, the hash-based message authentication code (HMAC) value, based on the encoded request string. For more information, see the definition in RFC 2104.

This topic uses the raw access parameters in the following table to describe how to create an API signature.

| Parameter | Description |
| --- | --- |
| Endpoint | <code>http://yundunprivate.[ RegionId].example.com/?</code> |
| Operation-specific parameters | <code>Action=DescribeFeatures</code> |
| Common parameters except Signature | <code>&amp;Timestamp=2016-02-23T12:46:24Z</code><br><code>&amp;Format=JSON</code><br><code>&amp;AccessKeyId=&lt;yourAccessKeyId&gt;</code><br><code>&amp;SignatureMethod=HMAC-SHA1</code><br><code>&amp;SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf</code><br><code>&amp;Version=2018-01-16</code><br><code>&amp;SignatureVersion=1.0</code> |
| AccessKey secret | <code>&lt;yourAccessKeySecret&gt;</code> |

1. Create a canonicalized query string by arranging the request parameters.

   Note

   The request parameters include all common and operation-specific parameters

   except Signature.

   <ol type="i">

   <li>

   Arrange the parameters.

   </li>

   </ol>

   Arrange the request parameters in alphabetical order.

   <ol type="i" start="2">

   <li>

   Encode the parameters.

   </li>

   </ol>

   Parameter names and values in the request URL must be encoded in UTF-8. The encoding rules are as follows:

   - Uppercase letters, lowercase letters, digits, and some special characters such as ampersands (&), hyphens (-), underscores (_), periods (.), and tildes (~) do not need to be encoded.

   - Other characters must be percent encoded in %XY format. XY represents the ASCII code of the characters in hexadecimal notation. For example, double quotation marks (") are encoded as %22.

   - Extended UTF-8 characters are encoded in %XY%ZA... format.

   - Spaces must be encoded as %20. Do not encode spaces as plus signs (+).

   <ol type="i" start="3">

   <li>

   Connect the encoded parameter names and values with equal signs (=).

   </li>

   <li>

   Arrange the parameter name and value pairs connected by equal signs in alphabetical order,

   </li>

   </ol>

   and connect them with ampersands (&) to produce the canonicalized query string.

2. Create a string-to-sign from the encoded canonicalized query string.

   ```text
   StringToSign=HTTPMethod + "&" + percentEncode("/") + "&" +
   percentEncode(CanonicalizedQueryString)
   ```

3. Calculate the HMAC value of the string-to-sign according to the definition in RFC 2104.

   Note

   The key used for signature calculation is your AccessKey secret plus the ampersand

   (&) (ASCII 38). Secure Hash Algorithm 1 (SHA1) is used as the hash algorithm.

4. Encode the HMAC value in Base64 to obtain the signature string.

   ```text
   LEW8N4y7Uasop******
   ```

5. Add the signature string to the request as the Signature parameter.

<a id="section-7-2-3"></a>

### 7.2.3. Common parameters

Common request parameters, such as the API version number and authentication information, must be included in all API requests.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Version | String | Yes | The version number of the API, in the format of YYYY-MM-DD.<br>Set the value to <em>2019-01-03</em>. |
| AccessKeyId | String | Yes | The AccessKey ID provided to you by Apsara Stack. |
| Signature | String | Yes | The signature string of the current request. |
| SignatureMethod | String | Yes | The encryption method of the signature string.<br>Set the value to <em>HMAC-SHA1</em>. |
| Timestamp | String | Yes | The timestamp of the request. Specify the time in the ISO 8601 standard. The time must be in UTC.<br>Format: <code> YYYY-MM-DDThh:mm:ssZ </code>.<br>For example, 2014-05-26T12:00:00Z indicates 20:00:00 on May 26, 2014 (UTC+8). |
| SignatureVersion | String | Yes | The version of the signature encryption algorithm.<br>Set the value to <em>1.0</em>. |
| SignatureNonce | String | Yes | A unique, random number used to prevent replay attacks. You must use different numbers for different requests. |
| ResourceOwnerAc count | String | No | The name of the account that owns the resource to be accessed through this API request. |
| Format | String | No | The format of the response.<br>Set the value to <em>JSON or XML</em>.<br>Note Default value: XML. |

<a id="section-7-2-4"></a>

### 7.2.4. Responses

Apsara Stack Security APIs can return responses in XML or JSON format. The system returns a unique identifier specified by RequestId each time you send a request to call an API operation, no matter whether the call is successful or not.

Sample response in XML format

```xml
<? xml version="1.0" encoding="UTF-8"? >
<! --Root node of the response -->
<Operation name+Response>
    <! --Returned request ID-->
    <RequestId>4C467B38-3910-447D-87BC-AC049166F216</RequestId>
    <! --Returned results-->
</Operation name+Response>
```

Sample response in JSON format

```json
{
"RequestId": "4C467B38-3910-447D-87BC-AC049166F216",
/* Returned results */
}
```

<a id="section-7-3"></a>

## 7.3. APIs

<a id="section-7-3-1"></a>

### 7.3.1. DescribeDataAssets

Description

You can call this operation to query data assets globally based on the specified conditions.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>DescribeDataAssets</em>. |
| RangeId | Integer | Yes | The type of the assets to query. Valid values:<br>• <em>1</em>: MaxCompute project.<br>• <em>2</em>: MaxCompute table.<br>• <em>3</em>: MaxCompute package.<br>• <em>21</em>: Object Storage Service (OSS) bucket.<br>• <em>22</em>: OSS object.<br>• <em>31</em>: Table Store instance.<br>• <em>32</em>: Table Store table.<br>• <em>51</em>: Relational Database Service (RDS) database.<br>• <em>52</em>: RDS table. |
| CurrentPage | Integer | Yes | The number of the page to return. |
| PageSize | Integer | Yes | The number of entries to return on each page. |
| Name | String | No | The search keyword. Fuzzy match is supported. |
| RuleId | Long | No | The ID of the rule. |
| RiskLevels | String | No | The ID of the risk level. Separate multiple IDs with commas (,). |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| TotalCount | Integer | The total number of returned pages. |
| CurrentPage | Integer | The page number of the returned page. |
| PageSize | Integer | The number of entries returned per page. |
| Items | Array | The list of assets. |
| Owner | String | The account of the asset owner. |
| ProductCode | String | The code of the big data service, for example, RDS or OSS. |
| Acl | String | The access control list (ACL) for the OSS bucket. |
| RiskLevelId | Long | The ID of the risk level. |
| RiskLevelName | String | The name of the risk level. |
| DepartName | String | The name of the department. |
| Name | String | The name of the asset. |
| Labelsec | Boolean | The label security flag of the MaxCompute asset. |
| CreationTime | Long | The time when the asset was created. Unit: milliseconds. |
| Id | Long | The ID of the primary key. |
| Protection | Boolean | The protection flag of the MaxCompute asset. |
| RuleName | String | The name of the hit rule. |
| ObjectKey | String | The key of the OSS object. |

Error codes

For a list of error codes, see Error codes.

Examples

- Sample request

  ```text
  https://sddp-api.[ RegionId].example.com/?Action=DescribeDataAssets
  &RangeId=1
  &CurrentPage=1
  &PageSize=10
  &<Common request parameters>           
  ```

- Sample success response in JSON format

  ```json
  {
      "RequestId":"71064826-726F-4ADA-B879-05D8055476FB"
      "TotalCount":4,
      "PageSize":10,
      "CurrentPage":1,
      "Items":[
          {
              "Owner":"dtdep-239-153536994****", 
              "ProductCode":"ODPS",
              "ProductId":1,
              "Acl":"",
              "RiskLevelId":2,
              "RiskLevelName":"Internal", 
              "DepartName":"DemoCenter", 
              "Name":"****data", 
              "Labelsec":false,
              "CreationTime":1536751124000, 
              "Sensitive":true, 
              "Id":268, 
              "Protection":false, 
              "RuleName":"Hit rule"
              "ObjectKey":"Internal"
          }
      ]
  }           
  ```

<a id="section-7-3-2"></a>

### 7.3.2. DescribeInstances

Description

You can call this operation to query instances, databases, projects, or buckets based on the specified conditions.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>DescribeInstances</em>. |
| ProductCode | String | Yes | The code of the big data service, for example, RDS or OSS. |
| CurrentPage | Integer | Yes | The number of the page to return. |
| PageSize | Integer | Yes | The number of entries to return on each page. |
| Name | String | No | The search keyword. Fuzzy match is supported. |
| RuleId | Long | No | The ID of the rule. |
| RiskLevelId | Long | No | The ID of the risk level. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| TotalCount | Integer | The total number of returned pages. |
| CurrentPage | Integer | The page number of the returned page. |
| PageSize | Integer | The number of entries returned per page. |
| Items | Array | The list of instances. |
| Owner | String | The account of the instance owner. |
| ProductCode | String | The code of the big data service, for example, RDS or OSS. |
| Acl | String | The access control list (ACL) for the OSS bucket. |
| RiskLevelId | Long | The ID of the risk level. |
| RiskLevelName | String | The name of the risk level. |
| DepartName | String | The name of the department. |
| Name | String | The name of the asset. |
| Labelsec | Boolean | The label security flag of the MaxCompute asset. |
| CreationTime | Long | The time when the instance was created. Unit: milliseconds. |
| Id | Long | The ID of the primary key. |
| Protection | Boolean | The protection flag of the MaxCompute asset. |

Error codes

For a list of error codes, see Error codes.

Examples

- Sample request

  ```text
  https://sddp-api.[ RegionId].example.com/?Action=DescribeInstances
  &CurrentPage=1
  &PageSize=10
  &ProductCode=ODPS
  &<Common request parameters>
  ```

- Sample success response in JSON format

  ```json
  {
      "RequestId":"71064826-726F-4ADA-B879-05D8055476FB"
      "TotalCount":4,
      "PageSize":10,
      "CurrentPage":1,
      "Items":[
          {
              "Owner":"dtdep-239-153536994****",
              "ProductCode":"ODPS",
              "ProductId":1,
              "Acl":"",
              "RiskLevelId":2,
              "RiskLevelName":"Internal",
              "DepartName":"DemoCenter",
              "Name":"****data",
              "Labelsec":false,
              "CreationTime":1536751124000,
              "Sensitive":true,
              "Id":268,
              "Protection":false
          }
      ]
  }
  ```

<a id="section-7-3-3"></a>

### 7.3.3. DescribeTables

Description

Queries data asset tables of MaxCompute, ApsaraDB for RDS, and Table Store that SDDP is authorized to scan.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>DescribeTables</em>. |
| InstanceId | Long | Yes | The ID of the instance. |
| CurrentPage | Integer | Yes | The number of the page to return. |
| PageSize | Integer | Yes | The number of entries to return on each page. |
| Name | String | No | The keyword. Fuzzy match is supported. |
| RuleId | Long | No | The ID of the rule. |
| RiskLevelId | Long | No | The ID of the risk level. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| TotalCount | Integer | The total number of returned pages. |
| CurrentPage | Integer | The number of the returned page. |
| PageSize | Integer | The number of entries returned per page. |
| Items | Array | The list of instances. |
| Owner | String | The account that owns the instance. |
| ProductCode | String | The code of the service, for example, RDS or OSS. |
| Acl | String | The access control list (ACL) for the OSS bucket. |
| RiskLevelId | Long | The ID of the risk level. |
| RiskLevelName | String | The name of the risk level. |
| DepartName | String | The name of the department. |
| Name | String | The name of the asset. |
| Labelsec | Boolean | The label security tag of the MaxCompute asset. |
| CreationTime | Long | The time when the table was created. Unit: milliseconds. |
| Id | Long | The ID of the primary key. |
| Protection | Boolean | The protection tag of the MaxCompute asset. |

Error codes

For a list of error codes, see Error codes.

Examples

- Sample requests

  ```text
  https://sddp-api.[ RegionId].example.com/?Action=DescribeInstances
  &CurrentPage=1
  &PageSize=10
  &ProductCode=ODPS
  &<Common request parameters>
  ```

- Sample success responses in JSON format

  ```json
  {
      "RequestId":"71064826-726F-4ADA-B879-05D8055476FB"
      "TotalCount":4,
      "PageSize":10,
      "CurrentPage":1,
      "Items":[
          {
              "Owner":"dtdep-239-153536994****",
              "ProductCode":"ODPS",
              "ProductId":1,
              "Acl":"",
              "RiskLevelId":2,
              "RiskLevelName":"Internal",
              "DepartName":"DemoCenter",
              "Name":"****data",
              "Labelsec":false,
              "CreationTime":1536751124000,
              "Sensitive":true,
              "Id":268,
              "Protection":false
          }
      ]
  }
  ```

<a id="section-7-3-4"></a>

### 7.3.4. DescribePackages

Description

You can call this operation to query MaxCompute packages based on the specified conditions.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>DescribePackages</em>. |
| InstanceId | Long | Yes | The ID of the instance. |
| CurrentPage | Integer | Yes | The number of the page to return. |
| PageSize | Integer | Yes | The number of entries to return on each page. |
| Name | String | No | The search keyword. Fuzzy match is supported. |
| RuleId | Long | No | The ID of the rule. |
| RiskLevelId | Long | No | The ID of the risk level. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| TotalCount | Integer | The total number of returned pages. |
| CurrentPage | Integer | The page number of the returned page. |
| PageSize | Integer | The number of entries returned per page. |
| Items | Array | The list of packages. |
| Owner | String | The account of the package owner. |
| RiskLevelId | Long | The ID of the risk level. |
| RiskLevelName | String | The name of the risk level. |
| DepartName | String | The name of the department. |
| Name | String | The name of the asset. |
| CreationTime | Long | The time when the package was created. Unit: milliseconds. |
| Id | Long | The ID of the primary key. |
| InstanceId | Long | The ID of the instance. |

Error codes

For a list of error codes, see Error codes.

Examples

- Sample request

  ```text
  https://sddp-api.[ RegionId].example.com/?Action=DescribePackages
  &CurrentPage=1
  &PageSize=20
  &InstanceId=1
  &<Common request parameters>
  ```

- Sample success response in JSON format

  ```json
  {
      "RequestId":"769FB3C1-F4C9-42DF-9B72-7077A8989C13",
      "TotalCount":4,
      "PageSize":10,
      "CurrentPage":1,
      "Items":[
          {
              "Owner":"dtdep-239-153536994****",
              "ProductCode":"ODPS",
              "ProductId":1,
              "Acl":"",
              "RiskLevelId":2,
              "RiskLevelName":"Internal",
              "DepartName":"DemoCenter",
              "Name":"****data",
              "CreationTime":1536751124000,
              "Sensitive":true,
              "Id":268,
              "InstanceId":1
          }
      ]
  }
  ```

<a id="section-7-3-5"></a>

### 7.3.5. DescribeColumns

Description

Queries columns in tables of MaxCompute, ApsaraDB for RDS, and Table Store that SDDP is authorized to scan.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>DescribeColumns</em>. |
| InstanceId | Long | Yes | The ID of the instance. |
| TableId | Long | Yes | The ID of the table. |
| CurrentPage | Integer | Yes | The number of the page to return. |
| PageSize | Integer | Yes | The number of entries to return on each page. |
| Name | String | No | The keyword. Fuzzy match is supported. |
| RuleId | Long | No | The ID of the rule. |
| RiskLevelId | Long | No | The ID of the risk level. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| TotalCount | Integer | The total number of returned pages. |
| CurrentPage | Integer | The number of the returned page. |
| PageSize | Integer | The number of entries returned per page. |
| Items | Array | The list of packages. |
| Owner | String | The account that owns the package. |
| RiskLevelId | Long | The ID of the risk level. |
| RiskLevelName | String | The name of the risk level. |
| DepartName | String | The name of the department. |
| Name | String | The name of the asset. |
| CreationTime | Long | The time when the column was created. |
| Id | Long | The ID of the primary key. |
| RuleId | Long | The ID of the matched rule. |
| RuleName | String | The name of the matched rule. |
| TableId | Long | The ID of the table. |
| InstanceId | Long | The ID of the instance. |

Error codes

For a list of error codes, see Error codes.

Examples

- Sample requests

  ```text
  https://sddp-api.[ RegionId].example.com/?Action=DescribeColumns
  &CurrentPage=1
  &PageSize=20
  &InstanceId=1
  &TableId=1
  &<Common request parameters>
  ```

- Sample success responses in JSON format

  ```json
  {
      "RequestId":"769FB3C1-F4C9-42DF-9B72-7077A8989C13",
      "TotalCount":4,
      "PageSize":10,
      "CurrentPage":1,
      "Items":[
          {
              "Owner":"dtdep-239-153536994****",
              "ProductCode":"ODPS",
              "ProductId":1,
              "Acl":"",
              "RiskLevelId":2,
              "RiskLevelName":"Internal",
              "DepartName":"DemoCenter",
              "Name":"****data",
              "CreationTime":1536751124000,
              "Sensitive":true,
              "Id":268,
              "RuleId":1,
              "RuleName":"Hit rule",
              "InstanceId":1,
              "TableId":1
          }
      ]
  }
  ```

<a id="section-7-3-6"></a>

### 7.3.6. DescribeOssObjects

Description

You can call this operation to query Object Storage Service (OSS) objects based on the specified conditions.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>DescribeOssObjects</em>. |
| InstanceId | Long | Yes | The ID of the instance. |
| CurrentPage | Integer | Yes | The number of the page to return. |
| PageSize | Integer | Yes | The number of entries to return on each page. |
| Name | String | No | The search keyword. Fuzzy match is supported. |
| RuleId | Long | No | The ID of the rule. |
| RiskLevelId | Long | No | The ID of the risk level. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| TotalCount | Integer | The total number of returned pages. |
| CurrentPage | Integer | The page number of the returned page. |
| PageSize | Integer | The number of entries returned per page. |
| Items | Array | The list of packages. |
| RiskLevelId | Long | The ID of the risk level. |
| RiskLevelName | String | The name of the risk level. |
| DepartName | String | The name of the department. |
| Name | String | The name of the asset. |
| Id | Long | The ID of the primary key. |
| RegionId | String | The ID of the region. |

Error codes

For a list of error codes, see Error codes.

Examples

- Sample request

  ```text
  https://sddp-api.[ RegionId].example.com/?Action=DescribeOssObjects
  &CurrentPage=1
  &PageSize=20
  &InstanceId=1
  &<Common request parameters>
  ```

- Sample success response in JSON format

  ```json
  {
      "RequestId":"769FB3C1-F4C9-42DF-9B72-7077A8989C13",
      "TotalCount":4,
      "PageSize":10,
      "CurrentPage":1,
      "Items":[
           {
              "RiskLevelName":"Internal",
              "Id":17383,
              "RiskLevelId":2,
              "RegionId":"cn-hangzhou",
              "Name":"obj****"
          }
      ]
  }
  ```

<a id="section-7-3-7"></a>

### 7.3.7. DescribeOssObjectDetail

Description

You can call this operation to query the details of an Object Storage Service (OSS) object that SDDP is authorized to access.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>DescribeOssObjectDetail</em>. |
| Id | Long | Yes | The ID of the OSS object. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| OssObjectDetail | Object | The details of the OSS object. |
| RiskLevelId | Long | The ID of the risk level. |
| RiskLevelName | String | The name of the risk level. |
| Name | String | The name of the asset. |
| Id | Long | The ID of the primary key. |
| RegionId | String | The ID of the region. |
| CategoryName | String | The type of the OSS object. |
| RuleList | Array | A list of the matched rules. |
| RuleName | String | The name of the matched rule. |
| Count | Integer | The number of matches. |

Error codes

For a list of error codes, visit the Error codes.

Examples

- Sample requests

  ```text
  https://sddp-api.[ RegionId].example.com/?Action=DescribeOssObjectDetail
  &Id=12
  &<Common request parameters>
  ```

- Sample success responses in JSON format

  ```json
  {
      "RequestId":"769FB3C1-F4C9-42DF-9B72-7077A8989C13",
      "OssObjectDetail":{
          "RegionId":"cn-hangzhou",
          "BucketName":"",
          "RiskLevelName":"Internal",
          "Id":17383,
          "RiskLevelId":2,
          "CategoryName":"MAC address",
          "Name":"obj_id",
          "RuleList":[
              {
                  "RuleName":"ID card number",
                  "Count":10
              }
          ]
      }
  }
  ```

<a id="section-7-3-8"></a>

### 7.3.8. DescribeDeparts

Description

You can call this operation to query departments based on the specified conditions.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>DescribeDeparts</em>. |
| CurrentPage | Integer | Yes | The number of the page to return. |
| PageSize | Integer | Yes | The number of entries to return on each page. |
| Key | String | No | The search keyword. Fuzzy match is supported. |
| AccountType | Integer | No | The type of the query. Valid values:<br>• <em>1</em>: department query.<br>• <em>2</em>: account query. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| CurrentPage | Integer | The page number of the returned page. |
| PageSize | Integer | The number of entries returned per page. |
| TotalCount | Integer | The total number of returned pages. |
| Items | Array | The list of departments. |
| Id | Long | The ID of the primary key. |
| DepartName | String | The name of the department. |
| DepartId | Long | The ID of the department. |

Error codes

For a list of error codes, see Error codes.

Examples

- Sample request

  ```text
  https://sddp-api.[ RegionId].example.com/?Action=DescribeDeparts
  &CurrentPage=1
  &PageSize=10
  &<Common request parameters>
  ```

- Sample success response in JSON format

  ```json
  {
      "RequestId":"769FB3C1-F4C9-42DF-9B72-7077A8989C13",
      "PageSize":10,
      "CurrentPage":1
      "TotalCount":1,
      "Items":[
          {
              "Id":283,
              "DepartId":2,
              "DepartName":"Development"
          }
      ]
  }
  ```

<a id="section-7-3-9"></a>

### 7.3.9. DescribeAccounts

Description

You can call this operation to query accounts based on the specified conditions.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>DescribeAccounts</em>. |
| CurrentPage | Integer | Yes | The number of the page to return. |
| PageSize | Integer | Yes | The number of entries to return on each page. |
| Key | String | No | The search keyword. Fuzzy match is supported. |
| DepartId | Long | No | The ID of the department. |
| QueryType | Integer | No | The type of the resource. Valid values:<br>• <em>1</em>: instance.<br>• <em>2</em>: table.<br>• <em>3</em>: package.<br>• <em>4</em>: column.<br>• <em>5</em>: table in a package. |
| ProductCode | String | No | The code of the service. Valid values:<br>• <em>MaxCompute</em><br>• <em>RDS</em><br>• <em>OTS</em> |
| OperationId | Integer | No | The type of the operation. For more information, see Operation type definition. |
| InstanceId | Long | No | The ID of the instance. |
| TableId | Long | No | The ID of the table. |
| PackageId | Long | No | The ID of the package. |
| ColumnId | Long | No | The ID of the column. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| CurrentPage | Integer | The page number of the returned page. |
| PageSize | Integer | The number of entries returned per page. |
| TotalCount | Integer | The total number of returned pages. |
| Items | Array | The list of accounts. |
| Id | Long | The ID of the primary key. |
| LongName | String | The name of the account. |
| Email | String | The email address. |
| CreateTime | Long | The time when the account was created. Unit: milliseconds. |
| LoginDataTime | Long | The last logon time of the account. Unit: milliseconds. |
| UserId | Long | The ID of the account. |
| FullName | String | The display name. |
| CellphoneNum | String | The mobile phone number. |
| TelephoneNum | String | The landline phone number. |
| AccountTypeId | Integer | The type of the account. Valid values:<br>• <em>2</em>: Apsara Stack Console account.<br>• <em>3</em>: Resource Access Management (RAM) account. |

Error codes

For a list of error codes, see Error codes.

Examples

- Sample request

  ```text
  https://sddp-api.[ RegionId].example.com/?Action=DescribeAccounts
  &CurrentPage=1
  &PageSize=10
  &<Common request parameters>
  ```

- Sample success response in JSON format

  ```json
  {
      "RequestId":"769FB3C1-F4C9-42DF-9B72-7077A8989C13",
      "PageSize":10,
      "CurrentPage":1
      "TotalCount":1,
      "Items":[
          {
              "LoginName":"sddp_****",
              "Email":"test@example.com",
              "CreateTime":1543300900000,
              "LoginDataTime":1544493748000,
              "UserId":10****,
              "FullName":"sddp****",
              "Id":1091,
              "CellphoneNum":"1300000****",
              "TelephoneNum":"0571-6000****",
              "AccountTypeId":1
          }
      ]
  }
  ```

<a id="section-7-3-10"></a>

### 7.3.10. DescribeAccountDetail

Description

You can call this operation to query the details of an account based on the account ID and account type.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>DescribeAccountDetail</em>. |
| UserId | Long | Yes | The ID of the account. |
| AccountTypeId | Integer | Yes | The type of the account. Valid values:<br>• <em>2</em>: Apsara Stack Console account.<br>• <em>3</em>: Resource Access Management (RAM) account. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| Account | Object | The details of the account. |
| Id | Long | The ID of the primary key. |
| LongName | String | The name of the account. |
| Email | String | The email address. |
| CreateTime | Long | The time when the account was created. Unit: milliseconds. |
| LoginDataTime | Long | The last logon time of the account. Unit: milliseconds. |
| UserId | Long | The ID of the account. |
| FullName | String | The display name. |
| CellphoneNum | String | The mobile phone number. |
| TelephoneNum | String | The landline phone number. |
| PrivilegeList | Array | The list of available accounts. |
| ProdcutName | String | The service that the account can operate. Separate multiple services with forward slashes (/). |
| UseAccountName | String | The name of the used account. |
| UseAccountId | Long | The ID of the used account. |
| UseAccountType | Integer | The type of the used account. |
| UseAccountCreateTime | Long | The time when the used account was created. Unit: milliseconds. |

Error codes

For a list of error codes, see Error codes.

Examples

- Sample request

  ```text
  https://sddp-api.[ RegionId].example.com/?Action=DescribeAccountDetail
  &UserId=1
  &AccountTypeId=2
  &<Common request parameters>
  ```

- Sample success response in JSON format

  ```json
  {
      "RequestId":"769FB3C1-F4C9-42DF-9B72-7077A8989C13",
      "Account":{
          "LoginName":"yundun****",
          "Email":"kf@example.com",
          "CreateTime":1543384996000,
          "LoginDataTime":1543385065000,
          "UserId":1045,
          "FullName":"yundun****",
          "Id":882,
          "CellphoneNum":"1300000****",
          "TelephoneNum":"0571-6000****",
          "PrivilegeList":[
              {
                  "UseAccountType":2,
                  "ProductName":"OSS/ODPS",
                  "UseAccountCreateTime":1546413235000,
                  "UseAccountName":"ram_****",
                  "UseAccountId":259
              }
          ]
      }
  }
  ```

<a id="section-7-3-11"></a>

### 7.3.11. DescribePrivileges

Description

You can call this operation to query permissions of an account based on the account ID and other specified conditions.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>DescribePrivileges</em>. |
| CurrentPage | Integer | Yes | The number of the page to return. |
| PageSize | Integer | Yes | The number of entries to return on each page. |
| AccountId | Long | Yes | The ID of the account. |
| UseAccountId | Long | No | The ID of the used account. |
| Key | String | No | The search keyword. Fuzzy match is supported. |
| DataTypeIds | String | No | The type of the resource. For more information, see Resource type definition. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| CurrentPage | Integer | The page number of the returned page. |
| PageSize | Integer | The number of entries returned per page. |
| TotalCount | Integer | The total number of returned pages. |
| Items | Array | The list of permissions. |
| Id | Long | The ID of the primary key. |
| AccountId | Long | The ID of the account. |
| AccountType | Integer | The type of the account. Valid values:<br>• <em>2</em>: Apsara Stack Console account.<br>• <em>3</em>: Resource Access Management (RAM) account. |
| UseAccountId | Long | The ID of the used account. |
| UseAccountType | Long | The type of the used account. Valid values:<br>• <em>2</em>: Apsara Stack Console account.<br>• <em>3</em>: RAM account. |
| DataType | String | The type of the resource. For more information, see Resource type definition |
| DataTypeId | Integer | The ID of the resource type. For more information, see Resource type definition |
| DataInstance | String | The instance. A value of <code> * </code> indicates all instances. |
| DataTable | String | The table. A value of <code> * </code> indicates all tables. |
| DataColumn | String | The column. A value of <code> * </code> indicates all columns. |
| DataPackage | String | The package. A value of <code> * </code> indicates all packages. |
| ResourceName | String | The name of the resource. |
| ResourcePath | String | The path of the resource. |
| Operation | String | The operation permission. Separate multiple permissions with semicolons (;). |
| PolicyCondition | String | The usage conditions. |
| Sensitive | Boolean | Indicates whether the permission is sensitive. |

Error codes

For a list of error codes, see Error codes.

Examples

- Sample request

  ```text
  https://sddp-api.[RegionId].example.com/?Action=DescribePrivileges
  &CurrentPage=1
  &PageSize=20
  &AccountId=1
  &<Common request parameters>
  ```

- Sample success response in JSON format

  ```json
  {
      "RequestId":"769FB3C1-F4C9-42DF-9B72-7077A8989C13",
      "PageSize":10,
      "CurrentPage":1
      "TotalCount":1,
      "Items":[
          {
              "UseAccountType":2,
              "DataInstance":"341",
              "AccountId":259,
              "ResourceName":"bucket****",
              "Operation":"GET;OPEARETE",
              "AccountType":2,
              "ResourcePath":"kf",
              "DataTypeId":21,
              "Sensitive":false,
              "DataType":"OSS_BUCKET",
              "Id":1,
              "UseAccountId":259
          }
      ]
  }
  ```

<a id="section-7-3-12"></a>

### 7.3.12. DescribeEventTypes

Description

You can call this operation to query types of anomalous activities based on the specified conditions.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>DescribeEventTypes</em>. |
| ParentTypeId | Long | No | The ID of the type. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| EventTypeList | Array | The list of types.<br>Note If you do not set the ParentTypeId parameter, the system returns the type list.Otherwise, the system returns the list of subtypes under the specified type. |
| Id | Long | The ID of the type. |
| Code | String | The code of the type. |
| Name | String | The name of the type. |
| SubTypeList | Array | The list of subtypes. |
| Id | Long | The ID of the subtype. |
| Code | String | The code of the subtype. |
| Name | String | The name of the subtype. |
| Status | String | The status of the subtype. Valid values:<br>• <em>1</em>: enabled.<br>• <em>2</em>: disabled. |

Error codes

For a list of error codes, see Error codes.

Examples

- Sample request

  ```text
  https://sddp-api.[RegionId].example.com/?Action=DescribeEventTypes
  &ParentTypeId=1
  &<Common request parameters>
  ```

- Sample success response in JSON format

  ```json
  {
      "RequestId":"769FB3C1-F4C9-42DF-9B72-7077A8989C13",
      "EventTypeList":[
          {
              "SubTypeList":[
                  {
                      "Id":1,
                      "Code":"010001",
                      "Name":"Incorrect configuration - Sensitive MaxCompute projects are not protected",
                      "Status":1
                  }
              ],
              "Id":1,
              "Code":"01",
              "Name":"Anomalous permission access"
          }
      ]
  }
  ```

<a id="section-7-3-13"></a>

### 7.3.13. DescribeEvents

Description

You can call this operation to query anomalous activities based on the specified conditions.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>DescribeEvents</em>. |
| CurrentPage | Integer | Yes | The number of the page to return. |
| PageSize | Integer | Yes | The number of entries to return on each page. |
| TypeCode | String | No | The ID of the type of the anomalous activity. |
| UserId | Long | No | The account ID of the operator of the anomalous activity. |
| DealUserId | Long | No | The account ID of the handler of the anomalous activity. |
| Status | Integer | No | The status of the anomalous activity.Valid values:<br>• <em>0</em>: unprocessed.<br>• <em>1</em>: confirmed as a violation.<br>• <em>2</em>: excluded as a false positive. |
| SubTypeCode | String | No | The ID of the subtype of the anomalous activity. |
| StartTime | Long | No | The beginning of the time range to query. Unit: milliseconds. |
| EndTime | Long | No | The end of the time range to query. Unit: milliseconds. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| CurrentPage | Integer | The page number of the returned page. |
| PageSize | Integer | The number of entries returned per page. |
| TotalCount | Integer | The total number of returned pages. |
| Items | Array | The list of anomalous activities. |
| Id | Long | The ID of the anomalous activity. |
| UserId | Long | The account ID of the operator. |
| LoginName | String | The account name of the operator. |
| DisplayName | String | The account display name of the operator. |
| ProductCode | String | The code of the service where the anomalous activity occurred. |
| TypeCode | String | The ID of the type. |
| TypeName | String | The name of the type. |
| SubTypeCode | String | The ID of the subtype. |
| SubTypeName | String | The name of the subtype. |
| AlertTime | Long | The time when the anomalous activity occurred. |
| EventTime | Long | The time when the alert was reported. |
| Status | Integer | The status of the anomalous activity. Valid values:<br>• <em>0</em>: unprocessed.<br>• <em>1</em>: confirmed as a violation.<br>• <em>2</em>: excluded as a false positive. |
| DealUserId | Long | The account ID of the handler. |
| DealLoginName | String | The account name of the handler. |
| DealDisplayName | String | The account display name of the handler. |
| DealTime | Long | The time when the anomalous activity was processed. Unit: milliseconds. |
| Backed | Boolean | Indicates whether the processing result of the anomalous activity was returned as a feedback to the detection algorithm. |

Error codes

For a list of error codes, see Error codes.

Examples

- Sample request

  ```text
  https://sddp-api.[RegionId].example.com/?Action=DescribeEvents
  &CurrentPage=1
  &TypeCode=01
  &PageSize=10
  &<Common request parameters>
  ```

- Sample success response in JSON format

  ```json
  {
      "RequestId":"769FB3C1-F4C9-42DF-9B72-7077A8989C13",
      "PageSize":10,
      "CurrentPage":1
      "TotalCount":1,
      "Items":[
          {
              "Status":0,
              "TypeName":"Anomalous data flow",
              "Backed":false,
              "TypeCode":"02",
              "ProductCode":"ODPS",
              "SubTypeName":"Download sensitive data in an abnormal geographical location",
              "EventTime":1545829129000,
              "UserId":22915744338501****,
              "LoginName":"det****",
              "DisplayName":"yundun****",
              "Id":4,
              "SubTypeCode":"020001",
              "AlertTime":1545829129000,
              "StatusName":"To be processed",
              "DealUserId":229157443385014132,
              "DealLoginName":"det****",
              "DeaulDisplayName":"yundun****",
              "DepartName":"kf"
          }
      ]
  }
  ```

<a id="section-7-3-14"></a>

### 7.3.14. DescribeEventDetail

Description

You can call this operation to query the details of an anomalous activity based on the specified ID.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>DescribeEventDetail</em>. |
| Id | Long | Yes | The ID of the anomalous activity. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| Event | Object | The details of the anomalous activity. |
| Id | Long | The ID of the anomalous activity. |
| UserId | Long | The account ID of the operator. |
| LoginName | String | The account name of the operator. |
| DisplayName | String | The account display name of the operator. |
| ProductCode | String | The code of the service where the anomalous activity occurred. |
| TypeCode | String | The ID of the type. |
| TypeName | String | The name of the type. |
| SubTypeCode | String | The ID of the subtype. |
| SubTypeName | String | The name of the subtype. |
| AlertTime | Long | The time when the anomalous activity occurred. |
| EventTime | Long | The time when the alert was reported. |
| Status | Integer | The status of the anomalous activity. Valid values:<br>• <em>0</em>: unprocessed.<br>• <em>1</em>: confirmed as a violation.<br>• <em>2</em>: excluded as a false positive. |
| DealUserId | Long | The account ID of the handler. |
| DealLoginName | String | The account name of the handler. |
| DealDisplayName | String | The account display name of the handler. |
| DealTime | Long | The time when the anomalous activity was processed. Unit: milliseconds. |
| Backed | Boolean | Indicates whether the processing result of the anomalous activity was returned as a feedback to the detection algorithm. |
| Detail | Object | The detailed content of the anomalous activity. |
| Content | Array | The content. |
| Label | String | The title. |
| Value | String | The description. |
| Chart | Array | The baseline. |
| XLabel | String | The X-axis title. |
| YLabel | String | The Y-axis title. |
| Data | Object | The content of the baseline. |
| X | Array | The array of data along the X-axis. |
| Y | Array | The array of data along the Y-axis. |

Error codes

For a list of error codes, see Error codes.

Examples

- Sample request

  ```text
  https://sddp-api.[RegionId].example.com/?Action=DescribeEventDetail
  &Id=1
  &<Common request parameters>
  ```

- Sample success response in JSON format

  ```json
  {
      "RequestId": "769FB3C1-F4C9-42DF-9B72-7077A8989C13",
      "Event": {
          "Status": 0,
          "TypeName": "Anomalous data flow",
          "Backed": false,
          "TypeCode": "02",
          "ProductCode": "ODPS",
          "SubTypeName": "Download sensitive data in an abnormal geographical location",
          "EventTime": 1545829129000,
          "UserId": 22915744338501****,
          "LoginName": "det****",
          "DisplayName": "yundun****",
          "Id": 4,
          "SubTypeCode": "020001",
          "AlertTime": 1545829129000,
          "StatusName": "To be processed",
          "DealUserId": 22915744338501****,
          "DealLoginName": "det****",
          "DealDisplayName": "yundun****",
          "DepartName": "kf",
          "Detail": {
              "Content": [
                  {
                      "Value": "This anomalous activity may cause exposure of sensitive data to risks and damage to the security baseline.",
                      "Label": "Risk exposure"
                  }
              ],
              "Chart": [
                  {
                      "YLabel": "Value",
                      "Label": "Event baseline",
                      "Data": {
                          "X": [
                              1,
                              2,
                              3,
                              4,
                              5,
                              6
                          ],
                          "Y": [
                              1,
                              2,
                              3,
                              4,
                              5,
                              6
                          ]
                      },
                      "XLabel": "Days"
                  }
              ]
          },
          "DealReason": "Confirmed violation"
      }
  }
  ```

<a id="section-7-3-15"></a>

### 7.3.15. ModifyEventStatus

Description

You can call this operation to process an anomalous activity.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>ModifyEventStatus</em>. |
| Id | Long | Yes | The ID of the anomalous activity. |
| Status | Integer | Yes | The status of the anomalous activity.Valid values:<br>• <em>1</em>: confirmed as a violation.<br>• <em>2</em>: excluded as a false positive. |
| DealReason | String | Yes | The processing comments. |
| Backed | Boolean | No | Specifies whether to return the processing result of the anomalous activity as a feedback to the detection algorithm. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |

Error codes

For a list of error codes, see Error codes.

Examples

- Sample request

  ```text
  https://sddp-api.[RegionId].example.com/?Action=ModifyEventStatus
  &Id=1
  &Status=1
  &DealReason=Confirmed violation
  &<Common request parameters>
  ```

- Sample success response in JSON format

  ```json
  {
      "RequestId":"8491DBFD-48C0-4E11-B6FC-6F38921244A9"
  }
  ```

<a id="section-7-3-16"></a>

### 7.3.16. ModifyEventTypeStatus

Description

Enables detection of exceptions of subtypes.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>ModifyEventTypeStatus</em>. |
| SubTypeIds | String | Yes | The subtype IDs of exceptions. Separate multiple IDs with commas (,). |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |

Error codes

For a list of error codes, see Error codes.

Examples

- Sample requests

  ```text
  https://sddp-api.[ RegionId].example.com/?Action=ModifyEventTypeStatus
  &SubTypeIds=1,2,3,4
  &<Common request parameters>
  ```

- Sample success responses in JSON format

  ```json
  {
      "RequestId":"208B016D-4CB9-4A85-96A5-0B8ED1EBF271"
  }
  ```

<a id="section-7-3-17"></a>

### 7.3.17. ModifyDefaultLevel

Description

You can call this operation to set the default risk level or modify the risk levels of sensitive data.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>ModifyDefaultLevel</em>. |
| DefaultId | Long | No | The ID of the default risk level. |
| SensitiveIds | String | No | The ID of the risk level of sensitive data.Separate multiple IDs with commas (,). |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |

Error codes

For a list of error codes, see Error codes.

Examples

- Sample request

  ```text
  https://sddp-api.[RegionId].example.com/?Action=ModifyDefaultLevel
  &Type=15
  &DefaultId=2
  &SensitiveIds=3,4
  &<Common request parameters>
  ```

- Sample success response in JSON format

  ```json
  {
      "RequestId":"208B016D-4CB9-4A85-96A5-0B8ED1EBF271"
  }
  ```

<a id="section-7-3-18"></a>

### 7.3.18. DescribeRules

Description

You can call this operation to query rules based on the specified conditions.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>DescribeRules</em>. |
| Name | String | No | The search keyword. Fuzzy match is supported. |
| RiskLevelId | Long | No | The ID of the risk level. |
| Category | Integer | No | The type of the rule. Valid values:<br>• <em>0</em>: keyword.<br>• <em>2</em>: regular expression. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| CurrentPage | Integer | The page number of the returned page. |
| PageSize | Integer | The number of entries returned per page. |
| TotalCount | Integer | The total number of returned pages. |
| Items | Array | The list of rules. |
| Id | Long | The ID of the rule. |
| Name | String | The name of the rule. |
| Content | String | The content of the rule. |
| Description | String | The description of the rule. |
| RiskLevelId | Long | The ID of the risk level. |
| Status | Integer | The status of the rule. Valid values:<br>• <em>0</em>: disabled.<br>• <em>1</em>: enabled. |
| Category | Integer | The type of the rule. Valid values:<br>• <em>0</em>: keyword.<br>• <em>2</em>: regular expression. |
| CategoryName | String | The name of the rule type. |
| UserId | Long | The account ID of the rule creator. |
| LoginName | String | The account name of the rule creator. |
| DisplayName | String | The account display name of the rule creator. |

Error codes

For a list of error codes, see Error codes.

Examples

- Sample request

  ```text
  https://sddp-api.[RegionId].example.com/?Action=DescribeRules
  &<Common request parameters>
  ```

- Sample success response in JSON format

  ```json
  {
      "RequestId":"769FB3C1-F4C9-42DF-9B72-7077A8989C13",
      "Items":[
          {
              "Description":"IP address",
              "Category":2,
              "GmtModified":1545277010000,
              "RiskLevelId":2,
              "Name":"IP address",
              "GmtCreate":1545277010000,
              "UserId":0,
              "Status":1, //0: disabled. 1: enabled.
              "Content":"(?:\\D|^)((?:(?:25[0-4]|2[0-4]\\d|1\\d{2}|[1-9]\\d{1})\\.)(?:(?:25
  [0-5]|2[0-4]\\d|[01]? \\d? \\d)\\.){2} (?:25[0-5]|2[0-4]\\d|1[0-9]\\d|[1-9]\\d|[1-9]))(?:
  \\D|$)",
              "CategoryName":"Regular expression",
              "RiskLevelName":"Internal",
              "DepartName":"KF",
              "LoginName":"det****",
              "Id":2000
          }
      ],
      "TotalCount":18,
      "PageSize":10,
      "CurrentPage":1
  }
       
  ```

<a id="section-7-3-19"></a>

### 7.3.19. CreateRule

Description

You can call this operation to create a custom rule.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>CreateRule</em>. |
| Name | String | Yes | The name of the rule. |
| Content | String | Yes | The content of the rule. |
| Category | Integer | Yes | The type of the rule. Valid values:<br>• <em>0</em>: keyword.<br>• <em>2</em>: regular expression. |
| RiskLevelId | Long | Yes | The ID of the risk level. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |

Error codes

For a list of error codes, see Error codes.

Examples

- Sample request

  ```text
  https://sddp-api.[RegionId].aliyuncs.com/?Action=CreateRule
  &Name=Mobile phone number
  &Category=0
  &Content=1300000****
  &RiskLevelId=4
  &<Common request parameters>
  ```

- Sample success response in JSON format

  ```json
  {
      "RequestId":"208B016D-4CB9-4A85-96A5-0B8ED1EBF271"
  }
  ```

<a id="section-7-3-20"></a>

### 7.3.20. ModifyRule

Description

You can call this operation to modify a custom rule.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>ModifyRule</em>. |
| Id | Long | Yes | The ID of the rule. |
| Name | String | Yes | The name of the rule. |
| Content | String | Yes | The content of the rule. |
| Category | Integer | Yes | The type of the rule. Valid values:<br>• <em>0</em>: keyword.<br>• <em>2</em>: regular expression. |
| RiskLevelId | Long | Yes | The ID of the risk level. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |

Error codes

For a list of error codes, see Error codes.

Examples

- Sample request

  ```text
  https://sddp-api.[RegionId].example.com/?Action=ModifyRule
  &Id=1
  &Name=Mobile phone number
  &Category=0
  &Content=1300000****
  &RiskLevelId=4
  &<Common request parameters>
  ```

- Sample success response in JSON format

  ```json
  {
      "RequestId":"208B016D-4CB9-4A85-96A5-0B8ED1EBF271"
  }
  ```

<a id="section-7-3-21"></a>

### 7.3.21. ModifyRuleStatus

Description

You can call this operation to enable or disable a rule.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>ModifyRuleStatus</em>. |
| Id | Long | Yes | The ID of the rule. |
| Status | Integer | Yes | The status of the rule. Valid values:<br>• <em>0</em>: disabled.<br>• <em>1</em>: enabled. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |

Error codes

For a list of error codes, see Error codes.

Examples

- Sample request

  ```text
  https://sddp-api.[RegionId].example.com/?Action=ModifyRuleStatus
  &Id=1
  &Status=1
  &<Common request parameters>
  ```

- Sample success response in JSON format

  ```json
  {
      "RequestId":"208B016D-4CB9-4A85-96A5-0B8ED1EBF271"
  }
  ```

<a id="section-7-3-22"></a>

### 7.3.22. DeleteRule

Description

You can call this operation to delete a custom rule.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>DeleteRule</em>. |
| Id | Long | Yes | The ID of the rule. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |

Error codes

For a list of error codes, see Error codes.

Examples

- Sample request

  ```text
  https://sddp-api.[RegionId].example.com/?Action=DeleteRule
  &Id=1
  &<Common request parameters>
  ```

- Sample success response in JSON format

  ```json
  {
      "RequestId":"208B016D-4CB9-4A85-96A5-0B8ED1EBF271"
  }
  ```

<a id="section-7-3-23"></a>

### 7.3.23. DescribeDataLimitSet

Description

You can call this operation to query the instances, databases, or buckets of a specified service that Sensitive Data Discovery and Protection (SDDP) is authorized to scan.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>DescribeDataLimitSet</em>. |
| ResourceType | Integer | Yes | The ID of the service. Valid values:<br>• <em>1</em>: MaxCompute.<br>• <em>2</em>: Object Storage Service (OSS).<br>• <em>5</em>: Relational Database Service (RDS). |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| DataLimitList | Array | The list of instances that SDDP is authorized to scan. |
| Id | Long | The ID of the primary key. |
| RegionId | String | The ID of the region. |
| LocalName | String | The name of the region. |
| ParentId | String | The name of the instance. |
| UserName | String | The username. |
| Password | String | The password. |
| Connector | String | The connection string of the database. |
| OssBucketList | Array | The list of existing OSS buckets. |
| RegionId | String | The ID of the region. |
| BucketName | String | The name of the OSS bucket. |
| RegionList | Array | The list of regions. |
| RegionId | String | The ID of the region. |
| LocalName | String | The name of the region. |

Error codes

For a list of error codes, see Error codes.

Examples

- Sample request

  ```text
  https://sddp-api.[RegionId].example.com/?Action=DescribeDataLimitSet
  &ResourceType=1
  &<Common request parameters>
  ```

- Sample success response in JSON format

  ```json
  {
      "RequestId":"769FB3C1-F4C9-42DF-9B72-7077A8989C13",
      "DataLimitSet":{
          "ResourceType":1,
          "DataLimitList":[
              {
                  "Id":1,
                  "RegionId":"cn-hangzhou",
                  "LocalName":"China (Hangzhou)",
                  "ParentId":"oss-bucket",
                  "UserName":"Username",
                  "Password":"Password",
                  "Connector":"Connection string"
              }
          ],
          "OssBucketList":[
              {
                  "RegionId":"cn-hangzhou",
                  "BucketName":"oss-bucket"
              }
          ],
          "RegionList":[
              {
                  "RegionId":"cn-hangzhou",
                  "LocalName":"Hangzhou"
              }
          ]
      }
  }
  ```

<a id="section-7-3-24"></a>

### 7.3.24. CreateDataLimit

Description

Authorizes SDDP to scan instances, databases, or buckets of a specified service.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>CreateDataLimit</em>. |
| ResourceType | Integer | Yes | The ID of the service. Valid values:<br>• <em>1</em>: MaxCompute<br>• <em>2</em>: OSS<br>• <em>5</em>: RDS |
| ResourceType | String | Yes | The ID of the region. |
| ParentId | String | Yes | The name of the instance. |
| UserName | String | Yes | The username. |
| Password | String | Yes | The password. |
| Connector | String | Yes | The connection string of the database. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |

Error codes

For a list of error codes, see Error codes.

Examples

- Sample requests

  ```text
  https://sddp-api.[ RegionId].example.com/?Action=CreateDataLimit
  &ResourceType=1
  &ServiceRegionId=cn-hangzhou
  &ParentId=test
  &UserName=<userName>
  &Password=<passWord>
  @Connector=jdbc:mysql://localhost:3306/test
  &<Common request parameters>
  ```

- Sample success responses in JSON format

  ```json
  {
      "RequestId":"7C3AC882-E5A8-4855-BE77-B6837B695EF1"
  }
  ```

<a id="section-7-3-25"></a>

### 7.3.25. DeleteDataLimit

Description

Revokes permissions granted to SDDP for scanning instances, databases, or buckets of a specified service.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.<br>Set the value to <em>DeleteDataLimit</em>. |
| Id | Long | Yes | The authorization ID. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |

Error codes

For a list of error codes, see Error codes.

Examples

- Sample requests

  ```text
  https://sddp-api.[ RegionId].example.com/?Action=DeleteDataLimit
  &Id=1
  &<Common request parameters>
  ```

- Sample success responses in JSON format

  ```json
  {
      "RequestId":"208B016D-4CB9-4A85-96A5-0B8ED1EBF271"
  }
  ```

<a id="section-7-4"></a>

## 7.4. Data dictionaries

<a id="section-7-4-1"></a>

### 7.4.1. Operation type definition

| ID | Description |
| --- | --- |
| 1 | Get |
| 2 | CreateDelete |
| 3 | Operate |
| 4 | Read |
| 5 | Write |
| 6 | List |
| 7 | CreateTable |
| 8 | CreateInstance |
| 9 | CreateFunction |
| 10 | CreateResource |
| 11 | CreateJob |
| 12 | CreateVolume |
| 13 | CreateOfflineModel |
| 14 | CreateXflow |
| 15 | All |
| 16 | Describe |
| 17 | Select |
| 18 | Alter |
| 19 | Update |
| 20 | Drop |
| 21 | Create |
| 22 | Delete |
| 23 | Modify |
| 24 | Insert |
| 201 | CreateBucket |
| 202 | ModifyBucket |
| 203 | GetBucket |
| 204 | DeleteBucket |
| 205 | CreateObject |
| 206 | ModifyObject |
| 207 | GetObject |
| 208 | DeleteObject |
| 301 | LoadData |
| 302 | DumpData |
| 303 | Show |

<a id="section-7-4-2"></a>

### 7.4.2. Resource type definition

| ID | Name | Description |
| --- | --- | --- |
| 1 | ODPS_PROJECT | MaxCompute project |
| 2 | ODPS_TABLE | MaxCompute table |
| 3 | ODPS_PACKAGE | MaxCompute package |
| 4 | ODPS_PACKAGE_TABLE | Table in a MaxCompute package |
| 5 | ODPS_COLUMN | MaxCompute column |
| 21 | OSS_BUCKET | OSS bucket |
| 31 | OTS_INSTANCE | Table Store instance |
| 32 | OTS_TABLE | Table Store table |

<a id="section-7-4-3"></a>

### 7.4.3. Risk level definition

| ID | Name | Description |
| --- | --- | --- |
| 1 | S1 | Weak risk level |
| 2 | S2 | Medium risk level |
| 3 | S3 | High risk level |
| 4 | S4 | Highest risk level |

<a id="section-8"></a>

# 8.Security Operations Center

<a id="section-8-1"></a>

## 8.1. List of operations by function

The following tables list API operations available for use in Security Operations Center (SOC). For more information, see the corresponding operation description.

| Operation | Description |
| --- | --- |
| QueryDataCount | You can call this operation to query data on attacks, alerts, security risks, and protected departments. |
| GetAssetCount | You can call this operation to query the information of assets added within a specified time range and the information of all assets. |
| GetEcsProtectCount | You can call this operation to query the number of ECS instances with an online Server Guard agent and the number of ECS instances with an offline agent. |
| DescribeAttacks |  |
| DescribeAlarms |  |
| DescribeVulFrangs |  |
| DescribeHcFrangs |  |
| DescribePBLineFrangs | You can call this operation to query the baseline risks on the platform. |
| QueryDataEnum | You can call this operation to query the types of attacks, alerts, and security risks. |
| QueryDataCodeValue | You can call this operation to query the code of a specified server configuration type. |
| QueryDataDistribution | You can call this operation to query the number of a specified type of security issue. |
| SaveOrUpdateSocReportTask | You can call this operation to create or modify report tasks. |
| QuerySocReportTasks | You can call this operation to query report tasks. |
| DelSocReportTask | You can call this operation to delete a report task. |
| QuerySocReportRecords | You can call this operation to query the report records of a specified report task. |
| GetDeptMap | You can call this operation to obtain a list of departments. |
| GetRegionMap | You can call this operation to obtain a list of regions to which your assets belong. |
| DownloadFile | You can call this operation to export a report on the assets. |
| GetEcsList | You can call this operation to obtain a list of ECS instances. |
| GetDiskList | You can call this operation to query disk information of ECS instances. |
| GetSecurityGroupList | You can call this operation to obtain a list of security groups. |
| GetEcsInfo | You can call this operation to query the details of a specified ECS instance. |
| GetRdsList | You can call this operation to query ApsaraDB RDS instances. |
| GetRdsInstanceIPArrayList | You can call this operation to query the whitelists configured for an ApsaraDB RDS instance. |
| GetRdsInfo | You can call this operation to obtain a list of OSS buckets. |
| GetOssList | You can call this operation to obtain a list of OSS buckets. |
| GetSlbList | You can call this operation to obtain a list of SLB instances. |
| GetEipList | You can call this operation to obtain a list of Elastic IP addresses. |
| GetAlarmConfig | You can call this operation to query the alert configuration. |
| UpdateAlarmConfig | You can call this operation to update the alert configuration. |
| GetAlarmContacts | You can call this operation to obtain a list of alert recipients. |
| AddAlarmContacts | You can call this operation to add an alert recipient or modify alert recipient information. |
| DeleteAlarmContacts | You can call this operation to delete alert recipients. |
| SendAlarm | You can call this operation to send an alert. |
| QuerySource | You can call this operation to query log sources. |
| QueryType | You can call this operation to query the types of logs from a specified log source. |
| QueryLog | You can call this operation to query log records from a specified log source. |
| GetVpcList | You can call this operation to obtain a list of VPCs. |
| GetMachineList | You can call this operation to obtain a list of assets. |
| GetMachineInfo | You can call this operation to query asset information. |
| DescribeSocUsers | You can call this operation to query users. |
| DeleteSocUser | You can call this operation to delete a user. |
| SaveOrUpdateSocUser | You can call this operation to add a user or modify user information. |

<a id="section-8-2"></a>

## 8.2. Request method

<a id="section-8-2-1"></a>

### 8.2.1. Request syntax

Description

where:

- `endpoint` : the endpoint of the Security Operations Center (SOC) API is  `yundunnewsoc-pop.[ Regio nId].example.com` .

  Note

- `Action` : the name of the operation being performed.

  For example, if  `Action=GetEcsProtectCount` ,You can call this operation to query the number of ECS instances with an online Server Guard agent and the number of ECS instances with an offline agent.

<a id="section-8-2-2"></a>

### 8.2.2. Sign API requests

Apsara Stack Security authenticates each access request. Therefore, a request must contain signature information regardless of whether it is sent over HTTP or HTTPS.

Authorization

To ensure the security of your account, we recommend that you use a RAM user to call API operations. Before you use a RAM user to call an API operation, you must grant the RAM user the required permissions by creating an policy and attaching the policy to the RAM user.

API signature

You must sign all API requests to ensure security. Alibaba Cloud uses the request signature to verify the identity of the API caller. When you manually make an API request, you must use the AccessKey secret to calculate an HMAC value based on the encoded and sorted request string. The HMAC value is the signature. For more information, see the definition in RFC 2104.

The following parameters are used in the following procedure to describe how to calculate a signature.

| Parameter | Description |
| --- | --- |
| Endpoint | <code>http://yundunnewsoc-pop.[ RegionId].example.com/?</code> |
| Operation-specific parameters | <code>Action=GetEcsProtectCount</code> |
| Common parameters except Signature | <code>&amp;Timestamp=2016-02-23T12:46:24Z</code><br><code>&amp;Format=JSON</code><br><code>&amp;AccessKeyId=&lt;yourAccessKeyId&gt;</code><br><code>&amp;SignatureMethod=HMAC-SHA1</code><br><code>&amp;SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf</code><br><code>&amp;Version=2019-07-23</code><br><code>&amp;SignatureVersion=1.0</code> |
| AccessKey secret | <code>&lt;yourAccessKeySecret&gt;</code> |

1. Create a canonicalized query string by arranging the request parameters.

   Note

   The request parameters include operation-specific parameters and all common

   request parameters except Signature.

   <ol type="i">

   <li>

   Sort the request parameters.

   </li>

   </ol>

   Sort the request parameters in alphabetical order.

   <ol type="i" start="2">

   <li>

   Encode the parameters.

   </li>

   </ol>

   Encode the canonicalized query string in UTF-8 based on the following rules:

   - Uppercase letters, lowercase letters, digits, and some special characters such as hyphens (-), underscores (_), periods (.), and tildes (~) do not need to be encoded.

   - Other characters must be percent encoded in the %XY format. XY represents the ASCII code of the characters in hexadecimal notation. For example, double quotation marks (") are encoded as %22.

   - Extended UTF-8 characters are encoded in the %XY%ZA… format.

   - Spaces must be encoded as %20. Do not encode spaces as plus signs (+).

   <ol type="i" start="3">

   <li>

   Connect the encoded parameter names and values by using equal signs (=).

   </li>

   <li>

   Sort the pairs of parameter names and values that are connected by using equal signs (=) in

   </li>

   </ol>

   alphabetical order. Connect the pairs with ampersands (&) to create a canonicalized query string.

2. Create a string-to-sign from the encoded canonicalized query string based on the following rule:

   ```text
   StringToSign=HTTPMethod + "&" + percentEncode("/") + "&" +
   percentEncode(CanonicalizedQueryString)
   ```

3. Calculate the HMAC value of the string-to-sign based on the HMAC definition in RFC 2104.

   Note

   Your AccessKey secret in combination with an ampersand (&) (ASCII:38) is used as

   the key for the HMAC calculation. The SHA1 algorithm is used to calculate the HMAC value of the string-to-sign.

4. Encode the HMAC value in Base64 to obtain the signature string.

   ```text
   LEW8N4y7Uasop******
   ```

5. Add the signature string to the request as the Signature parameter. The result is the signed API request.

<a id="section-8-2-3"></a>

### 8.2.3. Common parameters

Common request parameters must be included in all Apsara Stack Security API requests, such as the API version number and authentication information.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Version | String | Yes | The version number of the API. The value is in the format of YYYY-MM-DD.<br>Set the value to <em>2019-07-23</em>. |
| AccessKeyId | String | Yes | The AccessKey ID provided to you by Alibaba Cloud. |
| Signature | String | Yes | The signature string of the current request. |
| SignatureMethod | String | Yes | The encryption method of the signature string.<br>Set the value to <em>HMAC-SHA1</em>. |
| Timestamp | String | Yes | The timestamp of the request. Specify the time in the ISO 8601 standard in the <code> YYYY-MM-DDThh:mm:ssZ </code> format. The time must be in UTC.<br>For example, 2014-05-26T12:00:00Z indicates 20:00:00 on May 26, 2014 (UTC+8). |
| SignatureVersion | String | Yes | The version of the signature encryption algorithm. Set the value to <em>1.0</em>. |
| SignatureNonce | String | Yes | A unique, random number used to prevent replay attacks. You must use different numbers for different requests. |
| ResourceOwnerAc count | String | No | The owner account (the logon username) of the resource you want to access by using this API request. |
| Format | String | No | The format of the response.<br>Valid values: <em>JSON and XML</em>. Default value: XML. |

<a id="section-8-2-4"></a>

### 8.2.4. Response structure

Apsara Stack Security API responses can be returned in either the XML or JSON format. Every response returns a unique ID (indicated by RequestId) regardless of whether the call is successful.

Sample responses (XML format)

```xml
<? xml version="1.0" encoding="UTF-8"? >
<! --The root node of the result-->
<Operation name+Response>
    <! --Returned request ID-->
    <RequestId>4C467B38-3910-447D-87BC-AC049166F216</RequestId>
    <! --Returned data-->
</Operation name+Response>
```

Sample responses (JSON format)

```json
{
"RequestId": "4C467B38-3910-447D-87BC-AC049166F216",
/* Returned data */
}
```

<a id="section-8-3"></a>

## 8.3. Operations

<a id="section-8-3-1"></a>

### 8.3.1. QueryDataCount

You can call this operation to query data on attacks, alerts, security risks, and protected departments.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.Set the value to <em>QueryDataCount</em>. |
| ApiName | String | Yes | The object to query. Valid values:<br>• <em>describeNewAttackCount</em>: the number of new attacks<br>• <em>describeAttackCount</em>: the total number of attacks<br>• <em>describeNewAlarmCount</em>: the number of new alerts<br>• <em>describeAlarmCount</em>: the total number of alerts<br>• <em>describeUnProcessedAlarmCount</em>: the number of unhandled alerts<br>• <em>describeNewFrangCount</em>: the number of new security risks<br>• <em>describeFrangCount</em>: the total number of security risks<br>• <em>describeUnprocessedFrangCount</em>: the number of unhandled security risks<br>• <em>describeUserCount</em>: the number of protected departments |
| TimeSpan | String | No | The time range to query.<br>• <em>0</em>: past 24 hours<br>• <em>1</em>: last seven days<br>• <em>2</em>: last 30 days |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| Count | Long | The result of the query. |

Examples

Sample requests

```text
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=QueryDataCount
&TimeSpan=0
&ApiName=describeAttackCount
&<Common request parameters>
```

Sample success responses in JSON format

```json
{
    "code":200,
    "data":{
        "Data":{"Count":5011}
    },
    "requestId":"E404ADE2-D7FB-43B5-BDC9-31CBEF3EEDAC",
    "success":true
}
```

Error codes

For a list of error codes, visit the Error codes.

<a id="section-8-3-2"></a>

### 8.3.2. GetAssetCount

You can call this operation to query the information of assets added within a specified time range and the information of all assets.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.Set the value to <em>GetAssetCount</em>. |
| Aliuid | Long | Yes | The ID of the user. |
| StartDate | Long | No | The beginning of the time range where the assets to query were created. |
| EndDate | Long | No | The end of the time range where the assets to query were added. |
| TimeSpan | Integer | No | The unit of the time range. Valid values:<br>• <em>0</em>: day<br>• <em>1</em>: week<br>• <em>2</em>: month |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| AllAsset | Array | A list of all assets. |
| └Value | String | The number of assets. |
| └Key | String | The type of the asset. |
| NewAsset | Array | A list of new assets. |
| └Value | String | The number of new assets. |
| └Key | String | The type of the new asset. |

Examples

Sample requests

```text
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=GetAssetCount
&TimeSpan=0
&<Common request parameters>
```

Sample success responses in JSON format

```json
{
   "RequestId":"DBA8A3BC-5C61-494D-9B11-6DDC6E14D92C",
  "Data":{
    "NewAsset":[//A list of assets added within the period from StartDate to EndDate
      {
        "Value":"49",
        "Key":"ecsCount"
      },
      {
        "Value":"54",
        "Key":"rdsCount"
      },
      {
        "Value":"68",
        "Key":"ossCount"
      },
      {
        "Value":"20",
        "Key":"eipCount"
      },
      {
        "Value":"20",
        "Key":"slbCount"
      }
    ],
    "AllAsset":[//A list of all assets
      {
        "Value":"49",
        "Key":"ecsCount"
      },
      {
        "Value":"54",
        "Key":"rdsCount"
      },
      {
        "Value":"68",
        "Key":"ossCount"
      },
      {
        "Value":"20",
        "Key":"eipCount"
      },
      {
        "Value":"20",
        "Key":"slbCount"
      }
    ]
  }
}
```

Error codes

For a list of error codes, visit the Error codes.

<a id="section-8-3-3"></a>

### 8.3.3. GetEcsProtectCount

You can call this operation to query the number of ECS instances with an online Server Guard agent and the number of ECS instances with an offline agent.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.Set the value to <em>GetEcsProtectCount</em>. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| Total | Integer | The total number of entries. |
| Items | Array | The ECS protection data. |
| └Key | String | The protection status of the ECS instance. Valid values:<br>• <em>ecsCount</em>: The ECS instance is protected.<br>• <em>offlineCount</em>: The ECS instance is not protected.<br>Note If the value is offlineCount, the ECS instance is online, but the Server Guard agent is offline. |
| └Value | Integer | The number of ECS instances.<br>• If Key is <em>ecsCount</em>, this parameter indicates the number of protected ECS instances.<br>• If Key is <em>offlineCount</em>, this parameter indicates the number of unprotected ECS instances. |

Examples

Sample requests

```text
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=GetEcsProtectCount
&<Common request parameters>
```

Sample success responses in JSON format

```json
{
    "RequestId":"4D1E89E0-3140-46F2-808D-7D7940F65087",
    "Data":{
        "Total":1,
        "Items":[
            {
                "Value":"0",//The number of ECS instances on which the Server Guard agent is offline.
                "Key":"offlineCount"//The number of ECS instances on which the Server Guardagent is offline.
            },
            {
                "Value":"0",//The number of ECS instances.
                "Key":"ecsCount"//The number of ECS instances.
            }
        ]
    }
}
```

Error codes

For a list of error codes, visit the Error codes.

<a id="section-8-3-4"></a>

### 8.3.4. DescribeAttacks

You can call this operation to query attacks on users or on the platform based on specified conditions.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.Set the value to <em>DescribeAttacks</em>. |
| DataScope | Integer | Yes | Specifies whether the attacks on users or on the platform are queried. Valid values:<br>• <em>0</em>: platform<br>• <em>1</em>: users |
| SourceFrom | Integer | No | The source of attack data. |
| UserId | Long | No | The ID of the department to query. |
| PageSize | Integer | Yes | The number of attacks to return on each page. |
| PageNo | Integer | Yes | The number of the page to return. |
| AttackType | String | No | The type of the attacks to query. |
| ProcessState | Integer | No | The processing status of the attacks to query.<br>• <em>0</em>: An alert has been generated on the attack.<br>• <em>1</em>: The attack has been blocked.<br>• <em>3</em>: The attack traffic is being scrubbed.<br>• <em>4</em>: The attack traffic has been scrubbed. |
| StartTime | Long | No | The beginning of the time range to query. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC. |
| EndTime | Long | No | The end of the time range to query. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC. |
| KeyWord | String | No | The keyword of the attack name or asset name. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| PageNo | Integer | The page number of the returned page. |
| PageSize | Integer | The number of attacks returned per page. |
| Total | Integer | The total number of records. |
| RequestId | String | The ID of the request. |
| AttackName | String | The name of the attack. |
| AttackId | Long | The ID of the attack. |
| AssetType | Integer | The type of the asset. |
| Asset | String | The ID of the asset. |
| UserName | String | The name of the department. |
| RaisedTime | Long | The time of the attack. |
| ProcessState | Integer | The processing status of the attack. |
| UserId | Long | The ID of the user or department. |
| AttackType | String | The type of the attack. |
| SourceFrom | Integer | The data source of the attack. |
| AttackerIp | String | The IP address of the attacker. |
| AssetName | String | The name of the asset. |
| AssetPublicIps | String | The public IP address of the affected asset. |
| AssetPrivateIps | String | The internal IP address of the affected asset. |

Examples

Sample requests

```text
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=DescribeAttacks
&DataScope=1
&PageSize=20
&PageNo=1
&<Common request parameters>
```

Sample success responses in JSON format

```json
{
    "code":200,
    "data":{
        "Data":{
            "PageSize":20,
            "Total":222,
            "Items":[
                {
                    "UserName":"yundun****",
                    "SourceFrom":46,
                    "AttackType":"Brute-force",
                    "AttackerIp":"172. *. *.105",
                    "AssetName":"monodb****",
                    "SourceFromIp":"172. *. *.105",
                    "AssetPrivateIps":"172. *. *.92",
                    "AssetType":"ECS",
                    "UserId":163957166417****,
                    "AssetPublicIps":"",
                    "Asset":"0fbc7e34-b1f6-4eeb-b100-130c15eb1c3b",
            "RaisedTime":1572921381000
        }
            ],
            "PageNo":1
        }
    },
    "requestId":"69C66589-F448-4A47-BFEA-EC12F55DCB53",
    "success":true
}
```

Error codes

For a list of error codes, visit the Error codes.

<a id="section-8-3-5"></a>

### 8.3.5. DescribeAlarms

You can call this operation to query security alerts on users or on the platform based on specified conditions.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.Set the value to <em>DescribeAlarms</em>. |
| DataScope | Integer | Yes | Specifies whether the alerts on users or the platform are queried. Valid values:<br>• <em>0</em>: platform<br>• <em>1</em>: users |
| SourceFrom | Integer | No | The data source of security alerts. |
| UserId | Long | No | The ID of the department to query. |
| PageSize | Integer | Yes | The number of alerts to return on each page. |
| PageNo | Integer | Yes | The number of the page to return. |
| AlarmType | String | No | The type of the alerts to query. |
| ProcessState | Integer | No | The processing status of the alerts to query. |
| KeyWord | String | No | The keywords of the alerts or keywords in the ID or names of assets related to the alerts. |
| RiskLevels | List&lt;Integer&gt; | No | The risk levels of the alerts to query. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| AlarmId | Long | The ID of the alert. |
| RiskLevel | Integer | The risk level of the alert. |
| AlarmName | String | The name of the alert. |
| AssetType | String | The type of the asset. |
| Asset | String | The ID of the asset. |
| UserName | String | The user name. |
| UserId | Long | The ID of the user or platform. |
| RaisedTime | Long | The time when the alert was generated. |
| ProcessState | Integer | The processing status of the alert. |
| AlarmType | String | The type of the alert. |
| SourceFrom | Integer | The data source of the alert. |
| AttackerIp | String | The IP address of the attacker. |
| AssetName | String | The name of the asset. |
| AssetPublicIps | String | The public IP address of the affected asset. |
| AssetPrivateIps | String | The internal IP address of the affected asset. |
| AlarmUniqueInfo | String | The unique key of the alert. |
| LastTime | String | The last time when the alert was generated. |
| Total | Integer | The total number of entries returned. |

Examples

Sample requests

```text
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=DescribeAlarms
&RiskLevels=[0,1,2]
&DataScope=1
&PageSize=20
&PageNo=1
&<Common request parameters>
```

Sample success responses in JSON format

```json
{
    "code":200,
    "data":{
        "Data":{
            "PageSize":20,
            "Total":177,
            "Items":[
                {
                    "AlarmId":30307,
                    "UserName":"yundun****",
                    "AlarmType":"Malicious Process",
                    "SourceFrom":20,
                    "AssetName":"yun****",
                    "AssetPrivateIps":"192. *. *.1",
                    "ProcessState":1,
                    "AssetType":"ECS",
                    "AlarmName":"Mining process",
                    "UserId":1****,
                    "AlarmUniqueInfo":"34dsa1",
                    "AssetPublicIps":"10. *. *.1",
                    "Asset":"2f43eb69-****",
                    "RaisedTime":1571826361000,
                    "RiskLevel":2,
                    "LastTime":1573021501000
                }
            ],
            "PageNo":1
        }
    },
    "requestId":"B2C5D1EB-202F-4132-A763-2D16538B****",
    "success":true
}
```

Error codes

For a list of error codes, visit the Error codes.

<a id="section-8-3-6"></a>

### 8.3.6. DescribeVulFrangs

You can call this operation to query vulnerabilities.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.Set the value to <em>DescribeVulFrangs</em>. |
| UserId | Long | No | The ID of the department to query. |
| RiskLevels | Integer | No | The severity of the vulnerabilities to query. |
| ProcessState | Integer | No | The processing status of the vulnerabilities to query. |
| Page | Integer | Yes | The number of the page to return. |
| PageSize | Integer | Yes | The number of entries to return on each page. |
| VulType | String | No | The type of the vulnerabilities to query. |
| KeyWord | String | No | The name of the vulnerability or asset to query. |
| DataScope | Integer | Yes | Specifies whether the data of users or the platform is queried. Valid values:<br>• <em>0</em>: platform<br>• <em>1</em>: users |
| NeedFix | String | No | Specifies whether the vulnerabilities to query require fixes. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| PageSize | Integer | The number of entries returned per page. |
| PageNo | Integer | The page number of the returned page. |
| Total | Integer | The number of entries returned. |
| Items | Array | The list of vulnerabilities. |
| └LastTime | Long | The last time when the vulnerability was detected. |
| └RiskLevel | Integer | The severity of the vulnerability. |
| └ProcessState | Integer | The processing status of the vulnerability. |
| └AssetType | String | The type of the affected asset. |
| └NeedFix | String | Indicates whether the vulnerability requires a fix. |
| └VulRelated | String | The ID of the vulnerability details. |
| └Asset | String | The ID of the asset affected by the vulnerability. |
| └SourceFrom | Integer | The data source. |
| └Id | Long | The ID of the vulnerability. |
| └RaisedTime | Long | The first time when the vulnerability was detected. |
| └VulName | String | The name of the vulnerability. |
| └VulType | String | The type of the vulnerability. |
| └AssetPublicIps | String | The public IP address of the affected asset. |
| └AssetPrivateIps | String | The internal IP address of the affected asset. |
| └AssetName | String | The name of the affected asset. |

Examples

Sample requests

```text
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=DescribeVulFrangs
&DataScope=1
&PageSize=20
&Page=1
&<Common request parameters>
```

Sample success responses in JSON format

```json
{
    "code":200,
    "data":{
        "Data":{
            "PageSize":20,
            "Total":445,
            "Items":[
                {
                    "ProcessState":1,
                    "AssetType":"ECS",
                    "NeedFix":"later",
                    "VulRelated":"CVE-2016-5195",
                    "Asset":"eb9ea4b0-****",
                    "SourceFrom":1,
                    "Id":6370,
                    "RaisedTime":2019,
                    "RiskLevel":1,
                    "VulName":"RHSA-2017:0372: kernel-aarch64 security and bug fix update",
                    "LastTime":"2019-11-05 17:12:12",
                    "VulType":"cve"
                }
            ],
            "PageNo":1
        }
    },
    "requestId":"32B57B56-958C-49C5-BB49-0BABE2060305",
    "success":true
}
```

Error codes

For a list of error codes, visit the Error codes.

<a id="section-8-3-7"></a>

### 8.3.7. DescribeHcFrangs

You can call this operation to query the risks in the server configurations set by the user.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.Set the value to <em>DescribeHcFrangs</em>. |
| ProcessState | Integer | No | The processing status of the risks to query. |
| HcType | String | No | The type of server configuration risks to query. |
| Page | Integer | Yes | The number of the page to return. |
| PageSize | Integer | Yes | The number of entries to return on each page. |
| KeyWord | String | No | The server baseline name or asset name. |
| DataScope | Integer | Yes | Specifies whether the data of users or the platform is queried. Valid values:<br>• <em>0</em>: platform<br>• <em>1</em>: users |
| UserId | Long | No | The ID of the department to query. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| PageSize | Integer | The number of entries returned per page. |
| PageNo | Integer | The page number of the returned page. |
| Total | Integer | The total number of the returned entries. |
| Items | Array | The list of servers that SOC is authorized to scan. |
| └lastFoundTime | Long | The last time when risks were detected. |
| └RiskLevel | Integer | The level of the risk. Valid values:<br>• <em>0</em>: low<br>• <em>1</em>: medium<br>• <em>3</em>: high |
| └ProcessState | Integer | The processing status of the risk.<br>• <em>1</em>: handled<br>• <em>2</em>: unhandled |
| └HcName | String | The name of the server configuration risk. |
| └HcType | String | The type of the server configuration risk. |
| └UserName | String | The name of the department to which the affected asset belongs. |
| └UserId | Long | The ID of the department to which the affected asset belongs. |
| └SourceFrom | Integer | The data source. |
| └Id | Long | The ID of the entry. |
| └Asset | String | The ID of the affected asset. |
| └AssetType | String | The type of the affected asset. |
| └AssetName | String | The name of the affected asset. |
| └AssetPublicIps | String | The public IP address of the affected asset. |
| └AssetPrivateIps | String | The internal IP address of the affected asset. |

Examples

Sample requests

```text
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=DescribeHcFrangs
&DataScope=1
&PageSize=20
&Page=1
&<Common request parameters>
```

Sample success responses in JSON format

```json
{
    "code":200,
    "data":{
        "Data":{
            "PageSize":20,
            "Total":47,
            "Items":[
                {
                    "UserName":"yun****",
                    "SourceFrom":2,
                    "HcType":"Alibaba Cloud",
                    "AssetName":"yun3 ",
                    "LastFoundTime":"2019-11-06 01:03:55",
                    "AssetPrivateIps":"192. *. *.1",
                    "ProcessState":1,
                    "HcName":"Alibaba Cloud Standard",
                    "AssetType":"ECS",
                    "UserId":11424,
                    "AssetPublicIps":"10. *. *.1",
                    "Asset":"71513dfc ",
                    "Id":111,
                    "RiskLevel":2
                }
            ],
            "PageNo":1
        }
    },
    "requestId":"FE7137B7-84D8-4AF7-969B-C0DF5118****",
    "success":true
}
```

Error codes

For a list of error codes, visit the Error codes.

<a id="section-8-3-8"></a>

### 8.3.8. DescribePBLineFrangs

You can call this operation to query the baseline risks on the platform.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.Set the value to <em>DescribePBLineFrangs</em>. |
| BLType | String | No | The risk type to query. |
| Keyword | String | No | The name of the platform baseline to query. |
| BLLevel | Integer | No | The risk level to query. |
| ProcessState | Integer | No | The processing status of the baseline risks to query. |
| Page | Integer | Yes | The number of the page to return. |
| PageSize | Integer | Yes | The number of entries to return on each page. |
| DataScope | Integer | Yes | Specifies whether the data of users or the platform is queried. Valid values:<br>• <em>0</em>: platform<br>• <em>1</em>: users |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| BLLevel | Integer | The level of the risk. |
| ProcessState | Integer | The processing status of the risk. |
| UserName | String | The name of the department affected by the risk. |
| UserId | Long | The ID of the department affected by the risk. |
| BLName | String | The name of the baseline. |
| SourceFrom | Integer | The data source. |
| Id | Long | The ID of the entry. |

Examples

Sample requests

```text
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=DescribePBLineFrangs
&BLType=Network Security
&DataScope=0
&PageSize=20
&Page=1
&<Common request parameters>
```

Sample success responses in JSON format

```json
{
    "code":200,
    "data":{
        "Data":{
            "PageSize":20,
            "Total":1,
            "Items":[
                {
                    "BLLevel":1,
                    "ProcessState":1,
                    "BLType":"Network Security",
                    "UserName":"Platform",
                    "UserId":-1,
                    "BLName":"VPC Isolation Audit",
                    "SourceFrom":5,
                    "Id":6572
                }
            ],
            "PageNo":1
        }
    },
    "requestId":"FDAB3658-E2CD-4C95-BFF5-D0CF204C57D8",
    "success":true
}
```

Error codes

For a list of error codes, visit the Error codes.

<a id="section-8-3-9"></a>

### 8.3.9. QueryDataEnum

You can call this operation to query the types of attacks, alerts, and security risks.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.Set the value to <em>QueryDataEnum</em>. |
| ApiName | String | Yes | The object to query. Valid values:<br>• <em>alarmType</em>: types of alerts<br>• <em>attackType</em>: types of attacks<br>• <em>frangVulInnerType</em>: types of vulnerabilities<br>• <em>frangPBlineInnerType</em>: types of baseline risks on the cloud platform |
| DataScope | Integer | Yes | Specifies whether the data of users or the platform is queried. Valid values:<br>• <em>0</em>: platform<br>• <em>1</em>: users |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| Value | String | The query result. |

Examples

Sample requests

```text
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=QueryDataEnum
&ApiName=frangPBlineRisk
&DataScope=0
&<Common request parameters>
```

Sample success responses in JSON format

```json
{
    "code":200,
    "data":{
        "Data":[
            {
                "Value":"Suspicious Process"
            },
            {
                "Value":"System Backdoor"
            },
            {
                "Value":"Suspicious User Operation"
            },
            {
                "Value":"Suspicious Process"
            },
            {
                "Value":"Malicious Process"
            },
            {
                "Value":"Webshell"
            },
            {
                "Value":"Unusual Network Connection"
            }
        ]
    },
    "requestId":"47738BF3-5F11-437C-88EC-27E91D0E3158",
    "success":true
}
```

Error codes

For a list of error codes, visit the Error codes.

<a id="section-8-3-10"></a>

### 8.3.10. QueryDataCodeValue

You can call this operation to query the code of a specified server configuration type.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.Set the value to <em>QueryDataCodeValue</em>. |
| ApiName | String | Yes | The object to query. Valid values:<br>The object to query. Set the value to <em>frangHcInnerType</em>. |
| DataScope | Integer | Yes | Specifies whether the data of users or the platform is queried. Valid values:<br>• <em>0</em>: platform<br>• <em>1</em>: users |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| Value | String | The type of server configuration. |
| Code | String | The code of the server configuration type. |

Examples

Sample requests

```text
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=QueryDataCodeValue
&ApiName=frangHcInnerType
&DataScope=0
&<Common request parameters>
```

Sample success responses in JSON format

```json
{
    "code": 200,
    "data": {
        "Data": [{
            "Value": "Ubuntu security baseline check based on Alibaba Cloud standard",
            "Code": "xxx"
        }, {
            "Value": "Ubuntu 14 Security Baseline Check based on CIS Standard",
            "Code": "yyy"
        }]
    },
    "requestId": "7B773594-74A7-4920-9D3D-4EAFA45BC248",
    "success": true
}
```

Error codes

For a list of error codes, visit the Error codes.

<a id="section-8-3-11"></a>

### 8.3.11. QueryDataDistribution

You can call this operation to query the number of a specified type of security issue.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.Set the value to <em>QueryDataDistribution</em>. |
| ApiName | String | Yes | The type of the security issue to query.Valid values:<br>• <em>frangVulRisk</em>: vulnerabilities<br>• <em>frangHcRisk</em>: server configuration risks<br>• <em>alarmRisk</em>: alerts<br>• <em>frangPBlineRisk</em>: platform baseline risks |
| DataScope | Integer | Yes | Specifies whether the issues on users or on the platform are queried. Valid values:<br>• <em>0</em>: platform<br>• <em>1</em>: users |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| Type | Integer | The risk level of the issue. |
| Count | Integer | The number of the queried issue. |

Examples

Sample requests

```text
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=QueryDataDistribution
&ApiName=frangPBlineRisk
&DataScope=0
&<Common request parameters>
```

Sample success responses in JSON format

```json
{
    "code":200,
    "data":{
        "Data":[
            {
                "Type":1,
                "Count":1
            }
        ]
    },
    "requestId":"6A50A942-15FC-45ED-8242-E88710749B2F",
    "success":true
}
```

Error codes

For a list of error codes, visit the Error codes.

<a id="section-8-3-12"></a>

### 8.3.12. SaveOrUpdateSocReportTask

You can call this operation to create or modify report tasks.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.Set the value to <em>SaveOrUpdateSocReportTask</em>. |
| Id | Long | No. If you want to modify a report task, this parameter is required. | The ID of the report task.<br>Note<br>• This parameter is optional when you create a report task.<br>• This parameter is required when you modify a report task. |
| Name | String | No. If you want to create a report task, this parameter is required. | The name of the report task.<br>Note<br>• This parameter is required when you create a report task.<br>• This parameter is optional when you modify a report task. |
| Type | String | No. If you want to create a report task, this parameter is required. | The type of the report. Valid values:<br>• <em>day</em>: daily report<br>• <em>week</em>: weekly report<br>• <em>month</em>: monthly report<br>Note<br>• This parameter is required when you create a report task.<br>• This parameter is optional when you modify a report task. |
| DeptIds | String | No | The ID of the department related to the report. Separate multiple department IDs with commas (,). |
| Emails | String | No. If you want to create a report task, this parameter is required. | The email address that is used to receive reports. Separate multiple email addresses with commas (,).<br>Note<br>• This parameter is required when you create a report task.<br>• This parameter is optional when you modify a report task. |
| Aliuid | Long | Yes | The ID of the department to which the report creator belongs. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| Code | Integer | The HTTP status code. |
| Message | String | Indicates whether the operation is successful. |

Examples

Sample requests

```text
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=SaveOrUpdateSocReportTask
&Name=AAA****
&Type=day
&Emails=1999****@qq.com,1888****@163.com
&DeptIds=1231231,123123,1231231
&Aliuid=12312****
&<Common request parameters>
```

Sample success responses in JSON format

```json
{
    "code":200,
    "data":{},
    "requestId":"FDAB3658-E2CD-4C95-BFF5-D0CF204C57D8",
    "success":true
}          
```

Error codes

For a list of error codes, visit the Error codes.

<a id="section-8-3-13"></a>

### 8.3.13. QuerySocReportTasks

You can call this operation to query report tasks.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.Set the value to <em>QuerySocReportTasks</em>. |
| PageNo | Integer | Yes | The number of the page to return. |
| PageSize | Integer | Yes | The number of entries to return on each page. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| PageNo | Integer | The page number of the returned page. |
| PageSize | Integer | The number of entries returned per page. |
| Total | Integer | The total number of entries. |
| GmtModified | Long | The time when the report was modified. |
| CreatorName | String | The user name of the report creator. |
| CreatorId | Long | The user ID of the report creator. |
| Type | String | The type of the report task. |
| GmtCreate | Long | The time when the report was created. |
| RecordNum | Integer | The number of reports generated by the report task. |
| Emails | String | The email address that receives reports. |
| Name | String | The name of the report task. |
| Id | Long | The ID of the report task. |
| LastFinishExcuteTime | String | The last time when the report task finished generating a report. |
| NextBeginExcuteTime | String | The next time when the report task begins to generate a report. |
| LastFinishExcuteTimeSta mp | Long | The last timestamp when the report task finished generating a report. |
| NextBeginExcuteTimeSt amp | Long | The next timestamp when the report task begins to generate a report. |

Examples

Sample requests

```text
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=QuerySocReportTasks
&PageNo=1
&PageSize=10
&<Common request parameters>
```

Sample success responses in JSON format

```json
{
    "code":200,
    "data":{
        "Data":{
            "PageSize":10,
            "Total":8,
            "Items":[
                {
                    "PageSize":10,
                    "CreatorId":114247173828****,
                    "GmtModified":"2019-11-06T10:04Z",
                    "NextBeginExcuteTime":"2019-11-07T00:00Z",
                    "Lang":"zh",
                    "Name":"New report asdasd",
                    "DeptIds":"176597162720****,163957166417****",
                    "Type":"day",
                    "GmtCreate":"2019-11-06T10:04Z",
                    "NextBeginExcuteTimeStamp":1573084800000,
                    "PageNo":1,
                    "Emails":"as****@qq.com",
                    "Id":11,
                    "CreatorName":"dtdep-5-157173828****"
                }
            ],
            "PageNo":1
        }
    },
    "requestId":"3051F0D5-4F6D-4239-BE25-8150784BECCB",
    "success":true
}         
```

Error codes

For a list of error codes, visit the Error codes.

<a id="section-8-3-14"></a>

### 8.3.14. DelSocReportTask

You can call this operation to delete a report task.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.Set the value to <em>DelSocReportTask</em>. |
| Id | Integer | Yes | The ID of the report task.<br>You can call the QuerySocReportTasks operation to query the ID of a report task. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |

Examples

Sample requests

```text
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=DelSocReportTask
&<Common request parameters>
&Id=12
```

Sample success responses in JSON format

```json
{
    "code":200,
    "data":{},
    "requestId":"0AE9A558-A193-4E72-B2CE-6A351BFABDEF",
    "success":true
}
```

Error codes

For a list of error codes, visit the Error codes.

<a id="section-8-3-15"></a>

### 8.3.15. QuerySocReportRecords

You can call this operation to query the report records of a specified report task.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.Set the value to <em>QuerySocReportRecords</em>. |
| PageNo | Integer | Yes | The number of the page to return. |
| PageSize | Integer | Yes | The number of entries to return on each page. |
| Id | Integer | Yes | The ID of the report task.<br>You can call the QuerySocReportTasks operation to query the ID of a report task. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| BeginTimeStamp | Long | The start timestamp of the record. |
| ReportLink | String | The unique key of the report. |
| TaskId | Integer | The ID of the report task. |
| FinishTime | String | The end time of the record. |
| TaskName | String | The name of the report task. |
| BeginTime | String | The start time of the record. |
| FinishTimeStamp | Long | The end timestamp of the record. |
| Id | Integer | The ID of the record. |

Examples

Sample requests

```text
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=QuerySocReportRecords
&PageNo=1
&PageSize=10
&Id=5
&<Common request parameters>
```

Sample success responses in JSON format

```json
{
    "code":200,
    "data":{
        "Data":{
            "PageSize":10,
            "Total":1
            "Items":[
                {
                    "BeginTimeStamp":1572833105000,
                    "ReportLink":"5_week_2019-11-04",
                    "TaskId":5,
                    "FinishTime":"2019-11-04T02:05Z",
                    "PageSize":10,
                    "TaskName":"Weekly report 1024",
                    "BeginTime":"2019-11-04T02:05Z",
                    "FinishTimeStamp":1572833108000,
                    "PageNo":1,
                    "Id":131
                }
            ],
            "PageNo":1
        }
    },
    "requestId":"58294830-FD53-415B-AADE-F189CA9B2E72",
    "success":true
}
```

Error codes

For a list of error codes, visit the Error codes.

<a id="section-8-3-16"></a>

### 8.3.16. GetDeptMap

You can call this operation to obtain a list of departments.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.Set the value to <em>GetDeptMap</em>. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| Items | Array | The list of departments. |
| └Key | Long | The ID of the department. |
| └Value | String | The name of the department. |

Examples

Sample requests

```text
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=GetDeptMap
&<Common request parameters>
```

Sample success responses in JSON format

```json
{
    "code":200,
    "data":{
        "Data":{
            "PageSize":0,
            "Total":8,
            "Items":[
                {
                    "Value":"admin",
                    "Key":"176597162720****"
                },
                {
                    "Value":"yundun",
                    "Key":"163957166417****"
                }
            ],
            "PageNo":0
        }
    },
    "requestId":"CA964E09-D0B5-4B34-93C8-35E882E8DD04",
    "success":true
}
```

Error codes

For a list of error codes, visit the Error codes.

<a id="section-8-3-17"></a>

### 8.3.17. GetRegionMap

You can call this operation to obtain a list of regions to which your assets belong.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.Set the value to <em>GetRegionMap</em>. |
| UserId | Long | No | The ID of the department. |
|  |  |  |  |
| Parameter | Type | Required | Description |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| Items | Array | The list of regions. |
| └Key | String | The ID of the region. |
| └Value | String | The name of the region. |

Examples

Sample requests

```text
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=GetRegionMap
&<Common request parameters>
```

Sample success responses in JSON format

```json
{
    "RequestId":"DF618C9E-6B58-43A0-8E8A-B91162F198F4",
    "data":{
        "items":[
            {
                "key":"cn-qingdao",
                "value":"China (Qingdao)"
            },
            {
                "key":"cn-beijing",
                "value":"China (Beijing)"
            }
        ],
        "total":2
    }
}
```

Error codes

For a list of error codes, visit the Error codes.

<a id="section-8-3-18"></a>

### 8.3.18. DownloadFile

You can call this operation to export a report on the assets.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.Set the value to <em>DownloadFile</em>. |
| Aliuid | Long | No | The ID of the department. |
| Region | String | No | The region to query. |
| PageNo | Integer | No | The number of the page to return.Default value: <em>1</em> |
| PageSize | Integer | No | The number of entries to return on each page. Default value: <em>10</em> |
| ProcessState | Integer | No | The processing state of the assets to query. |
| SartDate | String | No | The beginning of the time range during which the instances to query were created. |
| EendDate | String | No | The end of the time range during which the instances to query were created. |
| Kyword | Integer | No | The keywords for query. |
| AsetType | String | Yes | The type of the assets to query. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| Key | String | The identifier of the link from which you can download the report. |
| Value | String | The link from which you can download the report. |

Examples

Sample requests

```text
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=DownloadFile
&Asettype=ecs
&<Common request parameters>
```

Sample success responses in JSON format

```json
{
   "RequestId":"A4823F6E-5A22-4603-BC68-AF60CE038149",
    "Data":{
        "Value":"http://11. *. *.6:18080/download_file.do?assetType=ecs&pageNo=1&pageSize=10&lang=zh&sortWord=instance_create_time&sortType=desc",
        "Key":"downloadUrl"
    }
}
```

Error codes

For a list of error codes, visit the Error codes.

<a id="section-8-3-19"></a>

### 8.3.19. GetEcsList

You can call this operation to obtain a list of ECS instances.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.Set the value to <em>GetEcsList</em>. |
| Aliuid | Long | No | The ID of the department. |
| Region | String | No | The region to query. |
| StartDate | String | No | The beginning of the time range during which the instances to query were created. |
| EndDate | String | No | The end of the time range during which the instances to query were created. |
| ProcessState | Integer | No | The processing state of the instances to query. |
| PageNo | Integer | No | The number of the page to return. |
| PageSize | Integer | No | The number of entries to return on each page. |
| KeyWord | String | No | The keywords for the query. |
| SecurityGroupId | String | No | The ID of the security group to which the instances to query belong. |
| InstanceStatus | String | No | The states of the instances to query. By default, all states are selected.<br>• <em>Running</em><br>• <em>Starting</em><br>• <em>Stopping</em><br>• <em>Stopped</em> |
| EventFlag | Boolean | No | Specifies whether the instances to query are related to security events. |
| VulFlag | Boolean | No | Specifies whether the instances to query have vulnerabilities. |
| FrangFlag | Boolean | No | Specifies whether the instances to query have security risks. |
| ScurityGroupFlag | Boolean | No | Specifies whether the instances to query belong to suspicious security groups. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| PageNo | Integer | The page number of the returned page. |
| PageSize | Integer | The number of entries returned per page. |
| Total | Integer | The total number of entries. |
| Items | Array | The list of instances. |
| └Uuid | Long | The UUID of the ECS instance. |
| └reationTime | String | The time when the instance was created. |
| └InstanceCreateTime | Long | The time when the instance was created. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC. |
| └eate | Long | The name of the baseline associated with the instance. |
| └Eip | String | The Elastic IP address associated with the instance. |
| └encryptedDisk | String | The disk encryption information. |
| └eventCount | Integer | The number of security events related to the instance. |
| └innerIps | String | The internal IP address of the instance. |
| └instanceId | String | The ID of the instance. |
| └instanceName | String | The name of the instance. |
| └instanceStatus | String | The status of the instance. |
| └loginName | String | The username. |
| └osType | String | The operating system of the instance. |
| └publicIps | String | The public IP address of the instance. |
| └privateIps | String | The internal IP address of the instance. |
| └securityGroupIds | String | The IDs of the security groups. |
| └suspectSecurityGroup Count | Integer | The number of suspicious security groups. |
| └vulCount | Integer | The number of vulnerabilities detected on the instance. |
| └frangCount | Integer | The number of security risks detected on the instance. |
| └vpcId | String | The ID of the VPC network connected to the instance. |
| └aegisOnlineStatus | String | Indicates whether the Server Guard client is online. |
| └hostname | String | The name of the server. |
| └Cpu | Integer | The number of CPU cores. |
| └Memery | Integer | The size of memory. |
| └instanceNetworkType | String | The network type of the ECS instance. |

Examples

Sample requests

```text
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=GetEcsList
&PageNo=1
&PageSize=20
&<Common request parameters>
```

Sample success responses in JSON format

```json
{
    "code":200,
    "data":{
        "Data":{
            "PageSize":1,
            "Total":41,
            "Items":[
                {
                    "LoginName":"dtdep-4-157166417****",
                    "EventCount":6,
                    "InstanceCreateTime":1572228180000,
                    "Cpu":1,
                    "InstanceNetworkType":"vpc",
                    "EncryptedDisk":"0/1",
                    "OsType":"linux",
                    "InstanceStatus":"Running",
                    "DeptName":"yundun",
                    "Aliuid":163957166417****,
                    "Status":1,
                    "AegisOnlineStatus":"online",
                    "InstanceId":"i-3zn05zrit4i77ucl****",
                    "Hostname":"iZ3zn05zrit4i77ucl2****",
                    "SecurityGroupIds":"sg-3zn05zrit4i45cm4****",
                    "Eip":"",
                    "VulCount":0,
                    "Memery":2048,
                    "InstanceName":"sastestcenteros",
                    "Uuid":"325491ec-a64d-4d93-82d3-296314a9e8d5",
                    "VpcId":"vpc-3znsfwch9ilwlc0tk****",
                    "FrangCount":0,
                    "PrivateIps":"172. *. *.98",
                    "CreationTime":"2019-10-28T02:03Z",
                    "SuspectSecurityGroupCount":1,
                    "RegionId":"cn-qingdao-env8d****"
                }
            ],
            "PageNo":1
        }
    },
    "requestId":"BBF5CA91-4D69-4A57-8F0C-42989CA4E60F",
    "success":true
}
```

Error codes

For a list of error codes, visit the Error codes.

<a id="section-8-3-20"></a>

### 8.3.20. GetDiskList

You can call this operation to query disk information of ECS instances.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.Set the value to <em>GetDiskList</em>. |
| Aliuid | Long | No | The department to query. |
| Region | String | No | The region to query. |
| PageNo | Integer | No | The number of the page to return.Default value: <em>1</em> |
| PageSize | Integer | No | The number of entries to return on each page. Default value: <em>10</em> |
| ProcessState | Integer | No | The state of the disk. |
| Keyword | Integer | No | The keywords for query. |
| InstanceId | String | No | The ID of the ECS instance to query. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| Total | Integer | The total number of entries. |
| Items | Array | The list of disks. |
| └DeptNmae | String | The name of the department. |
| └Device | String | The mount point of the disk. |
| └diskId | String | The ID of the disk. |
| └diskName | String | The name of the disk. |
| └diskStatus | String | The usage status of the disk. |
| └Encrypted | Integer | Indicates whether the disk is encrypted. Valid values:<br>• <em>0</em>: no<br>• <em>1</em>: yes |
| └instanceId | String | The ID of the instance to which the disk belongs. |
| └InstanceName | String | The name of the instance to which the disk belongs. |
| └Size | Integer | The size of the disk. |
| └snapshotsCount | Integer | The number of snapshots. |
| └snapshotsTime | String | The time when the latest snapshot was created. |
| └Type | String | The type of the disk. |

Examples

Sample requests

```text
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=GetDiskList
&<Common request parameters>
```

Sample success responses in JSON format

```json
{
    "RequestId":"DF618C9E-6B58-43A0-8E8A-B91162F198F4",
    "data":{
        "items":[
            {
                "deptName":"cbctestdept****",
                "device":"/dev/xvdc",
                "diskId":"d-m5ef1im6qv2airbkocd2",
                "diskName":"cbctest",
                "diskStatus":"In_use",
                "encrypted":0,
                "instanceId":"i-m5eg3vpxqgaf9wox****",
                "instanceName":"cbctestinstance****",
                "size":20,
                "snapshotsCount":7,
                "snapshotsTime":"1536662000",
                "type":"data"
            }
        ],
        "total":1
    }
}
```

Error codes

For a list of error codes, visit the Error codes.

<a id="section-8-3-21"></a>

### 8.3.21. GetSecurityGroupList

You can call this operation to obtain a list of security groups.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.Set the value to <em>GetSecurityGroupList</em>. |
| Aliuid | Long | No | The department to query. |
| Region | String | No | The region to query. |
| PageNo | Integer | No | The number of the page to return.Default value: <em>1</em> |
| PageSize | Integer | No | The number of entries to return on each page. Default value: <em>10</em> |
| ProcessState | Integer | No | The processing state of the security groups to query. |
| Keyword | Integer | No | The keywords for query. |
| ScurityGroupIds | List | No | The list of security group IDs. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the instance. |
| Total | Integer | The total number of entries. |
| Items | Array | The list of security groups. |
| └Create | Long | The ID of the user that created the security group. |
| └createTime | String | The time when the security group was created. |
| └instanceCreateTime | Long | The time when the instance in the security group was created. |
| └DeptName | String | The name of the department. |
| └Description | String | The description of the security group. |
| └instanceCount | Integer | The number of instances in the security group. |
| └networkType | String | The network type of the security group. |
| └permissionsCount | Integer | The number of rules configured for the security group. |
| └regionId | String | The ID of the region. |
| └securityGroupId | String | The ID of the security group. |
| └securityGroupName | String | The name of the security group. |
| └suspectRule | String | Indicates whether the security group is related to suspicious rules. |

Examples

Sample requests

```text
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=GetSecurityGroupList
&<Common request parameters>
```

Sample success responses in JSON format

```json
{
    "RequestId":"DF618C9E-6B58-43A0-8E8A-B91162F198F4",
    "data":{
        "items":[
            {
                "create":1533110868000,
                "createTime":"2017-02-06T07:28:00Z",
                "instanceCreateTime":1537177380000,
                "deptName":"cbcTestDeptName",
                "description":"System created security group.",
                "instanceCount":3,
                "networkType":"vpc",
                "permissionsCount":8,
                "regionId":"cn-qingdao",
                "securityGroupId":"sg-m5e1f71l9kck0zh8pfry",
                "securityGroupName":"cbcgroup2",
                "suspectRule":true
            }
        ],
        "total":1
}
```

Error codes

For a list of error codes, visit the Error codes.

<a id="section-8-3-22"></a>

### 8.3.22. GetEcsInfo

You can call this operation to query the details of a specified ECS instance.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.Set the value to <em>GetEcsInfo</em>. |
| Uuid | String | Yes | The UUID of the ECS instance to query. |
| IstanceId | String | No | The ID of the ECS instance to query. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| Aliuid | Long | The ID of the user to which the ECS instance belongs. |
| Uuid | Long | The UUID of the ECS instance. |
| reationTime | String | The time when the instance was created. |
| InstanceCreateTime | Long | The timestamp when the instance was created. |
| eate | Long | The name of the baseline. |
| Eip | String | The Elastic IP address bound to the ECS instance. |
| encryptedDisk | String | The disk encryption status. |
| eventCount | Integer | The number of security events detected on the instance. |
| innerIps | String | The internal IP address of the instance. |
| instanceId | String | The ID of the instance. |
| instanceName | String | The name of the instance. |
| instanceStatus | String | The status of the instance. |
| loginName | String | The name of the user. |
| osType | String | The operating system of the instance. |
| publicIps | String | The public IP address of the instance. |
| privateIps | String | The internal IP address of the instance. |
| securityGroupIds | String | The IDs of the security groups to which the instance belongs. |
| suspectSecurityGroupCo unt | Integer | The number of suspicious security groups. |
| vulCount | Integer | The number of vulnerabilities detected on the instance. |
| frangCount | Integer | The number of security risks detected on the instance. |
| vpcId | String | The ID of the VPC to which the ECS instance is connected. |
| aegisOnlineStatus | String | Indicates whether the Server Guard client is online. |
| hostname | String | The name of the server. |
| Cpu | Integer | The number of CPU cores. |
| Memery | Integer | The size of memory. |
| instanceNetworkType | String | The network type of the ECS instance. |
| SecurityGroupIdList | Array | The information of the security group to which the ECS instance belongs. |
| Disks | Array | The disk information. |

Examples

Sample requests

```text
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=GetEcsInfo
&Uuid=7e77b1db-c29a-4548-8b32-533e3ae859da
&<Common request parameters>
```

Sample success responses in JSON format

```json
{
    "RequestId":"52734A7E-8E8B-46B1-822D-512A2A3085D3",
    "Data":{
        "Status":1,
        "LoginName":"bluecat****",
        "EventCount":0,
        "InstanceId":"i-m5eg3vpxqgaf9wox****",
        "InstanceCreateTime":1536564900000,
        "hostName":"m5e0hm705p9bhnd****",//The server name.
        "cpu":3,//The number of CPU cores.
        "memery":1024//The memory size.
        "instanceNetworkType":"vpc",//The network type.
        "SecurityGroupIdList":[
            {
                "InstanceCount":0,
                "Description":"System created security group.",
                "SecurityGroupName":"cbcgroup1",
                "PermissionsCount":0,
                "Create":1564045933000,
                "SecurityGroupId":"sg-m5e0hm705p9bhnd4xrsl",
                "DeptName":"Front end",
                "RegionId":"cn-qingdao"
            }
        ],
        "SecurityGroupIds":"sg-m5e0hm705p9bhnd4xrsl,sg-m5e8f3oy2h9b0hc8u6as",
        "Eip":"",
        "VulCount":0,
        "InstanceName":"cbctestinst****",
        "Uuid":"7e77b1db-c29a-4548-8b32-533e3ae859da",
        "PublicIps":"47. *. *.111",
        "OsType":"linux",
        "PrivateIps":"172. *. *.117",
        "InstanceStatus":"Stopped",
                "VpcId": "sg-m5e0",//vpcid
        "CreationTime":"2018-09-10T07:35Z",
        "Disks":[{"deptName": "cbctestdeptName",
            "device": "/dev/xvdc",
            "diskId": "d-m5ef1im6qv2airbk****",
            "diskName": "cbctest",
            "diskStatus": "In_use",
            "encrypted": 0,
            "instanceId": "i-m5eg3vpxqgaf9wox****",
            "instanceName": "cbctestinstanceName",
            "size": 20,
            "snapshotsCount": 7,
            "snapshotsTime": "1536662000",
            "type": "data"
        }],
        "DeptName":"Technical Department",
        "SuspectSecurityGroupCount":2,
        "RegionId":"cn-qingdao",
        "Aliuid":31234****
    }
}        
```

Error codes

For a list of error codes, visit the Error codes.

<a id="section-8-3-23"></a>

### 8.3.23. GetRdsList

You can call this operation to query ApsaraDB RDS instances.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.Set the value to <em>GetRdsList</em>. |
| Aliuid | Long | No | The ID of the department. |
| Region | String | No | The region where the instances to query are located. |
| PageNo | Integer | No | The number of the page to return.Default value: <em>1</em> |
| PageSize | Integer | No | The number of entries to return on each page. Default value: <em>10</em> |
| ProcessState | Integer | No | The processing state of the instances to query. |
| Keyword | Integer | No | The keywords for query. |
| StartDate | String | No | The beginning of the time range during which the instances to query were created. |
| EndDate | String | No | The end of the time range during which the instances to query were created. |
| InstanceStatus | String | No | The state of the instances to query. By default, all states are selected.<br>• <em>Creating</em><br>• <em>Running</em><br>• <em>Deleting</em><br>• <em>Rebooting</em><br>• <em>DBInstanceClassChanging</em>: queries instances that are being upgraded or downgraded.<br>• <em>TRANSING</em>: queries instances that are being migrated.<br>• <em>EngineVersionUpgrading</em>: queries instances that are being upgraded.<br>• <em>TransingToOthers</em>: queries instances whose data is being migrated to other instances.<br>• <em>GuardDBInstanceCreating</em>: queries instances for which a disaster recovery instance is being created.<br>• <em>Restoring</em>: queries instances that are restoring backup data.<br>• <em>Importing</em>: queries instances that are importing data.<br>• <em>ImportingFromOthers</em>: queries instances that are importing data from other ApsaraDB RDS instances.<br>• <em>DBInstanceNetTypeChanging</em>: queries instances that are switching between the internal network and the Internet.<br>• <em>GuardSwitching</em>: queries instances under disaster recover failover.<br>• <em>INS_CLONING</em>: queries instances that are being cloned. |
| whitelistIPLevel | String | No | The strictness degree of the whitelists to query. By default, all degrees are selected.<br>• <em>rds_whitelistiplevel_low</em>: loose<br>• <em>rds_whitelistiplevel_middle</em>: moderate<br>• <em>rds_whitelistiplevel_high</em>: strict |
| tdeFlag | Integer | No | Specifies whether Transparent Data Encryption (TDE) is enabled for the instances to query. By default, all options are selected.<br>• <em>0</em>: disabled<br>• <em>1</em>: enabled |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| Id | Integer | The total number of entries. |
| deptName | String | The name of the department. |
| backupRetentionPeriod | Integer | The number of retained backups. |
| backupTimes | String | The frequency at which the instance data is backed up. |
| create | Long | The timestamp when the instance was created. |
| instanceCreateTime | Long | The time when the instance was created. |
| creationTime | String | The time when the data in this instance was synchronized to SOC. |
| dbInstanceDescription | String | The name of the instance. |
| dbInstanceId | String | The ID of the instance. |
| dbInstanceStatus | String | The status of the instance. |
| Engine | String | The database engine used by the instance. |
| instanceNetworkType | String | The network type of the instance. |
| sslFlag | Integer | Indicates whether SSL encryption is enabled. Valid values:<br>• <em>0</em>: disabled<br>• <em>1</em>: enabled |
| tdeFlag | Integer | Indicates whether TDE is enabled. Valid values:<br>• <em>0</em>: disabled<br>• <em>1</em>: enabled |
| whitelistIPLevel | String | The strictness degree of the IP address whitelist. |

Examples

Sample requests

```text
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=GetRdsList
&<Common request parameters>
```

Sample success responses in JSON format

```json
{
    "code": 200,
    "data": {
        "items": [{
            "id": 10,//The primary key of the instance, which can be used to query details.
            "deptName": "cbcdept",//The department name.
            "backupRetentionPeriod": "7",//The number of backups.
            "backupTimes": "4/7",//The frequency at which the instance data is backed up.
            "create": 1536725464000,//The time when the data in this instance was synchronized to SOC.
            "instanceCreateTime": 1537177380000,//The time when the instance was created.
            "creationTime": "2018-09-12T12:11:4Z",
            "dbInstanceDescription": "cbctestrdsvpc2",//The instance name.
            "dbInstanceId": "rm-m5es6x22suia0****",//The instance ID.
            "dbInstanceStatus": "Running",//The instance status.
            "engine": "MySQL",//The database engine used by the instance.
            "instanceNetworkType": "vpc",//The network type of the instance.
            "sslFlag": 0,//Indicates that SSL encrytion is disabled.
            "tdeFlag": 1,//Indicates that TDE is enabled.
            "whitelistIPLevel": "rds_whitelistiplevel_middle"//The strictness degree of the
IP address whitelist.
        }, {
            "id": 9,//The primary key of the instance.
            "deptName": "cbcdept",//The department name.
            "backupRetentionPeriod": "7",
            "backupTimes": "4/7",
            "create": 1536725464000,
            "creationTime": "2018-09-12T12:11:4Z",
            "dbInstanceDescription": "cbctestrdsvpc",
            "dbInstanceId": "rm-m5ekf1602691f****",
            "dbInstanceStatus": "Running",
            "engine": "MySQL",
            "instanceNetworkType": "VPC",
            "sslFlag": 1,
            "tdeFlag": 0,
            "whitelistIPLevel": "rds_whitelistiplevel_middle"
        }],
        "total": 2
    },
    "message": "successful",
    "success": true
}
```

Error codes

For a list of error codes, visit the Error codes.

<a id="section-8-3-24"></a>

### 8.3.24. GetRdsInstanceIPArrayList

You can call this operation to query the whitelists configured for an ApsaraDB RDS instance.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.Set the value to <em>GetRdsInstanceIPArrayList</em>. |
| instanceId | Long | Yes | The ID of the ApsaraDB RDS instance to query. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| dbInstanceIPArrayName | String | The name of the IP address whitelist. |
| securityIPList | String | The IP addresses in the whitelist. |

Examples

Sample requests

```text
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=GetRdsInstanceIPArrayList
&InstanceId=12
&<Common request parameters>
```

Sample success responses in JSON format

```json
{
    "RequestId":"DF618C9E-6B58-43A0-8E8A-B91162F198F4",
    "data": {
        "items": [{
            "dbInstanceIPArrayName": "cbctestwhitelistgroup",//The whitelist name.
            "securityIPList": "172. *. *.117,192. *. *.1"//The IP addresses in the whitelist.
        }{
            "dbInstanceIPArrayName": "default",
            "securityIPList": "127.0.0.1"
        }],
        "total": 2
    }
}
```

Error codes

For a list of error codes, visit the Error codes.

<a id="section-8-3-25"></a>

### 8.3.25. GetRdsInfo

You can call this operation to query the details of an ApsaraDB RDS instance.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.Set the value to <em>GetRdsInfo</em>. |
| DbInstanceId | String | Yes | The ID of the ApsaraDB RDS instance to query. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| TdeFlag | Integer | Indicates whether Transparent Data Encryption (TDE) is enabled.<br>• <em>0</em>: disabled<br>• <em>1</em>: enabled |
| BackupTimes | String | The frequency at which the instance data is backed up. |
| DbInstanceStatus | String | The status of the instance. |
| SslFlag | Integer | Indicates whether SSL encryption is enabled. Valid values:<br>• <em>0</em>: disabled<br>• <em>1</em>: enabled |
| InstanceNetworkType | Long | The network type of the instance. |
| Create | String | The timestamp when the instance was created. |
| CreationTime | String | The time when the instance was created. |
| WhitelistIPLevel | String | Indicates the risk level of the IP address in the whitelist.<br>• <em>rds_whitelistiplevel_low</em>: low<br>• <em>rds_whitelistiplevel_middle</em>: medium<br>• <em>rds_whitelistiplevel_high</em>: high |
| DeptName | String | The name of the department. |
| DbInstanceDescription | Integer | The name of the instance. |
| BackupRetentionPeriod | String | The period for which the backup data is retained.Unit: days |
| Aliuid | String | The ID of the department. |
| DbInstanceId | String | The ID of the instance. |
| Engine | String | The database engine used by the instance. |
| RdsWhiteipList | Array | The IP address whitelists configured for the ApsaraDB RDS instance. |
| └DbInstanceIPArrayNa me | String | The name of the IP address whitelist. |
| └SecurityIPList | String | The IP addresses in the whitelist. |

Examples

Sample requests

```text
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=GetRdsInfo
&DbInstanceId=123
&<Common request parameters>
```

Sample success responses in JSON format

```json
{
    "RequestId":"60796AED-1FD6-4769-85FF-322B7990EA99",
    "Data":{
        "TdeFlag":0,
        "BackupTimes":"3/7",
        "DbInstanceStatus":"Running",
        "SslFlag":1,
        "InstanceNetworkType":"vpc",
        "Create":1537521344000,
        "CreationTime":"2018-09-12T16:30Z",
        "WhitelistIPLevel":"rds_whitelistiplevel_high",
        "DeptName":"waf-dept",
        "DbInstanceDescription":"cbctestrdsvpc2",
        "BackupRetentionPeriod":7,
        "Aliuid":12****,
        "DbInstanceId":"rm-m5es6x22suia0****",
        "Engine":"MySQL",
        "RdsWhiteipList":[
            {
                "DbInstanceIPArrayName":"cbctestwhitelistgroup",
                "SecurityIPList":"172. *. *.117,192. *. *.1"
            },
            {
                "DbInstanceIPArrayName":"default",
                "SecurityIPList":"127.0.0.1"
            }
        ]
    }
}
```

Error codes

For a list of error codes, visit the Error codes.

<a id="section-8-3-26"></a>

### 8.3.26. GetOssList

You can call this operation to obtain a list of OSS buckets.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.Set the value to <em>GetOssList</em>. |
| Aliuid | Long | No | The ID of the department. |
| Region | String | No | The region where the buckets to query are located. |
| PageNo | Integer | No | The number of the page to return.Default value: <em>1</em> |
| PageSize | Integer | No | The number of entries to return on each page. Default value: <em>10</em> |
| Keyword | Integer | No | The keywords for query. |
| StartDate | String | No | The beginning of the time range during which the buckets to query were created. |
| EndDate | String | No | The end of the time range during which the buckets to query were created. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| Total | Integer | The total number of entries. |
| allowEmptyReferer | Integer | Indicates whether the OSS bucket allows an access request with an empty Referer header. Valid values:<br>• <em>0</em>: no<br>• <em>1</em>: yes |
| bucketName | String | The name of the instance. |
| cannedACL | String | The ACL permission of the bucket. |
| configRefererList | Integer | Indicates whether a Referer header whitelist is configured.<br>• <em>0</em>: no<br>• <em>1</em>: yes |
| regionId | String | The region where the bucket is located. |
| Size | Integer | The used storage space. |
| instanceCreateTime | Long | The time when the bucket was created. |
| deptName | String | The name of the department. |

Examples

Sample requests

```text
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=GetOssList
&<Common request parameters>
```

Sample success responses in JSON format

```json
{
    "RequestId":"DF618C9E-6B58-43A0-8E8A-B91162F198F4",
    "data": {
        "items": [{
            "allowEmptyReferer": 1,//Indicates whether the OSS bucket allows an access request with an empty Referer header.
            "bucketName": "cbctestoss",//The bucket name.
            "cannedACL": "private",//The ACL permission of the bucket.
            "configRefererList": 1,//Indicates whether a Referer header whitelist is configured.
            "instanceCreateTime": 1537177380000,//The timestamp when the bucket was created.
            "deptName": "cbcTestDept",//The department name.
            "regionId": "oss-cn-qingdao",//The region.
            "size": 3278531//The used storage space. Unit: Byte
        }, {
            "allowEmptyReferer": 0,
            "bucketName": "cbctestoss2",
            "cannedACL": "public-read",
            "configRefererList": 0,
            "instanceCreateTime": 1536828385000,
            "deptName": "cbcTestDept",
            "regionId": "oss-cn-qingdao",
            "size": 1618792
        }],
        "total": 2
    }
}
```

Error codes

For a list of error codes, visit the Error codes.

<a id="section-8-3-27"></a>

### 8.3.27. GetSlbList

You can call this operation to obtain a list of SLB instances.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.Set the value to <em>GetSlbList</em>. |
| Aliuid | Long | No | The ID of the department to query. |
| Region | String | No | The region to query. |
| PageNo | Integer | No | The number of the page to return.Default value: <em>1</em> |
| PageSize | Integer | No | The number of entries to return on each page. Default value: <em>10</em> |
| Keyword | Integer | No | The keywords for query. |
| StartDate | String | No | The beginning of the time range during which the instances to query were created. |
| EndDate | String | No | The end of the time range during which the instances to query were created. |
| instanceStatus | String | No | The status of the instances to query. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| Total | Integer | The total number of entries. |
| address | String | The IP address of the SLB instance. |
| addressType | Long | The network type of the SLB IP address. |
| createTime | Long | The time when the instance was created. |
| instanceCreateTime | Long | The timestamp when the instance was created. |
| DeptName | String | The name of the department. |
| listenerPortAndProtocol | String | The listening protocol and listening port. |
| loadBalancerId | String | The ID of the SLB instance. |
| loadBalancerName | String | The name of the SLB instance. |
| loadBalancerStatus | String | The status of the SLB instance. |
| networkType | String | The network type of the SLB instance. |
| regionId | String | The region where the SLB instance is located. |

Examples

Sample requests

```text
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=GetSlbList
&<Common request parameters>
```

Sample success responses in JSON format

```json
{
    "RequestId":"DF618C9E-6B58-43A0-8E8A-B91162F198F4",
    "data": {
        "items": [{
            "address": "10. *. *.158",//The IP address of the SLB instance.
            "addressType": "intranet",//The network type of the instance IP address.
            "create": 1574222416000,//The time when the instance was created.
            "createTime": 2019-11-20T03:21:47Z,
            "instanceCreateTime": 1574220107000,//The timestamp when the instance was created.
            "deptName": "cbcTestDept",//The department name.
            "listenerPortAndProtocol": "notConfiged",//The listening protocol and listeningport.
            "loadBalancerId": "lb-m5egfr9bph8ki4ork****",//The instance ID.
            "loadBalancerName": "cbc_slb_2",//The instance name.
            "loadBalancerStatus": "inactive",//The instance status.
            "networkType": "classic",//The network type of the instance.
            "regionId": "cn-qingdao"//The region of the instance.
        }, {
            "address": "118. *. *.174",
            "addressType": "internet",
            "create": 1537168200000,
            "createTimeStamp": 1537168251000,
            "deptName": "cbcTestDept",
            "listenerPortAndProtocol": "http:8080@tcp:80",//The listening protocol and listening port.
            "loadBalancerId": "lb-m5e6yqpi4r34lxh5q****",
            "loadBalancerName": "cbc_slb_1",
            "loadBalancerStatus": "active",
            "networkType": "classic",
            "regionId": "cn-qingdao"
        }],
        "total": 2
    }
}
```

Error codes

For a list of error codes, visit the Error codes.

<a id="section-8-3-28"></a>

### 8.3.28. GetEipList

You can call this operation to obtain a list of Elastic IP addresses.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.Set the value to <em>GetEipList</em>. |
| Aliuid | Long | No | The ID of the department to query. |
| Region | String | No | The region to query. |
| PageNo | Integer | No | The number of the page to return.Default value: <em>1</em> |
| PageSize | Integer | No | The number of entries to return on each page. Default value: <em>10</em> |
| Keyword | Integer | No | The keywords for query. |
| StartDate | String | No | The beginning of the time range during which the instances to query were created. |
| EndDate | String | No | The end of the time range during which the instances to query were created. |
| instanceStatus | String | No | The status of the instances to query. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| Total | Integer | The total number of entries. |
| Items | Aray | The list of Elastic IP addresses. |
| └allocationId | Long | The ID of the user who created the instance. |
| └allocationTime | String | The time when the user applied for the instance. |
| └create | Long | The timestamp when the user applied for the instance. |
| └instanceCreateTime | String | The time when the instance was created. |
| └deptName | String | The name of the department. |
| └instanceId | String | The ID of the instance. |
| └instanceName | String | The name of the instance. |
| └instanceType | Integer | The type of the instance. |
| └ipAddress | String | The Elastic IP address. |
| └Bandwidth | String | The peak bandwidth of the Elastic IP address. Unit: Mbit/s. |
| └regionId | String | The region where the instance is located. |
| └eipStatus | String | The status of the Elastic IP address. Valid values:<br>• <em>Associating</em>: The Elastic IP address is being bound to an ECS instance.<br>• <em>Unassociating</em>: The Elastic IP address is being unbound from an ECS instance.<br>• <em>InUse</em>: The Elastic IP address is bound to an instance.<br>• <em>Available</em>: The Elastic IP address is available. |
| └status | Integer | Indicates whether the Elastic IP address is valid.Valid values:<br>• <em>1</em>: valid<br>• <em>0</em>: invalid |

Examples

Sample requests

```text
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=GetEipList
&<Common request parameters>
```

Sample success responses in JSON format

```json
{
    "RequestId":"DF618C9E-6B58-43A0-8E8A-B91162F198F4",
    "data":{
        "items":[
            {
                "allocationId":"eip-m5eg8x8npvmarymgg****",
                "allocationTime":"2018-09-17T09:22:10Z",
                "create":1537147330000,
                "instanceCreateTime":1537177380000,
                "deptName":"cbcTestDept",
                "instanceId":"",
                "instanceName":"cbctestInstance",
                "instanceType":"",
                "ipAddress":"47. *. *.200",
                "regionId":"cn-qingdao",
                "status":"Available"
            }
        ],
        "total":1
    }
}
```

Error codes

For a list of error codes, visit the Error codes.

<a id="section-8-3-29"></a>

### 8.3.29. GetAlarmConfig

You can call this operation to query the alert configuration.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.Set the value to <em>GetAlarmConfig</em>. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| Total | Integer | The total number of entries. |
| PageSize | Integer | The number of entries returned per page. |
| PageNo | Integer | The page number of the returned page. |
| Items | Array | The alert configuration. |
| └Dingding | Integer | Indicates whether to send alerts by DingTalk. Valid values:<br>• <em>1</em>: yes<br>• <em>0</em>: no |
| └Description | String | The description of the alert type. |
| └Mail | String | Indicates whether to send alerts by email. Valid values:<br>• <em>1</em>: yes<br>• <em>0</em>: no |
| └AlarmIdentify | Integer | The identifier of the alert configuration. |
| └Sms | Integer | Indicates whether to send alerts by SMS. Valid values:<br>• <em>1</em>: yes<br>• <em>0</em>: no |
| └Title | Integer | The name of the alert type. |
| └Level | String | The risk level of the alert. |
| └Id | Integer | The ID of the configuration. |
| └category | Integer | Indicates whether the alert source is a user or the platform. Valid values:<br>• <em>1</em>: user<br>• <em>2</em>: platform |

Examples

Sample requests

```text
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=GetAlarmConfig
&<Common request parameters>
```

Sample success responses in JSON format

```json
{
    "RequestId":"385333D5-1796-41EC-A62F-239881EC75E6",
    "Data":{
        "PageSize":10,
        "Total":1,
        "Items":[
            {
                "Dingding":0,
                "Description":"Attackers have intruded into the tenant system by webshells,malicious code, and suspicious processes.",
                "Mail":0,
                "AlarmIdentify":"USER_ALARM",
                "Sms":0,
                "Title":"Security Alerts",
                "Level":"",
                "Id":7,
                "category":1
            }
        ],
        "PageNo":1
    }
}
```

Error codes

For a list of error codes, visit the Error codes.

<a id="section-8-3-30"></a>

### 8.3.30. UpdateAlarmConfig

You can call this operation to update the alert configuration.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.Set the value to <em>UpdateAlarmConfig</em>. |
| Configs | String | Yes | The updated alert configuration. The value is a JSON array. Each object in this array specifies a parameter, such as id, mail, sms, and dingding.<br><code>//Example</code><br><code>[{\"id\":7,\"mail\":1,\"sms\":1</code><br><code>,\"dingding\":1,\"alarmIdentify</code><br><code>\":\"USER_ALARM\"}]</code> |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| Data | String | The result of the operation. |

Examples

Sample requests

```text
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=UpdateAlarmConfig
&<Common request parameters>
```

Sample success responses in JSON format

```json
{
    "RequestId":"15BFC394-3316-4948-BF54-E6B8875DA023",
    "Data":"succes"
}
```

Error codes

For a list of error codes, visit the Error codes.

<a id="section-8-3-31"></a>

### 8.3.31. GetAlarmContacts

You can call this operation to obtain a list of alert recipients.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.Set the value to <em>GetAlarmContacts</em>. |
| PageSize | Integer | No | The number of entries to return on each page. Default value: <em>10</em> |
| PageNo | Integer | No | The number of the page to return.Default value: <em>1</em> |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| Total | Interger | The total number of entries. |
| PageSize | Integer | The number of entries returned per page. |
| PageNo | Integer | The page number of the returned page. |
| Items | Array | The list of alert recipients. |
| └Dingding | Integer | The DingTalk username of the alert recipient. |
| └Mail | String | The email address of the alert recipient. |
| └Id | Integer | The ID of the alert recipient. |
| └Mobile | String | The mobile phone number of the alert recipient. |
| └Name | String | The name of the alert recipient. |

Examples

Sample requests

```text
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=GetAlarmContacts
&<Common request parameters>
```

Sample success responses in JSON format

```json
{
    "RequestId":"4DC990E4-2A59-4F4A-BDE6-CC35B5C730F1",
    "Data":{
        "PageSize":10,
        "Total":1,
        "Items":[
            {
                "Dingding":"dingding",//The Dingtalk username of the alert recipient.
                "Mail":"test@****.com",//The email address of the alert recipient.
                "Id":1,//The ID of the alert recipient.
                "Mobile":"1380000****",//The mobile phone number of the alert recipient.
                "Name":"test"//The name of the alert recipient.
            }
        ],
        "PageNo":1
    }
}
```

Error codes

For a list of error codes, visit the Error codes.

<a id="section-8-3-32"></a>

### 8.3.32. AddAlarmContacts

You can call this operation to add an alert recipient or modify alert recipient information.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.Set the value to <em>AddAlarmContacts</em>. |
| Name | String | Yes | The name of the alert recipient. |
| Mobile | String | No | The mobile phone number of the alert recipient. |
| Id | Long | No | The ID of the alert recipient.<br>• This parameter is optional when you add an alert recipient.<br>• This parameter is required when you modify an alert recipient. |
| Dingding | String | Yes | The DingTalk username of the alert recipient. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| Data | String | The result of the operation. |

Examples

Sample requests

```text
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=AddAlarmContacts
&Name=aaa
&Dingding=123123
&<Common request parameters>
```

Sample success responses in JSON format

```json
{
    "RequestId":"DF618C9E-6B58-43A0-8E8A-B91162F198F4",
    "data": “sucess”
}
```

Error codes

For a list of error codes, visit the Error codes.

<a id="section-8-3-33"></a>

### 8.3.33. DeleteAlarmContacts

You can call this operation to delete alert recipients.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.Set the value to <em>DeleteAlarmContacts</em>. |
| Id | Long | Yes | The ID of the alert recipient to delete. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| Data | String | Indicates whether the alert recipient is deleted. |

Examples

Sample requests

```text
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=DeleteAlarmContacts
&Id=123
&<Common request parameters>
```

Sample success responses in JSON format

```json
{
    "RequestId":"DF618C9E-6B58-43A0-8E8A-B91162F198F4",
    "data":”sucess”
}
```

Error codes

For a list of error codes, visit the Error codes.

<a id="section-8-3-34"></a>

### 8.3.34. SendAlarm

You can call this operation to send an alert.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.Set the value to <em>SendAlarm</em>. |
| AlarmIdentify | String | Yes | The identifier of the alert configuration.<br>• <em>USER_ATTACK</em> indicates an attack on a user.<br>• <em>USER_ALARM</em> indicates a security alert on a user.<br>• <em>USER_FRANG</em> indicates a security risk on a user.<br>• <em>PLATFORM_ATTACK</em> indicates an attack on the platform.<br>• <em>PLATFORM_ALARM</em> indicates a security alert on the platform.<br>• <em>PLATFORM_FRANG</em> indicates a security risk on the platform. |
| Message | String | Yes | The alert message. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| Data | String | Indicates whether the alert is sent. |

Examples

Sample requests

```text
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=SendAlarm
&AlarmIdentify=USER_ATTACK
&Message=aaaaaaaaaa
&<Common request parameters>
```

Sample success responses in JSON format

```json
{
    "RequestId":"DF618C9E-6B58-43A0-8E8A-B91162F198F4",
    "data":”sucess”
}
```

Error codes

For a list of error codes, visit the Error codes.

<a id="section-8-3-35"></a>

### 8.3.35. QuerySource

You can call this operation to query log sources.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.Set the value to <em>QuerySource</em>. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| PageSize | Integer | The number of entries returned per page. |
| PageNo | Integer | The page number of the returned page. |
| Total | Integer | The total number of entries. |
| Items | Array | The list of log sources. |
| └SourceFrom | String | The Chinese name of the log source. |
| └Source | String | The name of the log source. |

Examples

Sample requests

```text
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=QuerySource
&<Common request parameters>
```

Sample success responses in JSON format

```json
{
    "RequestId":"E2E67B85-0CCA-4C5F-90FE-382F4580C2D9",
    "Data":{
        "PageSize":1,
        "Total":1,
        "Items":[
            {
                "SourceName":"Server Guard",
                "Source":"aegis"
            }
        ],
        "PageNo":1
    }
}
```

Error codes

For a list of error codes, visit the Error codes.

<a id="section-8-3-36"></a>

### 8.3.36. QueryType

You can call this operation to query the types of logs from a specified log source.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.Set the value to <em>QueryType</em>. |
| Source | String | Yes | The log source. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| PageSize | Integer | The number of entries to return on each page. |
| PageNo | Integer | The number of the page to return. |
| Total | Integer | The total number of entries. |
| Items | Array | The list of log types. |
| └Id | Long | The ID of the log type. |
| └Topic | String | The name of the log type. |
| └TopicName | String | The Chinese name of the log type. |

Examples

Sample requests

```text
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=QueryType
&Source=beaver
&<Common request parameters>
```

Sample success responses in JSON format

```json
{
    "RequestId":"2D884100-06C5-42BE-B534-FD26A5454FE2",
    "Data":{
        "PageSize":1,
        "Total":1,
        "Items":[
            {
                "Id":1,
                "Topic":"T_MSG_SOFTWARE_INSTALL",
                "TopicName":"Installation software information"
            }
        ],
        "PageNo":1
    }
}
```

Error codes

For a list of error codes, visit the Error codes.

<a id="section-8-3-37"></a>

### 8.3.37. QueryLog

You can call this operation to query log records from a specified log source.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.Set the value to <em>QueryLog</em>. |
| Id | Long | Yes | The ID of the log source. |
| keyword | String | No | The keywords of the log records. |
| From | Long | Yes | The beginning of the time range to query. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC. |
| To | Long | Yes | The end of the time range to query. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC. |
| pageSize | Integer | Yes | The number of entries to return on each page. |
| PageNo | Integer | Yes | The number of the page to return. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| LogList | String | The log content. |
| HistogramList | List | The data in the graph displayed in the console. |
| KeyList | List | A list of the keys of all log records. |

Examples

Sample requests

```text
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=QueryLog
&Id=9
&From=1574149923989
&To=1574236323989
&PageSize=10
&PageNo=1
&<Common request parameters>
```

Sample success responses in JSON format

```json
{
    "LogList":[
        {
            "LogTime":1566273660000,
            "ColumnList":[
                {
                    "Value":"rpm",
                    "TokenList":[
                    ],
                    "Key":"type"
                },
                {
                    "Value":"inet-f74289a3-87fc-4a2d-8d04-b68b21489dd1",
                    "TokenList":[
                    ],
                    "Key":"uuid"
                }
            ],
            "Source":"T_MSG_SOFTWARE_INSTALL"
        },
        {
            "LogTime":1566273660000,
            "ColumnList":[
                {
                    "Value":"success",
                    "TokenList":[
                    ],
                    "Key":"status"
                }
            ],
            "Source":"T_MSG_SOFTWARE_INSTALL"
        }
    ],
    "TotalCount":891,
    "HistogramList":[
        {
            "EndTime":1566292920000,
            "Completed":true,
            "StartTime":1566288000000,
            "Count":0
        }
    ],
    "PageSize":2,
    "RequestId":"4F183A8B-402C-4BE4-83FD-000676AE00DE",
    "KeyList":[
        "app_version",
        "safe_mode",
        "update",
        "task_id",
        "bit",
        "type",
        "uuid",
        "cmd_idx",
        "path",
        "sys_version",
        "execresult",
        "vendor",
        "action",
        "exectime",
        "install_date",
        "seq",
        "etm",
        "app",
        "traceId",
        "product",
        "module_type",
        "ip",
        "os_version",
        "sys_kernel",
        "stm",
        "version",
        "module_id",
        "sys_product",
        "pro_version",
        "sys_vendor",
        "status"
    ]
}
```

Error codes

For a list of error codes, visit the Error codes.

<a id="section-8-3-38"></a>

### 8.3.38. GetVpcList

You can call this operation to obtain a list of VPCs.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.Set the value to <em>GetVpcList</em>. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| Data | List | The list. |
| Items | List | The information of VPCs. |
| Total | Integer | The total number of entries. |

Examples

Sample requests

```text
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=GetVpcList
&<Common request parameters>
```

Sample success responses in JSON format

```json
{
    "RequestId":"D533DCF9-2BFA-490C-99CF-DBA2A4BA6747",
    "Data":{
        "Total":3,
        "Items":[
                {
                "Value":"1",//vpcid
                "Key":"1"//vpcid
            },
            {
                "Value":"vpc-*********************",
                "Key":"vpc-*********************"
            }
            ]
     }
}
```

Error codes

For a list of error codes, visit the Error codes.

<a id="section-8-3-39"></a>

### 8.3.39. GetMachineList

You can call this operation to obtain a list of assets.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.Set the value to <em>GetMachineList</em>. |
| aliUid | Long | No | The AliUid of the department. |
| Region | String | No | The region to query. |
| pageNo | Integer | No | The number of the page to return.Default value: 1. |
| PageSize | Integer | No | The number of entries to return on each page. Default value: 10. |
| StartDate | String | No | The beginning of the time range during which the servers to query were created. |
| EndDate | String | No | The end of the time range during which the servers to query were created. |
| Keyword | String | No | The keyword of the assets to query. |
| EventFlag | Boolean | No | Specifies whether the assets to query are related to alert events. |
| VulFlag | Boolean | No | Specifies whether the assets to query have vulnerabilities. |
| FrangFlag | Boolean | No | Specifies whether the assets to query have security risks. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| Data | List | The list. |
| Items | List | The asset information. |
| Total | Integer | The total number of entries. |
| pageNo | Integer | The page number of the returned page. |
| PageSize | Integer | The number of entries returned per page. |

Examples

Sample requests

```text
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=GetMachineList
&PageSize=10
&PageNo=1
&keyword=aaa
&<Common request parameters>
```

Sample success responses in JSON format

```json
{
    "RequestId":"B06F0BC3-29AE-461A-9C2C-F50319C2FD1B",
    "Data":{
        "PageSize":10,
        "Total":1,
        "Items":[
                    {
                        "ClientStatus":"offline",//Indicates whether the Server Guard client is online.
                        "Uuid":"inet-8a0569b3-15f8-482d-9a9e-cf85760c3b3a",//The UUID of the asset.
                        "InternetIp":"*. *. *. *",//The public IP address of the asset.
                        "IntranetIp":"*. *. *. *",//The internal IP address of the asset.
                        "FrangCount":0,//The number of security risks.
                    "MachineName":"*. *. *. *",//The name of the server.
                        "Os":"linux",//The operating system.
                        "EventCount":0,//The number of attack events.
                        "Aliuid":123456789,//The default AliUid of a physical server is 123456789.
"MachineIp":"*. *. *. *",//The IP address of the server.
                        "VulCount":0//The number of alert events.
                     }
        ],
        "PageNo":1
    }
}
```

Error codes

For a list of error codes, visit the Error codes.

<a id="section-8-3-40"></a>

### 8.3.40. GetMachineInfo

You can call this operation to query asset information.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.Set the value to <em>GetMachineInfo</em>. |
| uuid | Long | Yes | The UUID of the asset. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| ClientStatus | String | Indicates whether the Server Guard client is online. |
| Uuid | String | The UUID of the asset. |
| InternetIp | String | The public IP address of the asset. |
| IntranetIp | String | The internal IP address of the asset. |
| FrangCount | Integer | The number of vulnerabilities on the asset. |
| MachineName | String | The name of the server. |
| Os | String | The operating system of the server. |
| EventCount | Integer | The number of attack events. |
| GroupId | Integer | The ID of the group. |
| Modified | Long | The time when the asset was modified. |
| Create | Long | The time when the asset was created. |
| MachineRegion | String | The region to which the server belongs. |
| Aliuid | Long | The AliUid of the department. |
| MachineIp | String | The IP address of the server. |
| VulCount | Integer | The number of alert events. |

Examples

Sample requests

```text
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=GetMachineInfo
&Uuid=inet-8a0569b3-15f8-482d-9a9e-cf85760c3b3a
&<Common request parameters>
```

Sample success responses in JSON format

```json
{
    "RequestId":"E0283B3D-C202-4EDD-9FF4-1BD5FF3F35FE",
    "Data":{
                "ClientStatus":"offline",//Indicates whether the Server Guard client is online.
                "Uuid":"inet-8a0569b3-15f8-482d-9a9e-cf85760c3b3a",//The UUID of the asset.
"InternetIp":"*. *. *. *",//The public IP address of the server.
                "IntranetIp":"*. *. *. *",//The internal IP address of the server.
                "FrangCount":0,//The number of security risks.
"MachineName":"*. *. *. *",//The name of the server.
                "Os":"linux",//The operating system.
                "EventCount":0,//The number of attack events.
                "GroupId":18,//The ID of the group.
                "Modified":1573716945000,//The time when the server was modified.
                "Create":1573716945000,//The time when the server was created.
                "MachineRegion":"outside-of-aliyun",//The region to which the server belongs.
                "Aliuid":123456789,//The default AliUid of a physical server is 123456789.
"MachineIp":"*. *. *. *",//The IP address of the server.
                "VulCount":0//The number of alert events.
     }
}
```

Error codes

For a list of error codes, visit the Error codes.

<a id="section-8-3-41"></a>

### 8.3.41. DescribeSocUsers

You can call this operation to query users.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.Set the value to <em>DescribeSocUsers</em>. |
| Aliuid | Long | No | The AliUid of the department. |
| DeptName | String | No | The name of the department. |
| Level | Integer | No | The level of the department. |
| LoginName | String | No | The logon username. |
| Source | String | No | The data source. Valid values:<br>• DT<br>• ASCM<br>• openApi |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| Items | Array | A list of the users. |

Examples

Sample requests

```text
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=DescribeSocUsers
&<Common request parameters>
```

Sample success responses in JSON format

```json
{
    "RequestId":"EDDB2FAF-2FFD-4D08-BB25-93BFC96BF7BB",
    "Data":[
                {
                    "AccountSystemName":"***",
                    "LoginName":"***bc",
                    "Modified":1548661368000,
                    "Create":1543318601000,
                    "Level":1,
                    "DeptName":"Legal Department",
                    "Id":2,
                    "ParentDeptId":1,
                    "Aliuid":1782421049074576,
                    "DeptId":2,
                    "ParentDeptName":"root",
                    "Source":"DT"
                },
                {
                    "AccountSystemName":"a***te",
                    "LoginName":"b**t",
                    "Modified":1548661368000,
                    "Create":1543318601000,
                    "Level":1,
                    "DeptName":"Technical Department",
                    "Id":3,
                    "ParentDeptId":1,
                    "Aliuid":1461680564,
                    "DeptId":3,
                    "ParentDeptName":"root",
                    "Source":"DT"
                }
           ],
    "Success":true
}
```

Error codes

For a list of error codes, visit the Error codes.

<a id="section-8-3-42"></a>

### 8.3.42. DeleteSocUser

You can call this operation to delete a user.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.Set the value to <em>DeleteSocUser</em>. |
| Aliuid | Long | Yes | The AliUid of the department. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| Success | Boolean | The value of True indicates a success. The value of False indicates a failure. |

Examples

Sample requests

```text
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=DeleteSocUser
&Aliuid=12312312312
&<Common request parameters>
```

Sample success responses in JSON format

```json
{
    "RequestId":"A3B53D56-C6CA-48F1-AF91-B5E28557DCAD",
    "Data":[
    ],
    "Success":true
}
```

Error codes

For a list of error codes, visit the Error codes.

<a id="section-8-3-43"></a>

### 8.3.43. SaveOrUpdateSocUser

You can call this operation to add a user or modify user information.

Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| Action | String | Yes | The operation that you want to perform.Set the value to <em>SaveOrUpdateSocUser</em>. |
| Aliuid | Long | Yes | The AliUid of the department. |
| DeptId | Long | Yes | The ID of the department. |
| DeptName | String | Yes | The name of the department. |
| Level | Integer | No | The level of the department. |
| LoginName | String | No | The logon username. |
| ParentDeptId | Long | No | The ID of the parent department. |
| ParentDeptName | String | No | The name of the parent department. |
| AccountSystemNa me | String | No | The name of the system account to add or modify. |
| AccessKey | String | No | The AccessKey ID.<br>Note This parameter is required when you add a new user but optional when you modify user information. |
| AccessSecret | String | No | The AccessKey secret.<br>Note This parameter is required when you add a new user but optional when you modify user information. |

Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| RequestId | String | The ID of the request. |
| Success | Boolean | The value of True indicates a success. The value of False indicates a failure. |

Examples

Sample requests

```text
http(s)://yundunnewsoc-pop.[ RegionId].example.com/? Action=SaveorupdateSocUser
&<Common request parameters>
```

Sample success responses in JSON format

```json
{
    "RequestId":"A3B53D56-C6CA-48F1-AF91-B5E28557DCAD",
    "Data":[
    ],
    "Success":true
}
```

Error codes

For a list of error codes, visit the Error codes.

<a id="section-9"></a>

# 9.Error codes

This topic describes the error codes returned by operations for Alibaba Cloud Security.

Common error codes of Apsara Stack Security

| Error code | Error message | Description |
| --- | --- | --- |
| yd.error.all.10001 | Authorization required. | The error message returned because you are not authorized to perform the operation. Check the account permissions. |
| yd.error.all.10002 | A system error has occurred. Try again later. | The error message returned because a system error has occurred. Try again later. |
| yd.error.all.10003 | The parameter is invalid. | The error message returned because the specified request parameter is invalid. Check the request parameter and try again. |
| yd.error.all.other | A system error has occurred. | The error message returned because a system error has occurred. Try again later. |
| yd.error.all.ConsoleSystemError_1 001 | An internal error has occurred. | The error message returned because a system error has occurred. Try again later. |
| yd.error.all.ConsoleSystemError_1 007 | The specified API is unavailable. | The error message returned because the operation has been brought offline. Contact Alibaba Cloud technical support. |
| yd.error.all.ConsoleSystemError_1 008 | An error occurred while verifying postOnly. | The error message returned because the verification has failed. Check the common request parameters and try again. |
| yd.error.all.ConsoleSystemError_1 009 | csrfToken must not be empty. | The error message returned because the csrfToken field is empty. Check the common request parameters and try again. |
| yd.error.all.ConsoleSystemError_1 010 | An error occurred while verifying csrfToken. | The error message returned because the verification has failed. Check the common request parameters and try again. |
| yd.error.all.ConsoleSystemError_1 011 | The Region ID must not be empty. | The error message returned because the RegionId request parameter is empty. Check the parameter. |
| yd.error.all.ConsoleSystemError_1 012 | The specified region ID format is invalid. | The error message returned because the specified region ID format is invalid. Check the RegionId parameter. |
| yd.error.all.ConsoleSystemError_1 013 | The parameter is null. | The error message returned because the specified request parameter is empty. Check the request parameter and try again. |
| yd.error.all.ConsoleSystemError_1 014 | The specified parameter format is invalid. | The error message returned because the specified parameter format is invalid. Check the request parameter and try again. |
| yd.error.all.ConsoleNeedLogin | You are not logged on. | The error message returned because you are not authorized to perform the operation. Check the account permissions. |
| yd.error.all.InvalidApi | The API is invalid. | The error message returned because an operation exception has occurred. Try again later. |
| yd.error.all.InvalidParameter | The parameter is invalid. | The error message returned because the specified request parameter is invalid. Check the request parameter and try again. |
| yd.error.all.InvalidResult | The return value is invalid. | The error message returned because the return value is invalid. Try again later. |
| yd.error.all.PropertyConvertFailed | An error occurred during conversion. | The error message returned because property conversion has failed. Try again later. |
| yd.error.all.NoPermission | Authorization required. | The error message returned because you are not authorized to perform the operation. Check the account permissions. |
| yd.error.all.ServerError | A server error has occurred. | The error message returned because a server error has occurred. Try again later or contact Alibaba Cloud technical support. |
| yd.error.all.UnkownError | An internal error has occurred. | The error message returned because an unknown error has occurred. Try again later or contact Alibaba Cloud technical support. |

Error codes of Threat Detection Service

| Error code | Error message | Description |
| --- | --- | --- |
| yd.error.sas.1 | The specified field has not been found in the metadata. | The error message returned because the field you queried does not exist in the metadata.Check the request and try again. |
| yd.error.sas.2 | An error occurred while invoking the task engine. Try again later. | The error message returned because the system has failed to call the task engine. Try again later. |
| yd.error.sas.3 | An error occurred while starting the task. Try again later. | The error message returned because the system has failed to start the task. Try again later. |
| yd.error.sas.4 | An error occurred while stopping the task. Try again later. | The error message returned because the system has failed to stop the task. Try again later. |
| yd.error.sas.5 | An error occurred while restarting the task. Try again later. | The error message returned because the system has failed to restart the task. Try again later. |
| yd.error.sas.6 | An error occurred while obtaining the task status. Try again later. | The error message returned because the system has failed to obtain the task status. Try again later. |
| yd.error.sas.7 | An error occurred while deleting the task. Try again later. | The error message returned because the system has failed to delete the task. Try again later. |
| yd.error.sas.8 | The specified table does not contain metadata. | The error message returned because the table you queried does not contain metadata.Check the request and try again. |
| yd.error.sas.100 | Request failed. Refresh the page and try again. | The error message returned because the request has failed.Try again later. |
| yd.error.sas.101 | The parameter is invalid. | The error message returned because the specified parameter is invalid. Check the request and try again. |
| yd.error.sas.103 | Request failed. | The error message returned because the request has failed.Try again later. |
| yd.error.sas.400 | The specified asset is under protection. Uninstall the Server Guard client and try again. | The error message returned because the asset you want to delete is protected. Uninstall the Server Guard agent from the server and try again. |
| yd.error.sas.500 | A system error has occurred. | The error message returned because a system error has occurred. Contact Alibaba Cloud technical support. |
| yd.error.sas.501 | The function is not available in the current version. | The error message returned because the version you used does not support this feature. |
| yd.error.sas.502 | You are not authorized to access the instance. | The error message returned because you are not authorized to operate the server. |

Error codes of Anti-DDoS

| Error code | Error message | Description |
| --- | --- | --- |
| yd.error.ddos.400 | An error occurred while accessing the server. Try again later. | The error message returned because the system has failed to access the server. Check the request and try again. |
| yd.error.ddos.500 | An error occurred on the server. | The error message returned because a server error has occurred. Contact Alibaba Cloud technical support. |
| yd.error.ddos.UNKNOWN_EXCEPTI ON | An internal error occurred. | The error message returned because an unknown error has occurred. Contact Alibaba Cloud technical support. |
| yd.error.ddos.REQUEST_TIMEOUT | The request has timed out. | The error message returned because the request has timed out. Try again later. |
| yd.error.ddos.SERVER_FAILED | An operation error occurred. | The error message returned because the operation has failed.Contact Alibaba Cloud technical support. |
| yd.error.ddos.NOT_AUTHORIZED | You are not authorized to perform this operation. | The error message returned because you are not authorized to perform the operation. Check the account permissions. |
| yd.error.ddos.PARAMETER_INVALI D | The specified parameter is invalid or missing. | The error message returned because the specified request parameter is invalid. Check the request parameter and try again. |
| yd.error.ddos.IP_SEGMENT_INVALI D | The specified CIDR block is invalid. | The error message returned because the specified CIDR block is invalid. Check the CIDR block specified in the request parameter. |
| yd.error.ddos.IP_SEGMENT_REPEA T | One CIDR block cannot be used in different regions. Enter another CIDR block. | The error message returned because one CIDR block belongs to multiple regions. Check the CIDR block specified in the request parameter. |
| yd.error.ddos.IP_SEGMENT_ALREA DY | The specified CIDR block already exists. | The error message returned because the specified CIDR block has been used. Check the CIDR block specified in the request parameter. |
| yd.error.ddos.IP_SEGMENT_MASK_LENGTH_ERR | The prefix length must be less than 24 bits. | The error message returned because the mask contains more than 24 bits. Check the CIDR block mask specified in the request parameter. |
| yd.error.ddos.QUERY_REGION_LIST _ERR | An error occurred while obtaining the region list. | The error message returned because the system has failed to obtain the region list. Try again later. |
| yd.error.ddos.IP_SEGMENT_OPERA TION_ERR | An error occurred while performing the operation on the CIDR block. | The error message returned because the system has failed to process the CIDR block. Try again later. |
| yd.error.ddos.QUERY_IP_SEGMENT _ERR | An error occurred while obtaining the CIDR block. | The error message returned because the system has failed to obtain information of the CIDR block. Try again later. |
| yd.error.ddos.MODIFY_IP_SEGMEN T_ERR | An error occurred while modifying the CIDR block. | The error message returned because the system has failed to modify the information of the CIDR block. Try again later. |
| yd.error.ddos.IP_SEGMENT_TYPE_ERR | Check whether the type of the CIDR block (internal or external) is specified. | The error message returned because the CIDR block type is not specified. Check the CIDR block type and try again. |
| yd.error.ddos.CANCEL_FLOW_CLEA N_ERR | An error occurred while canceling traffic scrubbing. Check the network connection to Beaver. | The error message returned because the system has failed to cancel traffic scrubbing. Check the network connection to Network Traffic Monitoring System and try again. |
| yd.error.ddos.QUERY_FLOW_ANAL YSIS_ERR | An error occurred while obtaining the traffic analysis result. Check the network connection to Beaver. | The error message returned because the system has failed to obtain the traffic analysis result.Check the network connection to Network Traffic Monitoring System and try again. |
| yd.error.ddos.QUERY_BEAVER_URL _ERR | An error occurred while obtaining the Beaver URL. | The error message returned because the system has failed to obtain the URL of Network Traffic Monitoring System. Check the network connection to Network Traffic Monitoring System and try again. |
| yd.error.ddos.SET_VALVE_INVALID | The specified thresholds are invalid. | The error message returned because the threshold verification has failed. Check the thresholds and try again. |
| yd.error.ddos.VALVE_DEFAULT_AL READY | You cannot add the default threshold again. | The error message returned because the system has failed to add the default threshold, which can only be modified. |
| yd.error.ddos.NOT_BELONG_BEAV ER_IP_SEGMENT | Check whether the specified CIDR block belongs to the internal network of Beaver. | The error message returned because the CIDR block you entered is not in the internal CIDR block of Network Traffic Monitoring System. Check the CIDR block. |
| yd.error.ddos.VALVE_DELETE_ERR | Do not delete the threshold. | The error message returned because the system has failed to delete the default threshold or the threshold of 128.0.0.0/1, which cannot be deleted. |
| yd.error.ddos.QUERY_CODE_ERR | An error occurred while obtaining the product configuration. | The error message returned because the system has failed to obtain the dictionary. Try again later. |
| yd.error.ddos.IS_OPENED | Enabled. | The error message returned because the specified switch has been turned on. |
| yd.error.ddos.IS_CLOSED | Disabled. | The error message returned because the specified switch has been turned off. |

Error codes of Server Guard

| Error code | Error message | Description |
| --- | --- | --- |
| yd.error.aqs.REQUEST_FAILED | Request failed. Try again later. | The error message returned because the request has failed.Try again later. |

Error codes of Security Audit

Error codes of Sync Center
