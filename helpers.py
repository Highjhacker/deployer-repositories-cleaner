import configparser

def get_from_config(key):
    config = configparser.ConfigParser()
    config.read('config.conf')
    return config['DEFAULT'][key]