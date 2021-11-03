class Livre:
    def __init__(self, titre):
        self.Ltitre = titre
        #self.auteur = Auteur()

    def print(self):
        print(self.Ltitre)
        #self.auteur.ecrivreUnLivre(self.Ltitre)

    def gettitre(self):
        return self.Ltitre