m = []
while 1:
    a = input()
    if (a != "end"):
        lst  = [int(i)for i in a.split()]
        aj = len(lst)#количество столбцов
        m.append(lst)
    else:
        break
ai = len(m)#количество строк
if (ai != 0):
    i = 0
    j = 0
    while i < ai:
        while j < aj:
           #print (m[i][j], end=" ")#"i",i,"j",j,
            if(j+1 == aj):
                if(i+1 == ai):
#                    print ("исключение по j + i",i,"/",j)
                    r = m[i-1][j] + m[0][j] + m[i][j-1] + m[i][0]
                    print (r, end=" ")
                else:
#                    print ("исключение по j",i,"/",j)
                    r = m[i-1][j] + m[i+1][j] + m[i][j-1] + m[i][0]
                    print (r, end=" ")
            else:
                if(i+1 == ai):
#                    print ("исключение по i общий j",i,"/",j)
                    r = m[i-1][j] + m[0][j] + m[i][j-1] + m[i][j+1]
                    print (r, end=" ")
                else:
#                    print ("общий случай",i,"/",j)
                    r = m[i-1][j] + m[i+1][j] + m[i][j-1] + m[i][j+1]
                    print (r, end=" ")
            j = j + 1
        print()
        i = i + 1
        j = 0
