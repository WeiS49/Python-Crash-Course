
aliens = [] # 创建空列表用以存储新建的外星人

for alien_number in range(30):  # 批量创建外星人

    new_alien = {   # 外星人的参数
        'color': 'green', 
        'points': '5', 
        'speed': 'slow',
    }

    aliens.append(new_alien)    # 向列表中添加(每个外星人都是独立的, 支持修改)

print(aliens[:5])   # 打印前5个外星人

print(f"Total numbers of aliens : {len(aliens)}")   # 打印外星人总数

for alien in aliens[:3]:    # 对列表中前三个外星人进行修改
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

    elif alien['color'] == 'yellow':    # 其他情况
        alien['color'] = 'red'
        alien['points'] = '15'
        alien['speed'] = 'fast'

    print(alien)

print()

for alien in aliens[:5]:
    print(alien)


