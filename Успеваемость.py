my_file = open("dataset_3363_4.txt", "r")
fd = my_file.readlines()
nu = [0,0,0]
r = 0
for i in fd:
    i = i.strip()
    n = i.split(";")
    k = len(n)
    a = 0
    while a < k - 1:
        nu[a] = int(n[a+1])+int(nu[a])
        a +=1
    print(sum(map(int,n[1:]))/(len(n)-1),end="\n")
    r +=1
print (*[ i/(r) for i in nu])



    
    
