
filename1 = 'dogs.txt'
filename2 = 'cats.txt'

try:
    with open(filename1) as f1: 
        dogs = f1.read()
except FileNotFoundError:
    print(f"Can't find file {filename1}!")
else:
    print(dogs)

try:
    with open(filename2) as f2: 
        cats = f2.read()
except FileNotFoundError:
    print(f"Can't find file {filename2}!")
else:
    print(cats)
