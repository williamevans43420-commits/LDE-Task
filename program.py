import sys

#Function that handles the Coinflip game
def game1():
    print("Coinflip")
    return

#Function that handles the Text Adventure game
def game2():
    print("PAUL.")
    return

#Function that handles the Rock Paper Scissors game
def game3():
    print("RPS.")
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
    return

def main():
    #Sets the default value of choice to 0 to setup for the while loop
    choice = 0

    #While loop to keep the user in the menu unless they pick an option
    while choice == 0:
        #Takes user input and parses to integer for match case.
        choice = int(input("Please choose the game you want to play.\n(1. Sudoku, 2. Go Fish, 3. ***, 4. Exit): "))
        match choice:
            #1st choice launches Sudoku
            case 1:
                print("Launching Coinflip...")
                game1()
                choice = 0
            #2nd choice launches Go Fish
            case 2:
                print("Launching Adventure Game...")
                game2()
                choice = 0
            #3rd choice launches Mahjong
            case 3:
                print("Launching Rock Paper Scissors...")
                game3()
                choice = 0
            #Exit the game menu
            case 4:
                sys.exit(0)
            #Default case when choice does not match 1, 2, 3, or 4.
            case _:
                print("Loop")
                choice = 0

if __name__ == "__main__":
    main()
