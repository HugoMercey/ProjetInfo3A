from Labyrinthe import *
from Case import *


def mainDroite(lab):
    """""""""""""""""""""""""""""""""
    Cette fonction résoud le labyrinthe en utilisant l'algorithme de la main droite
    """""""""""""""""""""""""""""""""
    caseActuelleIndc = (lab.getLargeur()-1, 0) #On récupère les coordonées de la case de départ
    caseActuelle = lab.getCase(caseActuelleIndc[0], caseActuelleIndc[1]) #On récupère l'objet case avec ces coordonnées
    direction = "est" #On initialise la variable directio à "est" car c'est la seule direction disponible
    chemin = [] #Création de la liste qui va retracer le chemin
    chemin.append(([lab.getLargeur()-1, -1], "est")) #Ajout de la case (lab.getLargeur()-1, -1) et "est" à la variable
    cheminVisu = [] #Création de la liste qui va servir à afficher le chemin
    cheminVisu.append([lab.getLargeur()-1, -1]) #Ajout de la case (lab.getLargeur()-1, -1) et à la variable
    listeNoeuds = [] #Créations de la liste qui va répertorier les noeuds par lesquelles ont est passé
    listeNoeuds.append([caseActuelle.indices, "est"]) #Ajout de la case de départ dans cette liste

    while caseActuelleIndc != [0, lab.getLongueur()-1]: #Tant que la case actuelle n'est pas la case d'arrivée
        if caseActuelle.indices != chemin[-1][0]: #On regarde si la case actuelle n'est pas le dernier noeud sur lequelle on est passé
            chemin.append([caseActuelle.indices, direction]) #On ajoute notre case avec sa direction dans le chemin
            cheminVisu.append(caseActuelle.indices)
        else: #Sinon
            if len(listeNoeuds)>2: #Si la liste de noeuds contient strictement plus de deux noeuds
                caseActuelle = lab.getCase(listeNoeuds[-1][0][0], listeNoeuds.pop()[0][1]) #On retourne au dernier noeud et on le supprime de la liste
            else: #Sinon
                caseActuelle = lab.getCase(listeNoeuds[-1][0][0], listeNoeuds[-1][0][1]) #On retourne juste au dernier noeud sans le supprimer de la liste


        if caseActuelle.getNbMurBloque() < 2 and [caseActuelle.indices] != listeNoeuds[-1][0][0] and not caseActuelle.getVisite(): #Si cette case est un noeud (compte plus de deux cases voisines), qui n'est pas le dernier noeud qu'on a visité, et qu'on a jamais visité cette case
            listeNoeuds.append([caseActuelleIndc, direction]) #On peux l'ajouter dans la liste de noeuds

        caseActuelle.setVisite(True) #On peux dire qu'on est déjà passer sur cette case

        if direction == "nord": #Si on est dirigé vers le nord
            direction, caseActuelleIndc = directionNord(lab, caseActuelle, listeNoeuds, cheminVisu) #La nouvelle direction et case suivante dépend des murs et cases alentours
        elif direction == "est": #Si on est dirigé vers l'est
            direction, caseActuelleIndc = directionEst(lab, caseActuelle, listeNoeuds, cheminVisu) #La nouvelle direction et case suivante dépend des murs et cases alentours
        elif direction == "sud": #Si on est dirigé vers le sud
            direction, caseActuelleIndc = directionSud(lab, caseActuelle, listeNoeuds, cheminVisu) #La nouvelle direction et case suivante dépend des murs et cases alentours
        elif direction == "ouest": #Si on est dirigé vers le ouest
            direction, caseActuelleIndc = directionOuest(lab, caseActuelle, listeNoeuds, cheminVisu) #La nouvelle direction et case suivante dépend des murs et cases alentours

        caseActuelle = lab.getCase(caseActuelleIndc[0], caseActuelleIndc[1]) #On actualise notre nouvelle case actuelle
        
    chemin.append((caseActuelle.indices, direction)) #On peux ajouter la case de sortie au chemin
    cheminVisu.append(caseActuelle.indices)
    return chemin, cheminVisu #On peux renvoyer les deux variables chemin


