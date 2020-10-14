
favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name in sorted(favorite_language.keys()): # 也可用于排序函数
    print(name)

print()

print("The following languages have been mentioned")
for language in favorite_language.values():
    print(f"\t{language.title()}")

print()

print(set(favorite_language.values()), type(set(favorite_language.values())), '\n')

print(set(favorite_language.items()), type(set(favorite_language.items())), '\n')

# 集合用{}(花括号)包围, 里面没有重复元素
# 集合内部的元素定义类似于列表, 但没有键值对
print("The following languages have been mentioned without repetition.")
for language in set(favorite_language.values()):
    print(f"\t{language.title()}")

print()

set1 = {'hello', 'hi'}
set1.add('test')    # 效果类似于列表中的append
print(set1)
set1.add('hello')   # 重复添加的元素会被自动忽略
print(set1)
