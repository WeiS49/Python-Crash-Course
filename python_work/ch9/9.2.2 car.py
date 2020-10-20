
class Car:
    """ Initialize property of cars. """
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0   # 直接在初始化函数中创建变量

    def get_description_name(self):

        pass

    def read_odometer(self):
        """ Print a message tells information about odometers """
        print(f"This car has {self.odometer_reading} miles on it")

my_new_car = Car('audi', 'a4', '2019')
my_new_car.read_odometer()



