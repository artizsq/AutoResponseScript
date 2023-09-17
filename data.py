import json

def read_data(file):
    try:
        with open(file, 'r', encoding='utf-8') as file:
            users_data = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        users_data = {}
    return users_data

def write_data(db, file):
    with open(file, 'w', encoding='utf-8') as file:
        json.dump(db, file, indent=4, ensure_ascii=False)

def check_user(user_id):
    db = read_data("users.json")
    if str(user_id) not in db:
        db = str(user_id)
        write_data(db, "users.json")
        return True
    else:
        return