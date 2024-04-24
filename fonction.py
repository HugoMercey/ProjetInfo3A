from pylab import *
from collections import *
from Labyrinthe import *
from Case import *

def affiche(lab, chemin = [], cheminGraphe = [], coul = 'black'):
    """""""""""""""""""""""""""""""""
    Cette fonction affiche le labyrinthe ainsi que les deux chemins des deux algorithmes
    """""""""""""""""""""""""""""""""

    for i in range(lab.getLargeur()): #Parcours de chaque ligne
        for j in range(lab.getLongueur()): #Parcours de chaque cellule
            caseActu = lab.getCase(i, j) #On récupère la case correcpondante aux coordonnées
            if caseActu.NordEstBloque(): #Si le mur Nord de cette case est bloqué
                tabNordIndc = [i+1, i+1]
                tabNord = [j, j+1]
                plt.plot(tabNord, tabNordIndc, coul) #Alors on trace un trait horizontal au dessus de la case
            if caseActu.EstEstBloque(): #Si le mur Est de cette case est bloqué
                tabEstIndc = [i, i+1]
                tabEst = [j+1, j+1]
                plt.plot(tabEst, tabEstIndc, coul) #Alors on trace un trait vertical à droite de la case
            if caseActu.SudEstBloque(): #Si le mur Sud de cette case est bloqué
                tabSudIndc = [i, i]
                tabSud = [j, j+1]
                plt.plot(tabSud, tabSudIndc, coul) #Alors on trace un trait horizontal en dessous de la case
            if caseActu.OuestEstBloque(): #Si le mur Ouest de cette case est bloqué
                tabOuestIndc = [i, i+1]
                tabOuest = [j, j]
                plt.plot(tabOuest, tabOuestIndc, coul) #Alors on trace un trait vertical à gauche de la case

    for i in range(1, len(chemin)): #On parcours toutes les cases de l'algorithme main droite
        if chemin[i] != False and chemin[i-1] != False: #S'il n'y a pas eu de retour à un noeud
            plt.plot([chemin[i-1][1]+0.5, chemin[i][1]+0.5], [chemin[i-1][0]+0.5, chemin[i][0]+0.5], 'r--') #On trace en trait qui va du centre de la case précédente au centre de la case suivante de couleur bleu

    for i in range(1, len(cheminGraphe)): #On parcours toutes les cases de l'algorithme utilisant les graphes
        plt.plot([cheminGraphe[i-1][1]+0.5, cheminGraphe[i][1]+0.5], [cheminGraphe[i-1][0]+0.5, cheminGraphe[i][0]+0.5], 'b--') #On trace en trait qui va du centre de la case précédente au centre de la case suivante de couleur bleu

    axis('equal') #On veut un repère orthonormé
    axis('off') #On enlève les axes pour mieux voir
    show() #On affiche la figure

def generation(lab):
    """""""""""""""""""""""""""""""""
    Cette fonction génère le labyrinthe
    """""""""""""""""""""""""""""""""
    tabGene = [[i*lab.getLongueur() + j for j in range(lab.getLongueur())] for i in range(lab.getLargeur())] #Création d'une matrice numérotés de 0 à longueur*largeur
    while not memeNombre(tabGene): #Tant que cette matrice est composé de plusieurs nombres
        valide = False
        while not valide: #tant que les variables randI, randJ et randCote ne correspondent pas
            valideCond = False

            randI = randint(0, lab.getLargeur()) #On choisit une ligne au hasard
            randJ = randint(0, lab.getLongueur()) #On choisit une colonne au hasard

            randI0 = randI == 0 #Est ce que randI vaut 0 ?
            randJ0 = randJ == 0 #Est ce que randJ vaut 0 ?
            randIMax = randI == lab.getLargeur()-1 #Est ce que randI vaut la largeur du labyrinthe ?
            randJMax =  randJ == lab.getLongueur()-1 #Est ce que randJ vaut la longueur du labyrinthe ?

            if randI0 and randJ0: #Si (randI, randJ) pointe vers la case en bas à gauche
                randCote = choice([0, 1]) #Alors les seuls cotés possibles sont le nord et l'est
            elif randI0 and randJMax: #Si (randI, randJ) pointe vers la case en bas à droite
                randCote = choice([0, 3]) #Alors les seuls cotés possibles sont le nord et l'ouest
            elif randIMax and randJ0: #Si (randI, randJ) pointe vers la case en haut à gauche
                randCote = choice([1, 2]) #Alors les seuls cotés possibles sont l'est' et le sud
            elif randIMax and randJMax: #Si (randI, randJ) pointe vers la case en haut à droite
                randCote = choice([2, 3]) #Alors les seuls cotés possibles sont le sud et l'ouest
            elif randI0: #Si la case si situe sur la bordure basse du labyrinthe
                randCote = choice([0, 1, 3]) #Alors les seuls cotés possibles sont le nord, l'est et l'ouest
            elif randIMax: #Si la case si situe sur la bordure haute du labyrinthe
                randCote = choice([1, 2, 3]) #Alors les seuls cotés possibles sont l'est, le sud et l'ouest
            elif randJ0: #Si la case si situe sur la bordure gauche du labyrinthe
                randCote = choice([0, 1, 2]) #Alors les seuls cotés possibles sont le nord et l'est et le sud
            elif randJMax: #Si la case si situe sur la bordure droite du labyrinthe
                randCote = choice([0, 2, 3]) #Alors les seuls cotés possibles sont le nord, le sud et l'ouest
            else: #Sinon, la case ne se situe pas en bordure
                randCote = randint(0, 3) #Donc on peux choisir n'importe quel coté
         

            if randCote==0: #Si on a choisi le coté nord
                if tabGene[randI][randJ]!=tabGene[randI+1][randJ]: #Si la case du dessus dans la matrice n'est pas la même valeur
                    valideCond = True
            elif randCote == 1: #Si on a choisi le coté est
                if tabGene[randI][randJ]!=tabGene[randI][randJ+1]: #Si la case à droite dans la matrice n'est pas la même valeur
                    valideCond = True
            elif randCote == 2: #Si on a choisi le coté sud
                if tabGene[randI][randJ]!=tabGene[randI-1][randJ]: #Si la case en dessous dans la matrice n'est pas la même valeur
                    valideCond = True
            elif randCote == 3: #Si on a choisi le coté ouest
                if tabGene[randI][randJ]!=tabGene[randI][randJ-1]: #Si la case à gauche dans la matrice n'est pas la même valeur
                    valideCond = True
            
            if valideCond and lab.getCase(randI, randJ).EstBloque(randCote): #Si les conditions précédentes sont remplies et que les deux cases ne sont pas déjà relié entre elles
                valide = True
                match randCote: #En fonction du coté choisi
                    case 0: tabGene = remplir(tabGene, tabGene[randI][randJ], tabGene[randI+1][randJ]) #On remplis toute les cases de la valeur de la case du dessus par la valeur de la case actuelle
                    case 1: tabGene = remplir(tabGene, tabGene[randI][randJ], tabGene[randI][randJ+1]) #On remplis toute les cases de la valeur de la case à droite par la valeur de la case actuelle
                    case 2: tabGene = remplir(tabGene, tabGene[randI][randJ], tabGene[randI-1][randJ]) #On remplis toute les cases de la valeur de la case du dessous par la valeur de la case actuelle
                    case 3: tabGene = remplir(tabGene, tabGene[randI][randJ], tabGene[randI][randJ-1]) #On remplis toute les cases de la valeur de la case à gauche par la valeur de la case actuelle
                lab.getCase(randI, randJ).setBloqueIndc(randCote, lab) #On peux supprimer le mur dans la direction choisie
            


