
class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        """ Initialize property of class Restaurant. """
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """ Description of the restaurant. """
        print(f"\nWelcome to {self.restaurant_name}.")
        print(f"Today we have {self.cuisine_type} for you.")

    def open_restaurant(self):
        """ Print a meesage tells the restaurant is open. """
        print("\tThe restaurant is open now.")

    def set_number_served(self, number):
        """ reset the number of served people. """
        self.number_served = number

    def increment_number_served(self, increment):
        """ increse the number of served people. """
        self.number_served += increment

    def print_number_served(self):
        """ Print the number of served people. """
        print(f"\nThere are {str(self.number_served)} people come today.")

class IceCreamStand(Restaurant):
    """ Inheritory class Restaurant. """
    def __init__(self, a, b):
        super().__init__(a, b)  # 初始化后可以调用父类的其他函数(用到这些参数)
        self.flavors = ['a', 'b', 'c']

    def show_flavors(self):
        " Print all the flavors the icecreamstand offers."
        for flavor in self.flavors:
            print(flavor)
        
ice_cream_shop = IceCreamStand('shop', 'tomas')
ice_cream_shop.show_flavors()
ice_cream_shop.describe_restaurant()
ice_cream_shop.open_restaurant()






