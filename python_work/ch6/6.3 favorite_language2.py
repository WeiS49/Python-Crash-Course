
favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

for name in favorite_language:  # 默认遍历字典的键值(key值)
    print(name.title())

print()

for name in favorite_language.keys(): # 只遍历字典的键值(key值)
    print(name.title())

print()

friends = ['phil', 'sarah']

for name in favorite_language.keys():
    print(f"Hello {name.title()}")

    if name in friends: # 在循环中加入逻辑判断
        language = favorite_language[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

print()





