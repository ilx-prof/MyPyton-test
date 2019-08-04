s = int(input())
slovar = []
while s > 0:
    slovar.append(input().lower())
    s -=1
st = int(input())
slova = {}
new = []
while st > 0:
    slova[st] = [i.lower()for i in input().split()]
    st -=1
for st in slova:
    for a in slova[st]:
        if a not in slovar:
            if a not in new:
                new.append(a)
                print (a)

            
        
        
    

        
