import os
import re
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from tqdm import tqdm

# Configuration
TOPIC = "cybersecurity"  # Easy to change this to any other topic
TOTAL_PROMPTS = 10  # Reduced total number of prompts
BATCH_SIZE = 5      # Reduced batch size

def create_filename(prompt_text):
    """Create a filename from the prompt text."""
    # Convert to lowercase
    text = prompt_text.lower()
    
    # Remove punctuation and special characters
    text = re.sub(r'[^\w\s-]', '', text)
    
    # Replace whitespace with hyphens
    text = re.sub(r'\s+', '-', text.strip())
    
    # Limit length and remove trailing hyphens
    text = text[:50].rstrip('-')
    
    return f"{text}.md"

# Step 1: Configure the LLM
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.7,
    max_tokens=50
)

# Step 2: Define the base prompt
base_prompt = f"""Generate a random prompt that a user might submit to a large language model about {TOPIC}. 
The prompt should:
- Be between 10 and 30 words in length
- Be specifically about {TOPIC}
- Ask a clear, focused question or request
- Be suitable for a general technical audience
In your response, output only the text of the prompt without any additional text."""

# Step 3: Generate prompts in batch
messages = [
    [HumanMessage(content=base_prompt)] for _ in range(TOTAL_PROMPTS)
]

# Process in smaller batches
responses = []

print(f"Generating {TOTAL_PROMPTS} prompts about {TOPIC}...")
for i in tqdm(range(0, TOTAL_PROMPTS, BATCH_SIZE)):
    sub_batch = messages[i:i + BATCH_SIZE]
    sub_responses = llm.batch(sub_batch)
    responses.extend(sub_responses)

# Step 4: Save each prompt as a markdown file
output_dir = "/your-dir"
os.makedirs(output_dir, exist_ok=True)

print(f"\nSaving prompts to {output_dir}...")
used_filenames = set()

for i, response in enumerate(responses):
    prompt_text = response.content.strip()
    
    # Create base filename from prompt content
    base_filename = create_filename(prompt_text)
    
    # Handle duplicate filenames by adding a number if necessary
    filename = base_filename
    counter = 1
    while filename in used_filenames:
        name, ext = os.path.splitext(base_filename)
        filename = f"{name}-{counter}{ext}"
        counter += 1
    
    used_filenames.add(filename)
    
    # Create markdown content with metadata
    markdown_content = f"""---
prompt_id: {i + 1}
type: {TOPIC}
---

{prompt_text}
"""
    file_path = os.path.join(output_dir, filename)
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(markdown_content)

print(f"Successfully generated {TOTAL_PROMPTS} {TOPIC} prompts and saved them to {output_dir}")