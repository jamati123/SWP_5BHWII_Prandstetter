class Haus:
    def __init__(self, höhe, baujahr):
        self.höhe = höhe
        self.baujahr = baujahr   

class Hochhaus(Haus):
    def __init__(self, höhe, baujahr, breite, name):
        super().__init__(höhe, baujahr)
        self.breite = breite
        self.name = name
      
class Wohnhaus(Haus):
    def __init__(self, höhe, baujahr, keller):
        super().__init__(höhe, baujahr)
        self.keller = keller
        
def main():
    Haus1 = Haus(50, 2000)
    print('Bauhjahr: ' + str(Haus1.baujahr) + ' Höhe: ' + str(Haus1.höhe))
    try:
        Haus2 = Haus1.breite
    except AttributeError:
        print("keine breite")

    add_haus_baujahr(Haus1, None)
    print('Bauhjahr: ' + str(Haus1.baujahr) + ' Höhe: ' + str(Haus1.höhe))

    add_haus_baujahr(Haus1, 2000)
    print('Bauhjahr: ' + str(Haus1.baujahr) + ' Höhe: ' + str(Haus1.höhe))

    add_hochhaus_name(Haus1, "Haus1") 
    

    


def add_hochhaus_name(Hochhause, name):
    if not isinstance(Hochhause, Hochhaus):
        raise TypeError("haus must be of type Hochhaus")
    
def add_haus_baujahr(haus, baujahr):
    if not isinstance(haus, Haus):
        raise TypeError("haus must be of type Haus")
    if baujahr is None:
        haus.baujahr = 'unbekannt'
    else:
        haus.baujahr = baujahr

    


    
if __name__ == "__main__":
    main()
    