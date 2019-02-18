import time
from skyfield.api import load
from skyfield.api import Topos


def calculateAngle(location,planet):
   astrometric = location.at(t).observe(planets[planet])
   ra, dec, distance = astrometric.radec()
   print(planet.replace(' barycenter','') + ','+str(dec))
   
planets = load('de421.bsp')
earth = planets['earth']

#change the city location here and assign the new 
#city to the location variable
mumbai = earth + Topos('19.0760 N', '72.8777 E')
location = mumbai

ts = load.timescale()
#t = ts.now() 
t = ts.utc(2018,30,11,4,00,00)
print("Time(in utc): " + t.utc_datetime().strftime("%Y-%m-%d %H:%M"))

planetsList = ['sun','moon','mercury','venus','mars','jupiter barycenter','saturn barycenter']

for planet in planetsList:
   calculateAngle(location,planet)


