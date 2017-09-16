# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 21:58:22 2017

@author: Alexandre
"""

############## FILE AKMC_test1.py
from time import time
a=time()
import module_site as mc
from random import randint

maille = [(0,0),(0.5,0.5)]
taille_sys = 25
systeme = []
proportion_b = 0.9
e_aa = 0
e_ab = 0
e_bb = 0.21

for i in range (taille_sys) :
    for j in range (taille_sys):
        for k in maille :
            systeme.append(mc.Site((i+k[0],j+k[1])))

nombre_b = int(len(systeme)*proportion_b)
while nombre_b > 0 :
    n = randint(0,len(systeme)-1) # tirage d'un site au hasard
    if not systeme[n].get_identite() : #
        nombre_b -= 1
        systeme[n].set_identite(True)
        
for i in systeme:
    i.set_voisin(systeme=systeme,taille=taille_sys,e_aa=e_aa,e_ab=e_ab,e_bb=e_bb)
file= open("coordonnee.txt","w")
file.writelines(str(len(systeme))+"\n")
file.writelines("\n")
for i in systeme :
    file.writelines("{} {:3.1f} {:3.1f} 0 \n".format(i.get_identite(), *i.get_coordonnees() ) )
print (time()-a)