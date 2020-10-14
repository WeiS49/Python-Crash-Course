
from os import times


users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton'
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris'
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    location = user_info.get('location', 'nothing here') # 这种的写法可以解决key值不存在的情况
    
    print(f"{full_name.title()}")
    print(f"Location: {location.title()}")





