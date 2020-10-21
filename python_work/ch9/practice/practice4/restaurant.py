
class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):

        print(f"\nWelcome to {self.restaurant_name}.")
        print(f"Today we have {self.cuisine_type} for you.")

    def open_restaurant(self):

        print("\tThe restaurant is open now.")








