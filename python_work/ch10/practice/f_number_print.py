
from favorite_number import save_number

import json


def print_number():

    filename = 'favorite_number.json'
    with open(filename) as f:
        number = json.load(f)
    print(f"I know your favorite number! It's {number}.")


save_number()
print_number()


