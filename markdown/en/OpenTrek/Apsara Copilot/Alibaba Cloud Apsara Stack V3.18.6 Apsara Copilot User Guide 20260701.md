Alibaba Cloud  
Apsara Stack  
Apsara Copilot User Guide  
Product Version: V3.18.6  
Document Version: 20260701

**Table of Contents**

- [1.Apsara Copilot homepage](#section-1)
- [2.Access control of Apsara Copilot](#section-2)
- [3.Configurations of Apsara Copilot](#section-3)
    - [3.1. Configure custom settings](#section-3-1)
    - [3.2. Accuracy evaluation](#section-3-2)
        - [3.2.1. Evaluation case management](#section-3-2-1)
            - [3.2.1.1. Create an evaluation case](#section-3-2-1-1)
            - [3.2.1.2. Manage an evaluation case](#section-3-2-1-2)
        - [3.2.2. Evaluation dataset management](#section-3-2-2)
            - [3.2.2.1. Create an evaluation dataset](#section-3-2-2-1)
            - [3.2.2.2. Manage an evaluation dataset](#section-3-2-2-2)
        - [3.2.3. Evaluation task management](#section-3-2-3)
            - [3.2.3.1. Create an evaluation task](#section-3-2-3-1)
            - [3.2.3.2. Manage an evaluation task](#section-3-2-3-2)
        - [3.2.4. Accuracy rate analysis](#section-3-2-4)
    - [3.3. Model configuration](#section-3-3)
    - [3.4. Knowledge base management](#section-3-4)
        - [3.4.1. Create a knowledge base](#section-3-4-1)
        - [3.4.2. Edit a knowledge base](#section-3-4-2)
        - [3.4.3. Configure the chunking policy](#section-3-4-3)
        - [3.4.4. Delete a knowledge base](#section-3-4-4)
        - [3.4.5. Import a file](#section-3-4-5)
        - [3.4.6. View file details](#section-3-4-6)
        - [3.4.7. Ingest files](#section-3-4-7)
        - [3.4.8. Delete an file](#section-3-4-8)
        - [3.4.9. View the knowledge graph](#section-3-4-9)
        - [3.4.10. View the mind map](#section-3-4-10)
        - [3.4.11. Retrieval configuration and retrieval testing](#section-3-4-11)
    - [3.5. AI-assisted cloud resource management](#section-3-5)
        - [3.5.1. AI-assisted creation](#section-3-5-1)
        - [3.5.2. AI-assisted configuration change](#section-3-5-2)
- [4.Application of Apsara Copilot](#section-4)
    - [4.1. Apsara Copilot chats](#section-4-1)
    - [4.2. Perform text-selection Q&A](#section-4-2)
    - [4.3. AI-based intelligent analysis](#section-4-3)
    - [4.4. AI-based bill analysis](#section-4-4)
    - [4.5. AI billing rule analysis](#section-4-5)
- [5.Apsara Copilot operations analytics](#section-5)
- [6.View operation logs](#section-6)
- [7.Appendix](#section-7)
    - [7.1. Log in to the Apsara Uni-manager Management Console](#section-7-1)

<a id="section-1"></a>

# 1.Apsara Copilot homepage

The homepage displays the full capabilities of Apsara Copilot to help you deeply understand the product's value and usage, and provide clear guidance.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.

2. Click <img src="assets/7036111951b1605e895939271975b629.jpeg" width="20" alt=""> in the top navigation bar or floating menu to enter Apsara Copilot.

   ![](assets/7ebd5351e1025d23b8f81745437a7e97.jpeg)

3. Click <img src="assets/a01acdae2242a6e11735589511b593b9.png" width="13" alt=""> above the **Apsara Copilot** dialog box, or click **Assistant Introduction** inside the

   dialog box.

   ![](assets/19b6584b0dbb526afaa69ce1e37afbb9.jpeg)

4. Go to the Apsara Copilot homepage to view its positioning, features, highlights, and benefits.

   > **Note**
   >
   > - **Experience now**: Click **Experience now** to open the Apsara Copilot dialog box.
   >
   > - **Official documents**: Click **Official documents** to go to the Apsara Copilot help documentation.

   ![](assets/79b41d4072a1f23be5ed9c4d87c5178c.jpeg)

<a id="section-2"></a>

# 2.Access control of Apsara Copilot

This topic describes how to implement the access control of Apsara Copilot by configuring custom roles with different permissions.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console as an administrator.

2. In the top navigation bar, click **Enterprise**.

3. In the left-side navigation pane, choose **Permissions** > **Role Permissions**.

4. Click **Create Custom Role**.

5. Configure the basic information, management permissions, application permissions, menu permissions, and custom permissions for the role.

   - For more information about the configurations, see the "Manage custom roles" topic in User Guide of the Apsara Uni-manager Management Console.

   - In the **Application Permissions** step, search for and find Apsara Stack Assistant and select the permissions that you want to grant to the role based on your business requirements.

     ![](assets/a5d7e9cc7ab85c2ad3ec2980e3d0f91e.jpeg)

6. After the role is created, assign the role to users.

<a id="section-3"></a>

# 3.Configurations of Apsara Copilot

<a id="section-3-1"></a>

## 3.1. Configure custom settings

This topic describes how to enable, disable, and configure the custom settings of Apsara Copilot.

**Prerequisites**

You are an operations administrator.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.

2. In the top navigation bar, click **Configurations**.

3. In the left-side navigation pane, choose **Apsara Copilot** > **Custom Settings**.

4. On the **Custom Settings** page, configure the parameters based on your business requirements. To restore Apsara Copilot to the default settings, click **Restore Default Settings** in the lower part of the page. The configurations take effect the next time you log in to the console.

   Parameter

   Description

   Specifies whether to display Apsara Copilot in the console. If you turn on the switch, Apsara Copilot is displayed in the floating menu and top navigation bar.

   **Enable on Platform**

   <img src="assets/d878fe568756329c79d0029c880c1e06.png" width="34" alt=""> : does not display Apsara Copilot.

   <img src="assets/0692f00fb448dae20b88a5c2123e09c6.png" width="34" alt=""> : displays Apsara Copilot.

   **Display Control**

   Specifies whether to display the switch for enabling internal network-based search in the Apsara Copilot pane.

   <img src="assets/d878fe568756329c79d0029c880c1e06.png" width="34" alt=""> : does not display the switch.

   <img src="assets/0692f00fb448dae20b88a5c2123e09c6.png" width="34" alt=""> : displays the switch. If you turn on the switch, you must

   also configure the information about a local knowledge base.

   > **Note**
   >
   > This feature allows users to determine whether to use internal network-based search in the Apsara Copilot pane.

   **Intranet Search**

   - **Knowledge Source**: The value is fixed to **Model Studio Dedicated Edition**.

   - **URL**: the API of the knowledge center of Model Studio, which can be used to retrieve relevant files in the specified workspace and knowledge base.

   - **APP_KEY**: the AppKey that is in effect.

   - **Workspace Code**: the code of the workspace to which the knowledge base belongs in workspace management.

   - **Knowledge Base Code**: the code of the knowledge base in knowledge services.

   **Specify a language for**

   You can select **Simplified Chinese**, **English**, or **Traditional**

   **the AI**

   **Chinese**.

   **assistant.**

   **Assistant**

   We recommend that you enter a name that does not exceed 40

   **Name**

   characters in length. The default name is Apsara Copilot.

   **Greetings**

   The greetings used by Apsara Copilot.

   The recommended questions to be displayed on the homepage of

   **Recommende**

   Apsara Copilot. You can click **Add Question** to add more

   **d Questions on Home Page**

   questions or click the <img src="assets/a08df07c9cdd14377bb745305c652bae.png" width="14" alt=""> icon in the row of a question to remove

   the question.

   The legal disclaimer used by Apsara Copilot.

   **AI Assistant**

   **Disclaimer**

   Default legal disclaimer: This content is AI-generated and may not

   **Settings**

   be completely accurate. Use it as a reference only.

   **Official Alternative**

   The alternative answer used by Apsara Copilot.

   **Answer**

   The display icon of Apsara Copilot. We recommend that you use

   **Entry Icon**

   an image whose aspect ratio is 1:1, such as 100 × 100 pixels in the GIF, PNG, JPG, or JPEG format.

   The logo to be displayed on the welcome page of Apsara Copilot.

   **Welcome**

   We recommend that you use an image whose aspect ratio is 1:1,

   **Page Icon**

   such as 100 × 100 pixels in the GIF, PNG, JPG, or JPEG format.

   The avatar used by Apsara Copilot during conversations. We

   **Conversation**

   recommend that you use an image whose aspect ratio is 1:1, such

   **Icon**

   as 100 × 100 pixels in the GIF, PNG, JPG, or JPEG format.

   The style of the answer. Valid values: **Expert Mode**, **Simple Mode**, and **Service Mode**.

   - **Expert Mode**: rigorous, clear structure, and standardized terminology. It is suitable for technical support engineers to implement in-depth Q&A, architecture design, and best

   **Preferred**

   practices.

   **Answer Style**

   **Style**

   - **Simple Mode**: concise, high information density, and no redundant expression. It is suitable for scenarios such as quick response, operation guidance, and troubleshooting.

   - **Service Mode**: patient, friendly, and positive. It is suitable for improving employee satisfaction and service reliability.

   ![](assets/ae62f1e9f45417d58ba9f80c34b5ea23.jpeg)

<a id="section-3-2"></a>

## 3.2. Accuracy evaluation

The system provides the accuracy evaluation feature that allows you to evaluate the accuracy of Apsara Copilot. By configuring evaluation cases, evaluation datasets, and evaluation tasks, you can initiate automated accuracy evaluation and export a detailed evaluation report.

<a id="section-3-2-1"></a>

### 3.2.1. Evaluation case management

<a id="section-3-2-1-1"></a>

#### 3.2.1.1. Create an evaluation case

This topic describes how to create an evaluation case.

**Prerequisites**

You are an operations administrator.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.

2. In the top navigation bar, click **Configurations**.

3. In the left-side navigation pane, choose **Apsara Copilot** > **Accuracy Evaluation**.

4. Click the **Evaluation Case Management** card.

5. On the **Evaluation Case Management** page, click **Add Use Case**.

6. In the **Add Evaluation Case** dialog box, configure the parameters.

   ![](assets/a440d010d15339528d9d7424fd9faa0a.jpeg)

   | Parameter | Description |
   | --- | --- |
   | Use Case Type | The type of the evaluation case. Set the value to rag. |
   | Product | The cloud service to which the evaluation case belongs. |
   | Question | The question of the evaluation case. |
   | Answer | The answer to the question of the evaluation case. |

7. Click **Add Use Case**.

<a id="section-3-2-1-2"></a>

#### 3.2.1.2. Manage an evaluation case

This topic describes how to manage an evaluation case after it is created. You can view and delete the evaluation case.

**Prerequisites**

- You are an operations administrator.

- An evaluation case is created.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.

2. In the top navigation bar, click **Configurations**.

3. In the left-side navigation pane, choose **Apsara Copilot** > **Accuracy Evaluation**.

4. Click the **Evaluation Case Management** card.

5. Manage the created evaluation case as needed.

   | Operation | Description |
   | --- | --- |
   | View the evaluation case | Find the evaluation case and click <strong>View</strong> in the Actions column. In the Evaluation Case Details panel, you can view the evaluation case details, including the associated evaluation datasets.<br>Note<br>• The evaluation case code can be copied with one click. To do so, move the pointer over the code and click the icon.<br><img src="assets/7c52bbe4842d559bd88e2c5facb61486.jpeg" width="17" alt=""><br>• An associated evaluation dataset can be disassociated from the current evaluation case. To do so, find the evaluation dataset in the list and click <strong>Disassociate</strong> in the Actions column. |
   | Delete the evaluation case | i. Find the evaluation case and click <strong>Delete</strong> in the Actions.<br>ii. In the message that appears, click <strong>OK</strong>. |

<a id="section-3-2-2"></a>

### 3.2.2. Evaluation dataset management

<a id="section-3-2-2-1"></a>

#### 3.2.2.1. Create an evaluation dataset

This topic describes how to create an evaluation set.

**Prerequisites**

- You are an operations administrator by default.

- You have created evaluation cases.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.

2. In the top navigation bar, select **Configurations**.

3. In the left-side navigation pane, select **Apsara Copilot** > **Accuracy Evaluation**.

4. Click the **Evaluation Dataset Management** card.

5. On the **Evaluation Dataset Management** page, click **Create Evaluation Dataset**.

6. In the **Create Evaluation Dataset** dialog box, configure the evaluation dataset information.

   ![](assets/90180282aca788548c6863ca667cbf3b.jpeg)

   | Configuration item | Description |
   | --- | --- |
   | Evaluation Dataset Type | Select the type of the evaluation set. The current version supports rag type only. |
   | Evaluation Dataset Name | Set a name for the evaluation set. |
   | Evaluation Scenario | Select an evaluation scenario. The system supports <strong>Test Q&amp;A</strong> and <strong>User</strong> <strong>Q&amp;A</strong>. |
   | Description | Optional. Enter a description for the evaluation set. |
   | Select Evaluation Cases | i. Click <strong>Create Evaluation Dataset From Evaluation Cases</strong>.<br>ii. Select cases. You can filter cases by <strong>User Case Code</strong>, <strong>Question</strong>, <strong>Product</strong>, and <strong>Reference Answer</strong>. After you set the filter conditions, click <strong>Search</strong> to apply the filters.<br>iii. Click <strong>OK</strong>.<br>You can also click <strong>Add All</strong> to add all cases to the evaluation dataset. |

7. Click **Create Evaluation Dataset**.

<a id="section-3-2-2-2"></a>

#### 3.2.2.2. Manage an evaluation dataset

This topic describes how to manage an evaluation dataset after it is created. You can view, modify, and delete the evaluation dataset.

**Prerequisites**

- You are an operations administrator.

- An evaluation dataset is created.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.

2. In the top navigation bar, click **Configurations**.

3. In the left-side navigation pane, choose **Apsara Copilot** > **Accuracy Evaluation**.

4. Click the **Evaluation Dataset Management** card.

5. Manage the created evaluation dataset as needed.

   | Operation | Description |
   | --- | --- |
   | View the evaluation dataset | Find the evaluation dataset and click <strong>View</strong> in the Actions column. On the <strong>Evaluation</strong> <strong>Dataset Use Case Management</strong> page, you can manage the evaluation cases in the dataset. |
   | Modify the evaluation dataset | i. Find the evaluation dataset and click <strong>Modify</strong> in the Actions column.<br>ii. In the <strong>Modify Evaluation Dataset</strong> panel, modify the <strong>Evaluation Dataset Name</strong> and <strong>Description</strong> parameters.<br>iii. Click <strong>OK</strong>. |
   | Delete the evaluation dataset | i. Find the evaluation dataset and click <strong>Delete</strong> in the Actions column.<br>ii. In the message that appears, click <strong>OK</strong>. |

<a id="section-3-2-3"></a>

### 3.2.3. Evaluation task management

<a id="section-3-2-3-1"></a>

#### 3.2.3.1. Create an evaluation task

This topic describes how to create an evaluation task.

**Prerequisites**

- You are an operations administrator by default.

- You have created an evaluation dataset.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.

2. In the top navigation bar, select **Configurations**.

3. In the left-side navigation pane, select **Apsara Copilot** > **Accuracy Evaluation**.

4. Click the **Evaluation Task Management** card.

5. On the **Evaluation Task Management** page, click **Create Evaluation Task**.

6. In the **Create Evaluation Task** dialog box, configure the evaluation task information.

   | Configuration item | Description |
   | --- | --- |
   | Task Name | Enter a name for the evaluation task. |
   | Evaluation Task Type | Select an evaluation task type. The current version supports rag type only. |
   | Evaluation Dataset | Select an evaluation set from the drop-down list. |
   | Evaluation Type | Select <strong>Manual</strong> or <strong>Automatic</strong>. |
   | Evaluator | When you select <strong>Manual</strong> for <strong>Evaluation Type</strong>, specify one or more evaluators.<br>You can specify up to three evaluators. All specified evaluators must complete the evaluation. If any evaluator selects <strong>Completely Wrong</strong> as the evaluation result, the evaluation fails. |
   | Evaluation Method | When you select <strong>Automatic</strong> for <strong>Evaluation Type</strong>, select an evaluation method.<br>Select <strong>Ground Truth</strong> or <strong>No Ground Truth</strong>. |

   **Manual evaluation task**

   ![](assets/058c96a2778e6f99fd80272113737409.jpeg)

   **Automatic evaluation task**

   ![](assets/bc11be7d16a92b2f099957986863b486.jpeg)

7. Click **Create Evaluation Task**.

   > **Note**
   >
   > After you create an evaluation task, the system does not automatically start the task. You must click **Start Evaluation** in the **Actions** column to start the evaluation task.

<a id="section-3-2-3-2"></a>

#### 3.2.3.2. Manage an evaluation task

This topic describes how to manage an evaluation task.

**Prerequisites**

- You are an operations administrator by default.

- You have created an evaluation task.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.

2. In the top navigation bar, click **Configurations**.

3. In the navigation pane on the left, choose **Apsara Copilot** > **Accuracy Assessment**.

4. Click the **Evaluation Task Management** card.

5. View the list of evaluation tasks. You can use the **Task ID**, **Evaluation Dataset**, **Evaluation Type**, and **Status** filters to quickly find a specific task.

   ![](assets/636c6f0adbb511150e5de7ae55e502b0.jpeg)

6. Manage the created evaluation task as needed.

   | Operation | Description |
   | --- | --- |
   | Perform manual evaluation | i. In the <strong>Actions</strong> column of the evaluation task, click <strong>Manual</strong> <strong>Evaluation</strong>.<br>Note<br>You can perform manual evaluation only on tasks whose <strong>Evaluation Type</strong> is <strong>Manual</strong> and whose status is <strong>Pending</strong> <strong>Manual Evaluation</strong> or <strong>In Progress</strong>.<br>ii. On the <strong>Manual Evaluation</strong> page, click <strong>Evaluate</strong> in the <strong>Actions</strong> column for a use case.<br>Note<br>Click <strong>View</strong> in the <strong>Actions</strong> column to view the details of the evaluation results.<br>![](assets/b7ca33762aa3d57abef863659224e9ca.jpeg)<br>iii. In the <strong>Evaluation Result Details</strong> panel, review the information to be evaluated. Then, in the <strong>Manual Evaluation</strong> section, set the <strong>Evaluation Result</strong> and <strong>Remarks</strong>.<br>Note<br>For <strong>Evaluation Result</strong>, you can select <strong>Completely</strong> <strong>Accurate</strong>, <strong>Partially Accurate</strong>, <strong>Completely Incorrect</strong>, or <strong>Not Evaluated</strong>. If you select <strong>Completely Incorrect</strong>, the evaluation fails. You must then select a reason from the <strong>Reason for Failure</strong> drop-down list below. Options include <strong>Unclear Question</strong>, <strong>Incomplete Reference Answer</strong>, <strong>Incomplete Content</strong>, <strong>Duplicate Use Case</strong>, or <strong>Other</strong>. |
   | View the evaluation results | i. In the <strong>Actions</strong> column of the evaluation task, click <strong>View Results</strong>.<br>Note<br>You can view the results only when the task status is iv. Click <strong>Submit</strong>. If there are multiple use cases, you can click <strong>Completed</strong>.<strong>Submit and Switch to Next</strong> after you finish evaluating the current use case.<br>ii. On the <strong>Evaluation Results</strong> page, view the evaluation results for the use cases.<br>![](assets/b8bc468ea5af25216667cf0024f0e3e0.jpeg)<br>iii. Click <strong>View</strong> in the <strong>Actions</strong> column for a use case to expand its result details. |

   ![](assets/95388d5cc54040eb3a0dd094d4d5d672.png)

   <table>
     <tr>
       <td>View the report</td>
       <td>i. In the <strong>Actions</strong> column of the evaluation task, click the<img src="assets/6f375cd5187afa56f3d6f9f376bb0259.png" width="14" alt="">icon and select <strong>View Report</strong>.<br>Note<br>You can view the report only when the task status is <strong>Completed</strong>.<br>ii. On the <strong>Evaluation Report</strong> page for the task, view the detailed evaluation and analysis report.</td>
     </tr>
     <tr>
       <td>Delete the evaluation task</td>
       <td>i. In the Actions column, click<img src="assets/6f375cd5187afa56f3d6f9f376bb0259.png" width="17" alt="">and select <strong>Delete</strong>.<br>ii. In the message that appears, click <strong>OK</strong>.</td>
     </tr>
     <tr>
       <td>Perform a re-evaluation</td>
       <td>i. If the evaluation task fails, click <strong>Re-evaluate</strong> in the Actions column.<br>ii. In the message that appears, click <strong>OK</strong>.</td>
     </tr>
   </table>

<a id="section-3-2-4"></a>

### 3.2.4. Accuracy rate analysis

View the accuracy status of Apsara Copilot.

**Prerequisites**

The operator is an operations administrator by default.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.

2. In the top navigation bar, select **Configurations**.

3. In the left-side navigation pane, select **Apsara Copilot** > **Accuracy Evaluation**.

4. Click the **Accuracy Rate Analysis** card.

5. On the **Accuracy Rate Analysis** page, view **Accuracy Rate Trend Analysis**, **Question Classification Statistics**, and **Data Details**.

   | Configuration item | Description |
   | --- | --- |
   | Accuracy Rate Trend Analysis | Displays accuracy rate analysis as a line chart. You can switch between <strong>Day</strong> <strong>Dimension</strong> or <strong>Month Dimension</strong>. |
   | Question Classification Statistics | Displays question classification statistics as a column chart. You can switch between <strong>Day Dimension</strong> or <strong>Month Dimension</strong>. |
   | Data Details | Enter the start date and end date for your query to view detailed data within the specified time range. You can switch between <strong>Day Dimension</strong> or Month Dimension<br>• Click <strong>View Report</strong> in the <strong>Actions</strong> column of a detail entry to go to the evaluation report details page.<br>• Click<img src="assets/0883c73ee777bbb775cde047915d7cc8.png" width="22" alt="">above the list to download the detailed data to your local device. |

   ![](assets/123618d3f75ac4c9359856a263d5a0aa.jpeg)

<a id="section-3-3"></a>

## 3.3. Model configuration

Manage and configure your AI models, including large language models, embedding models, and rerank models.

**Prerequisites**

The operator is an operations administrator by default.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.

2. In the top navigation bar, select **Configurations**.

3. In the left-side navigation pane, select **Apsara Copilot** > **Model Configurations**.

4. In the **Large Language Model (LLM)**/**Embedding Model**/**Rerank Model** section, click **Add Model**.

5. In the **Add Model Configuration** dialog box, configure the model.

   | Configuration item | Description |
   | --- | --- |
   | Model Name | Enter the display name of the model. |
   | Model Code | Enter the code of the model, representing the unique ID of the model. |
   | API Key | Enter the API key of the model. |
   | Request URL | Enter the API request URL of the model. |
   | Model Provider | Select a model provider. Options: <strong>Model Studio Dedicated Edition</strong>, <strong>Alibaba</strong> <strong>Cloud Model Studio</strong>, <strong>aibase</strong>, and <strong>openai</strong>. |
   | Set as Default Model | Specify whether to set the model as the default model. |

   ![](assets/d65ac1f527077a9f0ed7657702cd5d43.jpeg)

6. Click **Save**.

7. Perform other related operations.

   | Operation | Description |
   | --- | --- |
   | Edit the model | i. In the model card section, click <strong>Edit</strong> in the upper-right corner.<br>ii. In the <strong>Edit Model Configuration</strong> dialog box, update the model configuration.<br>Note<br>You cannot modify the model name or model code.<br>iii. Click <strong>Save</strong>. |
   | Delete the model | i. In the model card section, click <strong>Delete</strong> in the upper-right corner.<br>ii. Click <strong>OK</strong>. |
   | Change the default model | In the model card section, click <strong>Set as Default Model</strong> at the bottom to change the default model based on business requirements. |

<a id="section-3-4"></a>

## 3.4. Knowledge base management

<a id="section-3-4-1"></a>

### 3.4.1. Create a knowledge base

Create vector and graph knowledge bases on the Knowledge Base Management page.

**Prerequisites**

The operator is an operations administrator by default.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.

2. In the top navigation bar, select **Configurations**.

3. In the left-side navigation pane, select **Apsara Copilot** > **Knowledge Base Management**.

4. Click **Create Knowledge Base**.

5. In the **Create Knowledge Base** dialog box, configure the knowledge base.

   | Configuration item | Description |
   | --- | --- |
   | Knowledge Base Type | Select the type of knowledge base. The system supports <strong>Vector</strong> <strong>Knowledge Base</strong> and <strong>Graph Knowledge Base</strong>.<br>• <strong>Vector Knowledge Base</strong>: a production-grade vector database based on Milvus.<br>• <strong>Graph Knowledge Base</strong>: a knowledge base implementation based on LightRAG. |
   | Knowledge Base Name | Enter a name for the knowledge base. |
   | Embedding Model | Select the embedding model used to convert text into vectors.<br>Different models have different vector dimensions and semantic precision. You cannot change this setting after creation. |
   | Default Chunking Policy | Select a document chunking policy.<br>• General: general chunking, suitable for most scenarios.<br>• QA: question-answer chunking, suitable for FAQ documents.<br>• Structure: structured chunking, suitable for long structured content.<br>• Custom: custom delimiter-based chunking, suitable for documents with fixed formats such as laws and regulations. |
   | Chunk Size | Set this parameter when you select <strong>General</strong>, <strong>Structure</strong>, or <strong>Custom</strong> as the document chunking policy.<br>Set the number of units contained in each independent segment (chunk) when splitting the original long text. |
   | Chunk Overlap | Set this parameter when you select <strong>General</strong>, <strong>Structure</strong>, or <strong>Custom</strong> as the document chunking policy.<br>Set the length of repeated content between two adjacent text chunks. In other words, the end of the previous chunk overlaps with the beginning of the next chunk. |
   | Separator | Set this parameter when you select <strong>Custom</strong> as the document chunking policy.<br>Define a series of priority rules to guide the system to split long text into appropriately sized chunks while preserving semantic integrity.<br>Note<br>The system supports escape characters such as \\n (line break), \\t (tab), and \\r (carriage return). Separate multiple delimiters with commas (for example, \\n,\\t). Leave this field blank to disable pre-segmentation. |
   | Description | Enter a task description for the knowledge base. The more detailed the description, the easier it is to retrieve the knowledge base accurately. |

   ![](assets/3689fdf2a275ac89f8f0cc49b67915ea.jpeg)

6. Click **OK**.

<a id="section-3-4-2"></a>

### 3.4.2. Edit a knowledge base

You can modify the configuration when updates are available for a knowledge base.

**Prerequisites**

The operator is an operations administrator by default.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.

2. In the top navigation bar, select **Configurations**.

3. In the left-side navigation pane, select **Apsara Copilot** > **Knowledge Base Management**.

4. Click <img src="assets/bc02e03ca2f3b09edbeed4d99785933f.png" width="22" alt=""> in the upper-right corner of the target knowledge base card, and select **Modify**

   **Knowledge Base**.

5. In the **Modify Knowledge Base** dialog box, update the knowledge base configuration. For more information about configuration items, see Create a knowledge base.

   ![](assets/ba529cead93fd31c030caad785df1ed1.jpeg)

6. Click **OK**.

<a id="section-3-4-3"></a>

### 3.4.3. Configure the chunking policy

Adjusting chunking parameters controls how the system splits text, which affects retrieval quality and document loading efficiency.

**Prerequisites**

The operator is an operations administrator by default.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.

2. In the top navigation bar, select **Configurations**.

3. In the left-side navigation pane, select **Apsara Copilot** > **Knowledge Base Management**.

4. Click <img src="assets/bc02e03ca2f3b09edbeed4d99785933f.png" width="22" alt=""> in the upper-right corner of the target knowledge base card and select **Configure**

   **Chunking Policy**.

5. In the **Chunking Policy** dialog box, adjust the chunking policy for the knowledge base. For detailed descriptions of chunking policies, see Create a knowledge base.

   > **Note**
   >
   > The preset policies align with the followingRAGFlow chunking policies: General, QA, Book, and Laws. If you leave this parameter blank, the system uses the default policy of the knowledge base.

   ![](assets/6c859e5255dd3b137755d4d056020511.jpeg)

6. Click **OK**.

<a id="section-3-4-4"></a>

### 3.4.4. Delete a knowledge base

Delete any knowledge base you no longer need.

**Prerequisites**

The operater is an operations administrator by default.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.

2. In the top navigation bar, select **Configurations**.

3. In the left-side navigation pane, select **Apsara Copilot** > **Knowledge Base Management**.

4. Click <img src="assets/bc02e03ca2f3b09edbeed4d99785933f.png" width="22" alt=""> in the upper-right corner of the target knowledge base card and select **Delete**.

5. In the **Delete Knowledge Base** dialog box, enter the knowledge base name to confirm the operation.

   ![](assets/90f59331b61094bf574de9b22b9edb5c.jpeg)

6. Click **OK**.

<a id="section-3-4-5"></a>

### 3.4.5. Import a file

Import files into a knowledge base.

**Prerequisites**

The operator is an operations administrator by default.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.

2. In the top navigation bar, select **Configurations**.

3. In the left-side navigation pane, select **Apsara Copilot** > **Knowledge Base Management**.

4. Click the name of a knowledge base to go to its details page.

5. On the **Knowledge Base Details** page, click **Import File**.

6. In the **Import File** dialog box, select or drag a file into the dashed box to upload it.

   > **Note**
   >
   > Supported file types include txt, md, doc, docx, pdf, pptx, csv, xlsx, and html.

   ![](assets/52201cc128fd4ea698135937a2c8de5b.jpeg)

7. Click **OK**.

<a id="section-3-4-6"></a>

### 3.4.6. View file details

The file details page displays file preview and chunks information.

**Prerequisites**

The operator is an operations administrator by default.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.

2. In the top navigation bar, select **Configurations**.

3. In the left-side navigation pane, select **Apsara Copilot** > **Knowledge Base Management**.

4. Click the name of a knowledge base to go to its details page.

5. On the **Knowledge Base Details** page, click the file name to view its details.

   ![](assets/538cadb5e697ec894049e8c3ad7e7207.jpeg)

<a id="section-3-4-7"></a>

### 3.4.7. Ingest files

After importing files, you can ingest them.

**Prerequisites**

- The operator is an operations administrator by default.

- The file status is **Parsed**.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.

2. In the top navigation bar, select **Configurations**.

3. In the left-side navigation pane, select **Apsara Copilot** > **Knowledge Base Management**.

4. Click the name of a knowledge base to go to its details page.

5. On the **Knowledge Base Details** page, ingest files.

   | Operation | Description |
   | --- | --- |
   | Ingest a single file | Click <strong>Ingest</strong> in the <strong>Actions</strong> column corresponding to the file. |
   | Ingest multiple files at a time | i. Select multiple files that you want to ingest.<br>ii. Click <strong>Batch Ingest</strong> below the file list.<br>iii. In the <strong>Batch Ingest Chunking Policy</strong> dialog box, confirm or modify the chunking policy.<br>iv. Click <strong>OK</strong>. |

6. (Optional) Perform other related operations.

   - After ingesting a file, the file status changes to **Indexed**. You can download the file.

   - If file ingestion fails, the file status changes to **Index Error**. You can retry the operation.

<a id="section-3-4-8"></a>

### 3.4.8. Delete an file

**Prerequisites**

The operator is an operations administrator by default.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.

2. In the top navigation bar, select **Configurations**.

3. In the left-side navigation pane, select **Apsara Copilot** > **Knowledge Base Management**.

4. Click the name of a knowledge base to go to its details page.

5. On the **Knowledge Base Details** page, click **Delete** in the **Actions** column.

6. Click **OK**.

<a id="section-3-4-9"></a>

### 3.4.9. View the knowledge graph

View the generated knowledge graph in a graph-type knowledge base.

**Prerequisites**

- The operator is an operations administrator by default.

- The knowledge base is of graph type.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.

2. In the top navigation bar, select **Configurations**.

3. In the left-side navigation pane, select **Apsara Copilot** > **Knowledge Base Management**.

4. Click the name of the knowledge base to go to its details page.

5. On the **Knowledge Base Details** page, click <img src="assets/5a4e6ce7404032d786e68fcc70f2087c.png" width="22" alt=""> in the upper-right corner of the list.

6. On the **Knowledge Graph** tab, view the generated knowledge graph. If no knowledge graph exists, click **Generate Now**.

   > **Note**
   >
   > - The knowledge graph displays nodes and their relationships.
   >
   >   - Enter a node name in the drop-down list at the top to search for and view the specific node.
   >
   >   - Click a node in the graph to display its description, network metrics, tags, and associations.
   >
   > - Control the knowledge graph view.
   >
   >   - Click
   >
   >     in the upper-right corner of the knowledge graph to zoom in.
   >
   >     <img src="assets/6a744c86a6fad1f06aebe529376b0705.png" width="16" alt="">
   >
   >   - Click
   >
   >     in the upper-right corner of the knowledge graph to zoom out.
   >
   >     <img src="assets/71de923885ee43664dadb7147ff5a86d.png" width="18" alt="">
   >
   >   - Click
   >
   >     in the upper-right corner of the knowledge graph to enter full-
   >
   >     <img src="assets/0b2af08de02e63d355c764af03e2db3d.png" width="18" alt="">
   >
   >     screen mode.
   >
   >   - Click
   >
   >     in the upper-right corner of the knowledge graph to restore the
   >
   >     <img src="assets/7acb15a8b924c8885ccca5f2162cff0f.png" width="19" alt="">
   >
   >     default view.

   ![](assets/1c0cba0b97ee6a8aaa1ff9bccc2c93f0.jpeg)

<a id="section-3-4-10"></a>

### 3.4.10. View the mind map

View the generated mind map.

**Prerequisites**

The operator is an operations administrator by default.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.

2. In the top navigation bar, select **Configurations**.

3. In the left-side navigation pane, select **Apsara Copilot** > **Knowledge Base Management**.

4. Click the name of a knowledge base to go to its details page.

5. On the **Knowledge Base Details** page, click <img src="assets/5a4e6ce7404032d786e68fcc70f2087c.png" width="22" alt=""> in the upper-right corner of the list.

6. On the **Mind Map** tab, view the generated mind map.

   > **Note**
   >
   > - Click **Regenerate** above the mind map to regenerate the mind map.
   >
   > - Enter a node name above the mind map to search by node.
   >
   > - Control the display of the mind map.
   >
   >   - Enter a percentage in the upper-right corner of the mind map to adjust the display scale.
   >
   >   - Click
   >
   >     in the upper-right corner of the mind map to zoom in.
   >
   >     <img src="assets/6a744c86a6fad1f06aebe529376b0705.png" width="16" alt="">
   >
   >   - Click
   >
   >     in the upper-right corner of the mind map to zoom out.
   >
   >     <img src="assets/71de923885ee43664dadb7147ff5a86d.png" width="18" alt="">
   >
   >   - Click
   >
   >     in the upper-right corner of the mind map to enter full-screen
   >
   >     <img src="assets/0b2af08de02e63d355c764af03e2db3d.png" width="18" alt="">
   >
   >     mode.
   >
   >   - Click
   >
   >     in the upper-right corner of the mind map to restore the default
   >
   >     <img src="assets/7acb15a8b924c8885ccca5f2162cff0f.png" width="19" alt="">
   >
   >     view.

   ![](assets/160eb3d8b0130ab1c80c2b2c98542c36.jpeg)

<a id="section-3-4-11"></a>

### 3.4.11. Retrieval configuration and retrieval testing

The Retrieve Testing tab supports retrieval configuration and retrieval testing.

**Prerequisites**

The operator is an operations administrator by default.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.

2. In the top navigation bar, select **Configurations**.

3. In the left-side navigation pane, choose **Apsara Copilot** > **Knowledge Base Management**.

4. Click the name of a knowledge base to go to its details page.

5. On the **Knowledge Base Details** page, click <img src="assets/5a4e6ce7404032d786e68fcc70f2087c.png" width="22" alt=""> in the upper-right corner of the list.

6. Configure retieval settings.

   <ol type="i">

   <li>

   Click **Retrieval Configurations**.

   </li>

   <li>

   In the **Retrieval Configurations** dialog box, set **Query Mode (query_mode)**,

   </li>

   </ol>

   **Retieved Entity Relationships (top_k)**, **Retrieval Chunks (chunk_top_k)**, and **Enable Reranking (enable_rerank)**.

   > **Note**
   >
   > Query mode supports **hybrid** or **mix**.

   ![](assets/c9f28c86fa2c1efad62e7913ca4a9df5.jpeg)

   <ol type="i" start="3">

   <li>

   Click **OK**.

   </li>

   </ol>

7. Perform retrieval testing. Enter search content in the text box and click **Search**.

   > **Note**
   >
   > - Query Mode:
   >
   >   - The right side displays the currently configured query mode.
   >
   >   - Advanced Keywords: advanced keywords extracted from the search content.
   >
   >   - Basic Keywords: basic keywords extracted from the search content.
   >
   > - The section below displays the retrieved information.

   ![](assets/b03112368b50a3ca47eeb62a820b7ea1.jpeg)

<a id="section-3-5"></a>

## 3.5. AI-assisted cloud resource management

You can use custom configurations to better manage your cloud resources.

<a id="section-3-5-1"></a>

### 3.5.1. AI-assisted creation

Configure personalized scenarios for AI-assisted creation of cloud services.

**Prerequisites**

The operator is an operations administrator by default.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.

2. In the top navigation bar, select **Configurations**.

3. In the left-side navigation pane, select **Apsara Copilot** > **Auxiliary Cloud Resource Management**.

4. Click the **AI-assisted Creation** tab.

5. Complete the AI-assisted creation configuration.

   | Configuration item | Description |
   | --- | --- |
   | Cloud Service | Select a cloud service for AI-assisted creation. Currently, the system supports only Elastic Compute Service (ECS) Instance and Virtual Private Cloud (VPC). |
   | Custom Scenario | Configure custom scenarios as needed for use during assisted resource creation.<br>• <strong>Add a scenario</strong>: Click <strong>Add Scenario</strong> to customize a scenario. You can select <strong>Enumeration Scenario</strong>, <strong>Scenario Description</strong>, or <strong>None</strong>.<br>• <strong>Delete a scenario</strong>: Click<img src="assets/f06d8312670e30ae24c8af8ff4d86b96.png" width="19" alt="">next to the scenario.<br>• <strong>Adjust the scenario order</strong>: Drag<img src="assets/0fd2443b6c1d63d8c744314bd1335a0d.png" width="15" alt="">in front of a scenario to adjust its<br>display order.<br>• <strong>Restore the preset scenario</strong>: Click <strong>Restore Preset Scenario</strong>, and the system automatically loads the default layout and scenario configurations. |

   ![](assets/027f706c392b047625f89ec38ce67274.jpeg)

6. Click **Save**.

**Result display**

After you configure assisted creation for a cloud service, Apsara Copilot intelligently plans and assists users in creating resources based on personalized scenarios.

![](assets/52b6a1081c0423225c94a284fd4db4f5.jpeg)

<a id="section-3-5-2"></a>

### 3.5.2. AI-assisted configuration change

You can configure rules for the AI-assisted configuration change of cloud products. These rules are used to analyze and provide recommendations when you upgrade or downgrade a cloud product.

**Prerequisites**

The operator is an operations administrator by default.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.

2. In the top menu bar, select **Configurations**.

3. In the navigation pane on the left, select **Apsara Copilot** > **Auxiliary Cloud Resource Management**.

4. Click the **AI-assisted Configuration Change** tab.

5. Configure the settings for assisted Upgrade/Downgrade.

   | Configuration item | Description |
   | --- | --- |
   | Change Service Configurations | Select the cloud product to upgrade or downgrade. Currently, only Elastic Computing Service (ECS) and Server Load Balancer (SLB) are supported. |
   | Rule Template | Select a rule template. If the predefined templates do not meet your needs, customize a rule template. |
   | Rule Description | Displays the details of the selected rule template. |

   ![](assets/6829a2a6328c167d6ea90ad4fb527190.jpeg)

6. Click **Apply**.

**Customize a rule template**

1. On the **AI-assisted Configuration Change** tab, click **Manage Rules** to the right of **Rule Template**.

2. On the **Manage Rules** panel, click <img src="assets/5bf11701efacc416cf4771108f90ca96.png" width="10" alt=""> .

3. Configure the rule.

   | Configuration item | Description |
   | --- | --- |
   | Rule Name | Enter a name for the rule. The name must be unique. |
   | Monitoring metrics | Displays the monitoring metrics supported by the current cloud product.These metrics are used for monitoring analysis and in the rule description. |
   | Rule Description | Create an analysis rule for the cloud resource. This rule is used for assisted resource upgrade/downgrade. You can enter a description in <strong>Generate rules with AI</strong> and then insert the generated result. |

   ![](assets/9d258ea0df00d73fad1f61e93e1f63b1.jpeg)

4. Click **Save**.

5. You can perform other operations on rule templates.

   | Operation | Description |
   | --- | --- |
   | Edit a rule template | i. On the <strong>Manage Rules</strong> panel, select a rule and click <strong>Modify</strong>.<br>Note<br>Predefined rule templates cannot be edited.<br>ii. Update the rule name and description.<br>iii. Click <strong>Save</strong>. |
   | Delete a rule template | On the <strong>Manage Rules</strong> panel, select a rule and click <strong>Delete</strong>.<br>Note<br>Predefined rule templates cannot be deleted. |

**Results**

After configuring the AI-assisted configuration change for a cloud product, Apsara Assistant uses the applied rules to provide recommendations during an upgrade or downgrade.

![](assets/495c74526dee099bc0b4d024d5f00777.jpeg)

<a id="section-4"></a>

# 4.Application of Apsara Copilot

<a id="section-4-1"></a>

## 4.1. Apsara Copilot chats

Apsara Copilot allows users to ask the platform questions about cloud services in natural language, consult AI for information, and engage in intelligent chats with AI.

**Prerequisites**

The user, as an operations administrator, has enabled the display of the AI assistant in the Apsara Uni-manager Management Console under **Configurations** > **Apsara Copilot** > **Custom Settings**.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.

2. Click <img src="assets/7036111951b1605e895939271975b629.jpeg" width="20" alt=""> in the top navigation bar or floating menu to enter Apsara Copilot.

   ![](assets/7ebd5351e1025d23b8f81745437a7e97.jpeg)

   <img src="assets/dd103ca8d4b0cc2e5ad28d59dc27c10c.png" width="26" alt="">

3. In the **Apsara Copilot** dialog box, enter your question and click

   .

   ![](assets/19b6584b0dbb526afaa69ce1e37afbb9.jpeg)

   | Scenario | Description |
   | --- | --- |
   | Knowledge Q&amp;A | Provides accurate answers and guidance for usage-related questions regarding cloud service recommendations, feature operations, limitations, and best practices. |
   | Resource Search | Precisely locates target resources, provides detailed information, and enables viewing of associated resources. |
   | Resource Operation | Supports operations such as creating, modifying, and deleting cloud resources to simplify your resource management process. |
   | Bill Analysis | Analyzes your cloud resource usage costs, generates detailed expense reports, and provides optimization suggestions to reduce overall spending. |
   | Resource Analysis | Tracks cloud resource usage, including utilization and performance metrics, to help you fully understand resource status and optimize resource allocation. |
   | Code Generation | Automatically generates code samples in multiple programming languages for OpenAPI and Terraform based on your requirements, improving development efficiency and code quality. |

   > **Note**
   >
   > - Apsara Copilot supports multiple models. You can switch between different models when asking questions. If the selected model supports deep thinking, you can enable or disable deep thinking mode.
   >
   > - Enter "/" in the input box to add a slot, then select the corresponding slot value based on the slot type.
   >
   > - Click
   >
   >   in the input box to expand the command center.
   >
   >   <img src="assets/64ee49ded714d96db92d6190e7d05c56.png" width="28" alt="">
   >
   >   - The command center provides a complete list of common Apsara Copilot command examples for quick instruction sending.
   >
   >   - Enter keywords in the input box under the command center to quickly find related command questions.
   >
   >   - View recommended questions by command type and trigger them with one click.
   >
   > - Click
   >
   >   in the input box to choose whether to enable MCP and intranet search.
   >
   >   <img src="assets/25a332dd44b8987bef110fefd86a5024.png" width="21" alt="">
   >
   >   - After enabling MCP and selecting connected cloud services, you can invoke MCP services of those cloud services.
   >
   >   - The intranet search option appears here only when you have enabled its display in the custom settings of Apsara Copilot.

4. After Apsara Copilot responds, you can perform the following operations.

   <img src="assets/6738bce5918c2c4327a2413d4903807e.png" width="14" alt=""> : Like — indicates approval of the response.

   <img src="assets/8a936d57fa7f7688a14cc083fc7d1905.png" width="14" alt=""> : Dislike — indicates disapproval of the response.

   <img src="assets/b11ef75a4caea41c8e9753448f7364ae.png" width="14" alt=""> : Copy — copies the response content.

   <img src="assets/3f7f07362ba6ff3d73bcbca89efd7590.png" width="14" alt=""> : Export response — exports the generated response.

**Related operations**

| Related operation | Description |
| --- | --- |
| New chat | Click<img src="assets/a686a9db9c5be5f98d46a52f78660087.png" width="13" alt="">above the dialog box to start a new chat. |
| Chat history | Click<img src="assets/d463d2e91c38eb3f55cfbc77c2db8495.png" width="11" alt="">above the dialog box to view chat history. |
| Full screen | Click<img src="assets/a61f53bb3b0073d0c27ef5fcdb41b684.png" width="12" alt="">above the dialog box to display the Apsara Copilot dialog box in full<br>screen. |
| Settings | Click<img src="assets/1659a0d67d2d232fe29056448e089355.png" width="13" alt="">above the dialog box to select whether to enable word selection. When<br>enabled, left-click to highlight content on the console page, then click <strong>Consult</strong> <strong>Apsara Copilot</strong> to automatically trigger Q&amp;A for the selected content. |
| Homepage | Click<img src="assets/a01acdae2242a6e11735589511b593b9.png" width="13" alt="">above the dialog box or click <strong>Assistant Introduction</strong> in the dialog box to<br>go to the Apsara Copilot homepage. |
| Close | Click<img src="assets/e7b7a3de0d1b6133487da6474e906814.png" width="15" alt="">above the dialog box to close the Apsara Copilot dialog box. |
| Help documentation | Click <strong>Documentation</strong> in the dialog box to view Apsara Copilot help documentation. |

<a id="section-4-2"></a>

## 4.2. Perform text-selection Q&A

After you enable text-selection Q&A and select text on a console page, you can trigger Apsara Copilot to answer questions about the selected content.

**Prerequisites**

Text-selection Q&A is enabled for Apsara Copilot.

> **Note**
>
> To enable the feature, click the <img src="assets/1659a0d67d2d232fe29056448e089355.png" width="13" alt=""> icon in the upper-right corner of the Apsara Copilot
>
> pane and turn on Enable Word Selection.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.

2. Click and drag to select text on a console page and select Consult Apsara Copilot to send the selected text to Apsara Copilot.

   ![](assets/6f72e9b31caf53be7e34032d89aaee93.jpeg)

3. Apsara Copilot automatically searches for answers.

   ![](assets/0d3e0c7490728430a3373208b98edccc.jpeg)

<a id="section-4-3"></a>

## 4.3. AI-based intelligent analysis

Apsara Copilot provides intelligent data querying and data insights capabilities for AI-based intelligent analysis scenarios.

For detailed operations of AI-based intelligent analysis, see the **Data analysis** > **Custom analysis** > **Intelligent analysis** section in *Apsara Uni-manager Management Console User Guide*.

![](assets/f02ce88e935f8dc27cc0a822437b670e.jpeg)

<a id="section-4-4"></a>

## 4.4. AI-based bill analysis

Billing data is complex and voluminous. Users struggle to identify underlying trends or potential issues from raw numbers. Apsara Copilot provides AI-based bill analysis capabilities that deliver multi-dimensional insights into billing data. This helps platform users understand resource usage and cost patterns more quickly and efficiently, enabling them to control expenses effectively. Simultaneously, it offers intelligent analytics for platform operators— including anomaly detection in bill fluctuations and trend forecasting—to ensure billing accuracy and optimize operational strategies for revenue growth.

**AI-based bill analysis by product**

For detailed operations of AI-based bill analysis by product, see the **Bill management** > **AI-based bill analysis by product** section in *Apsara Uni-manager Management Console User Guide*.

![](assets/46f34f63d19f129862bba2313e74c0d2.jpeg)

**AI-based bill Aanalysis by organization**

For detailed operations of AI-based bill Aanalysis by organization, see the **Bill management** > **AI-based bill analysis by organization** section in *Apsara Uni-manager Management Console User Guide*.

![](assets/9e248e07ff42598afbf693816c7c1dea.jpeg)

**AI-based bill analysis by bill detail**

AI-based bill analysis by bill detail supports AI parsing of daily and hourly billing details. For detailed operations, see the **Bill management** > **AI-based bill analysis by bill detail** section in *Apsara Uni-manager Management Console User Guide*.

**Daily Details**

![](assets/29475aa61148ca12ecb625b3844af17b.jpeg)

**Hourly Details**

![](assets/7e7ca7f8433221534e6677e4348dbc03.jpeg)

<a id="section-4-5"></a>

## 4.5. AI billing rule analysis

Apsara Copilot provides AI analysis for billing rule scenarios.

For detailed operations of AI billing rule analysis, see the **Pricing** > **AI billing rule analysis** section in *Apsara Uni-manager Management Console User Guide*.

![](assets/bdd997bb1b856d01fa08105a0d331200.jpeg)

<a id="section-5"></a>

# 5.Apsara Copilot operations analytics

Apsara Copilot provides an operations analytics dashboard to help customers better monitor its usage and evaluate business effects.

**Prerequisites**

The operator is an operations administrator by default.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.

2. In the top navigation bar, select **Home**.

3. Click the **AI + Operation** tab to view metric data for **last week** and **last month**.

   | Item | Description |
   | --- | --- |
   | AI Assistant Core Metrics | Displays core data for the AI assistant, including <strong>Comprehensive Score</strong>, <strong>Daily</strong> <strong>Active Users</strong>, and <strong>Total Conversations</strong>.<br>Note<br>Comprehensive score is a composite metric that measures the overall service quality of Apsara Copilot. The system calculates this score based on three dimensions: user satisfaction, performance response, and request success rate. This score reflects the quality of service and user experience during actual usage. |
   | AI Assistant Feature Usage | Displays usage data for scenario-based features such as <strong>Intelligent Q&amp;A</strong>, <strong>Knowledge Coverage</strong>, <strong>Intelligent Analysis</strong>, <strong>AI-assisted Operations</strong>, <strong>Code</strong> <strong>Generation</strong>, and <strong>MPC Calls</strong>. |
   | AI Assistant Performance Response | Displays core performance data for the AI assistant, including <strong>TTFT (Time To</strong> <strong>First Token)</strong> and <strong>Average Generation Speed</strong>. |
   | AI Assistant Resource Consumption | Displays resource consumption data for the AI assistant, including <strong>Consumed</strong> <strong>Tokens</strong> and <strong>Model Inference Latency</strong>. |
   | AI Assistant License Usage | Displays license usage for the AI assistant, including <strong>Standard Agent</strong>, <strong>Resource Management Agent</strong>, <strong>Operations Management Agent</strong>, and <strong>Data</strong> <strong>Insight Agent</strong>. |

   ![](assets/0c4ea8e80baa18b6f33e96ed7c149ecd.jpeg)

<a id="section-6"></a>

# 6.View operation logs

This topic describes how to view the operation logs of Apsara Copilot.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.

2. In the top navigation bar, click **Enterprise**.

3. In the left-side navigation pane, choose **Operation Audit** > **Operation Log**.

4. On the **Operation Log** page, configure filter conditions such as Organization, Product Type, Resource Type, Event Type, Resource ID, Source IP, Event ID, and Start/End Time, and then click **Search**.

   > **Note**
   >
   > Select **Apsara Uni-manager** from the Product Type drop-down list and **Apsara Copilot** from the Resource Type drop-down list.

5. View the displayed operation logs.

   ![](assets/0ad2d2a10dbf2e41de65081225df1514.jpeg)

6. Find the operation log whose details you want to view and click **View** in the **Details** column.

   ![](assets/e63054d80570deafcd9c810d54312aaf.jpeg)

<a id="section-7"></a>

# 7.Appendix

<a id="section-7-1"></a>

## 7.1. Log in to the Apsara Uni-manager Management Console

This topic describes how to log in to the Apsara Uni-manager Management Console.

**Prerequisites**

- The URL of the Apsara Uni-manager Management Console is obtained from the deployment personnel.

- A web browser is available. We recommend that you use Google Chrome.

**Procedure**

1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and press the Enter key.

   ![](assets/687f6d006b35a4552292b1f7b3755914.jpeg)

   > **Note**
   >
   > - You can click the current language in the upper-right corner to switch to another language.

2. Enter your username and password.

   > **Note**
   >
   > - Obtain the username and password from an operations administrator.
   >
   > - If you log in to the Apsara Uni-manager Management Console for the first time, you must follow the on-screen instructions to change the password of your account. For security purposes, the password must be 10 to 32 characters in length. It must contain all of the following character types: uppercase letters, lowercase letters, digits, and special characters. The following special characters are supported: ! @ # $ %

3. Click **Log In**.

4. If multi-factor authentication (MFA) is enabled for your account, perform the corresponding operations in the following scenarios:

   - **This is the first time that you log in to the Apsara Uni-manager Management Console after MFA is forcefully enabled by the administrator.**

     <ol type="a">

     <li>

     On the Bind Virtual MFA Device page, follow the instructions to bind an MFA device.

     </li>

     <li>

     Enter the username and password again as in Step 2 and click **Log On**.

     </li>

     </ol>

     <ol type="i" start="100">

     <li>

     Enter a 6-digit MFA verification code and click **Authenticate**.

     </li>

     </ol>

   - **You have enabled MFA and bound an MFA device.**

     Enter a six-digit MFA verification code and click **Authenticate**.

     > **Note**
     >
     > For information about how to enable MFA and bind an MFA device, see Manage MFA.

**What to do next**

**Forget password**

1. If you forget the login password, click **Forgot Password** below the Password field.

2. On the Forgot Password page, configure the **Account Name** and **Email Address** parameters, specify the verification code, and then click **Confirm**.

   ![](assets/ac6a60f6a1f8edfafab7d3f08d294c4b.jpeg)

   > **Note**
   >
   > - You can use the username of your account and the email address that was used to create the account.
   >
   > - The system sends a link for resetting the password to the email address that you specify.
