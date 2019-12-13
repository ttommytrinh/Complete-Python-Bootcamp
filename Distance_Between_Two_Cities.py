'''
CALCULATE THE DISTANCE BETWEEN HOUSTON, DALLAS, AUSTIN, LOS ANGELES, NEW YORK, SEATTLE
LATITUDE = x, LONGITUDE = y
'''

Dallas = (32.776665, -96.796989)
Houston = (29.760427, -95.369804)
Austin = (30.267153, -97.743057)
LA = (34.0207305,-118.6919224)
NY = (40.6976701,-74.2598677)
Seattle = (47.606209, -122.332069)

import math

def distance(city1,city2):
    change_lat = math.radians(city2[0]-city1[0])
    change_long = math.radians(city2[1]-city1[1])
    R = 6371000
    
    a=math.sin(change_lat/2.0)**2+\
        math.cos(math.radians(city1[0]))*math.cos(math.radians(city2[0]))*\
        math.sin(change_long/2.0)**2
    c=2*math.atan2(math.sqrt(a),math.sqrt(1-a))
    
    c = 2*math.atan2(math.sqrt(a),math.sqrt(1-a))
    #IN METERS
    d_miles = R*c*0.000621371
    d_kilometers = R*c/1000
    
    while True:
        ask_unit=input("Would you like miles or kilometers?")
        if ask_unit=="miles":
            return(f"{d_miles} miles")
            break
        elif ask_unit=="kilometers":
            return(f"{d_kilometers} kilometers")
            break