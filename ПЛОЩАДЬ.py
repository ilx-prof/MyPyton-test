tup = input()
if tup == "треугольник":
    a = float(input())
    b = float(input())
    c = float(input())
    p = (a+b+c)/2
    import math
    print (math.sqrt(p*(p-a)*(p-b)*(p-c)))
elif tup == "прямоугольник":
    a = float(input())
    b = float(input())
    print (a*b)
elif tup == "круг":
    r = float(input())
    print (3.14*(r**2))
