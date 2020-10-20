
class Car:
    """ Initialize property of cars. """
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0   # 直接在初始化函数中创建变量

    def get_description_name(self):
        """ Return a clean descriptive information. """
        long_name = f"{self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """ Print a message tells information about odometers. """
        print(f"\nThis car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """ 
        Set the odometer to a new value. 
        roll back the mileage meter is forbidden.
        """
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("\nYou can't roll back an odometer!")

    def increment_odometer(self, miles):
        """ Increase the mileage meter a specified amount. """
        self.odometer_reading += miles

# 继承类
class ElectricCar(Car): # 括号内的内容即为继承的类
    """ The uniqueness of electrice cars. """

    def __init__(self, make, model, year):  # 子类形参必须和父类一样
        """ Initialize the properties of the parent class. """
        super().__init__(make, model, year) # 子类初始化 传入所有形参
        self.battrry_size = 75  #子类定义属性和方法

    def describe_battery(self): # 向子类添加新的方法
        """ Print a message describing the battery capacity. """
        print(f"This car has a {self.battrry_size}-kwh battery.")

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_description_name())
my_tesla.describe_battery()



