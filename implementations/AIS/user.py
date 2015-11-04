import json
from sets import Set
import operator

class User():
	
	def __init__(self, name, biasList):
		self.movieRatings = []
		self.biasList = biasList
		self.name = name
		self.concentration = 10.0

	def getMovieList(self):
		movieList = []
		for m in self.movieRatings:
			movieList.append(m[0])
		return movieList
	
	def getMovieMap(self):
		movieMap = dict()
		for m in self.movieRatings:
			movieMap[m[0]['Title']] = m[1]
		return movieMap

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