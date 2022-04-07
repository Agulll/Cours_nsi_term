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