
from car import Car # 导入就可调用
# import car  # 和函数的调用逻辑相同
# from car import *

my_new_car = Car('audi', 'a4', 2018)
print(my_new_car.get_descriptive_name())

my_new_car.read_odometer()

my_new_car.update_odometer(30)
my_new_car.read_odometer()

my_new_car.update_odometer(20)
my_new_car.read_odometer()

my_new_car.increment_odometer(70)
my_new_car.read_odometer()



