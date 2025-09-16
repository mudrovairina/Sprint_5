import random


def name_generator():
    names = ["Irina", "Ira", "Irinka", "Irusik", "Rusya"]
    return random.choice(names)

def email_generator():
    return f"ira_mudrova_31_{random.randint(100, 999)}@yandex.ru"

def password_generator():
    return str(random.randint(100000, 999999))

def registration_user():
    return {
        "name": name_generator(),
        "email": email_generator(),
        "password": password_generator()
    }
