
class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):

        print(f"\nWelcome to {self.restaurant_name}.")
        print(f"Today we have {self.cuisine_type} for you.")

    def open_restaurant(self):

        print("\tThe restaurant is open now.")

restaurant = Restaurant("Happy", "no's chicken")
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant1 = Restaurant('unHappy', "fry chicken")
restaurant1.describe_restaurant()

restaurant2 = Restaurant('Dragon', "pizza")
restaurant2.describe_restaurant()

restaurant3 = Restaurant('Monster', "Lock")
restaurant3.describe_restaurant()








