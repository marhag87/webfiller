"""Module for handling config"""
from pyyamlconfig import load_config


class ConfigError(Exception):
    """Config related error"""


class Config(object):  # pylint: disable=too-few-public-methods
    """Class for handling config"""
    def __init__(self, url):
        self.__config = load_config('config.yaml')
        try:
            conf = self.__config.get(url)
            self.username = conf.get('username')
            self.password = conf.get('password')
        except (KeyError, AttributeError):
            raise ConfigError('Could not get config for the url')
