

class Car:
    """ Initialize property of cars. """
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0   # 直接在初始化函数中创建变量

    def get_description_name(self):
        """ Return a clean descriptive information. """
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name

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

    def read_odometer(self):
        """ Print a message tells information about odometers. """
        print(f"\nThis car has {self.odometer_reading} miles on it.")

my_new_car = Car('audi', 'a4', '2019')
my_new_car.odometer_reading = 24    # 1. 直接在实例处修改数值
my_new_car.read_odometer()

my_new_car.update_odometer(37)  # 使用类中的函数对数值进行重新赋值
my_new_car.read_odometer()

my_new_car.update_odometer(12)  

my_new_car.increment_odometer(17)
my_new_car.read_odometer()

print("——————————————————")

my_used_car = Car('subaru', 'outback', 2015)
print(my_new_car.get_description_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()





