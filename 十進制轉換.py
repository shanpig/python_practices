def turnNum(Input):
      try : Num = int (Input)
      except : print "This is not a number. Please try again."
      return Num
      
def binNum(Input):
      Num = turnNum(Input)
      return bin(Num)

def  hexNum(Input):
      Num = turnNum(Input)
      return hex(Num)

#####################

print "@This is a program which translate your number into other types .\n5Type in 'bin' or 'hex', then enter a number.\nEnter x to leave."
while (True):
      method = raw_input ('Method : ')
      Input = raw_input ('Number : ')
      if method == 'bin':
            print binNum(Input)
            print 
      elif method == 'hex':
            print hexNum(Input)
            print 
      elif method == 'x' or Input == 'x':
            break
      else:
            print "Please try again, type in 'bin' or 'hex', then enter a number\n"
