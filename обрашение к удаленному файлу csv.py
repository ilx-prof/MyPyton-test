from urllib.request import urlopen
a = str (input())
f = urlopen('https://stepic.org/media/attachments/lesson/16462/boston_houses.csv')
r = urlopen(a)
print (f)
sbux = np.loadtxt(f, usecols=(0,1,4), skiprows=1, delimiter=",", 
                      dtype={'names': ('date', 'open', 'close'),
                             'formats': ('datetime64[D]', 'f4', 'f4')})
