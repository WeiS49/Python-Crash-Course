
age = input("How old are you? ") # 这里的结果是字符串类型
print(age, type(age))   # 字符串类型不可以用于数值比较

# 将输入类型转换成整型
# 如果输入的内容非数字, 则报错
age2 = int(input("How old are you? "))
print(age2, type(age2))



