# This file will be responsible for turning a markdown file into a json file, that can then be used for embeddings.
# Aim will be to use Alpaca format and trust the process.

from typing import List, Dict
from json import dump
from collections import deque
from random import choice
from pprint import pprint

DEBUG = True

def read_contents_from_md(md_file: str) -> str:
    """This function will simply read the contents from a markdown file, perform any necessary pre-processing, and return the contents..

    Args:
        md_file (str): The path to the file.

    Returns:
        str: The pre-processed contents of the markdown file as a string.
    """
    
    try:
        with open(md_file, "r") as f:
            contents: str = f.read()
            return contents
    except Exception as e:
        print(e)
        return ""

def create_hierarchy(contents: str) -> Dict[str, Dict[str, str | Dict]] | None:
    """This will create a hierarchy of headings and content as found in the markdown file.

    Example:
    ```
    {
        "Database Architecture & Major Types of Databases": {
            "content": '''some content''',
            "children": {
                "Centralized": {
                    "content": '''some other content''',
                    "children": {}
                },
                "Distributed": {
                    "content": '''Then some other content''',
                    "children": {}
                }
            }
        },
        "Types of Databases": {
            "content": '''Last set of content''',
            "children": {}
    }
    ```
    
    Args:
        contents (str): The contents of the markdown file to be parsed.

    Returns:
        (Dict[str, Dict[str, str | Dict]]): A dictionary of headings and their content!
    """
    
    if (not contents): return None
    
    hierarchy: Dict[str, Dict[str, str | List[Dict]]] = {}
    
    # By splitting the contents of the file by "#", we get the content separated by empty strings. The number of empty strings before text, indicates the heading level.
    # Issue: If # exists within the text outside of headings... Then we can have some problems.
    # Will go forward with this in mind.
    
    parsed_content: List[str] = contents.split("#")
    
    # If the file starts with a heading, we want to ignore the split space before it:
    
    if parsed_content[0] == "": parsed_content = parsed_content[1:]
    
    # Now, for the hierarchy building...
    # This process will involve going through a file, and finding the various headings and nested ones, and nesting them appropriately... Rec... Recu... 🤢... Recursively.
    
    #... SIKE! ITERATION BABYYYYY
    
    # Now, each block of split text, will be separated by 0 to 4 empty strings (''), indicative of headings from level 1 to 5.
    
    # Before going forward, we're going to need a heading stack!
    
    # When iterating, we need to keep track of the last heading for each level.
    
    # This will be in the format of: {heading_level: last_heading_for_that_level}
    
    heading_stack: Dict[int, str] = {}
    
    # As we iterate over each of these block of texts, we need to separate the headinigs from the rest of the body.
    
    current_heading_level = 1
    for text_block in parsed_content:
        # Step 1, determine the current heading level!
        if text_block == "": 
            current_heading_level += 1
            continue
        
        # Step 2, find the heading and the body
        # We can accomplish this by splitting that block by `\n`, where the first line would be the heading, and everything else will be the body
        
        heading, body = text_block.split("\n", 1)
        heading = heading.strip() # Need to remove the leading whitespace from the # split.
        
        # Step 3, create the dictionary that will hold the content for this level
        
        content_dict: Dict[str, str | List[Dict]] = {
            "content": body.lstrip("\n"), # Want to remove the leading \n from the split
            "children": {}
        }
        
        # Step 4! Determine where we are in the hierarchy, and whether we need to add this as a child or not.
        # If we're at level 1, then we don't have to worry about finiding the previous one.
        if current_heading_level == 1:
            hierarchy[heading] = content_dict
        else:
            # If we're not at level 1, then we find the heading for the previous levels, and work our way back down.
            prev_level = 1
            parent_dict = hierarchy
            while prev_level < current_heading_level:
                previous_heading = heading_stack[prev_level]
                parent_dict = parent_dict[previous_heading]["children"]
                prev_level += 1
                
            parent_dict[heading] = content_dict
        
        # Step 5, set this heading as the heading for the current level
        heading_stack[current_heading_level] = heading
        
        # Step 6, reset heading level to 1
        current_heading_level = 1
        
    # Once the loop is done, we can return the hierarchy
    
    # These just here for debugging purposes
    if DEBUG:
        if len(hierarchy) == 1:
            filename = "small_sample.json"
        else:
            filename = "sample.json"
        
        with open(filename, "w") as fp:
            dump(hierarchy, fp, indent=4)
    
    return hierarchy

