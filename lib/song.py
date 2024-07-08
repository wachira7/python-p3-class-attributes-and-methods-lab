class Song:
    '''Class "Song" in song.py'''

    count = 0
    genres = set()   # set for storing unique genres
    artists = set()
    genre_count = {} #dictionary for counting no. of songs for each genre
    artist_count = {} # dictionary for counting no. of songs by each artist

    def __init__(self, name, artist, genre):   #_init_ is a constructor
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.count += 1  # incrementation of total song count
        Song.genres.add(genre)
        Song.artists.add(artist)
        if genre in Song.genre_count:
            Song.genre_count[genre] += 1 #adds the new genre to the genre_count dictionary
        else:
            Song.genre_count[genre] = 1
        if artist in Song.artist_count:
            Song.artist_count[artist] += 1
        else:
            Song.artist_count[artist] = 1

   
    

    
    
