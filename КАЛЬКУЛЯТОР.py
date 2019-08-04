st = input()
a = float (input())
b = float (input())

if st == "+":
    print (a+b)
elif st == "-":
    print (a-b)
elif st =="*":
    print (a*b)
elif st == "mod":
    if b != 0:
        print (a%b)
    else:
        print ("Деление на 0!")
elif st == "pow":
    print (a**b)
elif st == "div":
    if b != 0:
        print (a//b)
    else:
        print ("Деление на 0!")
elif st == "/":
    if b != 0:
        print (a/b)
    else : print ("Деление на 0!")
