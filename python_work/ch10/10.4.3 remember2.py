
import json

def get_sorted_name():

    filename = 'username.json'
    try:
        with open(filename, encoding='utf-8') as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username




def greet_user():
    """If the file saves your username, load and print it."""

    username = get_sorted_name()

    if username:
        print(f"Welcome back, {username}!")
    else:
        username = input("What is your name? ")
        filename = 'username.json'
        with open(filename, 'w') as f:
            json.dump(username, f)
            print(f"We will remember you next time. {username}!")

greet_user()
