print('Rock')
print('paper')
print('scissors')

player1 = input ('player1. make your move ')
player2 = input ('player2. make your move ')
if player1 == 'rock' and player2 == 'paper':
    print('player1 wins')
elif player1 == 'rock' and player2 == 'scissors':
    print ('player2 wins')
elif player1 == 'scissors' and player2 == 'paper':
    print ('player2 wins')
elif player1 == 'paper' and player2 == 'rock':
    print ('player1 wins')
elif player1 == 'scissors' and player2 == 'paper':
    print ('player2 wins')
elif player1 ==  player2 :
    print('its a tie')
else:
    print("something went wrong")