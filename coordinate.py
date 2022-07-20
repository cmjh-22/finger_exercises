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
->An array locations which is a class variable of Location stores every Location that is created.
"""
class Location:
  locations = [0] #this here are class variables
  def __init__(self,coordinate,name):#constructor with its arguments
    self.coordinate = coordinate #this here are instance variables
    self.name = name #this here is a property of a class
    locations.append(self)
# Instance method to append locations


  def return_location():#method
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

  def populationCity(self):
    return self.population

