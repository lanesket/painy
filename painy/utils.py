import os

def get_package_path() -> str:
    return os.path.dirname(os.path.realpath(__file__))

def get_valid_extensions() -> str:
    with open(os.path.join(get_package_path(), "p_extensions.txt")) as f:
        extensions = f.read().splitlines()
    
    return extensions