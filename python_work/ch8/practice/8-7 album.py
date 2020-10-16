
def make_album(singer, title, number = None):
    """ Print album information and number of songs(optional). """
    music_album = {'singer': singer, 'title': title}
    
    if number:
        music_album['song_number'] = number

    return music_album

album1 =make_album("W", 'round 2')
album2 = make_album("S", 'Pascal')
album3 = make_album("G", 'VA-11 HALL-A', 46)

print(album1)
print(album2)
print(album3)




