
alien_0 = {'color': 'green', 'speed': 'slow'}
# print(alien_0['points']) # 不存在的键值, 会报错

# get() 尝试获取(第一个参数)key对应的value
# 若没有key则返回第二个参数的值, 没设置就返回None
point_value = alien_0.get('points', 'No point value assigned')
print(point_value) # 返回get()的第二个参数


