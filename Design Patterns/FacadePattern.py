#suppose you are a cook in the restaurant

class Cook():
    #Facade class
    #Desc: provides easy interface to prepare dish instead of calling three
    #different classes and making difficult for client to use.

    def prepareDish(self):
        self.cutter=Cutter()
        self.cutter.CutVegetables()

        self.boiler=Boiler()
        self.boiler.boilVegetables()

        self.frier=Frier()
        self.frier.fry()


class Cutter(object):
    #System class
    #Desc: Cutter class provide feature of cutting vegetables.
    def CutVegetables(self):
        print("All vegetables are cut")

class Boiler(object):
    #System class
    #Desc: Boiler class provide feature of Boiling vegetables.

    def boilVegetables(self):
        print("All vegetables are boiled")

class Frier(object):
    # System class
    # Desc: Fryer class provide feature of Frying vegetables.

    def fry(self):
        print("All vegetables are mixed and fried")


#Using facade class to prepare dish
cook=Cook()
cook.prepareDish()