def directionNord(lab, caseActuelle, listeNoeuds, cheminVisu): #Si on est dirigé vers le nord
    """""""""""""""""""""""""""""""""
    Cette fonction renvoie la prochaine case ainsi que la nouvelle direction en fonction de l'ancienne direction
    """""""""""""""""""""""""""""""""
    caseActuelleIndc = caseActuelle.indices
    if caseActuelle.indices[1] < lab.getLongueur()-1 and (not caseActuelle.EstEstBloque()) and not caseActuelle.getEst(lab).getVisite(): #Si on ne se situe pas sur la bordure droite du labyrinthe et que le mur à l'est n'est pas bloqué et qu'on a pas déjà visité la case à l'est
        caseActuelleIndc = [caseActuelleIndc[0], caseActuelleIndc[1]+1] #On peut donc se déplacer d'une case vers la droite
        direction = "est" #Notre direction est maintenant vers l'est
    elif caseActuelle.indices[0]<lab.getLargeur()-1 and (not caseActuelle.NordEstBloque()) and not caseActuelle.getNord(lab).getVisite(): #Si on ne se situe pas sur la bordure haute du labyrinthe et que le mur au nord n'est pas bloqué et qu'on a pas déjà visité la case au nord
        caseActuelleIndc = [caseActuelleIndc[0]+1, caseActuelleIndc[1]] #On peut donc se déplacer d'une case vers le haut
        direction = "nord" #Notre direction est maintenant vers le nord
    elif caseActuelle.indices[1] > 0 and (not caseActuelle.OuestEstBloque()) and not caseActuelle.getOuest(lab).getVisite(): #Si on ne se situe pas sur la bordure gauche du labyrinthe et que le mur à l'ouest n'est pas bloqué et qu'on a pas déjà visité la case à l'ouest
        caseActuelleIndc = [caseActuelleIndc[0], caseActuelleIndc[1]-1] #On peut donc se déplacer d'une case vers la gauche
        direction = "ouest" #Notre direction est maintenant vers l'ouest
    else: #Sinon, on est dans une impasse
        caseActuelleIndc = listeNoeuds[-1][0] #On retourne donc au dernier noeud rencontré
        if len(listeNoeuds)>2 and caseActuelle.getVisiteBloque(lab): #Si notre chemin comporte strictement plus de deux noeuds et que toute les cases voisines sont inaccessibles (visitées ou bloquées)
            direction = listeNoeuds.pop()[1] #On récupère la direction de ce dernier noeur et on le supprime de la liste
        else: #Sinon
            direction = listeNoeuds[-1][1] #On récupère simplement la direction
        cheminVisu.append(False) #On ajoute False à chemin visu pour signifier pendant l'affichage qu'il y a eu un retour en arrière sur le chemin
    return direction, caseActuelleIndc


def directionEst(lab, caseActuelle, listeNoeuds, cheminVisu): #Si on est dirigé vers l'est
    """""""""""""""""""""""""""""""""
    Cette fonction renvoie la prochaine case ainsi que la nouvelle direction en fonction de l'ancienne direction
    """""""""""""""""""""""""""""""""
    caseActuelleIndc = caseActuelle.indices
    if caseActuelle.indices[0] > 0 and (not caseActuelle.SudEstBloque()) and not caseActuelle.getSud(lab).getVisite():#Si on ne se situe pas sur la bordure basse du labyrinthe et que le mur au sud n'est pas bloqué et qu'on a pas déjà visité la case au sud
        caseActuelleIndc = [caseActuelleIndc[0]-1, caseActuelleIndc[1]] #On peut donc se déplacer d'une case vers le bas
        direction = "sud" #Notre direction est maintenant vers le sud
    elif caseActuelle.indices[1] < lab.getLongueur()-1 and (not caseActuelle.EstEstBloque()) and not caseActuelle.getEst(lab).getVisite():#Si on ne se situe pas sur la bordure droite du labyrinthe et que le mur à l'est n'est pas bloqué et qu'on a pas déjà visité la case à l'est
        caseActuelleIndc = [caseActuelleIndc[0], caseActuelleIndc[1]+1] #On peut donc se déplacer d'une case vers la droite
        direction = "est" #Notre direction est maintenant vers l'est
    elif caseActuelle.indices[0]<lab.getLargeur()-1 and (not caseActuelle.NordEstBloque()) and not caseActuelle.getNord(lab).getVisite():#Si on ne se situe pas sur la bordure haute du labyrinthe et que le mur au nord n'est pas bloqué et qu'on a pas déjà visité la case au nord
        caseActuelleIndc = [caseActuelleIndc[0]+1, caseActuelleIndc[1]] #On peut donc se déplacer d'une case vers le haut
        direction = "nord" #Notre direction est maintenant vers le nord
    else: #Sinon, on est dans une impasse
        caseActuelleIndc = listeNoeuds[-1][0] #On retourne donc au dernier noeud rencontré
        if len(listeNoeuds)>2 and caseActuelle.getVisiteBloque(lab): #Si notre chemin comporte strictement plus de deux noeuds et que toute les cases voisines sont inaccessibles (visitées ou bloquées)
            direction = listeNoeuds.pop()[1] #On récupère la direction de ce dernier noeur et on le supprime de la liste
        else: #Sinon
            direction = listeNoeuds[-1][1] #On récupère simplement la direction
        cheminVisu.append(False) #On ajoute False à chemin visu pour signifier pendant l'affichage qu'il y a eu un retour en arrière sur le chemin
    return direction, caseActuelleIndc


