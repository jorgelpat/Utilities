import platform
from os import system
import json

def clear_screen():
    if platform.system()=='Windows':
        system('cls')
    else:
        system('clear')

def load_data_from_file(json_filename):
    """
    Loads data from a JSON file.

    Parameters:
    - json_filename (str): The name of the JSON file to load from (excluding the ".json" extension).

    Returns:
    - data_list (list): The loaded data as a list. If an error occurs during loading, an empty list is returned.
    """
    data_list = []
    with open(f"data/{json_filename}.json") as f:
        try:
            data_list = json.load(f)
            return data_list
        except:
            return data_list

def save_data_to_file(json_filename, data_list=[]):
    """
    Saves data to a JSON file.

    Parameters:
    - json_filename (str): The name of the JSON file to save to (excluding the ".json" extension).
    - data_list (list): The data to be saved to the file. Defaults to an empty list if not provided.

    Returns:
    - None
    """
    with open(f"data/{json_filename}.json", "w", encoding="utf-8") as f:
        json.dump(data_list, f, ensure_ascii=False, indent=4)

def append_data_to_file(json_filename, data):
    """
    Appends data to a JSON file.

    Parameters:
    - json_filename (str): The name of the JSON file to append to (excluding the ".json" extension).
    - data: The data to be appended to the file.

    Returns:
    - None
    """
    data_list = load_data_from_file(json_filename)
    data_list.append(data)
    save_data_to_file(json_filename, data_list)

def print_json(input_dictionary, indent=0):
    """
    Prints a dictionary in a structured format.

    Parameters:
    - input_dictionary (dict): The dictionary to be printed.
    - indent (int): The indentation level. Defaults to 0.

    Returns:
    - None
    """
    for key, value in input_dictionary.items():
        if isinstance(value, dict):
            print(f"{'  ' * indent}\033[1;97m{str(key).replace('_', ' ').capitalize()}\033[00m:")
            print_json(value, indent + 1)
        elif isinstance(value, list):
            print(f"{'  ' * indent}\033[1;97m{str(key).replace('_', ' ').capitalize()}\033[00m:")
            for index, item in enumerate(value):
                if isinstance(item, dict):
                    print_json(item, indent + 1)
                else:
                    print(f"{'  ' * indent}\033[1;97m#{index+1}\033[00m: {item}")
        else:
            print(f"{'  ' * indent}\033[1;97m{str(key).replace('_', ' ').capitalize()}\033[00m: {value}")

def print_value_for_key(input_dictionary, target_key, current_key=None):
    """
    Prints the value associated with a specific key in a nested dictionary.

    Parameters:
    - input_dictionary (dict): The dictionary to search for the key.
    - target_key (str): The key to search for.
    - current_key (str): The current key being traversed. Defaults to None.

    Returns:
    - None
    """
    for key, value in input_dictionary.items():
        if isinstance(value, dict):
            current_key = key if current_key is None else current_key
            print_value_for_key(value, target_key, current_key)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict) or isinstance(item, list):
                    print_value_for_key(item, target_key, current_key)
        elif key == target_key:
            print(f"\033[1;97m{str(key).replace('_', ' ').capitalize()}\033[00m: {value}")


# Example dictionary
example_dict = {
    'key1': 1,
    'key2': {
        'nested_key1': 2,
        'nested_key2': [3, 4, {'nested_nested_key': 5}]
    },
    'key3': [6, 7, {'nested_key': 8}]
}

example_dict2 =     {
        "type": "C.C.",
        "id": "1099502408",
        "name": "Miguel",
        "lastname": "Castro",
        "age": "28",
        "address": "Carrera 48 # 69-54",
        "contact_numbers": [
            "3136054563"
        ],
        "classroom": {
            "name": "Artemis",
            "max_capacity": 4,
            "training_path": "NodeJS",
            "students": {
                "06:15-10:00": [
                    "1098792506",
                    "5555555555",
                    "987654321",
                    "123123123"
                ],
                "10:15-14:00": [
                    "987654321",
                    "220298327"
                ],
                "14:15-18:00": [],
                "18:15-22:00": []
            }
        },
        "training_path": "NodeJS"
    }

if __name__=="__main__":
    print_json(example_dict2)
# print_value_for_key(example_dict, "nested_nested_key")