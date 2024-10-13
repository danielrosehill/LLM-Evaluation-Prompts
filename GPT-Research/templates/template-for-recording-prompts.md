Here are additional pieces of metadata that you may want to capture when recording prompts for evaluating LLMs and fine-tuned models:

### Additional Metadata:
1. **Prompt ID**: A unique identifier for tracking and referencing each prompt.
2. **LLM Tested**: Models (LLMs or fine-tuned versions) that have been evaluated with this prompt.
3. **Evaluation Criteria**: Metrics or success criteria (e.g., accuracy, fluency, creativity, etc.) used to evaluate the LLM's performance.
4. **Expected Output**: A description of what the ideal response should look like.
5. **Prompt Category**: Classification of the prompt (e.g., summarization, sentiment analysis, code generation, etc.).
6. **Difficulty Level**: A subjective rating of how challenging the task is for an LLM (e.g., easy, medium, hard).
7. **Notes on Performance**: Space to record observations about the model's performance or behavior.
8. **Task-Specific Constraints**: Any limitations or constraints on the prompt (e.g., time-sensitive, word limit, etc.).
9. **Prompt Variants**: If the prompt has multiple versions or variations for testing.
10. **Response Length**: Suggested or expected length of the response (if applicable).
11. **Domain**: The specific domain or industry the prompt pertains to (e.g., healthcare, finance, etc.).
12. **Language**: Language the prompt is written in and/or expected to be answered in.

### Template for Capturing Prompts:
You can use the following template in **Markdown** or **JSON** to record and manage your prompts in the repository:

#### Markdown Template:
```markdown
### Prompt ID: [Unique Prompt Identifier]
- **Prompt Creation Date**: [YYYY-MM-DD]
- **Prompt Update Date**: [YYYY-MM-DD] (if applicable)
- **Target Use-Case**: [Brief description of the use case]
- **Prompt Text**: 
  ```
  [Insert the actual prompt here]
  ```

- **LLM Tested**: [List of models tested with this prompt]
- **Evaluation Criteria**: [Metrics for evaluation, e.g., accuracy, fluency, relevance]
- **Expected Output**: [Description of the ideal response]
- **Prompt Category**: [E.g., Summarization, Sentiment Analysis, etc.]
- **Difficulty Level**: [Easy, Medium, Hard]
- **Notes on Performance**: [Any observations about the model's behavior or results]
- **Task-Specific Constraints**: [Any limits, e.g., word count or response time]
- **Prompt Variants**: [Any variations of the prompt]
- **Response Length**: [Suggested length of the response]
- **Domain**: [E.g., healthcare, finance]
- **Language**: [Language used in the prompt and expected output]
```

#### JSON Template:
```json
{
  "prompt_id": "Unique Prompt Identifier",
  "prompt_creation_date": "YYYY-MM-DD",
  "prompt_update_date": "YYYY-MM-DD",
  "target_use_case": "Brief description of the use case",
  "prompt_text": "Insert the actual prompt here",
  "llm_tested": ["Model 1", "Model 2"],
  "evaluation_criteria": ["Accuracy", "Fluency", "Relevance"],
  "expected_output": "Description of the ideal response",
  "prompt_category": "Summarization, Sentiment Analysis, etc.",
  "difficulty_level": "Easy/Medium/Hard",
  "notes_on_performance": "Any observations about the model's behavior or results",
  "task_specific_constraints": "Any limits, e.g., word count or response time",
  "prompt_variants": ["Variant 1", "Variant 2"],
  "response_length": "Suggested length of the response",
  "domain": "Healthcare, Finance, etc.",
  "language": "Language used in the prompt and expected output"
}
```

This structured approach ensures you capture the necessary metadata, allowing you to systematically compare models across different tasks and workflows while maintaining detailed records.

# Prompt 2

Please provide a version in YAML too

# Output 2

Here's a **YAML** version of your prompt evaluation template:

```yaml
prompt_id: "Unique Prompt Identifier"
prompt_creation_date: "YYYY-MM-DD"
prompt_update_date: "YYYY-MM-DD"
target_use_case: "Brief description of the use case"
prompt_text: |
  Insert the actual prompt here
llm_tested:
  - Model 1
  - Model 2
evaluation_criteria:
  - Accuracy
  - Fluency
  - Relevance
expected_output: "Description of the ideal response"
prompt_category: "Summarization, Sentiment Analysis, etc."
difficulty_level: "Easy/Medium/Hard"
notes_on_performance: "Any observations about the model's behavior or results"
task_specific_constraints: "Any limits, e.g., word count or response time"
prompt_variants:
  - Variant 1
  - Variant 2
response_length: "Suggested length of the response"
domain: "Healthcare, Finance, etc."
language: "Language used in the prompt and expected output"
```

This **YAML** template follows the same structure as the JSON and Markdown versions, offering a human-readable format for organizing your prompts and associated metadata. It's especially useful if you're working with configuration files or want a more minimalist format for your repository.

# Prompt 3

Please provide a version in YAML without the comments:

# Output 3

Here is the **YAML** version of the template without comments:

```yaml
prompt_id: "Unique Prompt Identifier"
prompt_creation_date:  
prompt_update_date:  
target_use_case 
prompt_text: |
  Insert the actual prompt here
llm_tested:
  - Model 1
  - Model 2
evaluation_criteria:
  - Accuracy
  - Fluency
  - Relevance
expected_output:  
prompt_category: 
difficulty_level:  
notes_on_performance: " 
task_specific_constraints:  
prompt_variants:
  - Variant 1
  - Variant 2
response_length:  
domain:  
language:  
```

This **YAML** template is ready to use in your repository for capturing and organizing your evaluation prompts.