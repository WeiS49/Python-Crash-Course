
def describe_pet(animal_type, pet_name):
    """ Show pet infomation. """
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet(pet_name='harry', animal_type='hamster') # 根据形参名输入对应实参
describe_pet(animal_type='dog', pet_name='willie')  # 注意形参名输入应该正确无误






