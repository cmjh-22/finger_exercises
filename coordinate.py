"""
In coordinate.py, create a class Coordinate
each time a Coordinate is constructed it should take in 2 properties latitude and longitude.
Create a method return_coord that returns both properties
"""
class Coordinate:
    def __init__(self,latitude,longitude):
        self.latitude = latitude
        self.longitude = longitude
    def return_coord(self):
        return self.latitude, self.longitude
"""
Now create another class Location which has two properties called coordinate and name.
->Each time an instance of Location is created,
a class Coordinate should be created that gets passed in the coordinates that should be given as arguments when creating Location.<-
Further, you should create a return_location method that returns the name of the location.
An array locations which is a class variable of Location stores every Location that is created.
"""
class Location:
  locations = [] #this here are class variables
  def __init__(self,coordinate,name):#constructor with its arguments
    self.coordinate = coordinate #this here are instance variables
    #or did he meant this?
    #self.coordinate = coordinate(latitude,longitude) as a means to be an example of composition
    self.name = name #this here is a property of a class
    Location.locations.append(self)

  def return_location(self):#method
    return self.name

"""
Now create another class City that is a subclass of location.
It should take 4 parameters: latitude, longitude, name and population.
Pass latitude and longitude as well as name to the parent classes constructor.
Population is an attribute specific to the subclass City.
Lastly create a method that returns the population of a City.
"""
class City(Location):
  def __init__(self,latitude,longitude,name,population):
    coordinate().__init__(latitude,longitude)
    super().__init__(name)
    self.population = population

  def popCity(self):
    return self.population

def main():
  location1 = Location(Coordinate(19.43, -99.13), 'Mexico City')
  location2 = Location(Coordinate(43.65, -74.34), 'Toronto')

  for location in Location.locations:
    print(location.coordinate.return_coord(), location.return_location())

  print(Location.return_location(location1))#print name of the city


if __name__ == "__main__":
  main()
