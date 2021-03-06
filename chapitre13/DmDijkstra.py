class Graph:
    grapdico = {}
    def __init__(self,method,liste_sommets,data):
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
            #data --> Une liste de liste qui comptient la ponde'eration !
            for y in range(len(data)):
                for x in range(len(data[y])):
                    if data[x][y] != 0 or data[x][y] == None:
                        sommets[liste_sommets[x]].append((liste_sommets[y],data[x][y]))
        self.grapdico = sommets


    def __repr__(self):
        return(str(self.grapdico))


# EXEMPLE

# abc1 = Graph(1,['a','b','c'],[('a','b',2),('c','a',7),('b','c',25)])
# abc2 = Graph(2,['a','b','c'],{'a':[('b',2),('c',7)], 'b':[('a',2),('c',25)],'c':[('a',7),('b',25)]})
# abc3 = Graph(3,['a','b','c'],[[0,2,7],[2,0,25],[7,25,0]])


# print(abc1,"Grap 1")
# print(abc2,"Grap 2")
# print(abc3,"Grap 3")
# print(abc1==abc2==abc3)

# FIN DE L'EXEMPLE

if __name__ == "__main__":
    import csv 
    f = open("chapitre13\_routes.csv","r")
    reader = csv.reader(f)
    data = []
    for row in reader:
        data.append(row[0].split(';'))
    villes = data[0][1:]
    print(villes)
    strbuffer = ""
    for i in villes[:-2]:
        strbuffer+=i+", "
    strbuffer+=villes[-2] + " et " + villes[-1] + '.'
    print("Imagions la situation suviante :")
    print("Une apocalypse majeure c'est produite, uniquement les viles majeures de France sont fonctionlles :")
    print(strbuffer)
    start = str(input("Vous habitez à ? -> "))
    end = str(input("Et vous voulez rejoinde un•e proche qui habite à ? -> "))
    maxrange = int(input("Votre voiture peut faire un nombre limité de kilomètres ->"))
    databuffer = []
    print(data)
    for i in range(1,len(data)):
        for j in range(1,len(data[i])):
            if int(data[i][j]) < maxrange and data[i][j] != '0': 
                databuffer.append((data[i][0],data[0][j],int(data[i][j])))
    print(databuffer)