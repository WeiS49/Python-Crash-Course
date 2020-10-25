
filename = 'python_work/ch10/pi_million_digits.txt'

with open(filename) as f:
    # contents = f.read()
    lines = f.readlines()

contents = ''

for line in lines:
    contents += line.strip()

print(contents[:120])

print(type(contents))

birthday = input('Please enter your birthday. ')

if birthday in contents:
    print("found it!")
else:
    print("nope.")

print(len(contents))