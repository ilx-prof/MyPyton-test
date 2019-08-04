def uncod (l):
    le = len(l)
    n1 = ""
    i=0
    while i < le:
        if(l[i].isalpha()):
            a = l[i]
            i +=1
            n = ""
            while i < le and l[i].isdigit():
                n +=l[i]
                i +=1
            n1 = n1 + a * int(n)
    return n1

#print (uncod("a3b4c2e10b55"))
with open ("dataset_3363_2.txt","r") as fn:
    for line in fn:
        l = line.strip()
with open ("fi.txt","w") as fr:
    fr.write( uncod(l))
                
                
            
            
        
    
        
