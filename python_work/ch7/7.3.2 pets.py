
# 7.3.2
# 删除为特定值的所有列表元素

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

# 下面两句结合起来可以实现循环移除列表中所有某一重复元素
while 'cat' in pets:    # 当列表中存在某一字符串
    pets.remove('cat')  # 单次移除 'cat’ 字符串

print(pets)

