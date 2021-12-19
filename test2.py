#!/usr/bin/env python3
#import app_pi
""" pi approxiimation"""
import sys
import subprocess
import app_pi2

WHITE = '255 255 255\n'
RED = '255 0 0\n'  #RED
BLACK = '0 0 0\n'
BLUE = '0 0 255\n'
def trait_horizontal(colonne, debu_colo, fin_colo, couleur_actuelle):
    """tracege de trait horizontal qui sera utilise pour tracer les chiffres"""
    if debu_colo <= colonne <= fin_colo:
        return BLACK
    return couleur_actuelle
def trait_verticale(ligne, debut_ligne, fin_ligne, couleur_actuelle):
    """trace de trait verticale qui sera utilisé pour tracer les chiffres"""
    if debut_ligne <= ligne <= fin_ligne:
        return BLACK
    return couleur_actuelle

def trace_3(taille, ligne, debut_l, fin_l, colonne, debu_c, fin_c, couleur_actuelle):
    """tracer le chiffre 3 on pourra tracer le chiffre sans soustraire -1 mais le chiffre deviendra
    moins epais pour cela j'ai voulu faire ca pour augmenter l'epaisseur """
    color = couleur_actuelle
    if ligne in [debut_l, taille//2, fin_l, debut_l-1, taille//2-1, fin_l-1]:
        color = trait_horizontal(colonne, debu_c, fin_c, couleur_actuelle)
    if colonne in [fin_c, fin_c-1]:
        color = trait_verticale(ligne, debut_l, fin_l, couleur_actuelle)
    return color
def trace_2(taille, ligne, debut_l, fin_l, colonne, debu_c, fin_c, couleur_actuelle):
    """tracer le chiffre 3 on pourra tracer le chiffre sans soustraire -1 mais le chiffre deviendra
    moins epais pour cela j'ai voulu faire ca pour augmenter l'epaisseur """
    color = couleur_actuelle
    if ligne in [debut_l, taille//2, fin_l, debut_l-1, taille//2-1, fin_l-1]:
        color = trait_horizontal(colonne, debu_c, fin_c, couleur_actuelle)
    if colonne in [debu_c, debu_c -1]:
        color = trait_verticale(ligne, taille//2, fin_l, couleur_actuelle)
    if colonne in [fin_c, fin_c-1]:
        color = trait_verticale(ligne, debut_l, taille//2, couleur_actuelle)
    return color
def trace_4(taille, ligne, debut_l, fin_l, colonne, debu_c, fin_c, couleur_actuelle):
    """tracer le chiffre 4 on pourra tracer le chiffre sans soustraire -1 mais le chiffre deviendra
    moins epais pour cela j'ai voulu faire ca pour augmenter l'epaisseur """
    color = couleur_actuelle
    if ligne in [taille//2, taille//2 -1]:
        color = trait_horizontal(colonne, debu_c, fin_c, couleur_actuelle)
    if colonne in [debu_c, debu_c -1]:
        color = trait_verticale(ligne, debut_l, taille//2, couleur_actuelle)
    if colonne in [fin_c, fin_c-1]:
        color = trait_verticale(ligne, debut_l, fin_l, couleur_actuelle)
    return color
def trace_5(taille, ligne, debut_l, fin_l, colonne, debu_c, fin_c, couleur_actuelle):
    """tracer le chiffre 5 on pourra tracer le chiffre sans soustraire -1 mais le chiffre deviendra
    moins epais pour cela j'ai voulu faire ca pour augmenter l'epaisseur """
    color = couleur_actuelle
    if ligne in [debut_l, taille//2, fin_l, debut_l-1, taille//2-1, fin_l-1]:
        color = trait_horizontal(colonne, debu_c, fin_c, couleur_actuelle)
    if colonne in [debu_c, debu_c -1]:
        color = trait_verticale(ligne, debut_l, taille//2, couleur_actuelle)
    if colonne in [fin_c, fin_c-1]:
        color = trait_verticale(ligne, taille//2, fin_l, couleur_actuelle)
    return color
def trace_6(taille, ligne, debut_l, fin_l, colonne, debu_c, fin_c, couleur_actuelle):
    """tracer le chiffre 6 on pourra tracer le chiffre sans soustraire -1 mais le chiffre deviendra
    moins epais pour cela j'ai voulu faire ca pour augmenter l'epaisseur """
    color = couleur_actuelle
    if ligne in [debut_l, taille//2, fin_l, debut_l-1, taille//2-1, fin_l-1]:
        color = trait_horizontal(colonne, debu_c, fin_c, couleur_actuelle)
    if colonne in [debu_c, debu_c -1]:
        color = trait_verticale(ligne, debut_l, fin_l, couleur_actuelle)
    if colonne in [fin_c, fin_c-1]:
        color = trait_verticale(ligne, taille//2, fin_l, couleur_actuelle)
    return color
def trace_7(ligne, debut_l, fin_l, colonne, debu_c, fin_c, couleur_actuelle):
    """tracer le chiffre 7 on pourra tracer le chiffre sans soustraire -1 mais le chiffre deviendra
    moins epais pour cela j'ai voulu faire ca pour augmenter l'epaisseur """
    color = couleur_actuelle
    if ligne in [debut_l, debut_l-1]:
        color = trait_horizontal(colonne, debu_c, fin_c, couleur_actuelle)
    if colonne in [fin_c, fin_c-1]:
        color = trait_verticale(ligne, debut_l, fin_l, couleur_actuelle)
    return color
def trace_8(taille, ligne, debut_l, fin_l, colonne, debu_c, fin_c, couleur_actuelle):
    """tracer le chiffre 3 on pourra tracer le chiffre sans soustraire -1 mais le chiffre deviendra
    moins epais pour cela j'ai voulu faire ca pour augmenter l'epaisseur """
    color = couleur_actuelle
    if ligne in [debut_l, taille//2, fin_l, debut_l-1, taille//2-1, fin_l-1]:
        color = trait_horizontal(colonne, debu_c, fin_c, couleur_actuelle)
    if colonne in [debu_c, debu_c -1]:
        color = trait_verticale(ligne, debut_l, fin_l, couleur_actuelle)
    if colonne in [fin_c, fin_c-1]:
        color = trait_verticale(ligne, debut_l, fin_l, couleur_actuelle)
    return color
def trace_9(taille, ligne, debut_l, fin_l, colonne, debu_c, fin_c, couleur_actuelle):
    """tracer le chiffre 9 on pourra tracer le chiffre sans soustraire -1 mais le chiffre deviendra
    moins epais pour cela j'ai voulu faire ca pour augmenter l'epaisseur """
    color = couleur_actuelle
    if ligne in [debut_l, taille//2, fin_l, debut_l-1, taille//2-1, fin_l-1]:
        color = trait_horizontal(colonne, debu_c, fin_c, couleur_actuelle)
    if colonne in [debu_c, debu_c -1]:
        color = trait_verticale(ligne, debut_l, taille//2, couleur_actuelle)
    if colonne in [fin_c, fin_c-1]:
        color = trait_verticale(ligne, debut_l, fin_l, couleur_actuelle)
    return color

def trace_1(ligne, debut_l, fin_l, colonne, fin_c, couleur_actuelle):
    """tracer le chiffre 1 on pourra tracer le chiffre sans soustraire -1 mais le chiffre deviendra
    moins epais pour cela j'ai voulu faire ca pour augmenter l'epaisseur """
    color = couleur_actuelle
    if colonne in [fin_c, fin_c-1]:
        color = trait_verticale(ligne, debut_l, fin_l, couleur_actuelle)
    return color

def virgule(ligne, debut_l, fin_l, colonne, debut_c, fin_c, couleur_actuelle):
    """tracage de la virgule"""
    color = couleur_actuelle
    if debut_l <= ligne <= fin_l:
        if debut_c <= colonne <= fin_c:
            color = BLACK
    return color
def trace_0(ligne, debut_l, fin_l, colonne, debut_c, fin_c, couleur_actuelle):
    """tracer le chiffre 0 on pourra tracer le chiffre sans soustraire -1 mais le chiffre deviendra
    moins epais pour cela j'ai voulu faire ca pour augmenter l'epaisseur """
    color = couleur_actuelle
    if ligne in [debut_l, fin_l, debut_l-1, fin_l-1]:
        color = trait_horizontal(colonne, debut_c, fin_c, couleur_actuelle)
    if colonne in [debut_c, fin_c, debut_c-1, fin_c-1]:
        color = trait_verticale(ligne, debut_l, fin_l, couleur_actuelle)
    return color







def ou_commencer(nombre, taille, longueur, distance_entre_deux):
    """ cette fonction retourne ou le tracage des chiffres doit commencer"""
    result = ''
    if nombre == 1:
        result = taille//2 - longueur//2
    if nombre == 2:
        result = taille//2 - longueur - distance_entre_deux//2
    if nombre == 3:
        result = taille//2 -distance_entre_deux - longueur*(3/2)
    if nombre == 4:
        result = taille//2 - distance_entre_deux*(1.5) - 2*longueur
    if nombre == 5:
        result = taille//2 - 2*distance_entre_deux - 2.5*longueur
    if nombre == 6:
        result = taille//2 - 2.5*distance_entre_deux -3*longueur
    return result




def generate_ppm_file(taille, pixel_list, j, chiffres, chiffres_a_dessiner, app_pi_chaine):
    """fonction principale"""
    file = open('img{}_3-{}.ppm'.format(j, app_pi_chaine[2:chiffres +1]), 'w')
    file.write('P3\n')
    file.write('{0} {0}\n'.format(taille))
    file.write('255\n')
    index = 0
    pixel_actuel = pixel_list[index]
    color = ""
    points = 0
    debut_l = ((2+0.2)*taille//5)
    longueur = (taille//2 - debut_l)//1
    fin_l = debut_l + 2*longueur
    distance_entre_deux = longueur//4
    debut_c = int(ou_commencer(chiffres, taille, longueur, distance_entre_deux))
    fin_c = debut_c + longueur
    debut_l_virgule = taille//2 + 3.5*longueur//4
    debut_c_virgule = fin_c + distance_entre_deux//2 - distance_entre_deux//4
    fin_c_virgule = fin_c + distance_entre_deux//2 + distance_entre_deux//4
    for ligne in range(0, taille):
        for colonne in range(0, taille):
            color = WHITE
            if pixel_actuel[0] == ligne:
                if pixel_actuel[1] == colonne:
                    if pixel_actuel[2] == 0:
                        color = RED
                    else:
                        color = BLUE
                        points += 1
                    if index+1 < len(pixel_list):
                        index = index + 1
                        colonne_courante = pixel_actuel[1]
                        ligne_courante = pixel_actuel[0]
                        pixel_actuel = pixel_list[index]
                        if (pixel_actuel[0] == ligne_courante and\
                           pixel_actuel[1] == colonne_courante):
                            if pixel_actuel[2] == 0:
                                color = RED
                            else:
                                color = BLUE
                            if index+1 < len(pixel_list):
                                index = index+1
                                pixel_actuel = pixel_list[index]
            couleur_actuelle = color
            if debut_l-1 <= ligne <= fin_l:
                color = trace_3(taille, ligne, debut_l, fin_l,
                                colonne, debut_c, fin_c, couleur_actuelle)
                if chiffres > 1 and color == couleur_actuelle:
                    debut_c_2 = fin_c + distance_entre_deux
                    fin_c_2 = debut_c_2 + longueur
                    if chiffres_a_dessiner[1] == '0':
                        color = trace_0(ligne, debut_l, fin_l,\
                                        colonne, debut_c_2, fin_c_2, couleur_actuelle)
                    if chiffres_a_dessiner[1] == '1':
                        color = trace_1(ligne, debut_l, fin_l, colonne, fin_c_2, couleur_actuelle)
                    if chiffres_a_dessiner[1] == '2':
                        color = trace_2(taille, ligne, debut_l, fin_l,\
                                        colonne, debut_c_2, fin_c_2, couleur_actuelle)
                    if chiffres_a_dessiner[1] == '3':
                        color = trace_3(taille, ligne, debut_l, fin_l,\
                                        colonne, debut_c_2, fin_c_2, couleur_actuelle)
                    if chiffres_a_dessiner[1] == '4':
                        color = trace_4(taille, ligne, debut_l, fin_l,\
                                        colonne, debut_c_2, fin_c_2, couleur_actuelle)
                    if chiffres_a_dessiner[1] == '5':
                        color = trace_5(taille, ligne, debut_l, fin_l,\
                                        colonne, debut_c_2, fin_c_2, couleur_actuelle)
                    if chiffres_a_dessiner[1] == '6':
                        color = trace_6(taille, ligne, debut_l, fin_l,\
                                        colonne, debut_c_2, fin_c_2, couleur_actuelle)
                    if chiffres_a_dessiner[1] == '7':
                        color = trace_7(ligne, debut_l, fin_l,\
                                        colonne, debut_c_2, fin_c_2, couleur_actuelle)
                    if chiffres_a_dessiner[1] == '8':
                        color = trace_8(taille, ligne, debut_l, fin_l,\
                                        colonne, debut_c_2, fin_c_2, couleur_actuelle)
                    if chiffres_a_dessiner[1] == '9':
                        color = trace_9(taille, ligne, debut_l, fin_l,\
                                        colonne, debut_c_2, fin_c_2, couleur_actuelle)
                    if color == couleur_actuelle:
                        color = virgule(ligne, debut_l_virgule, fin_l,\
                                        colonne, debut_c_virgule, fin_c_virgule, couleur_actuelle)
                    if chiffres > 2 and color == couleur_actuelle:
                        debut_c_3 = fin_c_2 + distance_entre_deux
                        fin_c_3 = debut_c_3 + longueur
                        if chiffres_a_dessiner[2] == '0':
                            color = trace_0(ligne, debut_l, fin_l,\
                                            colonne, debut_c_3, fin_c_3, couleur_actuelle)
                        if chiffres_a_dessiner[2] == '1':
                            color = trace_1(ligne, debut_l, fin_l,\
                                            colonne, fin_c_3, couleur_actuelle)
                        if chiffres_a_dessiner[2] == '2':
                            color = trace_2(taille, ligne, debut_l, fin_l,\
                                            colonne, debut_c_3, fin_c_3, couleur_actuelle)
                        if chiffres_a_dessiner[2] == '3':
                            color = trace_3(taille, ligne, debut_l, fin_l,\
                                            colonne, debut_c_3, fin_c_3, couleur_actuelle)
                        if chiffres_a_dessiner[2] == '4':
                            color = trace_4(taille, ligne, debut_l, fin_l,\
                                            colonne, debut_c_3, fin_c_3, couleur_actuelle)
                        if chiffres_a_dessiner[2] == '5':
                            color = trace_5(taille, ligne, debut_l, fin_l,\
                                            colonne, debut_c_3, fin_c_3, couleur_actuelle)
                        if chiffres_a_dessiner[2] == '6':
                            color = trace_6(taille, ligne, debut_l, fin_l,\
                                            colonne, debut_c_3, fin_c_3, couleur_actuelle)
                        if chiffres_a_dessiner[2] == '7':
                            color = trace_7(ligne, debut_l, fin_l,\
                                            colonne, debut_c_3, fin_c_3, couleur_actuelle)
                        if chiffres_a_dessiner[2] == '8':
                            color = trace_8(taille, ligne, debut_l, fin_l,\
                                            colonne, debut_c_3, fin_c_3, couleur_actuelle)
                        if chiffres_a_dessiner[2] == '9':
                            color = trace_9(taille, ligne, debut_l, fin_l,\
                                            colonne, debut_c_3, fin_c_3, couleur_actuelle)
                        if chiffres > 3 and color == couleur_actuelle:
                            debut_c_4 = fin_c_3 + distance_entre_deux
                            fin_c_4 = debut_c_4 + longueur
                            if chiffres_a_dessiner[3] == '0':
                                color = trace_0(ligne, debut_l, fin_l,\
                                                colonne, debut_c_4, fin_c_4, couleur_actuelle)
                            if chiffres_a_dessiner[3] == '1':
                                color = trace_1(ligne, debut_l, fin_l,\
                                                colonne, fin_c_4, couleur_actuelle)
                            if chiffres_a_dessiner[3] == '2':
                                color = trace_2(taille, ligne, debut_l, fin_l,\
                                                colonne, debut_c_4, fin_c_4, couleur_actuelle)
                            if chiffres_a_dessiner[3] == '3':
                                color = trace_3(taille, ligne, debut_l, fin_l,\
                                                colonne, debut_c_4, fin_c_4, couleur_actuelle)
                            if chiffres_a_dessiner[3] == '4':
                                color = trace_4(taille, ligne, debut_l, fin_l,\
                                                colonne, debut_c_4, fin_c_4, couleur_actuelle)
                            if chiffres_a_dessiner[3] == '5':
                                color = trace_5(taille, ligne, debut_l, fin_l,\
                                                colonne, debut_c_4, fin_c_4, couleur_actuelle)
                            if chiffres_a_dessiner[3] == '6':
                                color = trace_6(taille, ligne, debut_l, fin_l,\
                                                colonne, debut_c_4, fin_c_4, couleur_actuelle)
                            if chiffres_a_dessiner[3] == '7':
                                color = trace_7(ligne, debut_l, fin_l,\
                                                colonne, debut_c_4, fin_c_4, couleur_actuelle)
                            if chiffres_a_dessiner[3] == '8':
                                color = trace_8(taille, ligne, debut_l, fin_l,\
                                                colonne, debut_c_4, fin_c_4, couleur_actuelle)
                            if chiffres_a_dessiner[3] == '9':
                                color = trace_9(taille, ligne, debut_l, fin_l,\
                                                colonne, debut_c_4, fin_c_4, couleur_actuelle)
                            if chiffres > 4 and color == couleur_actuelle:
                                debut_c_5 = fin_c_4 + distance_entre_deux
                                fin_c_5 = debut_c_5 + longueur
                                if chiffres_a_dessiner[4] == '0':
                                    color = trace_0(ligne, debut_l, fin_l,\
                                                    colonne, debut_c_5, fin_c_5, couleur_actuelle)
                                if chiffres_a_dessiner[4] == '1':
                                    color = trace_1(ligne, debut_l, fin_l,\
                                                    colonne, fin_c_5, couleur_actuelle)
                                if chiffres_a_dessiner[4] == '2':
                                    color = trace_2(taille, ligne, debut_l, fin_l,\
                                                    colonne, debut_c_5, fin_c_5, couleur_actuelle)
                                if chiffres_a_dessiner[4] == '3':
                                    color = trace_3(taille, ligne, debut_l, fin_l,\
                                                    colonne, debut_c_5, fin_c_5, couleur_actuelle)
                                if chiffres_a_dessiner[4] == '4':
                                    color = trace_4(taille, ligne, debut_l, fin_l,\
                                                    colonne, debut_c_5, fin_c_5, couleur_actuelle)
                                if chiffres_a_dessiner[4] == '5':
                                    color = trace_5(taille, ligne, debut_l, fin_l,\
                                                    colonne, debut_c_5, fin_c_5, couleur_actuelle)
                                if chiffres_a_dessiner[4] == '6':
                                    color = trace_6(taille, ligne, debut_l, fin_l,\
                                                    colonne, debut_c_5, fin_c_5, couleur_actuelle)
                                if chiffres_a_dessiner[4] == '7':
                                    color = trace_7(ligne, debut_l, fin_l,\
                                                    colonne, debut_c_5, fin_c_5, couleur_actuelle)
                                if chiffres_a_dessiner[4] == '8':
                                    color = trace_8(taille, ligne, debut_l, fin_l,\
                                                    colonne, debut_c_5, fin_c_5, couleur_actuelle)
                                if chiffres_a_dessiner[4] == '9':
                                    color = trace_9(taille, ligne, debut_l, fin_l,\
                                                    colonne, debut_c_5, fin_c_5, couleur_actuelle)
                                if chiffres > 5 and color == couleur_actuelle:
                                    debut_c_6 = fin_c_5 + distance_entre_deux
                                    fin_c_6 = debut_c_6 + longueur
                                    if chiffres_a_dessiner[5] == '0':
                                        color = trace_0(ligne, debut_l, fin_l,\
                                                        colonne, debut_c_6, fin_c_6,\
                                                             couleur_actuelle)
                                    if chiffres_a_dessiner[5] == '1':
                                        color = trace_1(ligne, debut_l, fin_l,\
                                                        colonne, fin_c_6, couleur_actuelle)
                                    if chiffres_a_dessiner[5] == '2':
                                        color = trace_2(taille, ligne, debut_l, fin_l,\
                                                        colonne, debut_c_6, fin_c_6,\
                                                             couleur_actuelle)
                                    if chiffres_a_dessiner[5] == '3':
                                        color = trace_3(taille, ligne, debut_l, fin_l,\
                                                        colonne, debut_c_6, fin_c_6,\
                                                             couleur_actuelle)
                                    if chiffres_a_dessiner[5] == '4':
                                        color = trace_4(taille, ligne, debut_l, fin_l,\
                                                        colonne, debut_c_6, fin_c_6,\
                                                             couleur_actuelle)
                                    if chiffres_a_dessiner[5] == '5':
                                        color = trace_5(taille, ligne, debut_l, fin_l,\
                                                        colonne, debut_c_6, fin_c_6,\
                                                             couleur_actuelle)
                                    if chiffres_a_dessiner[5] == '6':
                                        color = trace_6(taille, ligne, debut_l, fin_l,\
                                                        colonne, debut_c_6, fin_c_6,\
                                                             couleur_actuelle)
                                    if chiffres_a_dessiner[5] == '7':
                                        color = trace_7(ligne, debut_l, fin_l,\
                                                        colonne, debut_c_6, fin_c_6,\
                                                             couleur_actuelle)
                                    if chiffres_a_dessiner[5] == '8':
                                        color = trace_8(taille, ligne, debut_l, fin_l,\
                                                        colonne, debut_c_6, fin_c_6,\
                                                             couleur_actuelle)
                                    if chiffres_a_dessiner[5] == '9':
                                        color = trace_9(taille, ligne, debut_l, fin_l,\
                                                        colonne, debut_c_6, fin_c_6,\
                                                             couleur_actuelle)
            file.write(color)

    return file

def main():
    """ fonction main fait la plupart du travail d'organisation"""
    if len(sys.argv) != 4:
        print('usage entrer la taille puis le nombre de point a generer puis les chiffres apres la virgule')
        return
    taille = sys.argv[1]
    nombre = sys.argv[2]
    chiffres = sys.argv[3]
    taille = int(taille)
    nombre = int(nombre)
    # chiffres entrés par l'utilisateur c'est le nombre de chiffres apres la virgule
    chiffres = int(chiffres) +1
    #chiffres utilisé ici c'est le nombre total des chiffres
    pixels_list = []
    pixels_ensemble = set()
    combien_danscercle = 0
    dix_pourcent = nombre / 10
    dix_pourcent_entier = int(dix_pourcent)
    j = 1
    for i in range(nombre):
        point = app_pi2.generer_point()
        in_circl = app_pi2.in_circle(point)
        if in_circl == 1:
            combien_danscercle += 1
        pixel_ligne = int(taille/2 + point[1]*(taille/2))
        pixel_colonne = int(taille/2 + point[0]*(taille/2))
        pixel = (pixel_ligne, pixel_colonne, in_circl)
        if pixel not in pixels_ensemble:
            pixels_list.append(pixel)
            pixels_ensemble.add(pixel)
        chiffres_a_dessiner = []
        if i+1 in [k*dix_pourcent_entier for k in range(1, 11)]:
            pixels_list.sort()
            app_pi = (4*combien_danscercle)/(j*dix_pourcent)
            print(app_pi)
            app_pi_chaine = str(app_pi)
            for element in app_pi_chaine:
                if element != '.':
                    chiffres_a_dessiner.append(element)
            while len(chiffres_a_dessiner) < chiffres:
                chiffres_a_dessiner.append('0')
            generate_ppm_file(taille, pixels_list, j, chiffres, chiffres_a_dessiner, app_pi_chaine)
            j = j+1
    subprocess.call('convert -delay 100 *.ppm pi.gif', shell=True)

if __name__ == '__main__':
    main()
