import os
import yaml
from pathlib import Path

CONFIG_FILE = Path.home() / ".comfydl_config"

def load_config():
    if not CONFIG_FILE.exists():
        return {}
    try:
        with open(CONFIG_FILE, 'r') as f:
            return yaml.safe_load(f) or {}
    except Exception as e:
        print(f"Warning: Could not load config file: {e}")
        return {}

def save_config(config):
    try:
        with open(CONFIG_FILE, 'w') as f:
            yaml.dump(config, f)
    except Exception as e:
        print(f"Error: Could not save config file: {e}")

def set_config_value(key, value):
    config = load_config()
    config[key] = value
    save_config(config)
    print(f"Configuration saved: {key} = {value}")

def get_config_value(key):
    config = load_config()
    return config.get(key)
