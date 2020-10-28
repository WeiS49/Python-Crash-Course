
def test():
    print('hello')



while True:

    print("\nPlease enter two numbers. ")
    a = input("\nPlease enter the first number. ")

    if a == 'q':
        break

    b = input("Please enter the second number. ")

    if b == 'q':
        break

    try:
        a = int(a)
        b = int(b)
    except ValueError:
        print("Wrong input!")
    else:
        print(f"\tThe answer is : {a + b}")







