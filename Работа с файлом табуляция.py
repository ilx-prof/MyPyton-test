d ={a: ["-",0,0] for a in range(1,12)}
my_file = open("dataset_3380_5.txt", "r")
for st in my_file.readlines():
    clas, _ , rost = st.split()
    d[int(clas)][1] = d[int(clas)][1] +  int(rost)
    d[int(clas)][2] = d[int(clas)][2] + 1

for cl in d:
    if d[cl][1]>0:
        print (cl, d[cl][1]/d[cl][2])
    else:
        print (cl, d[cl][0])




