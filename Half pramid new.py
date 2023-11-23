a=int(input('Enter the number\n'))
for i in range(a,0,-1):
    num = i
    for j in range(i,0,-1):
        print(" ",num,end="")
        num = num+6-j
    print()

    
