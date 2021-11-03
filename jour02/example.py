class Personne:
    def __init__(self, firstname, lastname):
        self.Pfirstname = firstname
        self.Plastname = lastname

    def sepresenter(self):
        print(self.Plastname)
        print(self.Pfirstname)


#p1 = Personne("Luis", "Suarez")

#p1.sepresenter()


# Héritage
class Player(Personne):
    def __init__(self, firstname, lastname):
        self.PLfirstname = firstname
        self.PLlastname = lastname
        # Personne.__init__(firstname, lastname)
        super(Player, self).__init__(firstname, lastname)
        # => récupére les constructeurs de toutes les classes parentes


p2 = Player('Jose', 'Garcia')

p2.sepresenter()


