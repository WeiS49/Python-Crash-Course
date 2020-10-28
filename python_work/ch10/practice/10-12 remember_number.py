
import json

# def save_number():

#     number = input("Please enter your favorite number. ")
#     filename = 'favorite_number.json'
#     with open(filename, 'w') as f:
#         json.dump(number, f)

# def print_number():

#     filename = 'favorite_number.json'
#     with open(filename) as f:
#         number = json.load(f)
#     print(f"I know your favorite number! It's {number}.")


# save_number()
# print_number()


filename = 'favorite_number.json'
try:
    with open(filename) as f:
        number = json.load(f)
except FileNotFoundError:
    number = input("Please enter your favorite number. ")
    with open(filename, 'w') as f:
            json.dump(number, f)
    print(f"You entered {number}, I will remember it.")
else:
    print(f"I know your favorite number! It's {number}.")







