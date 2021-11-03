class Personne:
    def __init__(self, firstname, lastname):
        self.Pfirstname = firstname
        self.Plastname = lastname

    def sepresenter(self):
        print(self.Plastname)
        print(self.Pfirstname)

    def setlasname(self, lastname):
        self.Plastname = lastname

    def getlastname(self):
        return self.Plastname

    def setfirstname(self, firstname):
        self.Pfirstname = firstname

    def getfirstname(self):
        return self.Pfirstname


p = Personne("Martin", "Bozon")
p.sepresenter()
p.setlasname("Toto")
p.setfirstname("Jose")
print(p.getfirstname())
print(p.getlastname())


