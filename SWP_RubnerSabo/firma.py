class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender  

class Mitarbeiter(Person):
    def __init__(self, name, gender, abteilung):
        super().__init__(name, gender)
        self.abteilung = abteilung

class Abteilungsleiter(Mitarbeiter):
    def __init__(self, name, gender, abteilung):
        super().__init__(name, gender, abteilung)
        self.abteilung.set_leiter(self)

class Abteilung:
    def __init__(self, name):
        self.name = name
        self.mitarbeiter = []
        self.leiter = None

    def add_mitarbeiter(self, mitarbeiter):
        self.mitarbeiter.append(mitarbeiter)

    def set_leiter(self, leiter):
        self.leiter = leiter

    def mitarbeiter_count(self):
        return len(self.mitarbeiter)

class Firma:
    def __init__(self, name):
        self.name = name
        self.abteilungen = []

    def add_abteilung(self, abteilung):
        self.abteilungen.append(abteilung)

    def mitarbeiter_und_leiter_count(self):
        mitarbeiter_count = sum(len(abt.mitarbeiter) for abt in self.abteilungen)
        leiter_count = sum(1 for abt in self.abteilungen if abt.leiter is not None)
        return mitarbeiter_count, leiter_count

    def abteilungs_count(self):
        return len(self.abteilungen)

    def groesste_abteilung(self):
        if not self.abteilungen:
            return None
        return max(self.abteilungen, key=lambda abt: abt.mitarbeiter_count())

    def geschlechter_verhaeltnis(self):
        total = 0
        maenner = 0
        frauen = 0
        for abt in self.abteilungen:
            for mitarbeiter in abt.mitarbeiter:
                total += 1
                if mitarbeiter.gender == 'M':
                    maenner += 1
                elif mitarbeiter.gender == 'F':
                    frauen += 1
        if total == 0:
            return 0, 0
        return (frauen / total) * 100, (maenner / total) * 100

def main():
    firma = Firma("TechCorp")

    abteilung1 = Abteilung("Entwicklung")
    abteilung2 = Abteilung("Marketing")

    firma.add_abteilung(abteilung1)
    firma.add_abteilung(abteilung2)

    mitarbeiter1 = Mitarbeiter("Alice", 'F', abteilung1)
    abteilung1.add_mitarbeiter(mitarbeiter1)

    mitarbeiter2 = Mitarbeiter("Bob", 'M', abteilung1)
    abteilung1.add_mitarbeiter(mitarbeiter2)

    mitarbeiter3 = Mitarbeiter("Charlie", 'M', abteilung2)
    abteilung2.add_mitarbeiter(mitarbeiter3)

    leiter1 = Abteilungsleiter("Diana", 'F', abteilung1)
    leiter2 = Abteilungsleiter("Eve", 'F', abteilung2)

    print(f"Anzahl der Abteilungen: {firma.abteilungs_count()}")
    mitarbeiter_count, leiter_count = firma.mitarbeiter_und_leiter_count()
    print(f"Anzahl der Mitarbeiter: {mitarbeiter_count}")
    print(f"Anzahl der Abteilungsleiter: {leiter_count}")

    groesste_abt = firma.groesste_abteilung()
    print(f"Abteilung mit der größten Mitarbeiterstärke: {groesste_abt.name}")

    frauen_anteil, maenner_anteil = firma.geschlechter_verhaeltnis()
    print(f"Frauenanteil: {frauen_anteil:.2f}%")
    print(f"Männeranteil: {maenner_anteil:.2f}%")

if __name__ == "__main__":
    main()
