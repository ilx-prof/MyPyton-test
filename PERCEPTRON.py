s = (1,1,-1,1,1)
wd = (1,0.5,0.5,0.1,-1)#внимание
c = -1 #учитель
i = 0 
while i < 5:
    Sn = s[i]*wd[i] + Sn
    print (Sn,"перемножение на этапе -",i)
    i = i + 1





'''
def perceptron(xv,wv):
    I = int(sum(x*w for x,w in zip(xv,wv))>0)
    return I
print (list(z))
exw = int()
for x,w in zip(a,b) :
    print (x,w,w*x,exw)
    exw = w*x + exw

R = perceptron(a, b)
print (R)


import numpy as np
w = np.array([[0, 0, 0]])
print("w shape ", w.shape)
def Target (ex):
    if ex[1] == 1 and ex[2] == 0.3:
        return 1
    elif ex[1] == 0.4 and ex[2] == 0.5:
        return 1
    elif ex[1] == 0.7 and ex[2] == 0.8:
        return 0
def Predict (examp):
    sum = examp[0]*w[0][0]+examp[1]*w[0][1]+exemp[2] * w[0][2]
    #5:: = 7.‘_I)E: *‘e'
    print ("examp", examp)
    print ("sum ", sum)
    if sum > 0:
        return 1
    else:
        return 0
examples = np.array([[1, 1, 0.3],[1, 0.4, 0.5],[1, 0.7, 0.8]])
perfect = False
while not perfect:
    perfect = True
    for e in examples:
        print("e", e)
        if Predict(e) != Target(e):
            perfect = False
            if Predict(e) == 0:
                    w = w + e
                    print ("w",w)
            else:
                    w = w - e
                    print ("w", w)
print ("Final answer", w)
...
...
