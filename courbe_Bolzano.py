# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 20:21:48 2017

@author: pstmr
Trace la courbe de Bolzano : une courbe continue mais nulle part dérivable.
"""

import numpy as np
import matplotlib.pyplot as plt

from fractale import Fractale

class CourbeBolzanno(Fractale):
    def __init__(self):
        self.param = {"itérations" : 8}

    def f(xi, xf, n):
        """Fonction récursive."""
        x1 = xi + (xf - xi)/3
        x2 = xi + (xf - xi)*2/3
        
        if n == 0:
            return [xi]#Ajoute le premier point (donc le dernier n'est pas pris en compte)
        
        return CourbeBolzanno.f(xi, x2, n-1) + CourbeBolzanno.f(x2, x1, n-1) + CourbeBolzanno.f(x1, xf, n-1)
        
    def tracer_f(n):
        Y = CourbeBolzanno.f(0, 1, n) + [1]#Ajoute le dernier point
        X = np.linspace(0, 1, len(Y))
        plt.plot(X, Y)
        plt.show()
	
    def launch(self):
        CourbeBolzanno.tracer_f(self.param["itérations"])

if __name__ == "__main__":
    c = CourbeBolzanno()
    c.launch()