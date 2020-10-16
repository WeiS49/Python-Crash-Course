
# 8.3.4
# 结合使用函数和while循环

def get_formatted_name(first_name, last_name):
    """ Return a clean name. """
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("Enter 'q' at any time to quit")
    f_name = input("Enter first name: ")
    if f_name == 'quit':
        break
    
    l_name = input("Enter last name: ")
    if l_name == 'quit':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(formatted_name)

