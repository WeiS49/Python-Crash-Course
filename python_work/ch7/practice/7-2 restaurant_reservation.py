
people_to_serve = input("How many people will have dinner here today? ")
people_to_serve = int(people_to_serve)


if people_to_serve > 8:
    print("\nSorry, we don't have room for so many people today.")

elif 0 < people_to_serve <= 8:
    print("\nThis way, sir.")

