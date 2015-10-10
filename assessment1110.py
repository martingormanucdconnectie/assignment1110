# -*- coding: utf-8 -*-
"""
Created on Thu Oct 08 20:35:35 2015

@author: mgorman
"""
import numpy as np;
#import haversine

print ""                              #formating of report

# connect to database
import sqlite3
conn = sqlite3.connect('renewable.db')
c = conn.cursor()
#print each item in the table "location"
print ("The list of locations are: ")
print ""                             #formating of report
c.execute("SELECT * FROM location;")
location = []
for i in c:
    location.append(i)
print location

#print each item in the table "ports"
c.execute("SELECT * FROM ports;")
port = []
print ""                             #formating of report
print "The list of ports are: "
print ""                             #formating of report
for j in c:
    port.append(j)
print port
print ""

# as this information is a tuple i will now convert to a numpy array
la = np.array(port)   
ln = np.array(location)

# need a for loop to read each lat and long to calc distance
#print la[:,0] #testing
#print la[:,1] #testing

i = [0,1,2]
#print ln[:,0]
#print ln[:,1]
#print ""
for i in i :    #loop through two arrays and find the differences
    newlist = np.array(la[i,0] - ln[:,0] + la[i,1] - ln[:,1])
#   print newlist                   # testing only
x = min(newlist, key = abs)       # this is the smallest difference

y = newlist.argmin()              # this is the index of the smallest

z = abs(x) * 1 * 1.1508 *1000    # arbitrary valuation and conversion
print ""
print "The smallest distance is %f" %abs(x)
print ""
#print "The two locations are port %s and location %s" %p1 %l1  # wont work
#print ""
print "The expected cost is €%s" % z

  

    
    

