
def greet_users(names):
    """ Send greetings to every user in the list. """
    for name in names:
        msg = f"Hello, {name.title()}"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

