def up_d(d, key):#добавляетповторения в массив д или создает новое
    if key in d:
        d[key]=d[key]+1
    else:
        d[key] = 1
def sa (a):#создает изстроки массив
    s = [i for i in a.split()]
    return s
d={}
my_file = open("dataset_3363_3.txt", "r")
fd = my_file.readlines()
for i in fd:
    for r in sa(i):
        up_d(d,r.lower())
ot1=d.copy()
vin = {}
i = 0
key = ""
for s in ot1:
    if(i == 0):
        key = s
        i = ot1[s]
        continue
    if(d[s]<i):
        d.pop(s)
    elif(d[s]==d[key]):
        if (s < key):
            i = d[s]
            key = s
        continue    
    else:
        i = d[s]
        key = s
print (key, i)
    
        
        
