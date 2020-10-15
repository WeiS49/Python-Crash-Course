
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "Entet 'quit' to end the program. "

message = ""    # 为循环的首次进行提供条件
while message.lower() != 'quit':
    message = input(prompt)

    if message.lower() != 'quit':
        print(message)





