while True:
    print'\n'
    print'select a letter from the below box menu:'
    a1=input('(1). Open New client Account\n(2). The client withdraw a money\n(3). The client deposit a money\n(4). Check clients and Balance\n')
    if a1==2:
        print"Letter 'b' is selected by the client"
        a2=raw_input('Enter a name:\n')
        a3=input('Please enter your four digit PIN\n')
        print'Your current balance is: P ',a20
        a4=input('Insert a value to Withdraw:\n')
        if a4<a20:
            print'---Withdraw successfully---'
            a5=a20-a4
            print'Your new balance is:',a5
        else:
            print'---Insufficient balance---'
    elif a1==1:
        print'Enter your details'
        a6=input('Choose your account type\n(1).Saving account(2).Current account\n')
        if a6==1:
            a7=raw_input('Enter your name\n')
            a8=raw_input('Enter your father name\n')
            a9=raw_input('Enter your mother name\n')
            a10=input('Enter your addhar no:\n')
            print'Upload your passport size photo'
            print'Upload your addhar card'
            print'Upload your Signature'
            a20=input('Submit some ammount to open the account\n')
            print'---successfully Opened your account---'
        else:
            a11=raw_input('Enter your name\n')
            a12=raw_input('Enter your father name\n')
            a13=raw_input('Enter your mother name\n')
            a14=input('Enter your addhar no:\n')
            print'Upload your passport size photo'
            print'Upload your addhar card'
            print'Upload your Signature'
            a15=input('Submit some ammount to open the account\n')
            print'---Susscessfully opened your account---',a15
    elif a1==3:
        a16=input('Enter the amount you want to submit\n')
        a17=input('Enter your four digit PIN\n')
        print'You have successfully submited:',a16
        print'Previous balance is:',a5
        print'Current balance:',a5+a16
    else:
        a19=input('Enter your four digit PIN\n')
        print'Your account balance is:',a5+a16
        
    
    
        
        

         
         
