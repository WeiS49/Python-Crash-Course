
def build_profile(first, last, **user_info):    # 代表能接受任意数量的键值对用字典形式存储
    """ Create a dictionary, contains everything about user's profile. """
    user_info['first_name'] = first
    user_info['last_name'] = last

    print(user_info, type(user_info))
    return user_info

user_profile = build_profile('albert', 'einstein',
                            location='princetion',
                            field='physics')

print(user_profile)

def test(size, *test1, **test2):  # * -> 元组, ** -> 字典
                            # 这两种数据类型都不必有传入值
    print(test1, type(test1))
    print(test2, type(test2))
    print(size, type(size))

test(36, '12', '24', location='123', classa='high')  # 根据传入内容的特征不同, 所对应的形参也不同

