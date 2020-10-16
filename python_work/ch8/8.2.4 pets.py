def describe_pet(pet_name, animal_type='dog'): # 包含默认数值的形参必须放在后面
    """ show animal information. """
    print(f"\n I have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet('harry')  
describe_pet(pet_name='harry')  

describe_pet('harry', 'hamster')  
describe_pet(pet_name='harry', animal_type='hamster')  
describe_pet(animal_type='hamster', pet_name='harry')  






