def up_d(d, key):#добавляетповторения в массив д или создает новое
    if key in d:
        d[key]=d[key]+1
    else:
        d[key] = 1
def sa (a):#создает изстроки массив
    s = [i for i in a.split()]
    return s
d={}
s = sa(input())
print (s)
for a in s:
    up_d(d,a.lower())
print (d)
d={}
my_file = open("someILX4.txt", "r")
fd = my_file.readlines()
for i in fd:
    for r in sa(i):
        up_d(d,r)
ot1=d.copy()
for s in ot1:
    if(d[s]<10):
        d.pop(s)
    else:
        print(s,"-",d[s])
my_file = open("t.txt", "w")
print (d,file=my_file,sep="\n")
my_file.close()
