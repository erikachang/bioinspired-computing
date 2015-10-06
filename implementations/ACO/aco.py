import fileParser
import networkx as nx
import random

class Aco():
	cities = []
	connections = []
	G = nx.Graph()
	#Number of ants
	k = 1
	#Number of rounds
	rounds = 1
	def loadFile(self, f):
		self.cities, self.connections, self.G= fileParser.parseFile(f)

	def main(self):
		self.loadFile('cenario_10.txt')
		self.executeAco()
	def executeAco(self):
		
		edgesVisited = []
		antEdgeList = []
		for i in range(self.rounds):
			
			for j in range(self.k):
				#set to the initial state
				currentState = self.cities[0].cId
				# operations of ant j
				edgesVisited = []
				while currentState != 1:
					action = self.getAction(j, currentState)
					edgesVisited.append(action)
					currentState = action.b.cId
				#calculate pheronome distribution
				antEdgeList.append(edgesVisited)
				print edgesVisited
	def getAction(self, ant, state):
		index = random.randint(0, len(self.cities[state].connections)-1)
		return self.cities[state].connections[index]

if __name__ == "__main__":
    aco = Aco()
    aco.main()
