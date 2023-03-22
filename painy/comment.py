from .git import *
from .chat import Model
from .utils import get_package_path, get_valid_extensions


comment_prompt = """
    You are a program that looks at the git diff response and writes a concise, short and understandable comment based on these code changes.
    Your response should be just a comment for the git and nothing else. 
    Sort the changes in the comment by importance: from most important to least important.
    Do not mention the names of the files that have been modified unless it is very important.
    The shorter the comment, the better, but the maximum length is 200 characters.
"""

def get_comment(staged: bool = True):
    try:
        changed_files = get_changed_files(staged=staged)
    except subprocess.CalledProcessError:
        return "Error. Are you in a git repository?"
    
    valid_extensions = get_valid_extensions()
    
    changed_files = [file for file in changed_files if file != '']
    changed_files = [file for file in changed_files if f".{file.split('.')[-1]}" in valid_extensions]
    
    if len(changed_files) == 0:
        return "No files changed."
    
    print("Changed files: " + str(changed_files))
    
    diffs = []
    
    for file in changed_files:
        diff = get_file_changes(file)
        diffs.append(diff)
    
    diff_str = "\n".join(diffs)
        
    model = Model(purpose_prompt=comment_prompt)
    response = model.get_response(prompt=diff_str)
    
    return response