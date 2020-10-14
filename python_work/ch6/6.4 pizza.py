
pizza = {   # 字典中嵌套列表
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']    
}

print(f"You ordered a {pizza['crust']} -crust pizza "
    "With the following toppings:")

for topping in pizza['toppings']:
    print('\t',topping)

