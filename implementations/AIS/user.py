import json
from sets import Set
import operator

class User():
	movieRatings = []
	biasList = []
	name = ''

	def getMovieList(self):
		movieList = []
		for m in self.movieRatings:
			movieList.append(m[0])
		return movieList
	def __repr__(self):
		#print '======================='
		#print self.biasList
		s = 'User: ' +  self.name 
		#for movie in self.movieRatings:
		#	s = s + movie[0]['Title'].encode('utf-8') + ' ' + str(movie[1]) + '  ' + movie[0]['Genre'].encode('utf-8') +'\n'
		return s
	def printUserInfo(self):
		print '======================='
		print self.biasList
		print 'User: ' +  self.name 
		for movie in self.movieRatings:
			print movie[0]['Title'].encode('utf-8') + ' ' + str(movie[1]) + '  ' + movie[0]['Genre'].encode('utf-8') +'\n'