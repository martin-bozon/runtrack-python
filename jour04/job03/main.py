number = int(input("entrez un entier:"))


def plateau(n, m):
    # ligne = []
    if n == 0:
        return ''
    else:
        # ligne.append('O' * m)
        print(ligne(m))
        plateau(n-1, m)


def ligne(n):
    ligneplateau = []
    i = n
    while n > 0:
        ligneplateau.append('O')
        n -= 1
    return ligneplateau


# def reines(l):
    # condition de placement des reines
    # exemple un reine sur la ligne 1 emplacement 0
    # bloquer les emplacement 0 des toutes les autres lignes
    # bloquer les emplacement de cette ligne
    # bloquer les emplacement diagonales des lignes suivantes =>
    # lignes +1, emplacement +1 n fois
    # exemple ligne 2 emplacement 1, ligne 3 emplacement 2, ...

plateau(number, number)

