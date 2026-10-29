import random
#rock paper scissors options
options = ("rock", "paper", "scissors")
running = True
#main gameplay loop
while running:
#player and opponent 
    player = None
    opponent = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")

    print(f"Player: {player}")
    print(f"opponent: {opponent}")
#main gameplay loop
    if player == opponent:
        print("Draw!")
    elif player == "rock" and opponent == "scissors":
        print("Winner!")
    elif player == "paper" and opponent == "rock":
        print("Winner!")
    elif player == "scissors" and opponent == "paper":
        print("Winner!")
    else:
        print("Sorry you loose!")
#ask to play again
    if not input("Play again? (y/n): ").lower() == "y":
        running = False

print("Thank you for playing!")
