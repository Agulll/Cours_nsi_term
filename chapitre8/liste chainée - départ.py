from math import inf

class Cellule_Liste :



    """classe basique de cellule de liste chainée"""
    __valeur = None
    __suivant = 0

    def __init__(self, valeur) :
        self.__valeur = valeur

    def attr_suivant(self, suivant) :
        self.__suivant = hex(id(suivant))

    def lire_suivant(self) :
        return self.__suivant

    def lire_valeur(self) :
        return self.__valeur
    
    def __repr__(self) -> str:
        return "["+str(self.__valeur)+"]->"+str(self.__suivant)



class Liste :
    """Classe basique de liste chainée"""
    __debut = 0
    __fin = 0
    __nombre = 0
    __cellules = []

    def __init__(self, c) :
        self.__debut = hex(id(c))
        self.__fin = self.__debut
        self.__cellules = [c]
        self.__nombre = 1

    def __trouver_cellule(self, adresse_c):
        for i in self.__cellules:
            if hex(id(i)) == adresse_c:
                return(i)

        
    def __repr__(self) :
        # return(str(self.__cellules))
        string = ">>"
        i = self.__debut
        string += "["+str(self.__trouver_cellule(i).lire_valeur())+"]->"
        i = self.__trouver_cellule(i).lire_suivant()
        while (i != self.__fin):
            print(i,self.__fin)
            print(self.__cellules)
            s = self.__trouver_cellule(i)
            i = s.lire_suivant()
            string += "["+str(s.lire_valeur())+"]->"
        return(string[:-2])
        # print(self.__cellules)
        # adr1 = self.__cellules[0].lire_suivant
        # print(self.__trouver_cellule(adr1))
        # return("Sample text")


    def ajouter(self, c, position = inf) :
        """Cellule_liste * int -> None
           Ajoute la cellule c à la place position et à la fin si position >= nombre de cellule ou par défaut"""
        adr1 = self.__debut
        if position >= self.__nombre:   
            for i in range(self.__nombre):
                adr1 = self.__trouver_cellule(adr1).lire_suivant()
            print (self.__trouver_cellule(adr1))#.attr_suivant(hex(id(c)))
            self.__cellules.append(c)
            self.__fin = self.__trouver_cellule(adr1).lire_suivant()
        else:    
            for i in range(position):
                adr1 = self.__trouver_cellule(adr1).lire_suivant()
            adr2 = self.__trouver_cellule(adr1).lire_suivant()
            self.__trouver_cellule(adr1).attr_suivant((hex(id(c))))
            self.__cellules.append(c)
            self.__trouver_cellule(self.__trouver_cellule(adr1).lire_suivant()).attr_suivant(adr2)
        self.__nombre+=1

if __name__=="__main__" :
    c1 = Cellule_Liste(10)
    c2 = Cellule_Liste("A")
    c3 = Cellule_Liste(3.0)
    print(c1, c2, c3)
    print(hex(id(c2)))
    lst = Liste(c1)
    lst.ajouter(c2)
    print(lst)
    # lst.ajouter(c3)
    # print(lst)
    # c4 = Cellule_Liste(5)
    # lst.ajouter(c4,0)
    # print(lst)