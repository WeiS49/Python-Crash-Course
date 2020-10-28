
print("Please enter two numbers. ")
a = input("Please enter the first number. ")
b = input("Please enter the second number. ")

try:
    a = int(a)
    b = int(b)
except ValueError:
    print("Wrong input!")
else:
    print(a + b)




