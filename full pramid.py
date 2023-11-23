while 1:
    a=int(input('Enter the no of raws\n'))
    for i in range(1,a):
        for k in range(a,i,-1):
            print(' ',end="")
        for j in range(1,((i*2)-1)+1):
            print('*',end="")
        print()
    for i in range(a,0,-1):
        for k in range(a,i,-1):
            print(' ',end="")
        for j in range(1,((i*2)-1)+1):
            print('*',end="")
        print()

