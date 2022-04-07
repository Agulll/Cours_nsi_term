fh = open("chapitre9\hax.txt",'r',encoding='utf-8')
all_lines = fh.readlines()
fh.close()
txt=""
for i in all_lines:
    txt+=i
Dico={}
for i in txt:
    if i is not ' ':
        print(i)
        if i in Dico.keys():
            Dico[i] += 1
        else:
            Dico[i] = 1
print(Dico)

for n in range(Len(Dico)):
    Maximum = 0
    LastMaximum
    for i in Dico:
         if i > Maximum and i < Last
         Maximum = i
