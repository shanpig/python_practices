
def error():
      print 'Sorry, something in your typing is incorrect. Please try again.\n'

def isBin(Num):
      try :
            return int (Num, 2)
      except : return 'error'

def isDec(Num):
      try :
            return int (Num)
      except : return 'error'

def isHex(Num):
      try :
            return int (Num, 16)
      except : return 'error'

def checkNumType(Num, Type):
      
      if Type == 'bin':
            return isBin(Num)
      elif Type == 'dec':
            return isDec(Num)
      elif Type == 'hex':
            return isHex(Num)
      else : return 'error'

def checkToType (toType):
      if toType == 'bin' or toType == 'dec' or toType == 'hex':
            return toType
      else :
            return 'error'
def goToType (Num, toType):
      if toType == 'bin':
            return bin (Num)
      elif toType == 'dec':
            return Num
      elif toType == 'hex':
            return hex (Num)
      else :
            return 'error'

###########################################

print 'Enter your number and the type (bin, dec, or hex).\n'

while (True):
      #將數字全部轉換成十進制
      while (True):
            Number = raw_input ('Number = ')
            Type = raw_input ('Type = ')
            Number = checkNumType(Number, Type)
            #錯誤訊息處理      
            if Number == 'error':
                  error()
            else:
                  break
      while (True):
      #對不同要求做不同轉換
            toType = raw_input ('Enter the type you want to transform to (bin, dec, or hex).\n\nType = ')
            toType = checkToType(toType)
            #錯誤訊息處理
            if toType == 'error' :
                  error()
            else:
                  Number = goToType (Number, toType)
                  print '\n---Your number is '+Number+'---\n\n'
                  break
      



      












      
