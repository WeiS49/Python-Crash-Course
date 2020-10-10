
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort() # 永久排序 无法恢复
print(cars)

print()

cars.sort(reverse=True) # 通过传参实现反向排序
print(cars)

print()

cars = ['bmw', 'audi', 'toyota', 'subaru']

print("original list")
print(cars)

print("sorted list")    # 临时排序
print(sorted(cars))

print()

print("original list")
print(cars)

print()

print("reversed sorted list")   # 临时排序 倒序
print(sorted(cars, reverse=True))

print()

print("len list")
print(len(cars))