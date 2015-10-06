class City():

    def __init__(self, id, x, y):
        self.x = x
        self.y = y
        self.cId = id
        self.connections = []
        self.concentration = 0
    
    def __repr__(self):
        s = 'ID: ' + str(self.cId) +' X: ' +  str(self.x) + ' Y: ' + str(self.y)
        return s

    def addConnection(self, connection):
        self.connections.append(connection)
