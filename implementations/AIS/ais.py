import user as u
import movieDB as mdb
import random
from sets import Set



def main():
	mdb.loadDB(mdb.FIXDB)
	
	generateRandomUsers(3,150)

#generate random biased users
def generateRandomUsers(nUsers, nMovies):
	generatedUsers = []
	for i in range(nUsers):
		user = u.User()
		user.movieRatings = []
		user.name = str(i)
		user.biasList = generateRandomGenreBias(user, 5)
		copy = list(mdb.movies)
		for j in range(nMovies):
			index = random.randint(0, len(copy)-1)
			movie = copy.pop(index)			
			score = biasScore(user, movie)
			user.movieRatings.append((movie,score))
		generatedUsers.append(user)
		calculateGenreRate(user)
	print generatedUsers

#Give a score to a movie based on user genre bias
def biasScore(user, movie):
	genreString = movie['Genre']
	movieGenres = genreString.split(',')
	biasList = user.biasList
	score = 0;
	biasValue = 0;
	for i in range(len(biasList)):
		bias = biasList[i][0]
		for genre in movieGenres:
			genre = genre.strip()
			if bias == genre:
				biasValue =  biasList[i][1]
				break;
	if biasValue == 0:
		return random.randint(0, 8)	
	score = random.randint(1, (10 - biasValue)) + biasValue 
	return score

#generate genre bias for an user 
def generateRandomGenreBias(user, n):
	genreList = list(mdb.getGenreList())
	biasList = []
	for i in range(n):
		genre = genreList.pop(random.randrange(len(genreList)))
		biasList.append((genre, n-i))
	return biasList

#calculate how much an user likes each genre based on ratings
def calculateGenreRate(user):
	print '============='
	genreOccurence = dict(mdb.countGenres(user.getMovieList()))
	genreMap = dict()
	for mt in user.movieRatings:
		movie = mt[0]
		genreString = movie['Genre']
		genres = genreString.split(',')
		for genre in genres:
			genre = genre.strip()
			if(genreMap.has_key(genre)):
				genreMap[genre] = genreMap[genre] + mt[1]
			else:
				genreMap[genre] = mt[1]
	genreRatio = dict()
	for gen in genreMap.keys():
		genreRatio[gen] = genreMap[gen]/(genreOccurence[gen] * len(user.movieRatings))
		#print gen + ': ' + str(genreMap[gen]/(genreOccurence[gen] * len(user.movieRatings)))
	mdb.printOrderedMap(genreRatio)

main()
