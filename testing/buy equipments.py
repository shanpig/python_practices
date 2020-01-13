NIF = 100.05 #KNIFE
SPLA = 230.25 #SPATULA
STIR = 50.00 #STIR BAR
EMIX = 300.60 #ELECTRIC MIXER
TSPN = 20.00 #TEASPOON
'''
def add ( a , b , c , d , e ) :
      a = int ( a )
      b = int ( b )
      c = int ( c )
      d = int ( d )
      e = int ( e )
      return a*NIF + b*SPLA + c*STIR + d*EMIX + e*TSPN
'''
def ask ( a, b, c, d, e ):
      a = raw_input('a=?')
      b = raw_input('b=?')
      c = raw_input('c=?')
      d = raw_input('d=?')
      e = raw_input('e=?')
      a = int ( a )
      b = int ( b )
      c = int ( c )
      d = int ( d )
      e = int ( e )
      return a*NIF + b*SPLA + c*STIR + d*EMIX + e*TSPN
      #return a,b,c,d,e

###########################################################################

while (True):
      print 'we have knife100.05, spatula230.25, stir bar50.00, electic mixer300.60, teaspoon20.00'
      print 'what do you want?'
      a = b = c = d = e = 0
      print ask ( a, b, c, d, e )
      if ( a + b + c + d + e == 0):
            print 'bye'
            break
      
