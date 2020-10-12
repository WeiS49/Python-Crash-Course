
lots_of_pizza = ['pizza1', 'pizza2', 'pizza3']

friend_pizza = lots_of_pizza[:]

lots_of_pizza.append('chicken')

friend_pizza.append('cheese')

print("My pizza are:")
for pizza in lots_of_pizza:
    print('\t', f"I like {pizza}")

print("friend pizza are:")
for pizza in friend_pizza:
    print('\t', f"My friend like {pizza}")

print()

print("We really love pizza!")








