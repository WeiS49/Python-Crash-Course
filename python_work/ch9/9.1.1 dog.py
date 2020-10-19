
class Dog:
    """ A simple attempt to simulate a puppy. """

    def __init__(self, name, age):  # 类的初始化函数
        """ Initialize property name and age. """
        self.name = name
        self.age = age

    def sit(self):
        """ simlulate sit down when puppy receives the order. """
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """ simulate roll over when puppy receives the order."""
        print(f"{self.name} rolled over.")


my_dog = Dog('Willie', 6)   # 参数会被传入到__init__方法中
print(f"My dog's name is {my_dog.name}.")
print(f"My dog's is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()

your_dog = Dog('Lucy', 3)   # 输入信息可以相同 但变量名必须不同
print(f"Your dog's name is {your_dog.name}.")
print(f"Your dog's is {your_dog.age} years old.")
your_dog.sit()
your_dog.roll_over()


