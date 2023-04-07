from painy.utils import load_json, save_json
import re


class ConfigManager:
    def __init__(self, config_path='settings/config.json'):
        self.config_path = config_path
        self.config_dict = load_json(self.config_path)
        
    def set_option(self, option: str, value) -> None:
        self.config_dict[option] = value
        self.save_config()
        
    def get_option(self, option: str):
        if option not in self.config_dict:
            return None
        value = self.config_dict[option]
        return ConfigManager.process(value)
        
    def save_config(self) -> None:
        save_json(self.config_path, self.config_dict)
    
    @staticmethod
    def process(value):
        if type(value) == str:
            if value.lower() == 'true':
                return True
            elif value.lower() == 'false':
                return False
            elif value.isdigit():
                return int(value)

        return value
       
        
class RulesManager:
    def __init__(self, rules_path='settings/rules.json'):
        self.rules_path = rules_path
        self.rules_dict = load_json(self.rules_path)
        
    def add_rule(self, rule: str) -> None:
        self.rules_dict['rules'] = self.rules_dict['rules'] + [rule]
        self.save_rules()
        
    def remove_rule(self, i) -> None:
        self.rules_dict['rules'].pop(i)
        self.save_rules()
        
    def get_rules(self, config: dict = None) :
        rules_loaded = self.rules_dict['rules']
        if config is None:
            return rules_loaded
        return RulesManager.process_rules(rules_loaded, config)
    
    def get_length(self) -> int:
        return len(self.rules_dict['rules'])
    
    def remove_all_rules(self) -> None:
        self.rules_dict['rules'] = []
        self.save_rules()
    
    def save_rules(self) -> None:
        save_json(self.rules_path, self.rules_dict)
        
    @staticmethod
    def process_rules(rules: list, config: dict) -> str:
        pattern = r"(\<.+\>)"
        
        processed = []
        for rule in rules:
            var_matches = re.findall(pattern, rule)
            if not var_matches:
                processed.append(rule)
            for match in var_matches:
                var = match.strip('<>')
                
                if var in config:
                    rule = rule.replace(match, str(config[var]))
                    processed.append(rule)
                else:
                    raise NoSettingException(f"Setting {var} not found in config.json")
            
        return processed