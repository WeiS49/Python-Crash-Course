
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"original position: {alien_0['x_position']}")

alien_0['speed'] = 'fast'

if alien_0['speed'] == 'slow':
    x_increment = 1

elif alien_0['speed'] == 'medium':
    x_increment = 2

else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"new position {alien_0['x_position']}")  # 这种写法也可用于字符串赋值

# del alien_0 # del语句可直接删除字典或字典中元素

del alien_0['speed']

print('\n', alien_0)



