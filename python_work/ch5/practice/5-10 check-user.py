
current_users = ['admin', 'Lie', 'Usx', 'lin', 'dav']
current_users_compare = []
for user in current_users:
    current_users_compare.append(user.lower())


new_users = ['lie', 'john', 'usx', 'des','mii']

for user in new_users:
    if user.lower() in current_users_compare:
        print(f"{user} has already occupied!")
    else:
        print(f"{user} is avaliable.")


