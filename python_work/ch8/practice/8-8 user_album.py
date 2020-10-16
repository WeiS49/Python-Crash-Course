
def make_album(singer, title, number = None):
    """ Print album information and number of songs(optional). """
    music_album = {'singer': singer, 'title': title}
    
    if number:
        music_album['song_number'] = number

    return music_album


while True:
    print("\nTell me about album you like")
    print("Enter 'quit' to quit the program.")

    singer = input("Please enter the singer of your album. ")
    if singer == 'quit':
        break

    title = input("Please enter the title of your album. ")
    if title == 'quit':
        break

    print("Do you want to enter the number of songs in your album? (y/n)")
    
    album = {}

    choice = input()
    if choice == 'y':
        number = input("Tell me the number of your album. ")
        album = make_album(singer, title, int(number))
    elif choice == 'n':
        album = make_album(singer, title)

    print(f"\nHere is your album, enjoy!\n\t{album}")

