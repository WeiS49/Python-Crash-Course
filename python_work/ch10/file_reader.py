
with open('python_work/ch10/pi_digits.txt') as file_object:
    contents = file_object.read()
# print(contents)

filename = 'python_work/ch10/pi_digits.txt'

with open(filename) as file_object: # 使用完成后, 自动关闭文件
    lines = file_object.readlines() # readline & readlines 单行(字符串)和多行(列表)

print(type(lines))

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))   # 空行也算长度





