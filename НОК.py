a  = int( input ())
b = int(input())
def nood(a,b):
    while a!=0 and b!=0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return ((a+b))
if (a != b ):
    print (int(a*b/nood(a,b)))
else:
    print (int(a))
    
