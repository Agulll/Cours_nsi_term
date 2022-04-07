class Ultime:
    Pile = []
    l = 0
    typ = ""
    def __init__(self,typ,n=None):
        if n == None:        
            self.Pile = []
            self.l = 0
        else:
            self.Pile = [n]
            self.l = 1
        self.typ = typ

    def pop(self):
        if self.l > 0:
            self.l -= 1
            return self.Pile.pop(-1 if self.typ == "Pile" else 0)
        else : return(None)

    def GetType(self):
        return(self.typ)

    def SwapType(self):
        if self.typ == "Pile":
            self.typ = "File"
        elif self.typ == "File":
            self.typ = "Pile"

    def GetL(self):
        return(self.l)

    def isEmpty(self):
        return(True if len(self.Pile) == 0 else False)

    def add(self,n):
        self.l += 1
        self.Pile.append(n)

    def __repr__(self):
        buffer = ""
        for i in self.Pile:
            buffer += "["+str(i)+"] -> "
        return(buffer[:-4])

    def pretty_print(self):
        if self.typ == "Pile":
            buffer = "╔ ╗\n"
            for i in self.Pile:
                buffer += "║"+str(i)+"║\n"
            print(buffer+"╚═╩╡"+str(self.l)+"│")
        elif self.typ == "File":
            buffer = '╭'
            for i in range(self.l):
                if i == self.l-1:
                    buffer+="─╮ ╭─╮\n│"
                else:
                    buffer+="─┬"
            for i in self.Pile:
                buffer += str(i)+"│"
            buffer+="─┤"+str(self.l)+"│\n╰"
            for i in range(self.l):
                if i == self.l-1:
                    buffer+="─╯ ╰─╯"
                else:
                    buffer+="─┴"
            print(buffer) 

def copy(p1):
    WasSwaped = False
    p2 = Ultime(p1.GetType())
    if p1.GetType() == "Pile":
        p1.SwapType()
        WasSwaped = True
    for i in range(p1.GetL()):
        a = p1.pop()
        p2.add(a)
        p1.add(a)
    if WasSwaped:
        p1.SwapType()
    return(p2)

def premuter_Ultime(s,n):
    WasSwaped = False
    if s.GetType() == "Pile":
        s.SwapType()
        WasSwaped = True
    for i in range(n):
        s.add(s.pop())
    if WasSwaped == True:
        s.SwapType()
    return(p2)


from random import randint

if __name__ == "__main__":
    p1 = Ultime("Pile")
    for i in range(1,10):
        p1.add(randint(1,9))
        # p1.add(i)
    # \u250F
    p1.pretty_print()
    p2 = copy(p1)
    p2.pretty_print() 
    premuter_Ultime(p2,4)
    p2.pretty_print()