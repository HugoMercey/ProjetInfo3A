from Case import *

class Labyrinthe:
    def __init__(self, longueur, largeur):
        
        self.setTaille(longueur, largeur)
        self.setLabyrinthe()


    def setTaille(self, longueur, largeur): #Définis la largeur et la longueur du labyrinthe
        self.tab = []
        self.longueur = longueur
        self.largeur = largeur
    
    def setLabyrinthe(self): #Initialise le labyrinthe par une grille
        for i in range(self.largeur):
            temp = []
            for j in range(self.longueur):
                temp.append(Case([i, j], self))
            self.tab.append(temp)
        self.setEntree()
        self.setSortie()

    def getCase(self, i, j): #Renvoie la case aux coordonées (i, j)
        return self.tab[i][j]

    def getLongueur(self):
        return self.longueur
    def getLargeur(self):
        return self.largeur

    def setEntree(self): #Définis l'entrée du labyrinthe
        self.tab[self.largeur-1][0].setEntree();
    def setSortie(self): #Définis la sortie du labyrinthe
        self.tab[0][self.longueur-1].setSortie();
        

    def toString(self):
        for i in self.tab:
            for j in i:
                print(j.getIndice(), j.getMurBloque())