class Preces:
    def __init__(self, name, count, type):
        self.nosaukums = name
        self.skaits = count
        self.veids = type
        self.info()

    def info(self):
        print("Veikala plauktos atrodas", ,"preces.")
        

class datori(Preces):
    def __init__(self, name, count, manufacturer, )
        super().__init__(name, count, "dators")
        self.__razotajs = manufacturer
        self.info()