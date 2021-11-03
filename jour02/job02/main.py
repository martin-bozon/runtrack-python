import personne

class Livre:
    def __init__(self, titre):
        self.Ltitre = titre

    def print(self):
        print(self.Ltitre)


L = Livre("Python pour les nuls")

L.print()