def create_alpaca_json(hierarchy: Dict[str, Dict[str, str | Dict]]) -> List[Dict[str, str]]:
    """This function will create a list of dictionaries following Alpaca format.
    
    Example:
    ```
    [
        {
            "instruction": "Give me information about {Database Architecture & Major Types of Databasees}",
            "input": "{Centralized, Distributed}",
            "output": "{content}"
        }
    ]
    ```

    Args:
        hierarchy (Dict[str, Dict[str, str | Dict]]): A dictionary of headings and their content

    Returns:
        (List[Dict[str, str]]): A list of dictionaries following Alpaca format.
    """
    
    # Okay, now we have our hierarchy for all the data we need. Now to transform it into Alpaca format.
    
    alpaca_json: List[Dict[str, str]] = []
    
    # For this process, we might actually have to use recursion 😷.
    
    # The aim is to go through the hierarchy and create a dictionary from each one matching the alpaca format.
    
    # The instruction will be `{basic prompt} {heading}`.
    basic_prompts = ["Tell me about {}", "Can you clarify {}", "What is {}", "Give me information about {}", "Can you explain {}"]
    
    # The input will be the names of all the subheadings under it by 1 level. (So it's immediate children)
    # The output will be the content of that heading, which at higher levels won't be as useful as the lower levels.
    
    # But of course. Never use Recursion! We'll use an iterative breadth first search instead!

    # level_stack = ["" for _ in range(5)] # We'll go a max of 5 headings deep. This is an improvement to the heading level dictionary!  #UPdate: Nevermind, no need for it
    
    queue = deque([(heading, level_dict) for heading, level_dict in list(hierarchy.items())])
    
    # current_level = 1
    while queue:
        heading, level_dict = queue.popleft()
        # level_stack[current_level - 1] = heading
        
        # Check for children
        children = level_dict["children"]
        if children:
            for child_heading, child_level_dict in children.items():
                queue.append((child_heading, child_level_dict))
        
        # Now that we have the children, we can create what we need!
        
        alpaca_json_dict = {
            "instruction": choice(basic_prompts).format(heading),
            "input": ' '.join(list(children.keys())),
            "output": level_dict["content"]
        }
        
        alpaca_json.append(alpaca_json_dict)
    
    if DEBUG:
        with open("alpaca_json.json", "w") as fp:
            dump(alpaca_json, fp, indent=4)
    
    return alpaca_json

def md_to_alpaca_json(md_file: str) -> List[Dict[str, Dict[str, str]]]:
    """This function will be responsible for turning a given markdown file, into a json file following Alpaca format, ie, [{instruction, input, output}]

    Args:
        md_file (str): The filepath to the markdown file.

    Returns:
        List[Dict[str, Dict]]: A list of dictionaries following Alpaca format built using the data from the markdown file.
    """
    
    # The process!
    
    # Read the contents of the markdown file.
    contents: str = read_contents_from_md(md_file)
    
    # Create a hierarchy using the headings of the markdown file. (Would love to use grep, but we have to be platform friendly)
    hierarchy: Dict[str, Dict[str, str | Dict]] = create_hierarchy(contents)
    
    # For each heading, create a dictionary with the instruction, input, and output.
        # The instruction will be a prompt such as: "Give me information about {heading_title}"
        # The input will be the names of the subheadings, which will serve to provide some form of additional context. (I hope)
        # The output will be the text content of the current heading.

    alpaca_json: List[Dict[str, str]] = create_alpaca_json(hierarchy)
    
    # Return the list of dictionaries.
    
    return alpaca_json

if __name__ == "__main__":
    print(md_to_alpaca_json("./sample.md"))