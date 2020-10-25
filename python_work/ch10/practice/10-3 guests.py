
filename = 'python_work/ch10/practice/guest.txt'
username = input("Please enter your name. ")

with open(filename, 'w') as file:
    file.write(username)
    print("Writing Complete.")




