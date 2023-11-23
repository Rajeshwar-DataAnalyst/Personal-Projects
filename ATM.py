import time
import random
print('-------Welcome in PNB--------')
while True:
    PIN=int(input('Enter you four digit PIN\n'))
    b=50000
    if PIN==1234 or 5678 or 5263:
        while True:
            print(' (a) Withdraw money \n (b) Balance Enquery\n (c) Deposit money\n (d) Change PIN\n')
            a=int(input('Select option from Above\n'))
            if a==1:
                print('Current balance: ',b)
                c= int(input('Enter the amount\n'))
                b=b-c
                print('Please wait for the transection')
                m=[1,2,3,4,5]
                n=random.choice(m)
                time.sleep(n)
                print('successfully withdraw')
                print('Current balance: ',b)
            elif a==2:
                print('Your current balance is :',b)
            elif a==3:
                l=int(input('Enter the amount you want to deposit'))
                b=b+l
                print('Please wait for few seconds we are try to fetch your current balance')
                o=[8,6,3,4,5]
                p=random.choice(o)
                time.sleep(p)
                print('Now your current balance is : ',b)
            elif a==4:
                change_PIN=int(input('Enter your current PIN'))
                change_PIN1=int(input('Set your PIN'))
                change_PIN2=int(input('Conform your PIN'))
                if change_PIN1== change_PIN2:
                    PIN = change_PIN2
                    print('PIN successfully changed')
                else:
                    print('Something want to be wrong \n ---------Try again--------')
            print()
            print()
    else:
            print('you entered wrong passward')
                    
            
            

            
