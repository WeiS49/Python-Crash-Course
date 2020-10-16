
# 8.3.1
# 返回简单值

def get_formatted_name(first_name, last_name):
    """ return a formatted name. """
    full_name = f"{first_name} {last_name}" # full_name是个字符串变量
    
    return full_name.title()

user_name = get_formatted_name('jimi', 'hendrix')
print(user_name)

