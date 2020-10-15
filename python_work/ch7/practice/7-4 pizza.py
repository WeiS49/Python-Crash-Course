
prompt = "\nPlease enter the materials you like, "
prompt += "We will print that on the screen."
prompt += "\nEnter 'quit' to end the program. "


# 方法一: 条件测试控制循环

message = ''

while message.lower() != 'quit':
    message = material = input(prompt)

    if material.lower() != 'quit':
        print(f"We will add {material.title()} to your pizza")


# 方法二: 标志位控制循环

active = True
while active:
    
    message = input(prompt)
    if message.lower() == 'quit':
        active = False

    else:
        print(message)


# 方法三: break语句控制循环

while True:

    message = input(prompt)

    if message.lower() != 'quit':
        print("brfore continue")
        continue

    else:
        break



