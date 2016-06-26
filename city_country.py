# city_country.py

# def city_country(city, country):
# 	print(city.title() + ' is in the ' + country.title() + '.')

# city_country('oakland', 'united states')

# def make_album(album_name, album_artist, album_tracks = ''):
# 	album = { 'album_name': album_name, 'album_artist': album_artist, 'album_tracks': album_tracks}	
# 	print(album)

# make_album('Experienced','Jim Hendrix',14)

def make_album():
	while True:
		print('print q at anytime to quit')	
		album_name = input('Album Name :')
		if album_name == 'q':
			break
		album_artist = input('Album Artist :')
		if album_artist == 'q':
			break	
		album_tracks = input('Album Tracks :')
		if album_tracks == 'q':
			break
		else:	
			album = { 'album_name': album_name, 'album_artist': album_artist, 'album_tracks': album_tracks}	
			print(album)

make_album()