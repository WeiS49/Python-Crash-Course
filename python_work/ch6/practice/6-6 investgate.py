
favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

name_list = {'sarah', 'robort', 'john', 'edward'}

for name, language in favorite_language.items():
    print(f"\n{name}, Thank you for coming!")

    if name in name_list:
        print(f"{name.title()}, You are special!")
        
    





