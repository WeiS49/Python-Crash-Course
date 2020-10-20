
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

    def full_gas_tank(self):
        """ Tell user that the gas tank is full. """
        print("The gas tank is full, let's go!")

class Battery:
    """ A simple attempt to simulate a clectric car's battery. """

    def __init__(self, battery_size=75):
        """ Initialize the property of battery. """
        self.battery_size = battery_size

    def describe_battery(self):
        """ Print a meesage tells the size of battery. """
        print(f"\nThis car has a {str(self.battery_size)}-kwh battery.")

    def set_battery(self, battery_size):  
        """ Reset the battery size. """
        self.battery_size = battery_size

    def get_range(self):
        """ Print a messasge indicating the battery life mileage """
        # range = 0

        if self.battery_size <= 75:
            range = 260
        elif self.battery_size >= 100:
            range = 315
        else:
            range = 280

        print(f"This car can go about {range} miles on a full charge.")

# 继承类
class ElectricCar(Car): # 括号内的内容即为继承的类
    """ The uniqueness of electrice cars. """

    def __init__(self, make, model, year):  # 子类形参必须和父类一样
        """ Initialize the properties of the parent class. """
        super().__init__(make, model, year) # 子类初始化 传入所有形参
        self.battery = Battery()

    def full_gas_tank(self):    # 重写父类的方法
        """ Tell users that electice car has no gas tank. """
        print("This car doesn't need a gas tank!")

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_description_name())
my_tesla.full_gas_tank()

my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

my_tesla.battery.set_battery(99)
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()



my_tesla.battery.battery_size = 107
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

















