
# 7.2.5
# 在循环中使用continue

current_number = 0
count = 0

while current_number < 10:
    
    # current_number += 1 # 循环的退出条件, 若没有则出现无限循环
    
    # print(count)
    # count += 1

    if current_number % 2 == 0:
        continue    # 忽略余下代码 回到条件判断 继续执行循环
    
    print(current_number)




