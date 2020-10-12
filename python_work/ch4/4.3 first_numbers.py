
for value in range(1, 5):
    print(value)

numbers = list(range(6))    # 如果只有一个数字x, 则从0开始到x结束
print(numbers)

squares = []
for value in range(1, 11):
    # square = value ** 2
    # squares.append(square)

    squares.append(value ** 2)  # 和上面两句等价

print(squares)

digits = list(range(10))
print(min(digits))
print(max(digits))
print(sum(digits))






