from personne import Personne
from livre import Livre


class Auteur(Personne):
    def __init__(self, firstname, lastname, oeuvre):
        super(Auteur, self).__init__(firstname, lastname)
        self.Oeuvre = oeuvre

    def listerOeuvre(self):
        return self.Oeuvre

    def ecrivreUnLivre(self, livre):
        nouvelle_oeuvre = Livre(livre)
        self.Oeuvre.append(nouvelle_oeuvre.gettitre())