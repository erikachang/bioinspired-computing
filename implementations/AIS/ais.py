import user as u
import movieDB as mdb
import random
import math
from sets import Set
from operator import itemgetter, attrgetter, methodcaller


#not used yet
dList = []

STIMULATION_RATIO = 0.5
SUPPRESION_RATIO = 0.3
DEATH_RATIO = 0.3
NEIGHBOURS_MAX = 10

def main():
	mdb.loadDB(mdb.FIXDB)
	users = generateRandomUsers(1500,150)
	executeAIS(users[0],users)

def executeAIS(antigen, users):
	neighbors = findNeighbors(users, antigen, len(users) - 1)
	stable = 0
	antibodies = []
	iterations = 0;
	while stable < 10:
		index = random.randrange(len(neighbors))
		
		nAb = neighbors.pop(index)
		antibodies.append(nAb[0])
		lastAbSize =  len(antibodies)
		stable = 0
		iterations += 1
		print iterations
		while stable < 10 & NEIGHBOURS_MAX <= len(antibodies):
			removeList = []
			for ab in antibodies:
				agStimulation = STIMULATION_RATIO * abs(compare(antigen,ab)) * antigen.concentration * ab.concentration
				deathRate = DEATH_RATIO * ab.concentration
				abSupression = 0
				for abody in antibodies:
					if abody == ab:
						continue
					abSupression = abSupression + ( abs(compare(ab,abody)) * ab.concentration * abody.concentration)
				abSupression = (SUPPRESION_RATIO/len(antibodies)) * abSupression
				print agStimulation
				ab.concentration = agStimulation + abSupression - deathRate
				if ab.concentration < 21:
					removeList.append(ab)
			for rm in removeList:
				antibodies.remove(rm)
			stable += 1
	for ab in antibodies:
		print ab.name +' ' + str(compare(ab,antigen)) + ' ' + str(ab.concentration)
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
		sum1 += ( (u1GenreRate[genre] - averageOfVector(u1GenreRate.values())) * (u2GenreRate[genre] - averageOfVector(u2GenreRate.values())) )
	sum2 = 0.0
	for genre in overlappedGenres:
		sum2 += pow(( (u1GenreRate[genre] - averageOfVector(u1GenreRate.values()))),2)
	sum3 = 0.0
	for genre in overlappedGenres:
		sum3 += pow(( (u2GenreRate[genre] - averageOfVector(u2GenreRate.values()))),2)
	pearson = sum1/pow((sum3*sum2),0.5)
	return pearson

#calculate the average value of a vector
def averageOfVector(vector):
	avg = 0
	for x in vector:
		avg = avg + x
	return avg/len(vector)


main()
