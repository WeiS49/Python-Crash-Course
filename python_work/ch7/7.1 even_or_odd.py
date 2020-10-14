
# % —— 求模运算符
# 返回值二者相除的余数
# 用以判断是否能整除

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even") # 偶数

else:
    print(f"The number {number} is odd")    # 奇数


