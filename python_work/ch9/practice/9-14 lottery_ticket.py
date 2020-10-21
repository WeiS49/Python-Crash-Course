
from random import choice

lottery_number = []

for i in range(15):
    lottery_number.append(i)

for i in 'abcdefg':
    lottery_number.append(i)

print(lottery_number)

print('--------------')

def get_winning_prize(lottery_number):
    prize = []
    while len(prize) < 4:
        lucky_number = choice(lottery_number)

        if lucky_number not in prize:
            prize.append(lucky_number)
        else:
            continue

    return prize

def get_my_ticket(lottery_number):
    my_ticket = []
    while len(my_ticket) < 4:

        lucky_number = choice(lottery_number)

        if lucky_number not in my_ticket:
            my_ticket.append(lucky_number)
        else:
            continue
    
    return my_ticket

def check_ticket(my_ticket, prize):
    for element in my_ticket:
        if element not in prize:
            return False
    return True

winning_ticket = get_winning_prize(lottery_number)
print(winning_ticket)
winning = False

count = 0

while not winning:
    count += 1
    my_ticket = get_my_ticket(lottery_number)
    print(my_ticket)
    winning = check_ticket(my_ticket, winning_ticket)
    
    if winning:
        print("winner!")

print()

print(count)

