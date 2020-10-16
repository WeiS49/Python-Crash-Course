
# 8.3.2
# 可选实参

def get_formatted_name(first_name, last_name, middle_name = None):
    """ return a formatted name(with middle name). """
    
    # 根据不同情况进行不同操作
    if middle_name: # python将非空字符串解读为True
        full_name = f"{first_name} {middle_name} {last_name}"
    
    else:
        full_name = f"{first_name} {last_name}"

    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician2 = get_formatted_name('john', 'hooker', 'lee')
print(musician2)

