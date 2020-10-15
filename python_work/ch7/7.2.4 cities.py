
from os import times


prompt = "\nPlease enter the name of a city you have visited':"
prompt += "\n(Enter 'quit' when you are finished.) "

while True: # 无限循环
    city = input(prompt)

    if city.lower() == 'quit':
        break   # 直接break跳出循环 有时候标志位也许有用

    else:
        print(f"I'd love to go {city.title()}!")

# break 语句可以退出任何循环, 包括for循环
