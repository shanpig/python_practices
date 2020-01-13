def cal (a1,a2,a3,a4):
    total = int (a1) + int (a2) + int (a3) + int (a4)
    print total/4
while (True):
    a1 = raw_input ( 'please enter first number')
    a2 = raw_input ( 'please enter second number')
    a3 = raw_input ( 'please enter third number') 
    a4 = raw_input ( 'please enter forth number')
    if (a1 or a2 or a3 or a4 == '0'):
        break
    else:
        cal (a1, a2, a3, a4)
    

        
