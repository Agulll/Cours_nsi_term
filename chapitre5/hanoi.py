def SetupList(n,l=[[],[],[]]):
    for i in range(n,0,-1):
        l[0].append(i)
    return(l)

def hanoï(n,Starting,Ending,Pause):
    if (n!=0):
        hanoï(n-1,Starting,Pause,Ending)
        Data[Ending].append(Data[Starting].pop())
        hanoï(n-1,Pause,Ending,Starting)

Data = SetupList(7)

print(Data)  

#hanoï(len(Data[0]),0,2,1)


from tkinter import * 

root = Tk()
root.title("Résolution des tours d'Hanoï")
root.geometry('640x480')
root.resizable(width=False,height=False)

def Set_n():
    global n 
    n = scale.get()

var = DoubleVar()
scale = Scale(root, orient='horizontal',length=350, from_=1, to=15,label='Nombre de Palets',variable=var)
scale.pack()
button = Button(root, text="Calculer",command = Set_n)
button.pack()

root.mainloop()
print(n)