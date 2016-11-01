#import the libraries I need
import matplotlib
matplotlib.use('Qt4Agg')

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.figure
import numpy as np
from mpl_toolkits.basemap import Basemap

fields=['Name', 'Country', 'Primary_Diameter (m)', 'Secondary_Diameter (m)']
m=pd.read_csv('data.csv', usecols=fields)


#identify various columns: primary and secondary diam from (m)
#for each and every line get primary (and secondary) diameter
#column 6 and 7 (diameters) d1 will be x coordinates, d2 will be y 

#Drew from Assignment 9 "Fun With Maps"
#set up a figure
#figure(figsize=(8,8),dpi=200)
#assign red 'o' for circles, blue 'triangle' for ovals 
c=0
e=0
shape=[] 
for i in range(len(m.index)):
	d1=m.iloc[i]['Primary_Diameter (m)']
	d2=m.iloc[i]['Secondary_Diameter (m)']
	if d1/d2 >= 1.25:
		point='^b'
		shape.append('circle')
		c=c+1
	else:
		point='or'
		shape.append('ellipse')
		e=e+1
	plt.figure(1)
	plt.title('Circles:%i and Ellipses:%i' %(c,e))
	plt.plot(d1,d2,point)
plt.show()

#create a number line (type of plot) for better readability
plt.figure(2)
plt.title('Number Line')
for i in range (len(m.index)):
	d1=m.iloc[i]['Primary_Diameter (m)']
	d2=m.iloc[i]['Secondary_Diameter (m)']
	ratio=d1/d2
	if ratio >= 1.25:
		point='^b'
	else:
		point='or'
	plt.plot(ratio,0,point)
	plt.xlim([0.7,3.1])
plt.show()


#All map stuff from here down
lons=[0]
lats=[0]
# draw map with markers for locations
plt.figure(3)
#figure(figsize=(20,20),dpi=200)
b = Basemap(projection='mill',lon_0=180)
x, y = b(lons,lats)
b.drawmapboundary(fill_color='#99ffff')
b.fillcontinents(color='coral',lake_color='#99ffff')
b.scatter(x,y,3,marker='o',color='k')
plt.title('Locations of Maars',fontsize=20)
plt.show()

#plot lat/longs to map
coordinates = {
	'USA': (38.8833, -77.0167),
	'Argentina': (-34.6000, -58.3833),
	'Cameroon': (3.8667, 11.5167),
	'Chile': (33.4333, -70.6667),
	'Costa Rica': (9.9333, -84.0833),
	'France': (47.0000, 2.0000),
	'GER': (52.5167, 13.3833),
	'Germany': (52.5167, 13.3833),
	'Indonesia': (-6.1750, 106.8283),
	'Guatemala': (15.783471, -90.230759),
	'Italy': (41.9000, 12.4833),
	'ITA': (41.9000, 12.4833),
	'JPN': (36.204824, 138.252924),
	'MEX': (19.0000, -99.1333),
	'Mexico': (19.0000, -99.1333),
	'New Zealand': (-40.900557, 174.885971),
	'PHI': (12.879721, 121.774017),
	'Spain': (40.463667, -3.749220),
	'Australia': (-25.274398, 133.775136)
}

for i in range(len(m.index)):
	country=m.iloc[i]['Country']
	x=coordinates[country][0]
	y=coordinates[country][1]
	b.plot(x,y,'or',markersize=24)


