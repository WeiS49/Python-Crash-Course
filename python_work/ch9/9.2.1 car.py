
class Car:
    """ A simple attempt to simulate cars. """
    def __init__(self, make, model, year):
        """ Initialize property of a car. """
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """ Return clean description information. """
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

my_new_car = Car('audi', 'a4', '2019')
print(my_new_car.get_descriptive_name())




