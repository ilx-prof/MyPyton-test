from decimal import Decimal
s = (1.0,1.0,-1.0,1.0,1.0)
wd = (1.0,0.5,0.50,0.1,-1.0)#внимание
c = -1 #учитель
i = 0 
Sn = float (0) 
while i < 5:
    Sn = round(s[i]*wd[i],2) + round(  Sn , 2)
    print (Sn,"сумма", s[i]*wd[i]," - перемножение на этапе -",i)
    i = i + 1



