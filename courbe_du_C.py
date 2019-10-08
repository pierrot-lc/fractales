# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 02:23:56 2017

@author: pstmr
Trace la courbe du C.
Pour cela, il faut mémoriser les points dans un tableau et déduire les points suivants.
Un point suivant s'insère entre deux points déjà calculés.
Il est déterminé de façon à avoir une rotation de (+/-) pi/4 par rapport à la droite passant par les deux points,
de façon a avoir un triangle équilatéral entre les points initiaux et le nouveau point.
Le signe dépends de la fonction var_i().
"""

import matplotlib.pyplot as plt
from math import cos, sin
from cmath import phase

from fractale import Fractale

class CourbeC(Fractale):
    def __init__(self):
        self.tab = [0+0j, 5+0j]
        self.param = {"itérations" : 15, "l" : 1}
    
    def next_step(tab, l=2):
        """Parcourt les couples (tab[i], tab[i+1]) et déduit le point à placer entre les deux.
        La fonction var_i est utilisée afin de créer une alternation de signe entre plusieurs points calculés.
        Permet de faire des variantes de la courbe du C en fonction de la valeur de k.
        La courbe du C originale se fait pour l=1."""
        new_tab = [tab[0]]
        z1, z2 = tab[0], tab[1]
        d = abs(z2 - z1)
        
        for i in range(len(tab) - 1):
            z1 = tab[i]
            z2 = tab[i + 1]
            arg = phase(z2 - z1)
            
            z3 = 0.5*d*(1 + CourbeC.var_i(i, k=l)*1j)*(cos(arg) + 1j*sin(arg)) + z1#Formule permettant d'avoir le nouveau point
            
            new_tab.append(z3)
            new_tab.append(z2)
            
        return new_tab
        
    def var_i(i, k=1):
        """Permet de changer le signe tout les k-éléments."""
        if i%k == 0:
            return 1
        else:
            return -1
    
    def draw_figure(points, point_size=1):
        """Trace les points en les plottants."""
        X, Y = [], []
        for i in range(len(points)):
            X.append(points[i].real)
            Y.append(points[i].imag)
        plt.plot(X, Y ,'blue', markersize=point_size)
        plt.axis("equal")
        plt.show()

    def launch(self):
        self.tab = [0+0j, 5+0j]#Réinitialise le tableau au cas où il est déjà rempli
        for i in range(self.param["itérations"]):
            self.tab = CourbeC.next_step(self.tab, l=self.param["l"])
        CourbeC.draw_figure(self.tab)
        
if __name__ == "__main__":
    c = CourbeC()
    c.launch()