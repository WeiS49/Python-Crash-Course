
def build_person(first_name, last_name):
    """ Return a dictionary, it contains information about a person. """
    # 向形参内容作为value值存入字典中
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

def build_person2(first_name, last_name, age=None):  # age值可有可无, 默认为空
    """ Return a dictionary, it contains information about a person. """    
    person = {
        'first_name': first_name.title(), 
        'last_name': last_name.title(),
    }

    if age: # None在条件判断中相当于False 
        person['age'] = age

    return person

person = build_person2('w', 's', 24)
print(person)


