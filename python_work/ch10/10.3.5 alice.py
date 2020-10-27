
# 以只读模式打开文件
# with open(filename, encoding='utf-8') as f:
    # contents = f.read()    
# 引发异常 FileNotFoundError
def count_words(filename):
    ''' Print number of words in file. '''
    try:    # 可能引发错误的语句
        with open(filename, encoding='utf-8') as f:
            file = f.read()

    except FileNotFoundError:
        print(f"Sorry, thed file {filename} does not exist.")

    else:
        words = file.split()
        print(len(words))

filenames = ['alice.txt', 'siddhartha.txt', 'little_women.txt', 'moby_dick.txt']

for filename in filenames:
    count_words(filename)
