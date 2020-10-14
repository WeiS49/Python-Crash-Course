
people = []

john = {
    'first_name': 'John',
    'last_name': 'Smith',
    'age': '24',
    'city': 'New York',
}

william = {
    'first_name': 'William',
    'last_name': 'Gabe',
    'age': '14',
    'city': 'Canda',
}

cassie = {
    'first_name': 'Cassie',
    'last_name': 'Chen',
    'age': '32',
    'city': 'China',
}

# people = [john, william, cassie]

people.append(john)   # 像这样后添加进来的数据, 可能不会有特定的语法高亮
people.append(william)
people.append(cassie)

print(f"Here are the person I invested:\n")

for someone in people:
    
    for describe, characteristic in someone.items():    # 这里没有语法高亮, 但依然生效
        print(f"his/her {describe.title()} is {characteristic.title()}")

    # for k in someone.keys():
        # print(f{k.title()})
        # print(f"{k.title()}")

    print()


# dictx = {
#     'asdf': '2',
#     'dfg': '4',
#     'gfj': '6',
# }

# for k in dictx.keys():
#     print(k.)



