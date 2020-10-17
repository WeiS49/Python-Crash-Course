
def make_sandwich(*toppings):
    """ Receive the ingredients and print them. """
    print('\nHere is your toppings.')
    for topping in toppings:
        print(F" - {topping}")

make_sandwich('cheese')
make_sandwich('cheese', 'chicken', 'apple')
make_sandwich('pineapple', 'mushroom', 'apple', 'pear')


