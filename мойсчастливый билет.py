n = input()
def serlog(n):#рекурсивная функция суммирует любое многозначное число до цифры
    i,s1 = 0,0
    n = str(n)
    l = len(n)
    while i < l:
            s1 = int(n[i])+s1
            i = i + 1
    if (len(str(s1)) > 1):
        return serlog(s1)
    else:
        return (s1)
    
n = str(n)
l = int(len(n))
if(l%2 == 0):
    s1 = serlog(n[:(l//2)])
    s2 = serlog(n[(l//2):])
    if (s1 == s2):
        print ("Счастливый")
    else:
        print ("Обычный")

    
            
    
    

