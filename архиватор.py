s=input()
st=int(0)
a = s[0]
newstr = str("")
n = int(0)
for i in s:
    if (a == i):
        st = st+1
    else:
        newstr = newstr + a + str(st)
        st = int(1)
    a=i
    n = n + 1
newstr = newstr + a + str(st)
print (newstr)
