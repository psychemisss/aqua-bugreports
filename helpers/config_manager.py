import os
from from_root import from_root
import json


def load_env_variable(variable: str) -> str:
    """
    Load variable, from system environment
    :param variable: variable name
    """
    return os.environ[variable]


def load_config_variable(category: str, variable: str, config_filename: str = "config.json"):
    """
    Load variable from config file, it will be found in root directory
    :param category: category name
    :param variable: variable name (inside category)
    :param config_filename: config file name (optional)
    """
    with open(from_root(config_filename), 'r') as configuration_file:
        config = json.load(configuration_file)

    return config[category][variable]