def directionSud(lab, caseActuelle, listeNoeuds, cheminVisu): #Si on est dirigé vers le sud
    """""""""""""""""""""""""""""""""
    Cette fonction renvoie la prochaine case ainsi que la nouvelle direction en fonction de l'ancienne direction
    """""""""""""""""""""""""""""""""
    caseActuelleIndc = caseActuelle.indices
    if caseActuelle.indices[1] > 0 and (not caseActuelle.OuestEstBloque()) and not caseActuelle.getOuest(lab).getVisite():#Si on ne se situe pas sur la bordure gauche du labyrinthe et que le mur à l'ouest n'est pas bloqué et qu'on a pas déjà visité la case à l'ouest
        caseActuelleIndc = [caseActuelleIndc[0], caseActuelleIndc[1]-1] #On peut donc se déplacer d'une case vers la gauche
        direction = "ouest" #Notre direction est maintenant vers l'ouest
    elif caseActuelle.indices[0] > 0 and (not caseActuelle.SudEstBloque()) and not caseActuelle.getSud(lab).getVisite():#Si on ne se situe pas sur la bordure basse du labyrinthe et que le mur au sud n'est pas bloqué et qu'on a pas déjà visité la case au sud
        caseActuelleIndc = [caseActuelleIndc[0]-1, caseActuelleIndc[1]] #On peut donc se déplacer d'une case vers le bas
        direction = "sud" #Notre direction est maintenant vers le sud
    elif caseActuelle.indices[1] < lab.getLongueur()-1 and (not caseActuelle.EstEstBloque()) and not caseActuelle.getEst(lab).getVisite():#Si on ne se situe pas sur la bordure droite du labyrinthe et que le mur à l'est n'est pas bloqué et qu'on a pas déjà visité la case à l'est
        caseActuelleIndc = [caseActuelleIndc[0], caseActuelleIndc[1]+1] #On peut donc se déplacer d'une case vers la droite
        direction = "est" #Notre direction est maintenant vers l'est
    else: #Sinon, on est dans une impasse
        caseActuelleIndc = listeNoeuds[-1][0] #On retourne donc au dernier noeud rencontré
        if len(listeNoeuds)>2 and caseActuelle.getVisiteBloque(lab): #Si notre chemin comporte strictement plus de deux noeuds et que toute les cases voisines sont inaccessibles (visitées ou bloquées)
            direction = listeNoeuds.pop()[1] #On récupère la direction de ce dernier noeur et on le supprime de la liste
        else: #Sinon
            direction = listeNoeuds[-1][1] #On récupère simplement la direction
        cheminVisu.append(False) #On ajoute False à chemin visu pour signifier pendant l'affichage qu'il y a eu un retour en arrière sur le chemin
    return direction, caseActuelleIndc
    

