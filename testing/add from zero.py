def addFromZero(end):
      flag=1
      total=0
      while flag<=end:
            total+=flag
            flag+=1
      print total
            
#start
while (True):
      end=raw_input('please enter a number\n')
      if(end=='kill'):
            break
      addFromZero(int(end))
quit
