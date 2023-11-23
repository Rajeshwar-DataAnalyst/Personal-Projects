a = input('Enter 1st string\n')
b= input('Enter 2nd String\n')
k=[]
if len(a)!=len(b):
    print('Not Anagram')
for i in a:
    for j in b:
        if j!=i:
            print(end="")
        elif j==i:
            k.append(j)
            break          
                    
if len(a)==len(k):
    print('Anagram')
else:
    print('Not Anagram')
