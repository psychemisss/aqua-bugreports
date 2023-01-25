import os


def load_env_variable(variable: str) -> str:
    """
    Load variable, from system environment
    :param variable: variable name
    """
    return os.environ[variable]


# Deprecated, used for .json files
# def load_config_variable(variable: str):
#     """Load config from config.json, file will be found in root directory"""
#     with open(from_root("config.json"), 'r') as configuration_file:
#         config = json.load(configuration_file)
#     return config[variable]
