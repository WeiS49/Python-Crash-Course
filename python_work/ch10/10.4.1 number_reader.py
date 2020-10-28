
import json

filename = 'numbers.json'
# filename = 'alice.txt'
with open(filename, encoding='utf-8') as f:
    numbers = json.load(f)  # 该模块只能读取json格式的文件

print(numbers, type(numbers))
