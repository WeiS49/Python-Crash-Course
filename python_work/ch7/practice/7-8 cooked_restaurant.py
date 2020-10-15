
sandwich_orders = ['cheese', 'chicken', 'beef', 'cucumber']
finished_sandwiches = []

# for sandwich_order in range(len(sandwich_orders)):

#     sandwich = sandwich_orders.pop()
#     print(f"I made your {sandwich.title()}")
#     finished_sandwiches.append(sandwich)

# print()

# print(sandwich_orders)
# print(finished_sandwiches)

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich.title()}")
    finished_sandwiches.append(sandwich)

print()

print(sandwich_orders)
print(finished_sandwiches)










