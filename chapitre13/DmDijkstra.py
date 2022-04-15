# {"A":[(B,3),(C,4)]}
    dico
class Graph:
    sommets = {}
    def __init__(self,method,data,liste_sommets):
        ''' str/int,tuple(str/arrary[char],array[data] -> Dictrionary{str/char}:[array[tuple(str/char,int)]]
        '''

        for i in liste_sommets:
            sommets[i] = []
        if method == "listesommetlistearc" or method == 1:
            #data = liste des arcs !
            for i in data:
                sommets{i[0]}.append(i[1],i[2])
                sommets{i[1]}.append(i[0],i[2])
        if method == "listesommetlisteadjacent" or method == 2:
            #data = liste des sommets et de leurs liaisons (rien a faire car ce format de données est le bon) !
            sommets = data
        if method == "listesommetmatrice" or method == 3:
            [
                []
                []
                []
                []
                []
            ]
            



