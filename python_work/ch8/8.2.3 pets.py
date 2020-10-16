
def describe_pet(pet_name, animal_type='dog'):
    """ show animal information. """
    print(f"\n I have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}'")

# # 在不指定的情况下 传入的实参依然是位置实参
describe_pet('harry')   # 另一个参数已经有默认值, 所以不必输入也能执行函数




