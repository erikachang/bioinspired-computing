import city as c

class Connection():
    #enclidean distance
    concentration = 0

    def __init__(self, origin, destination):
        self.a = origin
        self.b = destination
        self.size = self._euclidean(self.a, self.b)

    def __repr__(self):
        s = 'cA: ' + str(self.a.cId) +' cB: ' +  str(self.b.cId) + ' size: ' +str(self.size) 
        return s

    # x and y are vectors of the same size
    def _euclidean(self, c1, c2):
        x = [c1.x, c1.y]
        y = [c2.x, c2.y]
        sumSq = 0.0
        for i in range(len(y)):
            sumSq += (x[i] - y[i]) ** 2
        return (sumSq ** 0.5)
