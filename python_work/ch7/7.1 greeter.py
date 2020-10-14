
# 声明一个字符串变量prompt, 用以保存输入的提示文本
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)    # input()的输入默认为字符串
print(f"\nHello, {name.title()}!")




