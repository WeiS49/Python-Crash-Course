
def get_formatted_city(city: str, country: str, population: int=0):
    """ Return a formatted city and country. """
    if population:
        formatted_info = f'{city.title()} {country.title()} - {population}'
    else:
        formatted_info = f'{city.title()} {country.title()}'
    return formatted_info

