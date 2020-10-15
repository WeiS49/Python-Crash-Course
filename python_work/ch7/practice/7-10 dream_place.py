
user_name = 'please tell me your name: '
dream_place = "If you could visit one place in the world, Where would you go? "
responses = {}


while True:

    name = input(user_name) # 这两个名字不应该一样
    place = input(dream_place)
    responses[name] = place

    repeat = input("Would you like to respond again? (yes/ no) ")
    if repeat.lower() == 'no':
        break

print(" --- Here is your response --- ")
for name, place in responses.items():
    print(name, place)






