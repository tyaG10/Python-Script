import lyricsgenius

api_key = "wNoop8K6Zb5ORrQCEqp7JW-yNSMFrY5jGTyZoC3SmWR2nLCxJkbGq2GbYCjTOWpX"
genius = lyricsgenius.Genius(api_key)
nom = input("Donnez le nom de l'artiste : ")
artiste = genius.search_artist(nom, max_songs=3, sort="title")
son = input("Donnez le titre du son : ")
son = artiste.song(son)
print(son.lyrics)