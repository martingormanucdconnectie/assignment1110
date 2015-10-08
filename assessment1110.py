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
for item in c:
    print item

#print each item in the table "ports"
c.execute("SELECT * FROM ports;")
print "Ports are: "
for item in c:
    print item

