shab= input()
zame = input()
pram= input()
obr= input()
cpram = ""
cobr = ""
i = 0
def zam(a,shab,zame):
    ind = shab.find(a)
    if (ind!=-1):
       return zame[ind]
    else:
        return a
i = 0
while i < len(pram):
    cpram = cpram+str(zam(pram[i],shab,zame))
    i +=1
i = 0
while i < len(obr):
    cobr = cobr+str(zam(obr[i],zame,shab))
    i +=1
print (cpram)
print (cobr)

'''
# лучший
cod,decod,coded,toDecod=[input() for i in range(4)]
print(*[decod[cod.find(i)] for i in coded],sep="")
print(*[cod[decod.find(i)] for i in toDecod],sep="")
'''
