
import random

#variables
coin=1
#funcs
def flipACoin():
      print 'coin number'+str(coin)+' : '
      side=random.randrange(2)
      global coin
      coin+=1
      if (side==0):
            print 'head\n'
      else:
            print 'tail\n'

#start
while (True):
      getCoin=raw_input ('press any key to flip a coin')
      flipACoin()
      if(getCoin=='kill'):
            break
quit
