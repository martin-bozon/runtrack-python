def sol_mur(longueur):
    trait = ""
    x = 0
    while x < (longueur - 2):
        trait = (trait + '-')
        x += 1
    return '|' + trait + '|'


def mur_vide(longueur):
    trait = ""
    x = 0
    while x < (longueur - 2):
        trait = (trait + ' ')
        x += 1
    return '|' + trait + '|'


def rectangle(hauteur, longueur):
    i = 0
    while i < hauteur:
        if (i == 0) or (i == hauteur - 1):
            print(sol_mur(longueur))
        else:
            print(mur_vide(longueur))
        i += 1


def draw_rectangle(hauteur, longueur):
    if longueur < 3:
        print('trop court')
    else:
        rectangle(hauteur, longueur)


draw_rectangle(9, 14)
