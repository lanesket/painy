from .comment import get_comment
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
   
    parser.add_argument("--check-all", action="store_true")
    args = parser.parse_args()
    
    only_staged = not args.check_all
    comment = get_comment(only_staged=only_staged)
    print(comment)

if __name__ == "__main__":
    main()