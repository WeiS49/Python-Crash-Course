
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

restaurant = Restaurant("Happy", "no's chicken")
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant.number_served = 27   # 这种设置方法能不能禁止或添加条件判断?
restaurant.print_number_served()

restaurant.set_number_served(79)
restaurant.print_number_served()

restaurant.increment_number_served(21)
restaurant.print_number_served()















