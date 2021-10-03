# Project 5 - Earthquakes
#
# Name: Kelsey Nguyen
# Instructor: Workman
from quakeFuncs import *

def main():
    quakes = read_quakes_from_file("quakes.txt")
    print()
    displayData(quakes)
    choice = input("Choice: ")
    while choice != "q":       
        if choice == "s" or choice == "S":
            choice_sort = input("Sort by (m)agnitude, (t)ime, (l)ongitude, or l(a)titude? ")
            if choice_sort == "m" or choice_sort == "M":
                sortMag(quakes) 
                print()
                displayData(quakes)
            elif choice_sort == "t" or choice_sort == "T":
                sortTime(quakes)
                print()
                displayData(quakes)
            elif choice_sort == "l" or choice_sort == "L":
                sortLongitude(quakes) 
                print()
                displayData(quakes)
            elif choice_sort == "a" or choice_sort == "A":
                sortLatitude(quakes)
                print()
                displayData(quakes) 
        if choice == "f" or choice == "f":
            choice_filter = input("Filter by (m)agnitude or (p)lace? ")
            if choice_filter == "m" or choice_filter == "M":
                lower_input = float(input("Lower bound: "))
                upper_input = float(input("Upper bound: "))
                print()
                displayData(filter_by_mag(quakes, lower_input, upper_input))
            elif choice_filter == "p" or choice_filter == "P":
                string_input = input("Search for what string? ")
                print()
                displayData(filter_by_place(quakes, string_input))
        if choice == "n" or choice == "N":
            original_quakes = list(quakes)
            x = get_json("http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_hour.geojson")
            if len(x["features"]) != 0:                
                for i in range(len(x['features'])):              
                    y = ((x['features'][i]))
                    newQuake = quake_from_feature(y)
                    if newQuake not in quakes:
                        quakes.append(newQuake)
            #comparing the new data/earthquakes to originl list
                if quakes != original_quakes:
                    print("\nNew quakes found!!!")
                print()
                displayData(quakes)
        choice = input("Choice: ")
    quit_file("quakes.txt", quakes)
    




            


        
















if __name__ == '__main__':
   main()