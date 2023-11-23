a=[]
b = int(input('How many element of list you want to enter '))
for i in range(b):
    A = int(input('Enter the element of a list'))
    a.append(A)
print(a)
c=int(input('Enter your target number'))
f = []
for j in a:
    if  (j+1) +j == c:
        d = a.index(j+1)
        g = a.index(j)
        f.append(g)
        f.append(d)
print(f)
            
