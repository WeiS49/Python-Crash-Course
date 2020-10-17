
def car_info(manufacturer, model, **car_info):
    """ create a dictionary which contains car's information. """
    
    car_info['Manufacturer'] = manufacturer
    car_info['Model'] = model

    return car_info

subaru = car_info('subaru', 'outback', color = 'blue', tow_packge = True )
print(subaru)



