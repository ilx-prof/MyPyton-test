m = [int(input()),int(input()),int(input())]
print (max(m))
print (min(m))
m.remove(max(m))
m.remove(min(m))
for r in m:
    print (r)
