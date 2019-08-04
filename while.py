import timeit #таймер
import math
t = timeit.default_timer()#таймер
x = float (0)
y = float (0)
while t < 1:
    x = x*x+1
    y = y*y+1
    s = 0
    if y > 0 and math.isfinite(s):
        s = (3*(x*x))- math.sin(2*x)*math.log(y)
        print ("Логаифм",math.log(y))
        print ("Функция = ",s)
    else :
        print ("разочарование");
'''
while t < 20:
    x = float(input("введите число х"))
    y = float(input("введите число y больше нуля"))
    while  y <= 0 :
        y = float(input("введите число y больше нуля"))
    
    if y > 0:
        print ("Логаифм",math.log(y))
        print ("Функция = ",(3*(x*x))- math.sin(2*x)*math.log(y))
        except ValueError:
        print "Вы ошиблись. Попробуйте c нормальными данными."
'''





"""


name = input("Как Вас зовут?")
print("Привет, ", name)
dela = input("как дела")
i = 0
while i < 2:
    print ("Ура у ",name,"дела",dela)
    i = i + 1
    a = 0
    while a < 2:
            print ("Поэтому мне тоже ", dela)
            a = a + 1
f=0
s = "привет мир"
for r in s:
    print (r,f,end="")
    f = f + 1




while i < 15:
    print("hello world")
    i = i + 1

for y in 'hello world':
    print(y * 2, end='')

    a = tuple('hello, world!')
    print (a)

def add(x, y):
    return x + y


 
def f(x, y):    
    return x*y
a = [1,3,4]
b = [3,4,5]
print (list(map(f, a, b)))#использует функцию f для каждого элемента массива а и б выводит массив

x = [1, 2]

print(list(map(lambda c: c % 2, x)))


class A:
    def _private(self):
        print("Это приватный метод!A")
a = A()
a._private()
'''
class B:
   def __private(self):
    print("Это приватный метод!")
    b = B()
    b.__private()
b._B__private()



class Mydict(dict):
    def get(self, key, default = 0):
    return dict.get(self, key, default)

    a = dict(a=1, b=2)
    b = Mydict(a=1, b=2)
    b['c'] = 4
    print(b)
{'a': 1, 'c': 4, 'b': 2}
    print(a.get('v'))
    print(b.get('v'))
"""
print("Время исполнения = ",timeit.default_timer()-t)#таймер вывод
