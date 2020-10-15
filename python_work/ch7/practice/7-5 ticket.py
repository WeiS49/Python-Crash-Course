
ask_age = "\nPlease tell me how old are you? "

# 方法一: 条件测试控制循环

# age = 1 # 使用方法一, 应该给条件赋初始值

# while age > 0:
#     age = int(input(ask_age))
#     price = 0   # 这里应该赋初始值, 否则后面price的数值无法保存

#     if age < 3:
#         price = 0

#     elif age <= 12:
#         price = 10

#     elif age > 12:
#         price = 15
    
#     print(f"You are {age} years old,"
#     f" I will charge you ${price}")

# 方法二: 标志位控制循环
# 这种方法不需要对age设初值

# active = True   # 标志位设为'真'
# while active: # 无限循环

#     user_age = int(input(ask_age))
#     age = int(user_age) # 可以加一个try 如果出现非法输入 直接结束程序
#     price = 0

#     if age < 0:
#         active = False
#         continue    # 这里可以直接用continue跳过剩下的语句

#     elif age < 3:
#         price = 0

#     elif age < 12:
#         price = 10

#     else:
#         price = 15

#     print(f"You are {age} years old,"
#     f" I will charge you ${price}")


# 方法三: break语句控制循环

while True:

    user_age = input(ask_age)
    age = int(user_age)

    if age < 0:
        break
    
    elif age < 3:
        price = 0

    elif age < 12:
        price = 10

    else:
        price = 15

    print(f"You are {age} years old,"
    f" I will charge you ${price}")




