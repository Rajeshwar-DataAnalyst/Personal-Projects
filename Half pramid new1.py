k=0
a=int(input('Enter the number\n'))
for i in range(a,0,-1):
    for j in range(i,0,-1):
        if j==i:
            k=j
        if j==i:
            print(' ',k,end="")
        k= k+(j-1)
        if j==1:
            print()
    

    
