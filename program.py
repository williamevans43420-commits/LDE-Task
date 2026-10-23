import mahjong
import sys
from sudoku import Sudoku

#Function that handles the Sudoku game
def game1():
    puzzle = Sudoku(3).difficulty(0.5)
    puzzle.show()

    return

#Function that handles the Go Fish game
def game2():
    print("Go Fish.")
    return

#Function that handles the Mahjong game
def game3():
    print("Mahjong.")
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
                print("Launching Sudoku.")
                game1()
                choice = 0
            #2nd choice launches Go Fish
            case 2:
                print("Launching Go Fish.")
                game2()
                choice = 0
            #3rd choice launches Mahjong
            case 3:
                print("Launching Mahjong.")
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