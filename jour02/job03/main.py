class Bibliotheque:
    def __init__(self, nom, catalogue):
        self.Bnom = nom
        self.Bcatalogue = catalogue

    def inventaire(self):
        print(self.Bcatalogue)

    def acheterlivre(self, nom, quantite):



B = Bibliotheque('alcasar', [['livre un', 5], ['livre deux ', 4]])

B.inventaire()