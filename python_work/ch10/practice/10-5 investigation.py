
filename = 'python_work/ch10/practice/programming.txt'
reasons = []
reason = ''

while reason != 'quit':
    reason = input("Why do you like programming? ")
    if reason == 'quit':
        break
    reasons.append(reason)


with open(filename, 'w') as file:
    file.write("Here are reasons why people love programming: \n")
    for reason in reasons:
        file.write(f"\t{reason}\n")

