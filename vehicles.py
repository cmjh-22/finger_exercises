class vehicle(object):
    v_list = [] #this is a class variable
    id = 1 #the superclass should include an attribute ‘ID’ which is initially set to 1.
    #ToDo constructor
    def __init__(self,type,passengers,brand):
        self.type = type
        self.passengers = passengers
        self.brand = brand
        vehicle.id += 1 #with every instance that is created of class vehicle the ID should increase by 1.
        vehicle.v_list.append(self)#after every time a instance of class vehicle is created this instance should be automatically appended to the predefined list called “v_list”

    def get_id(self):
        #done
        return vehicle.id

    def return_vehicle(self):
        #done
        return "ID" + ":" + (str(self.id)) + "; Type" + ":" + (str(self.type)) + "; Name" + ":" + (str(self.name)) + "; Brand" + ":" + (str(self.brand)) + "; Passengers" + ":" + (str(self.passengers)) + ";"

    def br_path(self):
        #done
        if isinstance(self,car) or isinstance(self,truck): #object self, type car/truck
            brake_path = (self.max_speed_kmh / 10 * self.max_speed_kmh / 10) / 2
            return brake_path
        else:
            return False

    def get_speed(self):
        #done
        return self.max_speed_kmh

    def set_speed(self, speed):
        #done
        if isinstance(self,car) or isinstance(self,truck):
            self.max_speed_kmh = speed
        else:
            return False

    def get_name(self):
        #done
        return self.name

    def set_name(self, name):
        #done
        self.name = name


class car(vehicle):
    #ToDo constructor
    def __init__(self,name,passengers,brand,hp,max_speed_kmh):
        super().__init__('car',passengers,brand)
        self.name = name
        self.hp = hp
        self.max_speed_kmh = max_speed_kmh

class truck(vehicle):
    #ToDo constructor
    def __init__(self,name,passengers,brand,hp,speed_kmh,max_load_kg):
        super().__init__('truck',passengers,brand)
        self.name = name
        self.hp = hp
        self.speed_kmh = speed_kmh
        self.max_load_kg = max_load_kg

    def get_max_load(self):
        #done
        return self.max_load_kg

    def set_max_load(self, new_load):
        #done
        self.max_load_kg = new_load

class bike(vehicle):
    #ToDo constructor
    def __init__(self,name,passengers,brand,gears):
        super().__init__('bike',passengers,brand)
        self.name = name
        self.gears = gears

    def get_gear(self):
        #done
        return self.gears

    def set_gear(self, gears):
        #done
        self.gears = gears

# checking if ID increments with every new instance created
"""
v1 = vehicle(type, 2, 'volvo')
v2 = vehicle(type, 2, 'brand')
print(v1.id)
print(v2.id)
v3 = vehicle(type, 2, 'bbb')
print(v3.id)
for id in vehicle.v_list:
    print(vehicle.id)
"""
