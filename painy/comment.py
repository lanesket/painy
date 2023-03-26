from painy.git import *
from painy.chat import Model
from painy import console
from painy.utils import print_commit_message


comment_prompt = """
    You are a professional software that looks at the git diff response and writes a concise, short and understandable comment based on this response.
    Your response should be just a short commit message for the git and nothing else. 
    Sort the changes in the commit message by importance: from most important to least important.
    Do not mention the names of the files that have been modified unless it is very important.
    The shorter the commit message, the better, but the maximum length is 200 characters.
    
    Here are examples for you. They are in format (git diff in `<git-diff>` and possible response commit messages for this git diff, separated by new lines and comma):
    1)
        `index 30f6c85..a16b8e9 100644
        --- a/my_module.py
        +++ b/my_module.py
        @@ -1,3 +1,4 @@
        +import math
        
        def square(x):
        -    return x * x
        +    return math.pow(x, 2)`   
        
    [
        "Refactor square function. Use math.pow instead of multiplication.",
        "Refactor square function.",
        "Use pow instead of multiplication."
    ]
    
    2) 
        `index 9c59da1..f0c12f2 100644
        --- a/my_module.py
        +++ b/my_module.py
        @@ -1,5 +1,8 @@
        +from typing import List
        +
        def filter_even_numbers(numbers):
        -    return [n for n in numbers if n % 2 == 0]
        +    if not isinstance(numbers, List):
        +        raise TypeError("numbers must be a list")
        +    return [n for n in numbers if n % 2 == 0]`
        
    [
        "Add input validation to filter_even_numbers function",
        "Check if numbers is a list in filter_even_numbers function",
        "Check if numbers is a list",
        "Validation for filter_even_numbers function"
    ]
    
    
    
"""

def get_commmit_message(diff_str: str, interactive: bool = False):
    with console.status(status="Generating commit message...", spinner='aesthetic'):
        model = Model(purpose_prompt=comment_prompt)
        response = model.get_response(prompt=diff_str)
    
    return response

def comment_interactive(msg: str, diff_str: str) -> str:
    """
    Interactive mode for generating commit messages.
    
    Args:
        msg (str): Already (first time) generated commit message
    
    Returns:
        str: Final commit message
    """
    while True:
        console.rule(characters="=", style="cyan")
        option = console.input("Try another one? [green]y[/green]/[red]n[/red]: ")
        
        if option.lower() in ["y", "yes"]:
            msg = get_commmit_message(diff_str)
            print_commit_message(console, msg)
        else:
            return msg