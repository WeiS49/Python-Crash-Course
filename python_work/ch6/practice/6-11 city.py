
cities = {
    'Shanghai': {
        'country': 'China',
        'population': '2000w',
        'fact': 'economic center in China',
    },

    'Beijing': {
        'country': 'China',
        'population': '3000w',
        'fact': 'capital in China',
    },

    'Shenzhen': {
        'country': 'China',
        'population': '1500w',
        'fact': 'city of 996',
    },
}

for name, detail in cities.items():
    print(f"This city is {name.title()}")
    country = detail['country']
    population = detail['population']
    fact = detail['fact']

    print(f"\tIt belong to {country}")
    print(f"\tIt has {population} people live here")
    print(f"\tWhat interesting most is, it is the {fact}")

    print()




