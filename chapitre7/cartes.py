class Carte:
    """Une classe carte rudimentaire définie par \n
        - sa valeur : 1 à 10, Valet, Dame, Roi\n
        - sa couleur : Carreau, Coeur, Pique, Trèfle\n
        - sa figure (le nom du fichier image correspondant)"""
    
    __valeur = 0
    __couleur = 0
    __figure = ""

    def __init__(self, valeur, couleur):
        """String*String->Carte
           Construit l'objet Carte avec la valeur et la couleur fournie"""
        if valeur == "Valet":
            self.__valeur = 11
        elif valeur == "Dame":
            self.__valeur = 12
        elif valeur == "Roi":
            self.__valeur = 13
        else :
            self.__valeur = int(valeur)
        if couleur == "Carreau":
            self.__couleur = 1
        elif couleur == "Coeur":
            self.__couleur = 2
        elif couleur == "Pique":
            self.__couleur = 3
        else:
            self.__couleur = 4
        self.__Attribuer_Figure(self.__valeur, self.__couleur)

    def Obtenir_Valeur(self):
        """None->String
           Retourne la valeur de la carte"""
        if self.__valeur < 11:
            return str(self.__valeur)
        elif self.__valeur == 11:
            return "Valet"
        elif self.__valeur == 12:
            return "Dame"
        elif self.__valeur == 13:
            return "Roi"

    def Obtenir_Couleur(self):
        """None->String
           retourne la couleur de la carte"""
        if self.__couleur == 1:
            return "Carreau"
        elif self.__couleur == 2:
            return "Coeur"
        elif self.__couleur == 3:
            return "Pique"
        else:
            return "Trèfle"
    
    def Obtenir_Figure(self):
        """None->String
           Retourne le nom du fichier image correspondant à la carte"""
        return self.__figure

    def Attribuer_Valeur(self, valeur):
        """String->None
           Change la valeur de la carte"""
        if valeur == "Valet":
            self.__valeur = 11
        elif valeur == "Dame":
            self.__valeur = 12
        elif valeur == "Roi":
            self.__valeur = 13
        else :
            self.__valeur = int(valeur)
        self.__Attribuer_Figure(self.__valeur, self.__couleur)
    
    def Attribuer_Couleur(self, couleur):
        """String->None
           Change la couleur de la carte"""
        if couleur == "Carreau":
            self.__couleur = 1
        elif couleur == "Coeur":
            self.__couleur = 2
        elif couleur == "Pique":
            self.__couleur = 3
        else:
            self.__couleur = 4
        self.__Attribuer_Figure(self.__valeur, self.__couleur)
    
    def __Attribuer_Figure(self, valeur, couleur):
        """String*String->None
           Attribue le fichier image en fonction de la valeur et de la couleur"""
        self.__figure = str(self.__valeur*10+self.__couleur)+".jpg"

    def __repr__(self):
        """None->None
           Permet d'afficher la carte lors de l'appel par print"""
        return "le {0} de {1}".format(self.Obtenir_Valeur(), self.Obtenir_Couleur()) 

    def __eq__(self, carte):
        return ((self.Obtenir_Couleur() == carte.Obtenir_Couleur()) and (self.Obtenir_Valeur() == carte.Obtenir_Valeur()))



if __name__ == "__main__":
    carte_exemple = Carte("Valet", "Pique")
    print(carte_exemple.Obtenir_Valeur())
    print(carte_exemple.Obtenir_Couleur())
    print(carte_exemple.Obtenir_Figure())
    carte_exemple.Attribuer_Couleur("Carreau")
    print(carte_exemple.Obtenir_Figure())
    print(carte_exemple)
    print(carte_exemple.__class__)
    print(Carte("Valet", "Pique") == Carte("Valet", "Pique"))
    #help(Carte)