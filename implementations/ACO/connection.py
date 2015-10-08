import city as c

class Connection():
    concentration = 1

    """ Creates a new connection object linking origin to destination.
    
    The euclidean distance is also calculated and stored for future use.
    
    - When origin and destination are equal, instead of calculating the distance (which is 0) we assign a high value to the connection,
    so when calculating the heuristic this path has a lower probability of being chosen.
    """
    def __init__(self, origin, destination):
        self.origin = origin
        self.destination = destination
        if self.origin == self.destination:
            self.size = 1000
        else:
            self.size = self._euclidean(self.origin, self.destination)

    def __repr__(self):
        s = str(self.origin.cId) + '|' +  str(self.destination.cId) 
        return s

    # x and y are vectors of the same size
    def _euclidean(self, c1, c2):
        x = [c1.x, c1.y]
        y = [c2.x, c2.y]
        sumSq = 0.0
        for i in range(len(y)):
            sumSq += (x[i] - y[i]) ** 2
        return (sumSq ** 0.5)
