
user_list = ['admin', 'lie', 'usx', 'lin', 'dav']
user_list = []

if user_list:
    for user in user_list:
        if user == 'admin':
            print(f"execution, My {user}")

        else:
            print(f"greetings, {user}")

else:
    print("We need to find some users!")

