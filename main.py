from validators import *
from utilities import *
from controllers import *


def create_menu(menu_options):
    """
    Displays a menu based on the provided dictionary of options and executes the corresponding function when selected.

    Args:
        menu_options (dict): A dictionary where keys represent menu options and values represent the corresponding functions to execute.

    Returns:
        None
    """
    while True:
        print("Please select one of the options")
        option_index = 1
        equivalent_keys = {}
        valid_options = []
        for key in menu_options:
            print(f"{option_index}. {key}")
            valid_options.append(option_index)
            equivalent_keys[option_index] = key
            option_index += 1
        print("0. Exit")
        valid_options.append(0)
        opt = int(validate_user_input('', options=valid_options))
        clear_screen()
        if opt == 0:
            break
        menu_options[equivalent_keys[opt]]()

# Example functions
def camper_menu():
    options = {
        "Create camper": create_camper,
        "Update camper": update_camper,
    }
    create_menu(options)

def trainer_menu():
    print("This is the trainer menu.")

def coordination_menu():
    print("This is the coordination menu.")

def reports_menu():
    print("This is the reports menu.")

def set_user_preferences():
    print("This is the set user preferences menu.")

# Example usage
options = {
    "Camper menu": camper_menu,
    "Trainer menu": trainer_menu,
    "Coordination menu": coordination_menu,
    "Create reports": reports_menu,
    "Set the user preferences": set_user_preferences,
}

create_menu(options)

#Probando