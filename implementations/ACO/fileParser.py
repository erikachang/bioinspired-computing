#!/usr/bin/env python
import city as c
import connection as cn
import networkx as nx

def parseFile(file):
    f = open(file, 'r')
    cId = 0
    cityList = []
    connectionList = []
    connectionParse = False
    
    for line in f:
        if line in ['\n', '\r\n']:
            connectionParse = True
            continue
        if connectionParse:
            splitted = line.split('|')
            con = cn.Connection(cityList[int(splitted[0])], cityList[int(splitted[1])])
            connectionList.append(con)
            # connection both ways
            con = cn.Connection(cityList[int(splitted[1])], cityList[int(splitted[0])])
            connectionList.append(con)
        else:
            splitted = line.split('|')
            city = c.City(cId, int(splitted[0]), int(splitted[1]))
            cityList.append(city)
            cId += 1
            
    #populate connection in cities
    for city in cityList:
        for connection in connectionList:
            if connection.a is city:
                city.addConnection(connection)
                
    G = convertToNetworkx(cityList, connectionList)
    return cityList, connectionList, G

def convertToNetworkx(cList, cnList):
    G = nx.Graph()
#    G.add_edge(cList[0].cId,cList[1].cId,object= cnList[0])
    for city in cList:
        G.add_node(city.cId, x = city.x, y = city.y, concentration = city.concentration)
        #G[city.cId]['x'] = 'test'
    for connection in cnList:
        G.add_edge(connection.a.cId, connection.b.cId, object = connection)
    return G

#cList, cnList, G = parseFile('cenario_10.txt')
#print  cList
#print '\n=========\n'
#print cnList
#nx.draw(G)
#plt.show()
