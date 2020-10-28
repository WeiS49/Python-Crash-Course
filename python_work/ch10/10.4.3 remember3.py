
import json

def get_sorted_name():

    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)    
    except FileNotFoundError:
        return None
        
    return username

def get_new_name():
    
    username = input('Please enter your name. ')
    filename = 'username.json'
    
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():

    username = get_sorted_name()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_name()
        print(f"We will remember you next time, {username}!")

greet_user()




