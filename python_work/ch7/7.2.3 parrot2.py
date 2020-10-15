
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "Entet 'quit' to end the program. "

active = True # 添加标志位, 用以判断条件是否满足

while active:

    message = input(prompt)
    
    if message.lower() != "quit":
        print(message)
    
    else:
        # 这种方法可以将任何条件不符的情况设为False
        active = False  # 将标志位设为False, 终止循环






