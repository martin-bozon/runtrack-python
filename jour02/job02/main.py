import personne


class Livre:
    def __init__(self, titre):
        self.Ltitre = titre
        #self.auteur = Auteur()

    def print(self):
        print(self.Ltitre)
        #self.auteur.ecrivreUnLivre(self.Ltitre)


class Auteur(personne.Personne):
    def __init__(self, firstname, lastname):
        super(Auteur, self).__init__(firstname, lastname)
        self.Oeuvres = ["Un livre", "Deux livre"]

    def listerOeuvre(self):
        print(self.Oeuvres)
        
    def ecrivreUnLivre(self, livre):
        #nouvelle_oeuvre = Livre(livre)
        #nouvelle_oeuvre.()
        self.Oeuvres.append(livre)


L = Livre("Python pour les nuls")
A = Auteur("Bob", "Le bricoleur")
A.listerOeuvre()
A.ecrivreUnLivre("Trois livre")
A.listerOeuvre()

