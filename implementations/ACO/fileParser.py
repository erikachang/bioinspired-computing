#!/usr/bin/env python
import city as c
import connection as cn
import networkx as nx

def parse_file(file):
    f = open(file, 'r')
    city_index = 0
    cities_list = []
    connections_list = []
    has_parsed_cities = False
    
    for line in f:
        if line in ['\n', '\r\n']:
            has_parsed_cities = True
            continue
        if has_parsed_cities:
            splitted = line.split('|')
            con = cn.Connection(cities_list[int(splitted[0])], cities_list[int(splitted[1])])
            connections_list.append(con)
            # create redundant connection
            con = cn.Connection(cities_list[int(splitted[1])], cities_list[int(splitted[0])])
            connections_list.append(con)
        else:
            splitted = line.split('|')
            city = c.City(city_index, int(splitted[0]), int(splitted[1]))
            cities_list.append(city)
            city_index += 1
            
    #populate connection in cities
    for city in cities_list:
        for connection in connections_list:
            if connection.origin is city:
                city.add_connection(connection)
                
    G = convert_to_networkx(cities_list, connections_list)
    return cities_list, connections_list, G

def convert_to_networkx(cList, cnList):
    G = nx.Graph()
#    G.add_edge(cList[0].cId,cList[1].cId,object= cnList[0])
    for city in cList:
        G.add_node(city.cId, x = city.x, y = city.y, concentration = city.concentration)
        #G[city.cId]['x'] = 'test'
    for connection in cnList:
        G.add_edge(connection.origin.cId, connection.destination.cId, object = connection)
    return G

#cList, cnList, G = parse_file('cenario_10.txt')
#print  cList
#print '\n=========\n'
#print cnList
#nx.draw(G)
#plt.show()
