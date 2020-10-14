
favorite_numbers = {
    'A': [5, 3, 9],
    'B': [7, 1],
    'C': [34, 12, 28, 45, 63],
    'D': [565, 345, 1346],
    'E': [5114, 3214, 93675],
}

for name, numbers in favorite_numbers.items():
    print(f"\n\nname is {name.title()}")
    print("favorite numbers are:")
    for number in numbers:
        # print(f"favorite numbers are\t{number}", end=' ')
        print(f"\t{number}", end=' ')

print()


