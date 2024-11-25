import os
import re
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from tqdm import tqdm

# Configuration
TOPIC = "cybersecurity"   # Easy to change this to any other topic
TOTAL_PROMPTS = 10        # Total number of prompts to generate
BATCH_SIZE = 5            # Batch size for API calls
MIN_WORDS = 15           # Minimum words in prompt
MAX_WORDS = 30           # Maximum words in prompt
OUTPUT_DIR = "/the-place-you-save-your-prompts"

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

def is_valid_length(text):
    """Check if the prompt meets the word count requirements."""
    word_count = len(text.split())
    return MIN_WORDS <= word_count <= MAX_WORDS

# Step 1: Configure the LLM
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.7,
    max_tokens=100  # Increased to accommodate longer prompts
)

# Step 2: Define the base prompt
base_prompt = f"""Generate a random prompt that a user might submit to a large language model about {TOPIC}. 
The prompt MUST:
- Contain between {MIN_WORDS} and {MAX_WORDS} words (strictly enforced)
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
valid_responses = []

print(f"Generating {TOTAL_PROMPTS} prompts about {TOPIC}...")
while len(valid_responses) < TOTAL_PROMPTS:
    remaining = TOTAL_PROMPTS - len(valid_responses)
    batch_messages = messages[:min(remaining + 2, BATCH_SIZE)]  # Generate extra prompts to account for potential invalids
    
    for sub_batch in tqdm([batch_messages], desc="Processing batch"):
        sub_responses = llm.batch(sub_batch)
        for response in sub_responses:
            prompt_text = response.content.strip()
            if is_valid_length(prompt_text):
                valid_responses.append(prompt_text)
                if len(valid_responses) >= TOTAL_PROMPTS:
                    break

# Step 4: Save valid prompts as markdown files
os.makedirs(OUTPUT_DIR, exist_ok=True)

print(f"\nSaving prompts to {OUTPUT_DIR}...")
used_filenames = set()

for i, prompt_text in enumerate(valid_responses[:TOTAL_PROMPTS]):
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
word_count: {len(prompt_text.split())}
---

{prompt_text}
"""
    file_path = os.path.join(OUTPUT_DIR, filename)
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(markdown_content)

print(f"Successfully generated {TOTAL_PROMPTS} {TOPIC} prompts and saved them to {OUTPUT_DIR}")