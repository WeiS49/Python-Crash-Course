
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]  # 列表不能直接赋值(浅拷贝), 应该使用切片赋值(深拷贝)

my_foods.append('cannoli')

friend_foods.append('ice cream')

for mf in my_foods:
    print(mf)

print()

for ff in friend_foods:
    print(ff)


