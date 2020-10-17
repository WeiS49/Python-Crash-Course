
def make_pizza(*toppings):  # 接受任意数量的参数, 以元组形式存储
    """ Print all materials the customer ordered. """
    # print(toppings, type(toppings))
    print("\nHere is your orders.")
    for topping in toppings:
        print(f" - {topping}")

make_pizza('pepperoni')
make_pizza('pepperoni', 'mushrooms', 'green peppers', 'cheese')







