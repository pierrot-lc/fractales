# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 16:33:25 2017

@author: pstmr
Trace le flocon de Koch.
De la même manière que la courbe du C : déduit les points suivant des points précédents à partir d'une CI.
Les points sont déterminés grâce à des calculs complexes.
"""

import matplotlib.pyplot as plt
from math import cos, sin, sqrt, acos
from cmath import phase

from fractale import Fractale

class Koch(Fractale):
    def __init__(self):
        self.init_points()
        self.param = {"itérations" : 5, "dénominateur" : 3}
        

    def init_points(self):
        za = 0 + 0j
        zb = 5 + 0j
        zc = 2.5 + 2.5j*sqrt(3)
        self.points = [zb, za, zc, zb]
        #self.points = [za, zb, zc, za]#Autre fractale
        
    def next_step(tab, denom=3):
        """Parcourt les couples (tab[i], tab[i+1]) et déduit les points à placer entre les deux.
        Il est possible de faire varier le dénominateur, c'est-à-dire la distance a."""
        new_tab = [tab[0]]
        z1, z2 = tab[0], tab[1]
        a = abs(z2 - z1)/denom
        teta = acos((denom - 2)*0.5)#teta dépends de la distance a (donc de denom après simplifications)
        
        for i in range(len(tab) - 1):
            z1 = tab[i]
            z2 = tab[i + 1]
            arg = phase(z2 - z1)
            
            z1prime = z1 + a*(cos(arg) +1j*sin(arg))
            z3 = z1prime + a*(cos(teta+arg) + 1j*sin(teta+arg))
            z2prime = z1prime + a*(denom-2)*(cos(arg) + 1j*sin(arg))
            
            new_tab.append(z1prime)
            new_tab.append(z3)
            new_tab.append(z2prime)
            new_tab.append(z2)
            
        return new_tab
    
    def draw_figure(points, point_size=1):
        """Trace les points en les plottants."""
        X, Y = [], []
        for i in points:
            X.append(i.real)
            Y.append(i.imag)
        plt.plot(X, Y , color=(0, 0, 0), markersize=point_size)
        plt.axis("equal")
        plt.show()
        
    def launch(self):
        self.init_points()#Réinitialise le tableau au cas où il est déjà rempli
        for i in range(self.param["itérations"]):
            self.points = Koch.next_step(self.points, denom=self.param["dénominateur"])
        Koch.draw_figure(self.points)
    
if __name__ == "__main__":
    fract = Koch()
    fract.launch()