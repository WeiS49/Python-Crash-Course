
dog1 = {
    'name': 'doggy1',
    'age': '5',
}

dog2 = {
    'name': 'doggy2',
    'age': '6',
}

dog3 = {
    'name': 'doggy3',
    'age': '7',
}

dog4 = {
    'name': 'doggy4',
    'age': 8,
}

pets = [dog1, dog2, dog3] # 这种写法支持语法高亮

pets.append(dog4)    # 这种写法没有语法高亮

for pet in pets:

    pet_name = pet['name']
    pet_age = pet['age']

    print()
    print(f"Its name is {pet_name.title()}")
    print(f"Its age is {pet_age}")
    
    # for k, v in pet.items():  # 继续循环嵌套得到的值就是单独的字符串, 单个处理会很麻烦

        # pet_name = v['name']
        # pet_age = v['age']

        # print(v)

        # print(k)

        # print(f"Its name is {pet_name.title()}")
        # print(f"It is {pet_age} years old now.")







