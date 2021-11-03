from personne import Personne
from livre import Livre
from auteur import Auteur


class Bibliotheque:
    def __init__(self, nom, catalogue):
        self.Bnom = nom
        self.Bcatalogue = catalogue

    def inventaire(self):
        print(self.Bcatalogue)

    def acheterlivre(self, auteur, nom, quantite):
        if nom in auteur.listerOeuvre():
            nouvelle_quantite = self.Bcatalogue[nom] - quantite
            if nouvelle_quantite > -1:
                self.Bcatalogue[nom] = nouvelle_quantite
            else:
                print('pas assez de quantité')

class Client(Personne):
    def __init__(self, firstname, lastname):
        super(Client, self).__init__(firstname, lastname)


B = Bibliotheque('alcasar', {'livre un': 2, 'livre deux': 3})
B.inventaire()
A1 = Auteur("toto", "l'écrivain", "livre un")
A2 = Auteur("Nicolas", "Sarkozy", "livre deux")
B.acheterlivre(A1, 'livre un', 1)
B.acheterlivre(A2, 'livre deux', 2)
B.inventaire()
