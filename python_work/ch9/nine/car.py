
""" A class that can be used to represent cars. """

class Car:
    """ A simple attempt to simulate car. """

    def __init__(self, make, model ,year):
        """ Initialize the properties describing the car. """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """ Return a neat descriptive name. """
        # 对于这种变量, 不需要写self
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """ Print a message indicating the mileage of the car. """
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to a specified value.
        Refuse to call back the mileage schedule.
        """

        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """ Increase the odometer a specified amount. """
        self.odometer_reading += miles


