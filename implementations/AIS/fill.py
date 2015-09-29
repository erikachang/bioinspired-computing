#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json
r = requests.get('http://www.omdbapi.com/?t=Amélie&y=&plot=short&r=json')
obj = r.json()
f = open('movieList2.txt', 'r')
f2 = open('jsonList.txt','w')

for movie in f:
	print movie
	r2 = requests.get('http://www.omdbapi.com/?t='+movie+'&y=&plot=short&r=json')
	print r2.json()["Title"]
	json.dump(r2.json(), f2)
	f2.write("\n")




#f3 = open('jsonList.txt','r')
#for line in f3:
#	test = json.loads(line)
#	print test['Title']