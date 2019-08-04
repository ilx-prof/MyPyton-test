a , b = (int(input()),int(input()))
s = int(0) #суматор
n = int(0) #количество
for i in range(a,b+1):
    if (i%3 == 0):
        s = s + i
        n = n + 1
print (s/n)
