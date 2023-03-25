import argparse
import openai
import os
from painy import console
from painy.comment import get_commmit_message, comment_interactive
from painy.enums import Action
from painy.git import commit, get_changed_files, get_diff_str
from painy.utils import print_commit_message


def main():
    api_key = os.getenv("OPENAI_API_KEY")

    if api_key is None:
        console.print("[red]Error: OPENAI_API_KEY not set[/red]")
        exit(1)

    openai.api_key = api_key
    
    parser = argparse.ArgumentParser(
        prog="Painy",
        description="A tool to help you write better commit messages."
    )
    
    parser.add_argument("action", choices=["comment", "commit"], help="The action to perform")
    parser.add_argument("--check-all", action="store_true", help="Check all files previously registered in git, not just staged ones")
    parser.add_argument("-i", "--interactive", action="store_true", help="Run in interactive mode")
    
    args = parser.parse_args()
    
    action = args.action if args.action is not None else Action.COMMENT.value
    
    staged = not args.check_all
    interactive = args.interactive
    
    try:
        changed_files = get_changed_files(staged)
        diff_str = get_diff_str(changed_files)
    except Exception as e:
        console.print(f"[red]{e}[/red]")
        return
    
    if action == Action.COMMENT.value:
        msg = get_commmit_message(diff_str)
        print_commit_message(console, msg)
        
        if interactive:
            msg = comment_interactive(msg, diff_str)
            
    elif action == Action.COMMIT.value:
        msg = get_commmit_message(diff_str)
        print_commit_message(console, msg)
         
        if interactive:
            msg = comment_interactive(msg, diff_str)
            
            option = console.input("Do you want to commit with this message? [green]y[/green]/[red]n[/red]: ")
            
            if option.lower() in ["y", "yes"]:
                commit(msg)
        else:
            print_commit_message(console, msg)
            commit(msg)
        

if __name__ == "__main__":
    main()