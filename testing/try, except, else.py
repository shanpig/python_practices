Bool=True
while (Bool):
      number = raw_input ('Please enter a number.')
      try :
            number = int (number)
            Bool = False
      except:
            print 'Please enter number, not a sign or alphabet.'
            continue
      
      
