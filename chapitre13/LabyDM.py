from cmath import inf

class Graph:
    grapdico = {}
    def __init__(self,method,liste_sommets,data=None):
        sommets = {}
        ''' str/int,tuple(str/arrary[char],array[data] -> Dictrionary{str/char}:[array[tuple(str/char,int)]]
        '''
        ''' Method'''
        for i in liste_sommets:
            sommets[i] = []
        if method == "listesommetlistearc" or method == 1:
            #data --> liste des arcs !
            for i in data:
                sommets[i[0]].append((i[1],i[2]))
                sommets[i[1]].append((i[0],i[2]))
        if method == "listesommetlisteadjacent" or method == 2:
            #data --> liste des sommets et de leurs liaisons (rien a faire car ce format de données est le bon) !
            # {"A":[(B,3),(C,4)]}
            sommets = data
        if method == "listesommetmatrice" or method == 3:
            #data --> Une liste de liste qui comptient la pondération !
            for y in range(len(data)):
                for x in range(len(data[y])):
                    if data[x][y] != 0 or data[x][y] == None:
                        sommets[liste_sommets[x]].append((liste_sommets[y],data[x][y]))
        if method == "listesommet" or method == 0:
            pass
        self.grapdico = sommets

    def addarc(self,acr1,arc2,value):
        self.grapdico[acr1].append((arc2,value))
        self.grapdico[arc2].append((acr1,value))

    def suprarc(self,acr1,arc2,value):
        self.grapdico[acr1].remove((arc2,value))
        self.grapdico[arc2].remove((acr1,value))

    def __repr__(self):
        return(str(self.grapdico))


class Laby:
    Graph = None
    doublearray =[]
    height,width = None,None
    def __init__(self,height,width):
        '''All wall on each cell'''
        vertices = []
        i = 1
        tab = []
        for j in range(height):
            tab.append([])
            for k in range(width):
                vertices.append(str(j)'|'+str(k))
                tab[-1].append(i)
                i+=1
        self.labygraph   = Graph(0,vertices)
        self.doublearray = tab
        self.height      = height
        self.width       = width
    
    def Kruskal(self):
        n = self.height * self.width
        while(n > 1):
            x = randint(0,self.height)
            y = randint(0,self.width)
            pos = str(x)+'|'+str(y)
            


    def __repr__(self):
        return(str(self.doublearray))
            
labo = Laby(5,5)
print(labo)