def remplir(tabGene, intNouveau, intAncien):
    """""""""""""""""""""""""""""""""
    Cette fonction remplace toutes les occurences de intAncien par intNouveau
    """""""""""""""""""""""""""""""""
    for i in range(len(tabGene)):
        for j in range(len(tabGene[i])): #On parcours chaque case de la matrice
            if tabGene[i][j] == intAncien: #Si on trouve une valeur valant intAncien
                tabGene[i][j] = intNouveau #On la remplace par intNouveau
    return tabGene


def memeNombre(tabGene):
    """""""""""""""""""""""""""""""""
    Cette fonction vérifie si tout les nombres de la matrice sont les mêmes
    """""""""""""""""""""""""""""""""
    bool = True
    for i in range(len(tabGene)):
        for j in range(len(tabGene[i])): #On parcours chaque case de la matrice
            if tabGene[i][j] != tabGene[0][0]: #Si on trouve un nombre qui est différent
                bool = False #Alors on renvoie False
    return bool


def labyrinthe_to_graphe(lab):
    """""""""""""""""""""""""""""""""
    Cette fonction converti un labyrinthe en graphe
    """""""""""""""""""""""""""""""""
    dico = {} #Création du graphe représenté par un dictionnaire
    for i in range(lab.getLargeur()):
        for j in range(lab.getLongueur()): #Parcours de chaque case du labyrinthe
            Voisins = lab.getCase(i, j).getVoisin(lab) #On récupère tout les voisins accessibles de cette case
            res = []
            for k in Voisins:
                res.append((k.indices)) #On les ajoute dans res
            dico[tuple(([i, j]))] = res #Puis on ajoute res dans dico avec comme clé les coordonnées de la case et valeur ses voisins
    return dico


def dist_bfs(G, lab, s):
    """""""""""""""""""""""""""""""""
    Cette fonction renvoie la distance de chaque point au sommet
    """""""""""""""""""""""""""""""""
    dist = [[-1 for i in range(lab.getLongueur())] for x in range(lab.getLargeur())] #Initialisation d'une matrice avec comme distance -1 pour chaque points
    dist[s[0]][s[1]] = 0 #Le sommet est à une distance 0 de lui même
    grey=deque() #Création d'une file
    grey.append(s) #On ajoute le sommet à l'intérieur
    while len(grey)>0 and s!=[0, lab.getLongueur()-1]: #Tant que la file n'est pas vide et que la case actuelle n'est pas la sortie
        s=grey.popleft() #On récupère le premier élément de la file
        for v in G[tuple(s)]: #Pour chaque voisin de la case actuelle
            if dist[v[0]][v[1]]==-1: #On regarde si on a déjà traité cette case
                dist[v[0]][v[1]]=dist[s[0]][s[1]]+1 #Si non, sa distance est égale à la distance de la case Actuelle +1
                grey.append(v) #On l'ajoute à la fin dans la file
    return dist