from random import randint
import time
def liste():
    liste=[]
    sousliste = []
    for i in range(20):
        for j in range(randint(100,1000)):
            sousliste.append(randint(6,1000))
        liste.append(sousliste)
    return(liste)

def minimprea(l):
    nimi = l[0]
    for i in l:
        if i<nimi:
            nimi=i
    return(nimi)

def minirecu(l):
    n = int(len(l)/2)
    if len(l) == 1:
        return(l[0])
    else:
        m1=minirecu(l[:n])
        m2=minirecu(l[n:])
        if m1<m2:
            return m1
        else:
            return m2

def chrorecu(liste):
    tmie=[]
    for i in liste:
        start = time.time()
        minirecu(i)
        end = time.time()
        tmie.append(end - start)
    return(time)

def chroimpe(liste):
    tmie=[]
    for i in liste:
        start = time.time()
        minimprea(i)
        end = time.time()
        tmie.append(end - start)

def Chrono(liste):
    return([chrorecu(liste),chroimpe(liste)])

    
results = Chrono(liste())

for i in range(20):
    print("Récursif temps =",results[0][i])
    print("Impératif temps =",results[1][i])

#times is doing weird shit aka not a number so it's fucked