lst  = [int(i)for i in input().split()]
x = int(input())
a = lst.count(int(x))
if(a != 0 ):
        l = len(lst)
        i = 0
        b = 0
        while i<l and b<a :
            i =( lst.index(x,i,l))
            print (i, end=" ")
            i = i + 1
            b = b + 1 
else:
    print ("Отсутствует")
