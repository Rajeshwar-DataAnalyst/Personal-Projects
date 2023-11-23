a=[]
b = int(input('How many element of list you want to enter '))
for i in range(b):
    A = int(input('Enter the element of a list'))
    a.append(A)
print(a)
c=int(input('Enter your target number'))
f = []
for j in a:
    for k in range(0,b):
        if  (a[k]) + j == c:
            d = a.index(a[k])
            g = a.index(j)
            f.append(g)
            f.append(d)
            break
    if  (a[k]) + j == c:
        break
print(f)
            
