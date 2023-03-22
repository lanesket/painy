import subprocess
import re


def get_changed_files(staged=False) -> list:
    cmd = ["git", "diff", "--name-only"]
    
    if staged:
        cmd += ["--staged"]
    
    output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
    
    files = output.decode("utf-8").strip().split("\n")
    return files

def get_ipynb_changes_staged(file_path: str) -> str:
    assert file_path.endswith(".ipynb")
    
    cmd = ["nbdiff", file_path]    
    output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
    changes = output.decode("utf-8").strip() + "\n"
    
    # Remove additional info
    regs = [
        "##.* added \/nbformat:[\n \S]*?\n\n",
        "##.* added \/nbformat_minor:[\n \S]*?\n\n",
        "##.* added \/metadata:[\n \S]*?\n\n"]
    
    for reg in regs:
        changes = re.sub(reg, "", changes)
    
    return changes

def get_file_changes(file_path: str) -> str:
    if file_path.endswith(".ipynb"):
        changes = get_ipynb_changes_staged(file_path)
    else:
        output = subprocess.check_output(["git", "diff", "HEAD", "--", file_path])
        changes = output.decode("utf-8")
    return changes

def get_changes_staged() -> str:
    output = subprocess.check_output(["git", "diff", "--staged"], stderr=subprocess.STDOUT)
    changes = output.decode("utf-8").strip()
    return changes

def commit(commit_message: str) -> None:
    """
    Commits the staged changes with the given commit message.
    Used to commit the auto-generated commit message.
    
    Args:
        commit_message (str): The commit message to use.
    """
    subprocess.check_output(["git", "commit", "-m", commit_message], stderr=subprocess.STDOUT)