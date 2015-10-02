import city as c

class Connection():
	a = c.City()
	b = c.City()
	#enclidean distance
	size = 0
	concentration = 0
	def __repr__(self):
		s = 'cA: ' + str(self.a.cId) +' cB: ' +  str(self.b.cId) + ' size: ' +str(self.size) 
		return s