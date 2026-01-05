import configparser
#import json
import os
from pymongo import MongoClient

CONFIG_FILE = "config.ini"

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["devops_config_db"]
collection = db["configurations"]


def read_config():
    if not os.path.exists(CONFIG_FILE):
        raise FileNotFoundError("Configuration file not found")

    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)

    config_data = {}
    for section in config.sections():
        config_data[section] = dict(config.items(section))

    return config_data


def save_to_mongodb(data):
    collection.insert_one(data)


if __name__ == "__main__":
    try:
        parsed_data = read_config()
        save_to_mongodb(parsed_data)

        print("\nConfiguration File Parser Results:\n")
        for section, values in parsed_data.items():
            print(f"{section}:")
            for key, value in values.items():
                print(f"- {key}: {value}")
            print()

    except FileNotFoundError as e:
        print(f"ERROR: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
