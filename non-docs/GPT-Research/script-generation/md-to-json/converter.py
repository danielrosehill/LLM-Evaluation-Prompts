import os
import json
import glob

def extract_prompt_details(markdown_content):
    lines = markdown_content.split('\n')
    prompt_data = {}
    
    current_heading = ""
    for line in lines:
        line = line.strip()
        if line.startswith("#"):
            current_heading = line.lstrip("#").strip()  # Remove # and strip spaces
            prompt_data[current_heading] = ""
        elif current_heading:
            prompt_data[current_heading] += line + " "

    # Trim any extra spaces
    for key in prompt_data:
        prompt_data[key] = prompt_data[key].strip()

    # Calculate additional metadata
    prompt_text = prompt_data.get("Prompt text", "")
    prompt_data["Prompt character count"] = len(prompt_text)
    prompt_data["Estimated tokens"] = len(prompt_text.split()) // 4  # Rough estimation of token count

    return prompt_data

def markdown_to_json(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        
    for filepath in glob.glob(os.path.join(input_folder, "*.md")):
        filename = os.path.basename(filepath).replace('.md', '.json')
        output_path = os.path.join(output_folder, filename)
        
        with open(filepath, 'r') as file:
            markdown_content = file.read()
            prompt_data = extract_prompt_details(markdown_content)
            
            with open(output_path, 'w') as json_file:
                json.dump(prompt_data, json_file, indent=4)
                
    return f"JSON files have been generated in {output_folder}"

# Example usage
input_folder = input("Please specify the input folder path: ")
output_folder = input("Please specify the output folder path: ")
markdown_to_json(input_folder, output_folder)
