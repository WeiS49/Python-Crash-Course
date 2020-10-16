
def city_country(city, country):
    """ Print city and its country. """
    city_country = f"{city}, {country}"
    return city_country.title()


country = city_country('santiago', 'chile')
country2 = city_country('beijing', 'china')
country3 = city_country('new york', 'america')

print(country)
print(country2)
print(country3)



