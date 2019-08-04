a = [int(i)for i in input().split()]
i= int(0)
c = len(a)
if (c > 1):
    while i < c-1:
        print (int(a[i-1])+int(a[i+1]),end=" ")
        i = i + 1
    print (int(a[i-1])+int(a[0]))
else:
    print (a[0])
        


