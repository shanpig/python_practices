import random
playing =True

def claimWinner(result):
      print result

def comChoose():
      return random.randrange(playerChoice-1,playerChoice+2)
      
def compute(playerChoice, comChoice):
      if comChoice < playerChoice:
            return 'Player win !!!'
      elif comChoice == playerChoice:
            return 'Draw !!!'
      elif comChoice > playerChoice :
            return 'Player lose !!!'
      
def showChoice(Choice, person):
      if Choice == 1:
            print person+'choice is paper.'
      elif Choice == 2:
            print person+'choice is scissor.'
      elif Choice == 3 :
            print person+'choice is stone.'


#########################################################

while (playing):
      print '############################'
      print 'Paper, scissor, stone game !!!'
      playerChoice=raw_input ('Please choose \n(1) paper\n(2) scissor\n(3) stone\nPress quit to exit\n')

      if (playerChoice == '1') or (playerChoice == '2') or (playerChoice == '3'):
            
            playerChoice = int (playerChoice)
            comChoice = comChoose()
            result = compute(playerChoice, comChoice)
            
            showChoice (playerChoice, "Player's ")
            showChoice (comChoice, "Computer's ")
            claimWinner (result)
            
      elif playerChoice == 'quit':
            playing = False
      else:
            print 'Please enter 1, 2, or 3. \n'
