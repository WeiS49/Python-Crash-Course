
from user import User

class Privileges():
    """
    Show all privileges that admin have.
    """
    
    def __init__(self):
        """"""
        self.privileges = [
            "can add post",
            "can delete post",
            "can ban user",
        ]

    def show_privileges(self):
        print()
        """ Here are what an admin can do. """
        for privilege in self.privileges:
            print(privilege)

class Admin(User):

    def __init__(self):
        """ Initialize the property of class. """
        self.privileges = Privileges()

