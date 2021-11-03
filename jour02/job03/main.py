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
            self.Bcatalogue[nom] = quantite

    def louer(self, client, nom_livre):
        if nom_livre in self.Bcatalogue:
            nouvelle_quantite = self.Bcatalogue[nom_livre] - 1
            if nouvelle_quantite == -1:
                print("Ce livre n'est plus disponible")
            else:
                client.add_livre(nom_livre)
                self.Bcatalogue[nom_livre] = nouvelle_quantite

    def rendrelivres(self, client):
        livres = client.getcollection()
        for livre in livres:
            self.Bcatalogue[livre] = self.Bcatalogue[livre] + 1
            client.emptycollection()


class Client(Personne):
    def __init__(self, firstname, lastname, collection):
        super(Client, self).__init__(firstname, lastname)
        self.Ccollection = collection

    def inventaire(self):
        print(self.Ccollection)

    def add_livre(self, livre):
        self.Ccollection[livre] = 1

    def getcollection(self):
        return self.Ccollection

    def emptycollection(self):
        self.Ccollection = {}

#instanciation
B = Bibliotheque('alcasar', {})
A1 = Auteur("toto", "l'écrivain", ["livre un", "livre deux"])
A2 = Auteur("Nicolas", "Sarkozy", ["livre trois", "livre quatre"])
C = Client("Bob", "Le lecteur", {})
C1 = Client("Toto", "Le lecteur", {})
#Achat livres
B.acheterlivre(A1, "livre un", 10)
B.acheterlivre(A2, "livre trois", 20)
B.acheterlivre(A1, "livre deux", 5)
B.acheterlivre(A2, "livre quatre", 45)
B.inventaire()
#Location
B.louer(C, 'livre un')
B.louer(C1, 'livre trois')
B.louer(C, 'livre quatre')
C.inventaire()
C1.inventaire()
B.inventaire()
#Retour livres
B.rendrelivres(C)
B.inventaire()
C.inventaire()

