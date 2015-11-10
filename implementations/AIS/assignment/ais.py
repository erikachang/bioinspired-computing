import user as u
import movieDB as mdb
import random
import json
from operator import itemgetter, attrgetter, methodcaller



def main():
    mdb.loadDB(mdb.FIXDB)
    users = load('users.txt')
    #TODO

def load(file):
    f = open(file, 'r')
    users = []
    for line in f:
        jsonUser = json.loads(line)
        user = u.User(jsonUser['name'], jsonUser['biasList'])
        user.movieRatings = jsonUser['movieRatings']
        users.append(user)
    print 'User database loaded!'
    f.close()
    return users



def recomendMovies(user, neighbors):
    print 'Not Implemented'

def executeAIS(antigen, users):
    'Not Implemented'


# calculate how much an user likes each genre based on ratings
def calculateGenreRate(user):
    genreOccurence = dict(mdb.countGenres(user.getMovieList()))
    genreMap = dict()
    for mt in user.movieRatings:
        movie = mt[0]
        genreString = movie['Genre']
        genres = genreString.split(',')
        for genre in genres:
            genre = genre.strip()
            if (genreMap.has_key(genre)):
                genreMap[genre] = genreMap[genre] + mt[1]
            else:
                genreMap[genre] = mt[1]
    genreRatio = dict()
    for gen in genreMap.keys():
        genreRatio[gen] = genreMap[gen] / (genreOccurence[gen] * len(user.movieRatings))
    return genreRatio


# function used to calculate correlation metric between two users
def compare(user1, user2):
    print 'Not Implemented'


main()
