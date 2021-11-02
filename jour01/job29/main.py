def draw_triangle(hauteur):
    if hauteur < 2:
        print('trop court')
    else:
        longueur: int = hauteur * 2
        pente(longueur, hauteur)
        base(longueur)


def base(longueur):
    trait: str = ""
    x: int = 0
    while x < (longueur - 2):
        trait = (trait + '_')
        x += 1
    print('/' + trait + '\\')


def pente(longueur, hauteur):
    espace = " "
    bord1: str = '/'
    bord2: str = '\\'
    x: int = 0
    while x < (hauteur - 1):
        vide_bord: int = int(longueur / 2) - (x + 1)
        print((espace * vide_bord) + bord1 + (espace * (x*2)) + bord2)
        x += 1


draw_triangle(9)
