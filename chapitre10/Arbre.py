class node:
    Value = 0
    Dad = None
    SonLeft = None
    SonRight = None

    def __init__(self,val):
        self.Dad = None
        self.SonLeft = None
        self.SonRight = None
        self.Value = val

    def SetRightSon(self,Son):
        self.SonRight = Son

    def SetLeftSon(self,Son):
        self.SonLeft = Son

    def SetDad(self,Dad):
        self.Dad = Dad

    def GetRightSon(self):
        return(self.SonRight)

    def GetLeftSon(self):
        return(self.SonLeft)

    def GetDad(self):
        return(self.Dad)

    def GetValue(self):
        return(self.Value)

    def __repr__(self):
        """None->String
            Surcharge de la fonction appelée par print pour l'affichage"""
        if self.Dad == None :
            D = "None"
        else:
            D = self.Dad.GetValue()
        if self.SonLeft == None :
            Ls = "None"
        else:
            Ls = self.SonLeft.GetValue()
        if self.SonRight == None :
            Rs = "None"
        else:
            Rs = self.SonRight.GetValue()    
        return "  {"+str(D)+"}"+str(Ls)+"-"+str(self.Value)+"-"+str(Rs)


class tree:
    root = node(None)

    def __init__(self, root):
        self.root = root
        
    def read_root(self):
        return(self.root)

    def add_node_Right(self,Dad,n):
        Dad.SetRightSon(n)
        n.SetDad(Dad)


    def add_node_Left(self,Dad,n):
        Dad.SetLeftSon(n)
        n.SetDad(Dad)


    def get_subtree_Right(self):
        sub_tree = tree(self.root.GetRightSon())
        return(sub_tree)

    def get_subtree_Left(self):
        sub_tree = tree(self.root.GetLeftSon())
        return(sub_tree)

    def __repr__(self):
        """None->String
            Retourne la chaîne servant pour l'affichage de l'arbre"""
        if self.root.GetRightSon() == None and self.root.GetLeftSon() == None:
            return str(self.root.GetValue())
        elif self.root.GetRightSon() == None:
            return "("+str(self.get_subtree_Left())+")<-"+str(self.root.GetValue())
        elif self.root.GetLeftSon == None:
            return str(self.root.GetValue())+"->("+str(self.get_subtree_Right())+")"
        else :
            return "("+str(self.get_subtree_Left())+")<-"+str(self.root.GetValue())+"->("+str(self.get_subtree_Right())+")"



    def infixe(self):
        buffer = []
        if self.root.GetLeftSon() == None and self.root.GetRightSon() == None:
            return(self.root.GetValue())
        elif self.root.GetLeftSon() == None:
            buffer.append(self.root.GetValue())
            buffer.append(self.get_subtree_Right().infixe())
        elif self.root.GetRightSon() == None:
            buffer.append(self.get_subtree_Left().infixe())
            buffer.append(self.root.GetValue())
        else:
            buffer.append(self.get_subtree_Left().infixe())
            buffer.append(self.root.GetValue())
            buffer.append(self.get_subtree_Right().infixe())
        return(buffer)


    def Largeur(self):
        arr = [self.root]
        String = ""
        while len(arr) > 0:
            node = arr[0]
            if node.GetLeftSon() != None:
                arr.append(node.GetLeftSon())
            if node.GetRightSon() != None:
                arr.append(node.GetRightSon())
            String += str(node.GetValue())
            arr.pop(0)
        return (String)

def AddGenerationToLargeur(la):
    la2 = ""
    i,j,k=0,1,1
    for l in la:
        i+=1
        la2+=la[i-1]
        print(la,i,j,la2)
        if i == j:
            j+=2**k
            k +=1
            la2 += '§'
        i+=1
    return(la)

# TODO :: Finish this -> make a § at ever generatoon change
            
def make_a_tree():
    nodes = [node('A')]
    tr = tree(nodes[0])
    aplh = "BCDEFGHIJKLMNO"
    for i in aplh:
        nodes.append(node(i))

    tr.add_node_Left(nodes[0],nodes[1])
    tr.add_node_Right(nodes[0],nodes[8])

    for i in range(1,15,7):
        tr.add_node_Left(nodes[i],nodes[i+1])
        tr.add_node_Left(nodes[i+1],nodes[i+2])
        tr.add_node_Right(nodes[i+1],nodes[i+3])
        tr.add_node_Right(nodes[i],nodes[i+4])
        tr.add_node_Left(nodes[i+4],nodes[i+5])
        tr.add_node_Right(nodes[i+4],nodes[i+6])
    return(tr)


# class ABR(tree):

#     arb = None

#     def add(self,n):
#         print(type(n))
#         runing = True
#         node_scaned = self.read_root()
#         while(runing):
#             if node_scaned.GetValue() > n.GetValue():
#                 if node_scaned.GetLeftSon() == None:
#                     self.add_node_Left(node_scaned,n)
#                     print("Adding >",n ," to >",node_scaned)
#                     runing = False
#                 else:
#                     node_scaned = node_scaned.GetLeftSon()
#             elif node_scaned.GetValue() < n.GetValue():
#                 if node_scaned.GetRightSon() == None:
#                     self.add_node_Right(node_scaned,n)
#                     print("Adding >",n ," to >",node_scaned)
#                     runing = False
#                 else:
#                     node_scaned = node_scaned.GetRightSon()
#             else:
#                 print("Duplicates in the array !!")
#                 exit()

#     def __init__(self,tab):
#         super().__init__(node(tab.pop(0)))
#         for i in tab:
#             self.add(node(i))

# yee = ABR([10,2,5,12,15,20,1,3,7,25])

# print(yee)


tree = make_a_tree()
String = tree.Largeur()
print(AddGenerationToLargeur(String))