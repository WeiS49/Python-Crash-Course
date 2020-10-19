
class User:
    """ simulate person. """

    def __init__(self, first_name, last_name):
        """ Initialize property first_name and last_name. """
        self.first_name = first_name
        self.last_name = last_name
        # 声明的变量不用self的, 只能作用于这个函数
        # full_name = self.first_name + self.last_name


    def describe_user(self):
        """ Print user info. """
        # 像这样的变量只有先调用这个函数才能生成, 其他函数与才可用
        self.full_name = f"{self.first_name} {self.last_name}"
        print(f"\nYour name is {self.full_name.title()}.")
        
        # 用引号括起来表示它是字符串, 在下面的调用中才有语法高亮        

    def greet_user(self):
        """ Send personalize message to user. """
        print(f"\tHello, {self.full_name.title()}!")


user1 = User("w", "s")
user1.describe_user()   # 用这条语句生成full_name变量, 下面的函数才可用
user1.greet_user()

user2 = User("ab", "cd")
user2.describe_user()   # 用这条语句生成full_name变量, 下面的函数才可用
user2.greet_user()

user3 = User("ef", "gh")
user3.describe_user()   # 用这条语句生成full_name变量, 下面的函数才可用
user3.greet_user()

user4 = User("jk", "lm")
user4.describe_user()   # 用这条语句生成full_name变量, 下面的函数才可用
user4.greet_user()



