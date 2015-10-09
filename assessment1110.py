# -*- coding: utf-8 -*-
"""
Created on Thu Oct 08 20:35:35 2015

@author: mgorman
"""

# connect to database
import sqlite3
conn = sqlite3.connect('renewable.db')
c = conn.cursor()
#print each item in the table "location"
c.execute("SELECT * FROM location;")
print ("Locations are: ")
l = list(c.execute("SELECT * FROM location"))
print l
#for i in l:
#    print i

#print each item in the table "ports"
c.execute("SELECT * FROM ports;")
print "Ports are: "
p = list(c.execute("SELECT * FROM ports"))
print p
#for j in p:
#   print j


print " "
p0 = p[0]
print p0[0]
print p0[1]
print p0[0] - p0[1]
#print p[1]
#print p[2]
#print p[-1]
#print p[3]
#print l[0]



#print min(items[1],item[1])
