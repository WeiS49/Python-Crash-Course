

def build_profile(first, last, **user_info):    # 代表能接受任意数量的键值对用字典形式存储
    """ Create a dictionary, contains everything about user's profile. """
    user_info['first_name'] = first
    user_info['last_name'] = last

    print(user_info, type(user_info))
    return user_info

user_profile = build_profile('W', 'S',
                            location='WH',
                            field='CS',     
                            like='read')    # 字典优先创建后面这些内容

print(user_profile)









