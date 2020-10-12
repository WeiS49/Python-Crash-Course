
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]  # 列表不能直接赋值(浅拷贝), 应该使用切片赋值(深拷贝)

my_foods.append('cannoli')

friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods, '\n')

print("My friend's favorite foods are:")
print(friend_foods)


