print 'hello, what do you want to buy? cookies or cake?'
def get( first, second, third, forth):
      print first, second, third, forth
while(True):
    first = raw_input ()
    second = raw_input ()
    third = raw_input ()
    forth = raw_input ()
    if (first or second or third or forth== 'no' ):
        print 'Byebye then!'  
        break
    else:
        get ( first, second, third, forth)
        print 'Ok. What else?'
