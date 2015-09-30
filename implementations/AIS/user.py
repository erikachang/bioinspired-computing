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
	def compare(self,user):
		#implement here a metric for correlation (spearman, pearson or a different one)
		return 0
	def __repr__(self):
		print '======================='
		print self.biasList
		s = 'User: ' +  self.name + '\n'
		#for movie in self.movieRatings:
		#	s = s + movie[0]['Title'].encode('utf-8') + ' ' + str(movie[1]) + '  ' + movie[0]['Genre'].encode('utf-8') +'\n'
		return s