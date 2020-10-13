
someone = {
    'first_name': 'John',
    'last_name': 'Smith',
    'age': '24',
    'city': 'New York',
}

for i in someone.items():   # items内部元素的存储方式是元组
    print(i, type(i))

print(someone.items(), type(someone.items())) 

