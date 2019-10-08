# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 20:52:43 2018

@author: pstmr
Objet donnant les fonctions communes que doivent avoir toutes les fracatales.
"""

class Fractale:
    def __init__(self):
        self.param = {}
    
    def get_params(self):
        """Permet de récupérer un dictionnaire contenant les
        paramètres modulables pour la fractales."""
        return self.param
    
    def set_param(self, name, value):
        self.param[name] = value

    def launch(self):
        """Lance la création puis le tracé de la fractale."""
        pass