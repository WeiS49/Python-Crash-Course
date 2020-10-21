
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
        """ Here are what an admin can do. """
        for privilege in self.privileges:
            print(privilege)


class User:
    """ simulate person. """

    def __init__(self, first_name, last_name):
        """ Initialize property first_name and last_name. """
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
        # 声明的变量不用self的, 只能作用于这个函数
        # full_name = self.first_name + self.last_name

    def describe_user(self):
        """ Print user info. """
        # 像这样的变量只有先调用这个函数才能生成, 其他函数与才可用
        self.full_name = f"{self.first_name} {self.last_name}"
        print(f"\nYour name is {self.full_name.title()}.")

    def greet_user(self):
        """ Send personalize message to user. """
        print(f"\tHello, {self.full_name.title()}!")

    def read_login_attempts(self):
        """ Print the number of login attempts. """
        print(f"\nYou have failed login for {str(self.login_attempts)} times")

    def increment_login_attempts(self):
        """ Increse the number of login attempts. """
        self.login_attempts += 1

    def reset_login_attempts(self):
        """ Reset the number of login attempts to 0. """
        self.login_attempts = 0

class Admin(User):

    def __init__(self):

        self.privileges = Privileges()

    def show_privileges(self):
        """ Here are what an admin can do. """
        for privilege in self.privileges:
            print(privilege)

admin = Admin()
admin.privileges.show_privileges()


