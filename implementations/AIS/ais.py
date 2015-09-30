import user as u
import movieDB as mdb
import random
from sets import Set

def main():
	mdb.loadDB(mdb.FIXDB)
	generateRandomUsers(3,10)

def generateRandomUsers(nUsers, nMovies):
	generatedUsers = []
	for i in range(nUsers):
		user = u.User()
		user.movieRatings = []
		user.name = str(i)
		copy = mdb.movies
		for j in range(nMovies):
			index = random.randint(1, 10)
			print 'what?'
			movie = copy.pop(index)
			print movie['Title']
			#the score should maybe be based on genre....
			score = random.randint(1, 10)
			user.movieRatings.append((movie,score))
		generatedUsers.append(user)
	print generatedUsers


main()
