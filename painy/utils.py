import os
import rich
import json
import re


def get_package_path() -> str:
    return os.path.dirname(os.path.realpath(__file__))

def load_valid_extensions() -> str:
    with open(os.path.join(get_package_path(), "settings/p_extensions.txt")) as f:
        extensions = f.read().splitlines()
    
    return extensions

def load_json(path: str) -> dict:
    with open(os.path.join(get_package_path(), path)) as f:
        config = json.load(f)
    
    return config

def load_txt(path: str) -> str:
    with open(os.path.join(get_package_path(), path)) as f:
        prompt = f.read()
    
    return prompt

def print_commit_message(console: rich.console.Console, msg: str) -> None:
    console.print(f"[bold]Commit message[/bold]:\n[green]{msg}[/green]")
    
def process_rules(rules: list, config: dict) -> str:
    pattern = r"(\<.+\>)"
    
    processed = []
    for rule in rules:
        var_matches = re.findall(pattern, rule)
        
        for match in var_matches:
            var = match.strip('<>')
            
            if var in config:
                rule = rule.replace(match, str(config[var]))
                processed.append(rule)
            else:
                raise NoSettingException(f"Setting {var} not found in config.json")
        
    return processed