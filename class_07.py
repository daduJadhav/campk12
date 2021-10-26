import random
import time 


operation = ['Rock','Paper','Sceasser']

while True:
    computer = random.choice(operation)
    player = input("Enter you choice (Rock/Paper/Sceaser) : ")

    if player == computer:
        time.sleep(2)
        print('Tie !')

    if player == 'Rock' :
        time.sleep(2)
        if computer == 'Paper':
            print('You Lose !, computer choose Paper')
        elif computer == 'Sceasser':
            print('You Won ! Computer choose Sceasser')

    if player == 'Paper':
        time.sleep(2)
        if computer == 'Rock':
            print('You Win, computer choose Rock')
        elif computer == 'Sceasser':
            print('You Lose! Computer choose Sceasser')
    
    if player == 'Sceasser':
        time.sleep(2)
        if computer == 'Rock':
            print('You Lose, computer choose Rock')
        elif computer == 'Paper':
            print('You Win, computer choose Paper')