def directionOuest(lab, caseActuelle, listeNoeuds, cheminVisu): #Si on est dirigé vers l'ouest
    """""""""""""""""""""""""""""""""
    Cette fonction renvoie la prochaine case ainsi que la nouvelle direction en fonction de l'ancienne direction
    """""""""""""""""""""""""""""""""
    caseActuelleIndc = caseActuelle.indices
    if caseActuelle.indices[0] < lab.getLargeur()-1 and (not caseActuelle.NordEstBloque()) and not caseActuelle.getNord(lab).getVisite():#Si on ne se situe pas sur la bordure haute du labyrinthe et que le mur au nord n'est pas bloqué et qu'on a pas déjà visité la case au nord
        caseActuelleIndc = [caseActuelleIndc[0]+1, caseActuelleIndc[1]] #On peut donc se déplacer d'une case vers le haut
        direction = "nord" #Notre direction est maintenant vers le nord
    elif caseActuelle.indices[1] > 0 and (not caseActuelle.OuestEstBloque()) and not caseActuelle.getOuest(lab).getVisite():#Si on ne se situe pas sur la bordure gauche du labyrinthe et que le mur à l'ouest n'est pas bloqué et qu'on a pas déjà visité la case à l'ouest
        caseActuelleIndc = [caseActuelleIndc[0], caseActuelleIndc[1]-1] #On peut donc se déplacer d'une case vers la gauche
        direction = "ouest" #Notre direction est maintenant vers l'ouest
    elif caseActuelle.indices[0] > 0 and (not caseActuelle.SudEstBloque()) and not caseActuelle.getSud(lab).getVisite():#Si on ne se situe pas sur la bordure basse du labyrinthe et que le mur au sud n'est pas bloqué et qu'on a pas déjà visité la case au sud
        caseActuelleIndc = [caseActuelleIndc[0]-1, caseActuelleIndc[1]] #On peut donc se déplacer d'une case vers le bas
        direction = "sud" #Notre direction est maintenant vers le sud
    else: #Sinon, on est dans une impasse
        caseActuelleIndc = listeNoeuds[-1][0] #On retourne donc au dernier noeud rencontré
        if len(listeNoeuds)>2 and caseActuelle.getVisiteBloque(lab): #Si notre chemin comporte strictement plus de deux noeuds et que toute les cases voisines sont inaccessibles (visitées ou bloquées)
            direction = listeNoeuds.pop()[1] #On récupère la direction de ce dernier noeur et on le supprime de la liste
        else: #Sinon
            direction = listeNoeuds[-1][1] #On récupère simplement la direction
        cheminVisu.append(False) #On ajoute False à chemin visu pour signifier pendant l'affichage qu'il y a eu un retour en arrière sur le chemin
    return direction, caseActuelleIndc



def grapheResolv(tab, lab):
    """""""""""""""""""""""""""""""""
    Cette fonction résoud le labyrinthe en utilisant l'algorithme des graphes
    """""""""""""""""""""""""""""""""
    caseI = 0
    caseJ = len(tab[0])-1 #On défini la case de départ par les indices (0, longueur-1)
    chemin = [] #Création de la liste qui va retracer le chemin
    chemin.append((caseI, caseJ)) #On ajoute ces indices dans la liste
    while caseI != lab.getLargeur()-1 or caseJ != 0: #Tant que la case actuelle n'est pas la case d'arrivée
        score = tab[caseI][caseJ] #On récupère la distance de la case actuelle
        if caseI>0 and score == tab[caseI-1][caseJ]+1 and not lab.getCase(caseI, caseJ).SudEstBloque(): #Si on ne se situe pas sur la bordure basse du labyrinthe et que notre distance équivaut à la distance de la case en dessous -1 et qu'aucun mur nous sépare
            caseI -= 1 #On déplace notre case actuelle vers le bas
            chemin.append((caseI, caseJ)) #On ajoute cette nouvelle case dans le chemin
        elif caseJ>0 and score == tab[caseI][caseJ-1]+1 and not lab.getCase(caseI, caseJ).OuestEstBloque(): #Si on ne se situe pas sur la bordure gauche du labyrinthe et que notre distance équivaut à la distance de la case à gauche -1 et qu'aucun mur nous sépare
            caseJ -= 1 #On déplace notre case actuelle vers la gauche
            chemin.append((caseI, caseJ)) #On ajoute cette nouvelle case dans le chemin
        elif caseI<len(tab)-1 and score == tab[caseI+1][caseJ]+1 and not lab.getCase(caseI, caseJ).NordEstBloque(): #Si on ne se situe pas sur la bordure haute du labyrinthe et que notre distance équivaut à la distance de la case au dessus -1 et qu'aucun mur nous sépare
            caseI += 1 #On déplace notre case actuelle vers le haut
            chemin.append((caseI, caseJ)) #On ajoute cette nouvelle case dans le chemin
        elif caseJ<len(tab[0])-1 and score == tab[caseI][caseJ+1]+1 and not lab.getCase(caseI, caseJ).EstEstBloque(): #Si on ne se situe pas sur la bordure droite du labyrinthe et que notre distance équivaut à la distance de la case en à droite -1 et qu'aucun mur nous sépare
            caseJ += 1 #On déplace notre case actuelle vers la droite
            chemin.append((caseI, caseJ)) #On ajoute cette nouvelle case dans le chemin

    chemin.append((lab.getLargeur()-1, -1)) #On ajoute la première case dans le chemin
    chemin.reverse() #On retourne la liste chemin pour partir de la case de départ jusqu'à la case d'arrivée
    return chemin
