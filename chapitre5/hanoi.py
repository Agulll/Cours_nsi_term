from tkinter import *
from time import sleep

def SetupList(n):
    '''
    (int->void)
    SetupList initialise la variable Data
    Data est alors remplit d'une liste d'ordre décroissant de longeur n
    '''
    global Data
    Data=[[],[],[]]
    for i in range(n,0,-1):
        Data[0].append(i)
    return()

def Scale_moved(v):
    '''
    (int->void)
    Scale_moved permet d'assigner la valeur du slider a n
    Elle update aussi la canvas pour avoir un retour visuel
    '''
    global n
    n = int(v)
    SetupList(n)
    update()

def Button_pressed():
    '''
    (void->void)
    Button_pressed empèche l'utilisateur de relancer le calcul tant qu'il n'est pas fini
    Il lance aussi l'algorithme
    '''
    button.configure(text="Calcul en cours", state = DISABLED)
    hanoï(len(Data[0]),0,2,1)
    button.configure(text="Calculer", state = ACTIVE)
    update()


def Background(canvas):
    '''
    (tkinter.canas->void)
    Background dessine la base et les 3 poteaux
    '''
    Socle = 155,820,1065,860
    DSocle = canvas.create_rectangle(Socle, fill="Blue")
    Poteaux = [[375,390,385,820],[605,390,615,820],[835,390,845,820]]
    P1 = canvas.create_rectangle(Poteaux[0], fill="Red")
    P2 = canvas.create_rectangle(Poteaux[1], fill="Red")
    P3 = canvas.create_rectangle(Poteaux[2], fill="Red")

def update():
    '''
    (void->void)
    Update gère l'affiche en utilisant Background mais ajoute aussi les palets en calculant leurs positions
    '''
    global canvas
    global Data
    sleep(0.001)
    canvas.delete("all")
    Background(canvas)
    for i in range(0,len(Data)):
        for j in range(0,len(Data[i])):
            coord = 380-(12*Data[i][j])+230*i,780-(40*j),380+(12*Data[i][j])+230*i,780-(40*(j-1))
            canvas.create_rectangle(coord, fill="Green")
    canvas.update()


def hanoï(n,Starting,Ending,Pause):
    '''
    (int,int,int,int->void)
    hannoï est l'algorithme de tri qui nous permet de résoudre le problème
    '''
    if (n!=0):
        update()
        hanoï(n-1,Starting,Pause,Ending)
        Data[Ending].append(Data[Starting].pop())
        hanoï(n-1,Pause,Ending,Starting)

Data=[[],[],[]]
n=1

wi=Tk()
wi.title("Résolution des tours d'Hanoï")
wi.geometry('1220x970')
wi.resizable(width=False,height=False)
ui = PanedWindow(wi, orient=VERTICAL)
ui.pack(fill = BOTH, expand = 1)
options = PanedWindow(ui, orient = VERTICAL)
ui.add(options)
var = DoubleVar()
Slider = Scale(options,command=Scale_moved, orient='horizontal',length=350, from_=1, to=10,label='Nombre de Palets',variable=var)
Slider.pack()
button = Button(options, text="Calculer",command = Button_pressed)
button.pack()
canvas = Canvas(ui,bg="grey", width=1220, height=860)
Background(canvas)
canvas.pack()
ui.add(canvas)
wi.mainloop()
