import city as c
import connection as cn

def parse(file):
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
			con = cn.Connection()
			con.a = cityList[int(splitted[0])]
			con.b = cityList[int(splitted[1])]
			con.size = euclidean(con.a,con.b)
			connectionList.append(con)
			
			#connection both ways
			con = cn.Connection()
			con.a = cityList[int(splitted[1])]
			con.b = cityList[int(splitted[0])]
			con.size = euclidean(con.a,con.b)
			connectionList.append(con)
 		else:
			splitted = line.split('|')
			city = c.City()
			city.x = int(splitted[0])
			city.y = int(splitted[1])
			city.cId = cId
			cityList.append(city)
			cId += 1
	#populate connection in cities
	for ct in cityList:
		ct.connections = []
		for cnn in connectionList:
			if cnn.a == ct:
				ct.connections.append(cnn)

	return cityList, connectionList

# x and y are vectors of the same size
def euclidean(c1,c2):
	x = [c1.x,c1.y]
	y = [c2.x,c2.y]
	sumSq=0.0
	for i in range(len(y)):
		sumSq+=(x[i]-y[i])**2
	return (sumSq**0.5)

cList, cnList = parse('cenario_10.txt')
print  cList
print '\n=========\n'
print cnList