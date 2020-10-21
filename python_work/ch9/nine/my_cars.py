
from car import Car

# import electric_car # 全部导入时会将其关联类一并导入
from electric_car import ElectricCar as ecar # 导入单个类不会同时导入父类


my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = ecar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())


