
def describe_pet(animal_type, pet_name):
    """ Show pet infomation. """
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet('hamster', 'harry')    # 按顺序输入参数(位置实参)
describe_pet('dog', 'willie')

describe_pet('harry', 'hamster')    # 错误的传入顺序, 导致逻辑错误
