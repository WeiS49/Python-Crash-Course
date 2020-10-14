
favorite_places = {
    'john': ['Shanghai'],
    'mike': ['Beijing', 'Tianjin', 'Shenzhen'],
    'cassie': ['Canton', 'Changsha'],
}

for name, place in favorite_places.items():
    print(f"{name.title()}'s favorite place are: '")
    for location in place:
        print(f'\t{location}')








