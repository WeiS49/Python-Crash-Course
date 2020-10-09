
name_list = ['J', 'S', 'M']

print(f"{name_list[0]}, I invite you to have a dinner")
print(f"{name_list[1]}, welcome home")
print(f"{name_list[2]}, greetings")

print(f"oops, loos like Mr.{name_list[2]} can't come here today")
name_list[2] = 'T'
print(f"Welcome here! {name_list[2]}")

print("Now I found a bigger table!")

name_list.append('K')
print(f"Here is Mrs.{name_list[3]}!")

name_list.insert(0, 'Z')
print(f"I just insert {name_list[0]} to my list")

name_list.insert(2, 'A')
print(f"insert {name_list[2]} in the middle")

print("Sorry, but I can only invite 2 person to have dinner")

temp_name = name_list.pop()
print(f"{temp_name}, see you next time!")

temp_name = name_list.pop(1)
print(f"{temp_name}, see you next time!")

temp_name = name_list.pop(2)
print(f"{temp_name}, see you next time!")

temp_name = name_list.pop(0)
print(f"{temp_name}, see you next time!")

print(f"{name_list[0]}, but you can still come here!")
print(f"{name_list[-1]}, but you can still come here!")

del name_list[0]
del name_list[0]

print(name_list)
