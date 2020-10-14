
rivers = {
    'Yellow River': 'China',
    'Seine': 'France',
    'nile': 'egypt',
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}")

print()

for river in rivers.keys():
    print(f"Here is {river.upper()}.")

print()

for country in rivers.values():
    print(f"It originated in {country.title()}")

