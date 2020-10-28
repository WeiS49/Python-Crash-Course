
import json

def save_number():

    number = input("Please enter your favorite number. ")
    filename = 'favorite_number.json'
    with open(filename, 'w') as f:
        json.dump(number, f)



# print(f"I know your favorite number! It's {number}")



