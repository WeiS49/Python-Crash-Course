
filename1 = 'dogs.txt'
filename2 = 'catss.txt'

try:
    with open(filename1) as f1: 
        dogs = f1.read()
except FileNotFoundError:
    pass
else:
    print(dogs)

try:
    with open(filename2) as f2: 
        cats = f2.read()
except FileNotFoundError:
    pass
else:
    print(cats)




