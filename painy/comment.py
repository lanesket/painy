from painy.git import *
from painy.chat import Model
from painy import console
from painy.utils import print_commit_message, load_json, load_txt 
from painy.errors import NoSettingException
from painy.managers import ConfigManager, RulesManager


def get_rules(config: dict):
    rules_loaded = load_json("settings/rules.json")['rules']
    rules_processed = process_rules(rules_loaded, config)
    
    rules_str = '\n\nFollow this rules/restrictions when writing commit messages:\n'
    rules_str += '\n'.join([f'- {rule.strip()}' for rule in rules_processed])
            
    return rules_str
   
 
def get_prompt() -> str:
    prompt = load_txt('settings/prompt_comment_base.txt')
    config_manager = ConfigManager()
    rules_manager = RulesManager()
    rules = rules_manager.get_rules(config_manager.config_dict)
    
    rules_str = '\n\nFollow this rules/restrictions when writing commit messages:\n'
    rules_str += '\n'.join([f'- {rule.strip()}' for rule in rules])
    
    if config_manager.get_option('use_commit_history_style'):
        max_num_commits = config_manager.get_option('max_num_commits_style')
        max_num_commits = max_num_commits if max_num_commits is not None else 20
        commit_history = get_commit_messsage_history()[:max_num_commits]
        
        style_prompt = load_txt('settings/prompt_commit_style.txt')
        prompt += '\n\n' + style_prompt + '\n'
        prompt += '\n'.join([f'- {rule.strip()}' for rule in commit_history])
    
    return prompt


def get_commmit_message(diff_str: str, interactive: bool = False):
    with console.status(status="Generating commit message...", spinner='aesthetic'):
        comment_prompt = get_prompt()
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