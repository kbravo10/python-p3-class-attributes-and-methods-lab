class Song:

    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)
        
    
    @classmethod
    def add_song_to_count(self):
        self.count += 1

    @classmethod
    def add_to_genres(self, genre):
        located = False
        if len(self.genres) == 0:
            self.genres.append(genre)
        else:
            for item in self.genres:
                if item == genre:
                    located = True
            if located == False:
                self.genres.append(genre)
    @classmethod
    def add_to_artists(self, artist):
        located = False
        if len(self.artists) == 0:
            self.artists.append(artist)
        else:
            for item in self.artists:
                if item == artist:
                    located = True
            if  located == False:
                self.artists.append(artist)

    @classmethod
    def add_to_genre_count(self, genre):
        if self.genre_count == {}:
            self.genre_count[genre] = 1
        else:
            located = False
            for key in self.genre_count:
                if key == genre:
                    located = True
            if located == False:
                self.genre_count[genre] = 1
            else:
                self.genre_count[genre] += 1
    
    @classmethod
    def add_to_artist_count(self, artist):
        if artist not in self.artist_count.keys():
            self.artist_count[artist] = 1
        else:
            self.artist_count[artist] += 1

                 
    