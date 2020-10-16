
def send_message(messages, sent_messages):
    """ move message from list messages to sent_messages."""
    while messages:
        message = messages.pop()
        sent_messages.append(message)

def show_message(messages):
    print("Here is the messages in the list")
    for message in messages:
        print(f"\t{message.title()}")

messages = ['hello', 'hi', 'greetings', 'welcome']
sent_messages = []
send_message(messages[:], sent_messages)    # 传入切片
show_message(messages)  # 结果原列表没有被修改, 但这样降低了效率
show_message(sent_messages)






