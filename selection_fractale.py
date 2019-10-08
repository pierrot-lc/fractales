# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 11:07:11 2018

@author: pstmr

Permet de tracer toutes les fractales contenues dans le dossier.
Donne aussi les paramètres pour pouvoir les modifier avant de tracer une fractale.
"""

import os
import sys
import tkinter as tk

def get_classes(path='.'):
    """Retourne le nom de toutes les classes contenues dans le dossier donné."""
    classes = {}
    for file in os.listdir(path):
        if file.endswith('.py'):
            with open(file, mode='r') as f:
                for ligne in f:
                    if "class" in ligne[0:5]:
                        name, i = "", 6
                        while ligne[i] != '(' and ligne[i] != ':' and ligne[i] != '\n':
                            name += ligne[i]
                            i += 1
                        try:
                            classes[file[:-3]]  += [name]
                        except KeyError:
                            classes[file[:-3]] = [name]
    return classes

def create_classes(classes):
    """Retourne une instance de toutes les classes données.
    Retire certaines classes dont on sait qu'elles sont inutiles."""
    instances = []
    tab_interdit = ["Fractale", "EnsembleJuliaMandelbrot"]
    for c in classes.keys():
        for i in range(len(classes[c])):
            if classes[c][i] not in tab_interdit:
                module = __import__(c)
                classe = getattr(module, classes[c][i])
                instances.append(classe())
    return instances
    
def show_fractale(fractale, params):
    """Modifie les paramètres de la fractale puis la trace."""
    options = fractale.get_params()
    i = 0
    for cle in options.keys():
        try:
            fractale.set_param(cle, int(params[i].get()))
        except ValueError:#Lorsque c'est un float qui est rentré
            try:
                fractale.set_param(cle, float(params[i].get()))
            except ValueError:#Lorsque c'est un complexe qui est rentré
                fractale.set_param(cle, complex(params[i].get().replace(' ', '')))#Enlève les potentiels espaces
        i += 1
        
    fractale.launch()
    
def show_options(fractale, frame):
    """Affiche les paramètres de la fractale."""
    for widget in frame.winfo_children():#Efface le contenu de la frame auparavant
        widget.destroy()
        
    tab_var = []
    options = fractale.get_params()
    i = 0
    for cle in options.keys():
        lbl = tk.Label(frame, text=cle)
        lbl.grid(row=i, column=0)
        
        var_texte = tk.StringVar()
        var_texte.initialize(options[cle])
        tab_var.append(var_texte)
        ligne_texte = tk.Entry(frame, textvariable=var_texte, width=10)
        ligne_texte.grid(row=i, column=1)
        
        i += 1
        
    button = tk.Button(frame, text='OK', command=lambda f=fractale, t=tab_var : show_fractale(f, t))
    button.grid()
    
    frame.pack(side=tk.RIGHT, padx=10, pady=10)
    
def create_mainframe(fractales):
    """Créer la fenêtre Tkinter proposant toutes les fractales."""
    app = tk.Tk()
    main_frame = tk.Frame(app)
    option_frame = tk.Frame(app)
    for f in fractales:
        button = tk.Button(main_frame, text=f.__class__.__name__, command=lambda f=f, frame=option_frame : show_options(f, frame))
        button.pack()
    main_frame.pack(side=tk.LEFT)
        
    show_options(fractales[0], option_frame)
    app.mainloop()
    
if __name__ == "__main__":
    if 'python.exe' in sys.executable:#Si le programme est lancé par python (donc c'est le fichier.py que l'on lance)
        os.chdir(os.path.dirname(os.path.realpath(__file__)))#Change le working directory sinon il ne trouvera pas les fichiers cartes
    else:#Sinon c'est le fichier en .exe que l'on a lancé
        os.chdir(os.path.dirname(sys.executable))#Change le dossier lorsque ce programme est en .exe
    create_mainframe(create_classes(get_classes(".")))