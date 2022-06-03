from random import choice,randint

#TODO :: tkinter / affichage

class Graph:
    grapdico = {}
    def __init__(self,method,liste_sommets,data=None):
        vertices = {}
        ''' str/int,tuple(str/arrary[char],array[data] -> Dictrionary{str/char}:[array[tuple(str/char,int)]]
        '''
        ''' Method'''
        for i in liste_sommets:
            vertices[i] = []
        if method == "listesommetlistearc" or method == 1:
            #data --> liste des arcs !
            for i in data:
                vertices[i[0]].append((i[1],i[2]))
                vertices[i[1]].append((i[0],i[2]))
        if method == "listesommetlisteadjacent" or method == 2:
            #data --> liste des sommets et de leurs liaisons (rien a faire car ce format de données est le bon) !
            # {"A":[(B,3),(C,4)]}
            vertices = data
        if method == "listesommetmatrice" or method == 3:
            #data --> Une liste de liste qui comptient la pondération !
            for y in range(len(data)):
                for x in range(len(data[y])):
                    if data[x][y] != 0 or data[x][y] == None:
                        vertices[liste_sommets[x]].append((liste_sommets[y],data[x][y]))
        if method == "listesommet" or method == 0:
            pass
        self.grapdico = vertices

    def addarc(self,acr1,arc2,value):
        '''key1,key2,int->None'''
        self.grapdico[acr1].append((arc2,value))
        self.grapdico[arc2].append((acr1,value))

    def suprarc(self,acr1,arc2,value):
        '''key1,key2,int->None'''
        self.grapdico[acr1].remove((arc2,value))
        self.grapdico[arc2].remove((acr1,value))

    def getvertices(self):
        '''None->list'''
        return(list(self.grapdico.keys()))

    def __repr__(self):
        '''None->str'''
        return(str(self.grapdico))


class Laby:
    labygraph = None
    doublearray =[]
    height,width = None,None
    def __init__(self,height,width):
        '''All walls on each cell'''
        vertices = []
        i = 1
        tab = []
        for j in range(height):
            tab.append([])
            for k in range(width):
                vertices.append(str(j)+'|'+str(k))
                tab[-1].append(i)
                i+=1
        self.labygraph   = Graph(0,vertices)
        self.doublearray = tab
        self.height      = height
        self.width       = width
    
    def Kruskal(self):
        '''None->None'''
        n = self.height * self.width
        while(n > 1):
            x = randint(0,self.height-1)
            y = randint(0,self.width-1)
            n += self.Spread(x,y)

    def Spread(self,x,y):
        '''int,int->int'''
        r = []
        xyval = self.doublearray[y][x]
        if y > 1 : r.append((x,y-1))
        if x < self.width-1 : r.append((x+1,y))
        if y < self.height-1 : r.append((x,y+1))
        if x > 1 : r.append((x-1,y))
        r = choice(r)
        # print(x,y,r,self.doublearray)
        rval = self.doublearray[r[1]][r[0]] #xy in r but yx in the array
        if xyval != rval:
            self.Replace(xyval,rval) 
            self.labygraph.addarc(str(x)+'|'+str(y),str(r[0])+'|'+str(r[1]),1)
            return(-1)
        else:
            return(0)
            
    def Replace(self,v1,v2):
        '''int/str,int/str->None'''
        for i in range(len(self.doublearray)):
            for j in range(len(self.doublearray[i])):
                if self.doublearray[i][j] == v2:
                    self.doublearray[i][j] = v1


    def Backtrack(self,x=0,y=0,openlist = None):
        '''int,int->None'''
        if openlist == None:
            openlist = self.labygraph.getvertices()
        openlist.remove(str(x)+'|'+str(y))
        possible_moves = []
        if y > 1                and     (str(x)+'|'+str(y-1)    not in openlist : 
            possible_moves.append(      (str(x)+'|'+str(y-1))   )
        if x < self.width-1     and     (str(x+1)+'|'+str(y))   not in openlist : 
            possible_moves.append(      (str(x+1)+'|'+str(y))   )
        if y < self.height-1    and     (str(x)+'|'+str(y+1))   not in openlist : 
            possible_moves.append(      (str(x)+'|'+str(y+1))   )
        if x > 1                and     (str(x-1)+'|'+str(y))   not in openlist : 
            possible_moves.append(      (str(x-1)+'|'+str(y))   )

        while(len(possible_moves) > 0):
            move = choice(possible_moves)
            possible_moves.remove(move)
            self.labygraph.addarc(str(x)+'|'+str(y),move,1)
            [newx,newy] = move.split('|')
            self.Backtrack(int(newx),int(newy),openlist)
        return()

    def __repr__(self):
        return(str(self.doublearray))



labo1 = Laby(5,5)
labo2 = labo1
# print(labo1)
# print(labo2)
labo1.Kruskal()
labo2.Backtrack(2,2)
# print(labo1)
