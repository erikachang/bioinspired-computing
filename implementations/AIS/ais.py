import user as u
import movieDB as mdb
import random
from sets import Set
from operator import itemgetter, attrgetter, methodcaller


#not used yet
dList = []

def main():
	mdb.loadDB(mdb.FIXDB)
	users = generateRandomUsers(1500,150)
	neighbors = findNeighbors(users, users[0], 10)
	print neighbors

#find k closest neighbors for mainUser in the list users
def findNeighbors(users, mainUser, k):
	distances = []
	for user in users:
		if user == mainUser: continue
		distances.append([user,[compare(mainUser, user)]])
	distances = sorted(distances, key=itemgetter(1))
	#distances = distances[::-1]
	neighbors = []
	for i in range(k):
		neighbors.append(distances.pop())
	return neighbors
	#print distances


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
#		calculateGenreRate(user)
#	print generatedUsers
	return generatedUsers

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
	#mdb.printOrderedMap(genreRatio)
	return genreRatio

#function used to calculate correlation metric between two users
#only using one pearson correlation so far
def compare(user1,user2):
	u1GenreRate =  calculateGenreRate(user1)
	u2GenreRate =  calculateGenreRate(user2)
	overlappedGenres = []
	for genre1 in u1GenreRate.keys():
		if genre1 in u2GenreRate.keys():
			overlappedGenres.append(genre1)
	sum1 = 0.0
	for genre in overlappedGenres:
		sum1 = sum1 + ( (u1GenreRate[genre] - averageOfVector(u1GenreRate.values())) * (u2GenreRate[genre] - averageOfVector(u2GenreRate.values())) )
	sum2 = 0.0
	for genre in overlappedGenres:
		sum2 = sum2 + pow(( (u1GenreRate[genre] - averageOfVector(u1GenreRate.values()))),2)
	sum3 = 0.0
	for genre in overlappedGenres:
		sum3 = sum3 + pow(( (u2GenreRate[genre] - averageOfVector(u2GenreRate.values()))),2)
	pearson = sum1/pow((sum3*sum2),0.5)
	return pearson

#calculate the average value of a vector
def averageOfVector(vector):
	avg = 0
	for x in vector:
		avg = avg + x
	return avg/len(vector)


main()
