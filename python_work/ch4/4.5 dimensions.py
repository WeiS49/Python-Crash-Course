
tuplex = tuple(range(10))   # 元组的批量赋值方法类似于列表
# print(type(tuplex), tuplex)

dimensions = (200, 50)
print(dimensions[0])    # 打印元组数据  
print(dimensions[1])    # 写法和列表相同

# dimensions[0] = 200 # 元组中的元素值无法直接修改
dimensions = (100, 400, 700) # 但可以整个重新复制
print(dimensions)
