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

def get_comment(only_staged: bool = True):
    if not only_staged:
        try:
            changed_files = get_changed_files_git()
        except subprocess.CalledProcessError:
            return "Error. Are you in a git repository?"
        
        if len(changed_files) == 0:
            return "No files changed."
        
        changes = []
        
        valid_extensions = get_valid_extensions()
        
        changed_files = [file for file in changed_files if file != '']
        changed_files = [file for file in changed_files if file.split(".")[-1] in valid_extensions]
        
        print("Changed files: " + str(changed_files))
        
        for file in changed_files:
            changes.append(get_file_changes_git(file))
        
        changes_str = "\n".join(changes)
    else:
        try:
            changes_str = get_changes_staged_git()
            
            if not changes_str:
                return "No changes staged."
        except subprocess.CalledProcessError:
            return "Error. Are you in a git repository?"
        
    model = Model(purpose_prompt=comment_prompt)
    response = model.get_response(prompt=changes_str)
    
    return response