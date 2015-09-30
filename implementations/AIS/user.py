import json
from sets import Set
import operator

class User():
	movieRatings = []
	name = ''

	def compare(self,user):
		#implement here a metric for correlation (spearman, pearson or a different one)
		return 0
	def __repr__(self):
		print '======================='
		s = 'User: ' +  self.name + '\n'
		for movie in self.movieRatings:
			s = s + movie[0]['Title'].encode('utf-8') + ' ' + str(movie[1]) + '\n'
		return s