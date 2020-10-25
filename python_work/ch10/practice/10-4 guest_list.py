
filename = 'python_work/ch10/practice/guest_book.txt'
usernames = []
guest_name = ''
over = False

while not over:
    guest_name = input("Please enter your name. ")
    if guest_name.lower() == 'quit':
        over = True
    else:
        usernames.append(guest_name)

with open(filename, 'w') as file:
    for username in usernames:
        file.write(f"Welcome!,  {username}\n")





