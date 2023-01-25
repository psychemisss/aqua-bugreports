import json
from from_root import from_root


def load_config():
    """Load config from config.json, file will be found in root directory"""
    with open(from_root("config.json"), 'r') as configuration_file:
        config = json.load(configuration_file)
    return config


def load_config_variable(variable: str):
    """Load config from config.json, file will be found in root directory"""
    config = load_config()
    return config[variable]
