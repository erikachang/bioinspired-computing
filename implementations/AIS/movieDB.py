import requests
import json
from sets import Set
import operator


movies = []
FIXDB =  'fixedDataBase.txt'

def getGenreList():
	return countGenres(movies).keys()

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
		genreString = movie['Genre']
		genres = genreString.split(',')
		for genre in genres:
			genre = genre.strip()
			if(genreMap.has_key(genre)):
				genreMap[genre] = genreMap[genre] + 1.0/len(listMovies)
			else:
				genreMap[genre] = 1.0/len(listMovies)
	return genreMap

def countActors(listMovies):
	actorMap = dict()
	for movie in listMovies:
		actorsString = movie['Actors']
		actors = actorsString.split(',')
		i = 0;
		for actor in actors:
			if(i > 5): break
			actor = actor.strip()
			if(actorMap.has_key(actor)):
				actorMap[actor] = actorMap[actor] + 1.0/len(listMovies)
			else:
				actorMap[actor] = 1.0/len(listMovies)
			i = i +1

	return actorMap

def countDirectors(listMovies):
	directorMap = dict()
	for movie in listMovies:
		directorsString = movie['Director']
		directors = directorsString.split(',')
		i = 0;
		for director in directors:
			if(i > 5): break
			director = director.strip()
			if(directorMap.has_key(director)):
				directorMap[director] = directorMap[director] + 1.0/len(listMovies)
			else:
				directorMap[director] = 1.0/len(listMovies)
			i = i +1

	return directorMap

def printOrderedMap(map):
	sorted_x = sorted(map.items(), key=operator.itemgetter(1))
	for k, v in sorted_x:
		print k, v

def printMap(map):
	for k, v in map.iteritems():
		print k, v

def checkMovie(movie):
	print 'test'

def main():
	DB =  'movieListJson.txt'
	while True:
			print('---')
			print('Welcome to MovieDB:')
			print('---')
			print('(1) - Load movies from file ('+DB+')')
			print('(2) - Add movie to file ')
			print('(3) - Print all movies in DB')
			print('(4) - Load from fixed database (cannot be written) (file: '+FIXDB +')')
			print('(5) - Change file to load')
			print('(6) - Print statistics about the database')
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
			    			print('Movie discarded')
			    else: 
			    	print('Movie not found :(')
			elif option == '3':
				for movie in movies:
					print movie['Title']
			elif option == '4':
				loadDB(FIXDB)
			elif option == '5':
				DB =  raw_input('File: ')
			elif option == '6':
				genreMap = countGenres(movies)
				actorsMap = countActors(movies)
				directorsMap = countDirectors(movies)
				printOrderedMap(genreMap)
				print '============'
				printOrderedMap(actorsMap)
				print '============'
				printOrderedMap(directorsMap)
			elif option == '0':
				break
			else:
				print 'Option unrecognized. Please try again.'