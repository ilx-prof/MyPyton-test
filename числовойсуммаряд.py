a = int(input())
i = 1
d = 1
st = []
n = 1
'''
while i<=a:
        j=0
        t=n
        while j<n:
                print ("a",a,"i",i,"j",j,"t",t,"n",n)
                st.append(t)
                i = i + 1
                if (i<=a):
                        j = j + 1
                else:
                        break
        
        if (i<=a):
            n = n + 1
        else:
            break
print (st)
'''
while i<=a:
        j=0
        t=n
        while j<n:
                #print ("a",a,"i",i,"j",j,"t",t,"n",n)
                print (t,end=" ")
                i = i + 1
                if (i<=a):
                        j = j + 1
                else:
                        break
        
        if (i<=a):
            n = n + 1
        else:
            break



