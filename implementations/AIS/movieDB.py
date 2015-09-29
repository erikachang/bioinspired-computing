import requests
import json
from sets import Set

movies = []
FIXDB =  'fixedDataBase.txt'
DB =  'movieListJson.txt'

def loadDB(file):
	f = open(file, 'r')
	for line in f:
		test = json.loads(line)
		movies.append(test)
	print('Database loaded!')
	f.close()

def saveDB(file):
	f = open(file,'w')
	for movie in movies:
		json.dump(movie, f)
		f.write("\n")
	f.close()
	print('Saved!')

def countGenres(listMovies):
	genreMap = dict()
	for movie in listMovies:
		print movie['Genre']

def main():
	while True:
			print('---')
			print('Welcome to MovieDB:')
			print('---')
			print('(1) - Load movies from file ('+DB+')')
			print('(2) - Add movie to file ')
			print('(3) - Print all movies in DB')
			print('(4) - Load from fixed database (cannot be written) (file: '+FIXDB +')')
			print('(5) - Change file to load')
			print('(0) - Exit')
			option = raw_input('Your choice: ')
			if option == '1':
			    loadDB(DB)
			elif option == '2':
			    name = raw_input('Movie title: ')
			    year = raw_input('Year: ')
			    r = requests.get('http://www.omdbapi.com/?t='+name+'&y='+year+'&plot=short&r=json')
			    if(r.json()['Response'] == 'True'):
			    	print('Found: ' + r.json()['Title'] + ' ' + r.json()['Year'])
			    	save = raw_input('Want to save this movie on the Database file? (Y/N)')
			    	if(save.lower() == 'y'):
			    		movies.append(r.json())
			    		saveDB(DB)
			    	else:
			    		save = raw_input('Want to save this movie on local memory? (Y/N)')
			    		if(save.lower() == 'y'):
			    			movies.append(r.json())
			    			print('Only saved on memory, select option 1 to reset Memory')
			    		else:
			    			print('Movie discarted')
			    else: 
			    	print('Movie not found :(')
			elif option == '3':
				for movie in movies:
					print movie['Title']
			elif option == '4':
				loadDB(FIXDB)
			elif option == '0':
				break
			else:
				print 'Option unrecognized. Please try again.'
main()