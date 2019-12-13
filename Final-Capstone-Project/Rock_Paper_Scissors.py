import random
def winner(player,computer):
#WINNER
    if player == 0 and computer == 1:
        return("PAPER BEATS ROCK. COMPUTER WINS!")

    if player == 1 and computer == 2:
        return("SCISSORS BEATS PAPER. COMPUTER WINS!")

    if player == 2 and computer == 0:
        return("ROCK BEATS SCISSORS. COMPUTER WINS!")

    if player == 0 and computer == 2:
        return("ROCK BEATS SCISSORS. YOU WIN!")

    if player == 1 and computer == 0:
        return("PAPER BEATS ROCK. YOU WIN!")

    if player == 2 and computer == 1:
        return("SCISSORS BEATS PAPER. YOU WIN!")

    if player == computer:
        return("TIE GAME")
    
while True:
    p1 = int(input("ROCK: 0. PAPER: 1. SCISSORS: 2. "))
    cpu = random.randint(0,2)
    if p1 <= 2:
        break
    else:
        continue
winner(p1,cpu)
