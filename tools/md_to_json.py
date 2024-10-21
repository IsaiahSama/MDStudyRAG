# This file will be responsible for turning a markdown file into a json file, that can then be used for embeddings.
# Aim will be to use Alpaca format and trust the process.

from typing import List, Dict

def read_contents_from_md(md_file: str) -> str:
    """This function will simply read the contents from a markdown file, perform any necessary pre-processing, and return the contents..

    Args:
        md_file (str): The path to the file.

    Returns:
        str: The pre-processed contents of the markdown file as a string.
    """
    
    raise NotImplementedError

def create_hierarchy(contents: str) -> Dict[str, Dict[str, str | List[Dict]]]:
    """This will create a hierarchy of headings and content as found in the markdown file.

    Example:
    ```
    {
        "Database Architecture & Major Types of Databases": {
            "content": "some content",
            "children": [
                {
                    "Centralized": {
                        "content": "some other content",
                        "children": []
                    }
                },
                {
                    "Distributed": {
                        "content": "Then some other content",
                        "children": []
                    }
                }
            ]
        },
        "Types of Databases": {
            "content": "Last set of content",
            "children": []
    }
    ```
    
    Args:
        contents (str): The contents of the markdown file to be parsed.

    Returns:
        Dict[str, Dict[str, str | List[Dict]]]: A dictionary of headings and their content!
    """
    
    raise NotImplementedError

def create_alpaca_json(hierarchy: Dict[str, Dict[str, str | List[Dict]]]) -> List[Dict[str, str]]:
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
        hierarchy (Dict[str, Dict[str, str | List[Dict]]]): A dictionary of headings and their content

    Returns:
        List[Dict[str, str]]: A list of dictionaries following Alpaca format.
    """
    
    raise NotImplementedError

def md_to_json(md_file: str) -> List[Dict[str, Dict[str, str]]]:
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
    hierarchy: Dict[str, Dict[str, str | List[Dict]]] = create_hierarchy(contents)
    
    # For each heading, create a dictionary with the instruction, input, and output.
        # The instruction will be a prompt such as: "Give me information about {heading_title}"
        # The input will be the names of the subheadings, which will serve to provide some form of additional context. (I hope)
        # The output will be the text content of the current heading.

    alpaca_json: Dict[str, Dict[str, str]] = create_alpaca_json(hierarchy)
    
    # Return the list of dictionaries.
    
    return alpaca_json