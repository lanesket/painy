import subprocess


def get_changed_files_git() -> list:
    output = subprocess.check_output(["git", "diff", "--name-only", "HEAD"], stderr=subprocess.STDOUT)
    files = output.decode("utf-8").strip().split("\n")
    return files

def get_file_changes_git(file_path: str) -> str:
    output = subprocess.check_output(["git", "diff", "HEAD", "--", file_path])
    changes = output.decode("utf-8")
    return changes

def get_changes_staged_git() -> str:
    output = subprocess.check_output(["git", "diff", "--staged"], stderr=subprocess.STDOUT)
    changes = output.decode("utf-8").strip()
    return changes