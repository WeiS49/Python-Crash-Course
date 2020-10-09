
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'   # 根据下标修改数据
print(motorcycles)

motorcycles.append('honda') # 向列表末尾添加数据
print(motorcycles)

print()

motor = []
motor.insert(0, 'honda')
motor.insert(0, 'yamaha')
motor.insert(0, 'suzuki')
print(motor)

del(motor[0])    # 根据索引删除列表元素
print(motor)

item = motor.pop() # 默认弹出列表末尾的数据
print(f"The last motorcycle I owned was a {item}")
print(motor)

print()

motorcycle = 'yamaha'
print(motorcycles)
motorcycles.remove(motorcycle)  # 无法用于赋值
print(motorcycles)
print(f"\nA {motorcycle} is too expensive for me")
