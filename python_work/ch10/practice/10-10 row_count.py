
filename = 'sack_of_shakings.txt'

with open(filename, encoding='utf-8') as f:
    contents = f.read()

count_content = contents.lower()
count1 = count_content.count('the')
count2 = count_content.count('the ')
print(count1, count2)




