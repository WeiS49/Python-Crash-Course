
favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'test': 1,
}

# key、value值也可用于逻辑语句中, 判断该元素是否存在
if 'erin' not in favorite_language.keys():
    print(f"Erin, Please take our poll!")

print(favorite_language.keys(), type(favorite_language.keys()))
print(favorite_language.values(), type(favorite_language.values()))
print(favorite_language.items(), type(favorite_language.items()))

print()

for k in favorite_language.keys():
    print(type(k), k)

print()

for v in favorite_language.values():
    print(type(v), v)

print()

for item in favorite_language.items():  # items 中单个键值对以元组形式存储
    print(type(item), item)

print()

for k, v in favorite_language.items():  # 具体到每个元素是根据其数据类型而定
    print(type(k), k, '\n',type(v), v)

print()

# for v in favorite_language.values():
#     print(type(k), k)   # 如果上面的遍历用到了这个变量, 那么它不会被自动释放, 而且还可以打印





