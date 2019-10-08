# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 17:55:25 2017

@author: pstmr
Trace le triangle de sirpinski en 3D !
"""

import random
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import math

from fractale import Fractale

class Sirpinski3D(Fractale):
    def __init__(self):
        self.fix_points, self.first_point = Sirpinski3D.pyramide()
        self.param = {"points" : 3e4, "dénominateur" : 2}
        

    """Toutes ces premières fonctions ont pour but de donner les conditions initiales."""
    def pyramide():
        """Donne les points 3D pour avoir une pyramide à base triangle."""
        d = 100
        A = [0, 0, 0]
        B = [d, 0, 0]
        C = [d/2, d/2 * math.sqrt(3), 0]
        D = [math.cos(math.pi/6)*d/math.sqrt(3), math.sin(math.pi/6)*d/math.sqrt(3), math.sqrt(d**2 - (d/2)**2)]
        fix_points = [A, B, C, D]
    
        first_point = [d/2, d/2, d/2]
    
        return fix_points, first_point
        
    def cube():
        d = 100
        A = [0, 0, 0]
        B = [d, 0, 0]
        C = [d, d, 0]
        D = [0, d, 0]
        fix_points = [A, B, C, D]
    
        A = [0, 0, d]
        B = [d, 0, d]
        C = [d, d, d]
        D = [0, d, d]
        fix_points += [A, B, C, D]
    
        first_point = [d/2, d/2, d/2]
    
        return fix_points, first_point
    
    def new_point(actual_point, fix_points, denominateur=2):
        """Retourne la position du nouveau point à tracer. La variable dénominateur permet
        de décider la position entre le point fixe et le point précédent du nouveau point."""
        choosed_point = random.randint(0, len(fix_points) - 1)
    
        choosed_point = fix_points[choosed_point]
        next_point_x = (choosed_point[0] + actual_point[0]) / denominateur
        next_point_y = (choosed_point[1] + actual_point[1]) / denominateur
        next_point_z = (choosed_point[2] + actual_point[2]) / denominateur
                        
        return (next_point_x, next_point_y, next_point_z)
        
    def create_points(fix_points, first_point, nbr_point=3e4, denom=2):
        """Calcule tous les points en fonctions des conditions initiales et du nombre
        de points demandés."""
        X = []
        X.append(first_point[0])
        Y = []
        Y.append(first_point[1])
        Z = [first_point[2]]
        
        for i in range(0, int(nbr_point)):
            x, y, z = Sirpinski3D.new_point((X[-1], Y[-1], Z[-1]), fix_points, denominateur=denom)
            X.append(x)
            Y.append(y)
            Z.append(z)
            
        return X, Y, Z
        
        
    def draw_figure(X, Y, Z, point_size=1):
        """Trace les points en les plottants."""
        mpl.rcParams['legend.fontsize'] = 10
    
        fig = plt.figure()
        ax = Axes3D(fig)
        ax = fig.gca(projection='3d')
        ax.plot(X, Y, Z, '.', markersize=point_size)
        
        plt.show()
        
    def launch(self):
        X, Y, Z = Sirpinski3D.create_points(self.fix_points, self.first_point,
                                            nbr_point=self.param["points"], denom=self.param["dénominateur"])
        Sirpinski3D.draw_figure(X, Y, Z, point_size=2)
    
if __name__ == "__main__":
    s = Sirpinski3D()
    s.launch()