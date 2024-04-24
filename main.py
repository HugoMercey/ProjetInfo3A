from Labyrinthe import *
from Case import *
from fonction import *
from fonctionResolv import *

longueur = 20 #Longueur du labyrinthe
largeur =20 #Largeur du labyrinthe

lab = Labyrinthe(longueur, largeur) #Création de la grille du labyrinthe
generation(lab) #Création du labyrinthe

chemin, cheminVisu = mainDroite(lab) #Résolution du labyrinthe par l'algorithme de la main droite
#La variable chemin est le chemin pour aller jusqu'à la sortie
#La variable cheminVisu est une modification de chemin pour pouvoir être affiché correctement via pyplot
print(chemin)

graphe = labyrinthe_to_graphe(lab) #Conversion du labyrinthe en un graphe
mat = dist_bfs(graphe, lab, [lab.getLargeur()-1, 0]) #Calcul des distances de chaque sommet à la case de départ (lab.getLargeur()-1, 0)
cheminGraphe = grapheResolv(mat,lab) #Résolution du labyrinthe par l'algorythme utilisant les graphes
print(cheminGraphe)

affiche(lab, cheminVisu, cheminGraphe) #Affichage du labyrinthe ainsi que des chemins empruntés par les deux algorithmes
