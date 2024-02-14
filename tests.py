from utilities import *

camper2 =     {
        "type": "T.I.",
        "id": "1234567890",
        "name": "Ana Maria",
        "lastname": "Rodriguez",
        "age": 27,
        "address": "Carrera 70 #45-67",
        "contact_numbers": [
            "3112345678"
        ],
        "legal_rep": {},
        "status": 0,
        "trainer": None,
        "classroom": None,
        "training_path": None,
        "grades": [
            {
                "theory": 50,
                "practice": 40,
                "avg": 45.0
            }
        ],
        "warnings": 0,
        "schedule": None,
        "start_date": None,
        "end_date": None
    }


append_data_to_file("test", camper2)
camper_list = load_data_from_file("test")
print(camper_list)