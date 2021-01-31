import configparser
import os


class Config:
    base, file = os.path.split(os.path.abspath(__file__))

    cfg_path = os.path.join(base, 'config.cfg')

    @classmethod
    def get(cls, section, key):
        config = configparser.ConfigParser()
        config.read(cls.cfg_path)
        return config[section][key]
