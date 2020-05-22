"""
Étude de la caractéristique d'un conducteur ohmnique.
Niveau : Seconde
Chapitre : 11 Électricité


Ce programme reprend le tracé avec les points expérimentaux, 
mais des fonctions ont été ajouté pour permettre la modélisation 
de la caractéristique.

Consignes :
 Un travail préalable est a éffecturer dans la fonction calculer_coefdirecteur_modele
 Il manque également deux appels de fonction dans le programme principal
 Plus d'informations dans le code du programme sous la forme de commentaire.
"""
import matplotlib.pyplot as plt
import numpy as np




#### Fonctions
def  calculer_coefdirecteur_modele(I,U):
    """ Cette fonction n'est pas valide, elle doit être complétées pour pouvoir être utilisée """
    Xmoyen = sum(?)/len(?)   # Remplacer les ? par une variable contenant une liste
    Ymoyen = sum(?)/len(?)   # Remplacer les ? par une variable contenant une liste
    a = ???                  # Remplacer les ??? par l'expression qui permet de calculer le coefficient a
    return a

def tracer_modele(a):
    X =[x /10 for x in range(60)]
    Y = [x*a for x in X]
    plt.plot(X, Y, "b-", label="Modelisation")


def afficher_equation_modele(a):
    equation = "Équation du modèle : Y = a X"
    a = "Avec a =" + str(round(a, 1))
    plt.text(0.05, 11, equation, color="blue")
    plt.text(0.05, 10.5, a, color="blue")



def afficher_graphe():
    """Configuration de la représentation graphique et affichage"""
    plt.plot(I, U, 'r+', markersize=9)
    plt.xlim(0.00, 0.55)
    plt.ylim(0.00, 13)
    plt.xlabel("Intensité I, en A") 
    plt.ylabel("Tension U, en V") 
    plt.title("Caractéristique U=f(I)") 
    plt.grid()

    # Enregistrement sous la forme d'une image
    plt.savefig("Caractéristique de la bouilloire.png")

    # Affichage
    plt.show()


##### Programme principal
## Données expérimentales
U =[0.00, 3.00, 4.42, 6.03, 7.55, 9.08, 11.93]
I =[0.0, 0.13, 0.19, 0.23, 0.29, 0.36, 0.49]


## Appels de fonctions
a = calculer_coefdirecteur_modele(I, U)
# Remplacer ce commentaire par l'appel de la fonction permétant de tracer le modèle
# Remplacer ce commentaire par l'appel de la fonction permétant l'affichage de l'équation du modéle

afficher_graphe()
