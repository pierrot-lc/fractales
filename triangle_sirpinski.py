# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 14:36:39 2017

@author: pstmr

Dessine des fractales en utilisant une méthode vue sur youtube.
Le principe est d'avoir des points fixes et de dessiner des points petits à petits en choississant au
hasard un des points fixes. On trace alors un nouveau point entre le point précédent et le point fixe
choisi.

Pour le triangle, on reconnait le triangle de Sirpinski !

"""

import random
import matplotlib.pyplot as plt
import math

from fractale import Fractale

class Sirpinski(Fractale):
    def __init__(self):
        self.fix_points, self.first_point = Sirpinski.triangle()        
        self.param = {"points fixes" : 3, "points à calculer" : 3e5,
                      "dénominateur" : 2}
        
    """Toutes ces premières fonctions ont pour but de donner les conditions initiales."""
    def triangle():
        A = [0, 0]
        B = [100, 0]
        C = [50, 50]
        fix_points = [A, B, C]
    
        first_point = [25, 25]
    
        return fix_points, first_point
    
    def polygone(k=4):
        """k donne le nombre de côtés du polygone.
        Un k élevé fait tendre le polygone vers le cercle."""
        fix_points = []
        first_point = [25, 25]
        
        for i in range(k):
            x = 50 * (1 + math.cos(2*i*math.pi / k))
            y = 50 * (1 + math.sin(2*i*math.pi / k))
            fix_points.append((x, y))
            
        return fix_points, first_point
        
    def test():
        A = [0, 0]
        B = [100, 0]
        C = [25, 50]
        D = [75, 50]
        E = [50, 25]
        fix_points = [A, B, C, D, E]
    
        first_point = [25, 25]
    
        return fix_points, first_point
    
    def new_point(actual_point, fix_points, denominateur=2):
        """Retourne la position du nouveau point à tracer. La variable dénominateur permet
        de décider la position entre le point fixe et le point précédent du nouveau point."""
        choosed_point = random.randint(0, len(fix_points) - 1)
    
        choosed_point = fix_points[choosed_point]
        next_point_x = (choosed_point[0] + actual_point[0]) / denominateur
        next_point_y = (choosed_point[1] + actual_point[1]) / denominateur
                        
        return (next_point_x, next_point_y)
        
    def new_point_gauss(actual_point, fix_points, denominateur=2):
        """Même fonction que la précédente mais en prenant des fonctions aléatoires gaussiennes.
        Ceci permet de selectionner plus souvent des points fixes par rapport à d'autres."""
        choosed_point = -1
        mu = len(fix_points) / 2
        sigma = len(fix_points)*0.2
        
        while choosed_point >= len(fix_points) or choosed_point < 0:
            choosed_point = random.gauss(mu, sigma)
            choosed_point = round(choosed_point)
        
        choosed_point = fix_points[choosed_point]
        next_point_x = (choosed_point[0] + actual_point[0]) / denominateur
        next_point_y = (choosed_point[1] + actual_point[1]) / denominateur
    
        return (next_point_x, next_point_y)
        
    def create_points(fix_points, first_point, nbr_point=3e5, denom=2):
        """Calcule tous les points en fonctions des conditions initiales et du nombre
        de points demandés."""
        X = []
        X.append(first_point[0])
        Y = []
        Y.append(first_point[1])
        
        for i in range(0, int(nbr_point)):
            x, y = Sirpinski.new_point((X[-1], Y[-1]), fix_points, denominateur=denom)
            X.append(x)
            Y.append(y)
            
        return X, Y
        
        
    def draw_figure(X, Y, point_size=0.6):
        """Trace les points en les plottants."""
        ax=plt.gca()
        ax.set_xticks([]); ax.set_yticks([])
        plt.plot(X,Y,'r.', markersize=point_size)
        plt.show()
        
    def launch(self):
        if self.param["points fixes"] != 3:
            self.fix_points, self.first_point = Sirpinski.polygone(k=self.param["points fixes"])
        X, Y = Sirpinski.create_points(self.fix_points, self.first_point,
                                       self.param["points à calculer"], denom=self.param["dénominateur"])
        Sirpinski.draw_figure(X, Y)
    
if __name__ == "__main__":
    s = Sirpinski()
    s.launch()