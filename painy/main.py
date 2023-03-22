from .comment import get_comment
from .enums import Action
from .git import commit
import argparse
import openai
import os


def main():
    api_key = os.getenv("OPENAI_API_KEY")

    if api_key is None:
        print("Error: OPENAI_API_KEY not set")
        exit(1)

    openai.api_key = api_key
    
    parser = argparse.ArgumentParser(
        prog="Painy",
        description="A tool to help you write better commit messages."
    )
    
    parser.add_argument("action", choices=["comment", "commit"], help="The action to perform")
    parser.add_argument("--check-all", action="store_true", help="Check all files previously registered in git, not just staged ones")
    
    args = parser.parse_args()
    
    action = args.action if args.action is not None else Action.COMMENT.value
    
    staged = not args.check_all
    
    if action == Action.COMMENT.value:
        comment = get_comment(staged=staged)
        print(comment)
    elif action == Action.COMMIT.value:
        comment = get_comment(staged=staged)
        print(f"Commit message: {comment}")
        commit(comment)
        

if __name__ == "__main__":
    main()