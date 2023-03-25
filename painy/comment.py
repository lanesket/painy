from painy.git import *
from painy.chat import Model
from painy import console
from painy.utils import print_commit_message


comment_prompt = """
    You are a program that looks at the git diff response and writes a concise, short and understandable comment based on these code changes.
    Your response should be just a comment for the git and nothing else. 
    Sort the changes in the comment by importance: from most important to least important.
    Do not mention the names of the files that have been modified unless it is very important.
    The shorter the comment, the better, but the maximum length is 200 characters.
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