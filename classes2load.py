# define a basic class
class Human():
    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def print_features(self):
        print( "name:", self.name)
        print( "age:", self.age)
class Dog():
    # constructor
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    def print_features(self):
        print( "name:", self.name )
        print( "breed:", self.breed )
