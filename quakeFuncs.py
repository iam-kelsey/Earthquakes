# Project 5 - Earthquakes
#
# Name: Kelsey Nguyen
# Instructor: Workman


from urllib.request import *
from json import *
from datetime import *
from operator import *

# GIVEN FUNCTIONS:
# Use these two as-is and do not change them
def get_json(url):
   ''' Function to get a json dictionary from a website.
       url - a string'''
   with urlopen(url) as response:
      html = response.read()
   htmlstr = html.decode("utf-8")
   return loads(htmlstr)

def time_to_str(time):
   ''' Converts integer seconds since epoch to a string.
       time - an int '''
   return datetime.fromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S')    
   
class Earthquake:
   '''Attributes:
      place - a string
      mag - a float
      longitutde  a float
      latitude - a float
      time - an int'''  

   def __init__(self, place, mag, longitude, latitude, time):
      self.place = place
      self.mag = mag
      self.longitude = longitude
      self.latitude = latitude
      self.time = time

   def __eq__(self, other):
      return (self.place == other.place and
              self.mag == other.mag and 
              self.longitude == other.longitude and
              self.latitude == other.latitude and 
              self.time == other.time)
   
   def __str__(self):
      return "(%.2f) %40s at %s (%8.3f, %.3f)" %(self.mag, self.place, time_to_str(self.time), self.longitude, self.latitude)

   

# Required function - implement me!   
def read_quakes_from_file(filename):
   lst_of_quakes = []
   quake_file = open(filename, 'r')
   for line in quake_file:
      line = line.split()
      place = ' '.join(line[4:])
      mag = float(line[0])
      longitude = float(line[1])
      latitude = float(line[2])
      time = int(line[3])
      quakes = Earthquake(place, mag, longitude, latitude, time)
      lst_of_quakes.append(quakes)
   quake_file.close()
   return lst_of_quakes

def displayData(lst_of_quakes):
   print("Earthquakes:\n------------")
   for quake in lst_of_quakes:
      print (quake)
   print()
   print("Options:\n  (s)ort\n  (f)ilter\n  (n)ew quakes\n  (q)uit\n")

def keyMag(quakes):
   return quakes.mag

def keyTime(quakes):
   return quakes.time

def keyLongitude(quakes):
   return quakes.longitude

def keyLatitude(quakes):
   return quakes.latitude

def sortMag(lst_of_quakes):
   lst_of_quakes.sort(key = keyMag, reverse = True)
   return lst_of_quakes

def sortTime(lst_of_quakes):
   lst_of_quakes.sort(key = keyTime, reverse = True)

def sortLongitude(lst_of_quakes):
   lst_of_quakes.sort(key = keyLongitude, reverse = False)

def sortLatitude(lst_of_quakes):
   lst_of_quakes.sort(key = keyLatitude, reverse = False)


# Required function - implement me!
def filter_by_mag(quakes, low, high):
   new_quakes_lst = []
   for quake in quakes:
      if quake.mag >= low and quake.mag <= high:
         new_quakes_lst.append(quake)
   return new_quakes_lst

     
# Required function - implement me!
def filter_by_place(quakes, word):   
   new_quakes_lst = []
   for quake in quakes:
      if word.casefold() in quake.place.casefold():
         new_quakes_lst.append(quake)
   return new_quakes_lst

# Required function for final part - implement me too!   
def quake_from_feature(feature):
   place = str(feature["properties"]["place"])
   time = int(feature["properties"]["time"]*0.001)
   mag = float(feature["properties"]["mag"])
   latitude = float(feature["geometry"]["coordinates"][1])
   longitude = float(feature["geometry"]["coordinates"][0])
   quakes = Earthquake(place, mag, longitude, latitude, time)
   return quakes

def quit_file(filename, lst_of_quakes):
   f = open(filename, "w+")
   for quake in lst_of_quakes:
      f.write(str(quake.mag) + " ") 
      f.write(str(quake.longitude) + " ")
      f.write(str(quake.latitude) + " ")
      f.write(str(quake.time) + " ")
      f.write((quake.place) + " \n")
      







   



     


   