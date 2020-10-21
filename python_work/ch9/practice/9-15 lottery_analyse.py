

from random import choice

lottery_number = []

for i in range(10):
    lottery_number.append(i)

for i in 'abcde':
    lottery_number.append(i)

tuple(lottery_number)

prize = []
while len(prize) != 4:
    lucky_number = choice(lottery_number)
    
    if lucky_number not in prize:
        prize.append(lucky_number)
    else:
        continue

print(prize)

















