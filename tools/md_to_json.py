# This file will be responsible for turning a markdown file into a json file, that can then be used for embeddings.
# Aim will be to use Alpaca format and trust the process.

from typing import List, Dict

def md_to_json(md_file: str) -> List[Dict[str, Dict]]:
    """This function will be responsible for turning a given markdown file, into a json file following Alpaca format, ie, [{instruction, input, output}]

    Args:
        md_file (str): The filepath to the markdown file.

    Returns:
        List[Dict[str, Dict]]: A list of dictionaries following Alpaca format built using the data from the markdown file.
    """
    
    # The process!
    
    # Read the contents of the markdown file.
    
    # Create a hierarchy using the headings of the markdown file. (Would love to use grep, but we have to be platform friendly)
    
    # Can have an empty list defined here, which will be the item returned.
    
    # For each heading, create a dictionary with the instruction, input, and output.
        # The instruction will be a prompt such as: "Give me information about {heading_title}"
        # The input will be the names of the subheadings, which will serve to provide some form of additional context. (I hope)
        # The output will be the text content of the current heading.
    
    # Return the list of dictionaries.
    pass