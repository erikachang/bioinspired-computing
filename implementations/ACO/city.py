class City():
	connections = []
	x = 0
	y = 0
	#0 is start, 1 is goal
	cId = 0
	def __repr__(self):
		s = 'ID: ' + str(self.cId) +' X: ' +  str(self.x) + ' Y: ' + str(self.y)
		return s