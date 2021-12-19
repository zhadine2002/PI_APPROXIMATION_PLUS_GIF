#!/usr/bin/env python3
"""
on calcule pi par l'approximation de monte carlo
"""
import random
#from collections import namedtuple
import sys

def generer_point():
    """generer des points entre (-1,1)"""
    abscisse = random.uniform(-1, 1)
    ordonne = random.uniform(-1, 1)
    return (abscisse, ordonne)


def in_circle(point):
    """
    pour l instant point est un tuple
    """
    if (point[0])**2 + (point[1])**2 <= 1:
        return 1
    return 0
def how_many_in_circle(nombre):
    """calculer combien de points dans cercle"""
    compteur = 0
    i = 0
    while i < nombre:
        point = generer_point()
        if in_circle(point) == 1:
            compteur += 1
        i += 1
    return compteur
def app_pi(nombre):
    """
    on calcule pi
    """
    compteur = how_many_in_circle(nombre)
    return 4*(compteur/nombre)

def main():
    """"
    execution du programme
    """
    if len(sys.argv) != 2:
        print('usage:', sys.argv[0], "entrer le nom puis le nombre de points sup a 100")
        return
    nombre = int(sys.argv[1])
    print(app_pi(nombre))

if __name__ == '__main__':
    main()
