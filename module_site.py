# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 21:40:39 2017

@author: Alexandre
"""

############## FILE AKMC_func.py
class Site:
    """Un site du systeme"""
    def __init__(self, coordonnees: tuple):
        self.__coordonnees = coordonnees # species that the component belong to
        self.__identite = False # component index
        self.__voisin = []
        self.__energie = None
        
    def get_identite(self):
        return self.__identite
        
    def get_coordonnees(self):
        return self.__coordonnees
        
    def set_identite(self, identite: bool):
        self.__identite = identite
        
    def set_energie (self, e_aa, e_ab, e_bb) :
        self.__energie = 0
        if self.__identite:
            for i in self.__voisin :
                if i.get_identite() :
                    self.__energie += e_bb
                else :
                    self.__energie += e_ab
        else:
            for i in self.__voisin :
                if i.get_identite() :
                    self.__energie += e_ab
                else :
                    self.__energie += e_aa
                    self.__energie*=0.5
            
    def set_voisin (self, systeme, taille,e_aa,e_ab,e_bb) :
        for i in systeme :
            if pbc (self, i, taille) == [0.5,0.5]:
                self.__voisin.append(i)
        if len(self.__voisin)!=4:
            print("probleme de nombre de voisin")
        else :
            self.set_energie(e_aa,e_ab,e_bb)
            
def pbc (a, b, taille) :
    c=[0,0]
    for i in range(2):
        c[i]=min([abs(a.get_coordonnees()[i]-b.get_coordonnees()[i]),
        abs(a.get_coordonnees()[i] -b.get_coordonnees()[i]-taille),
        abs(a.get_coordonnees()[i] - b.get_coordonnees()[i]+taille)])
    return c