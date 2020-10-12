
players = ['charles', 'martina', 'micheal', 'florence', 'eli']

print(players[0:3]) # 打印列表的前三个元素
print(players[1:4]) # 打印列表的第二三四号元素
print(players[:4])  # 打印从第0号元素到第3号元素
print(players[2:])  # 打印从2号元素到末尾元素
print(players[-3:]) # 打印列表的最后三个元素

print(players[0::2], '\n') # 类似于range()，切片内也可输入三个数据

print("Here are the first three players:")
for player in players[:3]:  # 只遍历前三名队员
    print('\t', player.title())
