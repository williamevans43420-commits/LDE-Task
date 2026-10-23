import mahjong
import sys

def solitaire():
    print("Solitaire.")
    banana = 1


def mahjong():
    print("Mahjong.")


def goFish():
    print("Go Fish.")


def main():

    choice = 0

    while choice == 0:
        choice = int(input("Please choose the game you want to play.\n(1. Solitaire, 2. ***, 3. Go Fish, 4. Exit): "))
        match choice:
            case 1:
                solitaire()
                choice = 0
            case 2:
                mahjong()
                choice = 0
            case 3:
                goFish()
                choice = 0
            case 4:
                sys.exit(0)
            case _:
                print("Loop")
                choice = 0

    print("Main.")

if __name__ == "__main__":
    main()