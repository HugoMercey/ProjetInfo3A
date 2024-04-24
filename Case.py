from Labyrinthe import *

class Case:
    def __init__(self, indices, lab, Nord = True, Est = True, Sud = True, Ouest = True, Bloque = []):
        
        self.setIndices(indices)
        self.Init = False

        if Bloque == []:
            self.setNord(Nord, lab)
            self.setEst(Est, lab)
            self.setSud(Sud, lab)
            self.setOuest(Ouest, lab)
        else:
            self.setBloque(Bloque)
        self.setVisite(False)
        self.Init = True


    def NordEstBloque(self): #renvoie True si le mur nord est bloqué
        return self.Nord
    def EstEstBloque(self): #renvoie True si le mur est est bloqué
        return self.Est
    def SudEstBloque(self): #renvoie True si le mur sud est bloqué
        return self.Sud
    def OuestEstBloque(self): #renvoie True si le mur ouest est bloqué
        return self.Ouest
    
    def EstBloque(self, indc): #renvoie True ou False en fonction de l'indice et de la valeur du mur
        if indc == 0: #Si on veut savoir si le nord est bloqué
            return self.NordEstBloque()
        elif indc == 1: #Si on veut savoir si l'est est bloqué
            return self.EstEstBloque()
        elif indc == 2: #Si on veut savoir si le sud est bloqué
            return self.SudEstBloque()
        elif indc == 3: #Si on veut savoir si l'ouest est bloqué
            return self.OuestEstBloque()

    def setVisite(self, visite):
        self.visite = visite

    def setIndices(self, indices):
        self.indices = indices


    def setNord(self, Nord, lab, cpt = 0): #Cette fonction modifie le coté nord de soi-même mais aussi le coté sud de la case au dessus d'elle
        self.Nord = Nord
        if self.indices[0] != lab.getLargeur()-1 and cpt <= 1 and self.Init == True:
            lab.getCase(self.indices[0]+1, self.indices[1]).setSud(Nord, lab, cpt+1)

    def setEst(self, Est, lab, cpt = 0): #Cette fonction modifie le coté est de soi-même mais aussi le coté ouest de la case à droite d'elle
        self.Est = Est
        if self.indices[1] != lab.getLongueur()-1 and cpt <= 1 and self.Init == True:
            lab.getCase(self.indices[0], self.indices[1]+1).setOuest(Est, lab, cpt+1)

    def setSud(self, Sud, lab, cpt = 0): #Cette fonction modifie le coté sud de soi-même mais aussi le coté nord de la case en dessous d'elle
        self.Sud = Sud
        if self.indices[0] != 0 and cpt <= 1 and self.Init == True:
            lab.getCase(self.indices[0]-1, self.indices[1]).setNord(Sud, lab, cpt+1)

    def setOuest(self, Ouest, lab, cpt = 0): #Cette fonction modifie le coté ouest de soi-même mais aussi le coté est de la case à gauche d'elle
        self.Ouest = Ouest
        if self.indices[1] != 0 and cpt <= 1 and self.Init == True:
            lab.getCase(self.indices[0], self.indices[1]-1).setEst(Ouest, lab, cpt+1)

    def setBloque(self, Bloque, lab): #Bloque ou débloque des murs en fonction d'une liste de booléens
        self.setNord(Bloque[0], lab)
        self.setEst(Bloque[1], lab)
        self.setSud(Bloque[2], lab)
        self.setOuest(Bloque[3], lab)
    
    def setBloqueIndc(self, indc, lab): #Débloque des murs en fonction de l'indice donnée
        if indc == 0:
            self.setNord(False, lab)
        elif indc == 1:
            self.setEst(False, lab)
        elif indc == 2:
            self.setSud(False, lab)
        elif indc == 3:
            self.setOuest(False, lab)

    def setEntree(self):
        self.Ouest = False;
    def setSortie(self):
        self.Est = False;

    
    def getVisite(self):
        return self.visite

    def getMurBloque(self): #Renvoie une liste de booléens avec les valeurs des murs bloqués ou non
        res = []
        res.append(self.NordEstBloque())
        res.append(self.EstEstBloque())
        res.append(self.SudEstBloque())
        res.append(self.OuestEstBloque())
        return res

    def getCaseIndc(self, indc, lab): #Renvoie une case en fonction de l'indice choisi
        if indc == 0: #Si on choisi le nord
            return self.getNord(lab)
        elif indc == 1: #Si on choisi l'est
            return self.getEst(lab)
        elif indc == 2: #Si on choisi le sud
            return self.getSud(lab)
        elif indc == 3: #Si on choisi l'ouest
            return self.getOuest(lab)

    
    def getNbMurBloque(self): #Renvoie le nombre de mur bloqués
        temp = self.getMurBloque()
        res = 0
        for i in range(4):
            if temp[i]:
                res+=1
        return res
        
    def getNord(self, lab): #Renvoie la case au nord de celle là
        if self.indices[0] < lab.getLargeur()-1:
            return lab.getCase(self.indices[0]+1, self.indices[1])
        else:
            return self

    def getEst(self, lab): #Renvoie la case à l'est de celle là
        if self.indices[1] < lab.getLongueur()-1:
            return lab.getCase(self.indices[0], self.indices[1]+1)
        else:
            return self

    def getSud(self, lab): #Renvoie la case au sud de celle là
        if self.indices[0] > 0:
            return lab.getCase(self.indices[0]-1, self.indices[1])
        else:
            return self

    def getOuest(self, lab): #Renvoie la case à l'ouest de celle là
        if self.indices[1] > 0:
            return lab.getCase(self.indices[0], self.indices[1]-1)
        else:
            return self

    def getIndice(self):
        return self.indices

    def getVisiteBloque(self, lab): #Renvoie True si aucune case aux alentours n'est accessible car bloquées ou déjà visitées
        res = True
        if not self.getNord(lab).getVisite() or not self.NordEstBloque():
            res = False
        if not self.getEst(lab).getVisite() or not self.EstEstBloque():
            res = False
        if not self.getSud(lab).getVisite() or not self.SudEstBloque():
            res = False
        if not self.getOuest(lab).getVisite() or not self.OuestEstBloque():
            res = False
        return res

    def toString(self):
        return (str(self.getIndice()) + "," +str(self.getMurBloque()))

    def getVoisin(self, lab): #Renvoie une liste des voisins de cette case qui ne sont pas bloqués par un mur
        res = []
        if self.indices[0]<lab.getLargeur()-1 and not self.NordEstBloque():
            res.append(self.getNord(lab))
        if self.indices[1]<lab.getLongueur()-1 and not self.EstEstBloque():
            res.append(self.getEst(lab))
        if self.indices[0]>0 and not self.SudEstBloque():
            res.append(self.getSud(lab))
        if self.indices[1]>0 and not self.OuestEstBloque():
            res.append(self.getOuest(lab))
        return res