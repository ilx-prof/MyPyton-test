#s = input()
s = [int(i)for i in input().split()]
m = []
i = int()
for i in s:
    m.append(i)
m.sort()
a = m[0]
newstr = str("")
for i in m:
    if ((int(a)) != (int(i))):
        newstr = newstr+ str(a)+" "
    a = int(i)
newstr = newstr+ str(a) 
print (newstr)
