# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 19:24:15 2017

@author: pstmr

Fonctions permettant de dessiner les ensembles de Julia et de Mandelbrot.
"""

import matplotlib.pyplot as plt

from fractale import Fractale
class EnsembleJuliaMandelbrot(Fractale):
    def __init__(self):
        self.min_x, self.max_x, self.min_y, self.max_y = 0, 0, 0, 0
        self.param = {"pas" : 0.002, "itérations" : 10,
                      "taux rouge" : 1, "taux vert" : 1, "taux bleu" : 1}
        
    def is_convergent(z0, C, iterations):
        """Boolean donnant la convergence ou non de la suite z(n+1) = z(n)² + C.
        La convergence est estimée pour module de z < 2 à la fin des itérations
        Retourne aussi la valeur de i pour laquelle le module de z dépasse 2.
        """
        z = z0.real + 1j*z0.imag
        
        for i in range(iterations):
            z = z*z + C
            if abs(z) >= 2:#Diverge ?
                return False, i
        return True, 0
    
    def next_point(self, z):
        """Donne le point suivant à tester à partir du point précédent.
        Parcourt le plan des complexes de gauche à droite et de bas en haut.
        Utilise les valeurs max_x/max_y/min_x afin de savoir quel est le plan parcouru.
        """
        x = z.real
        y = z.imag
        
        if x + self.param["pas"] > self.max_x:
            x = self.min_x
            if y + self.param["pas"] > self.max_y:
                return None
            y += self.param["pas"]
        else:
            x += self.param["pas"]
        
        return x + y*1j
    
    def tracer_fract(self, tab_complexes, dict_complexes):
        plt.axis('scaled')
        plt.axis([self.min_x, self.max_x, self.min_y, self.max_y])
        
        X = []
        Y = []
        for i in tab_complexes:#Récupère les parties réelle et imaginaire des nombre pour tracer X = f(Y)
            X.append(i.real)
            Y.append(i.imag)
        plt.plot(X, Y, '.',
                 color=(self.param["taux rouge"]*0, self.param["taux vert"]*0, self.param["taux bleu"]*0), markersize=0.9)
        
        for cle in dict_complexes.keys():#Pour chaque sous tableau, fais de même que pour le tableau principal
            X = []
            Y = []
            for i in dict_complexes[cle]:
                X.append(i.real)
                Y.append(i.imag)
            plt.plot(X, Y, '.',
                     color=(cle/self.param["itérations"]*self.param["taux rouge"], cle/self.param["itérations"]*self.param["taux vert"],
                            cle/self.param["itérations"]*self.param["taux bleu"]), markersize=0.9)
            #La couleur dépends de la valeur de l'itérée donc de la clé !
        plt.show()

class Mandelbrot(EnsembleJuliaMandelbrot):
    def __init__(self):
        EnsembleJuliaMandelbrot.__init__(self)
        self.min_x, self.max_x, self.min_y, self.max_y = -2.1, 0.6, -1.2, 1.2
    
    def mandelbrot(self):
        """Renvoi le tableau des complexes qui convergent pour une constante valant z0.
        Renvoi aussi un dictionnaire qui donne 'la vitesse de convergence' qui est
        le nombre d'itérées au moment où le module de z dépassait 2."""
        z0 = self.min_x + 1j*self.min_y
        
        non_conv = {}
        conv = []
    
        while z0 != None:
            is_conv, i = EnsembleJuliaMandelbrot.is_convergent(z0, z0, iterations=self.param["itérations"])
            if is_conv:
                conv.append(z0)
            else:
                try:
                    non_conv[i] += [z0]
                except KeyError:
                    non_conv[i] = [z0]
            
            z0 = EnsembleJuliaMandelbrot.next_point(self, z0)
        
        return conv, non_conv
        
    def launch(self):
        tab = self.mandelbrot()
        EnsembleJuliaMandelbrot.tracer_fract(self, tab[0], tab[1])
        
class Julia(EnsembleJuliaMandelbrot):
    def __init__(self):
        EnsembleJuliaMandelbrot.__init__(self)
        self.min_x, self.max_x, self.min_y, self.max_y = -1.5, 1.5, -1.5, 1.5
        self.param["C"] = 0.285 + 0.01j
        
    def julia(self, C=0.285 + 0.01j):
        """Renvoi le tableau des complexes qui convergent pour une constante valant C.
        Renvoi aussi un dictionnaire qui donne 'la vitesse de convergence' qui est
        le nombre d'itérées au moment où le module de z dépassait 2."""
        z0 = self.min_x + 1j*self.min_y
        
        non_conv = {}
        conv = []
    
        while z0 != None:
            is_conv, i = EnsembleJuliaMandelbrot.is_convergent(z0, C, iterations=self.param["itérations"])
            if is_conv:
                conv.append(z0)
            else:
                try:
                    non_conv[i] += [z0]
                except KeyError:#Cas où la clé n'a pas encore été définie et donc où la case mémoire n'est pas allouée
                    non_conv[i] = [z0]#Initialise la case avec une première valeur
            
            z0 = EnsembleJuliaMandelbrot.next_point(self, z0)
        
        return conv, non_conv
        
    def launch(self):
        tab = self.julia(C=self.param["C"])
        EnsembleJuliaMandelbrot.tracer_fract(self, tab[0], tab[1])
        
if __name__ == "__main__":
    Mandelbrot().launch()