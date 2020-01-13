print 'Hello, stranger.'
print "Let's play a game. I have an orange. What will you do?(enter a or b)"
print ' a: cut it with a knife'
print ' b: blend it in a blender'
print
while(1):
    do = raw_input ()
    if (do == 'a'):
          print ' Now we have orange cutlets !'
    elif(do == 'b'):
          print ' Now we have orange juice !'
    else:
          print ' Told you to enter a or b you fool'
          break
    
    
