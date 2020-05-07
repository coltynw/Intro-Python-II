# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    
    def __init__(self, name, description, inventory=None): #initial values
        self.name = name
        self.description = description
        self.inventory = inventory
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
    def __str__(self):        #string representation of object
        return (self.name + ": " + self.description)   

        
