
import json

filename = 'username.json'

try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("Please enter your name. ")
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"We will remember you next time, {username}!")
else:
    print(f"Welcome back, {username}!")


