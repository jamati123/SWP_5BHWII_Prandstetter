class Haus:
    def __init__(self, höhe, baujahr):
        self.höhe = höhe
        self.baujahr = baujahr   

class Hochhaus(Haus):
    def __init__(self, höhe, baujahr, breite):
        super().__init__(höhe, baujahr)
        self.breite = breite
      
class Wohnhaus(Haus):
    def __init__(self, höhe, baujahr, keller):
        super().__init__(höhe, baujahr)
        self.keller = keller
        
def main():         
    Haus1 = Hochhaus(50,2000, 20)
    print('Bauhjahr: ' + str(Haus1.baujahr) + ' Höhe: ' + str(Haus1.höhe) + ' Breite: ' + str(Haus1.breite))
    Haus2 = Wohnhaus(10, 2010,True)   
    print('Bauhjahr: ' + str(Haus2.baujahr) + ' Höhe: ' + str(Haus2.höhe) + ' Keller: ' + str(Haus2.keller))
    Haus3 = Wohnhaus(10, 2010,True)   
    print('Bauhjahr: ' + str(Haus3.baujahr) + ' Höhe: ' + str(Haus3.höhe) + ' Keller: ' + str(Haus3.keller))

if __name__ == "__main__":
    main()
    