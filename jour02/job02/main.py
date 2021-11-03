from personne import Personne

class Livre:
    def __init__(self, titre):
        self.Ltitre = titre
        #self.auteur = Auteur()

    def print(self):
        print(self.Ltitre)
        #self.auteur.ecrivreUnLivre(self.Ltitre)

    def gettitre(self):
        return self.Ltitre


class Auteur(Personne):
    def __init__(self, firstname, lastname, oeuvre):
        super(Auteur, self).__init__(firstname, lastname)
        self.Oeuvre = oeuvre

    def listerOeuvre(self):
        print(self.Oeuvre)
        
    def ecrivreUnLivre(self, livre):
        nouvelle_oeuvre = Livre(livre)
        self.Oeuvre.append(nouvelle_oeuvre.gettitre())


A = Auteur("Bob", "Le bricoleur", ['un livre', 'deux livre'])
A.listerOeuvre()
A.ecrivreUnLivre("Trois livre")
A.listerOeuvre()

