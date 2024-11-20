# Prompt To Generate Script For Converting Stored Evaluation Prompts

Please provide a Let's devise a system for storing prompts in our evaluation prompt repository.

Let's develop a system that will allow the user to create a prompt in markdown using a basic structure like this:

Prompt title
Use case description
Prompt version
Creation date
Prompt text
Notes

The user will capture the prompts as simple markdown files. Each of these paramters will be a heading and then the user will input text. 

Like this:

# Prompt Title

OPML generation test prompt


Next, let's write a script. This script will glob through all the prompts in a specific folder. All the prompts will be structured as I described.

The script will create a JSON that corresponds to every prompt in the output folder. The script will ask the user to specify the input and output folder when it first runs. 

The script will create the JSON files using the same filename as the markdown documents they were generated from. If my prompt is opmlgeneration.md then the generated JSON file would be opmlgeneration.json

The generated JSON files will contain all of the parameters in the original markdown document as key-value pairs. But they will also include the following for each prompts:

- Prompt characteter count
- Estimated tokens