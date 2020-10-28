
import json

numbers = [2, 3, 5, 7, 11, 13]

# filename = 'numbers.json'
filename = 'alice.txt'
with open(filename, 'w') as f:
    json.dump(numbers, f)








