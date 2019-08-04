a = int(input())
b = int(input())
c = int(input())
d = int(input())
print (" \t",end="")
for i in range(c,d+1):
    print (i,"\t",end="")
print ()
for j in range(a,b+1):
    print (j,end="\t")
    for i in range(c,d+1):
        print (i*j,end="\t")
    print()
