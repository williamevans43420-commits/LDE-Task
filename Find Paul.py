
#initialize player data
player_name = None

#Display menu system
def main_menu():
    print("\nMain Menu:")
    print("1.)Enter Player Name")
    print("2.)Objective brakedown")
    print("3.)Start Game")
    print("4.)Exit")
    

#Option 1 Enter player name
def enter_player_name():
    global player_name
    player_name = input("Please enter your name player")
    print(f"player name set to {player_name}")

# Option 2 Objective brakedown
def objective_brakedown():
    print("Your friend Paul got lost in the jungle and you need to find him before he gets hurt")


# function - Beginning of game

def bridge_cross():
    print("\nYou have come accross an old bridge over a waterfall, it looks like its about to collapse.")
    #choices
    path_found = False
    while not path_found:
        print("\nWhat would you like to do?")
        print("1. Run")
        print("2. Find another path")
        print("3. walk")

        choice = input(" Enter your choice (1-3)")

        if choice == "1":
            print("\nYou attempt to run accross the bridge, However some wook breaks and you slip but find your footing.")
        elif choice == "2":
            print("\nYou try to find another path, there seems to be nothing but trees and shrub's for miles.")
        elif choice == "3":
                path_found = True
                print("You take your time walking accross the old bridge.")
        else:
            print(" you have no other choices paul needs you!")


    print("\nYou make it accross the bridge and advance forward, as you find pauls footprints.")
    panther_den()

#Function - section2 - panther den
def panther_den():
    #context
    print("footprints lead to a dark cave with only one torch lit, the torch reveals a group of hungry panthers who throw what looks to be steak at you.")
    steak_cooked = False

    while not steak_cooked:
        print("\nWhat would you like to do")
        print("1. leave the cave")
        print("2. fight the panthers")
        print("3. throw back the steak")
        print("4. torch the steak")

        choice = input("Enter your chocie (1-4)")

        if choice == "1":
            leave_cave()
            break
        elif choice == "2":
            print("\nYou muster up the courage to fight the panthers and charge at them.")
            panther_fight()
            break
        elif choice == "3":
            print("\nYou throw the steak back but the panthers keep throwing it back at you.")
        elif choice == "4":
            steak_cooked = True
            print("You throw the steak at the torch, the sizling distracts the panthers allowing you to pass by.")
        else:
            print("You have no other choices paul needs you.")

    print("\nYou make it past the panthers, paul is on the other side of a cliff waitiing for you!")
    cliff_final()

#leaving cave function
def leave_cave():
    print("\n You decide to turn around and leave the cave, you and paul were not that close anyway.")
    print("Game Over!")
    replay_game()

#panther fight function
def panther_fight():
    print("\nYou chose to fight panthers. what did you expact? you got torn appart!")
    print("Game Over!")
    replay_game()

#function - section 3 - cliff
def cliff_final():
    print("paul is accross the cliff there is only one way accross,however there is also treasure on the adjasant cliff.")

    while True:
        print("\nWhat would you like to do?")
        print("1. save paul")
        print("2. save treasure")
        
        choice = input("Enter your chouce between (1-2):")

        if choice == "1":
            save_paul()
            break
        elif choice == "2":
            save_treasure()
        else:
            print("invalid option please choose from the options available")

#function - save paul
def save_paul():
    print(f"\nYou decided to save paul, once reunited paul and {player_name} decide to head home")
    print("Good ending")
    print("Game Over")
    replay_game()

#function - save treasure
def save_treasure():
    print(f"\nYou decided to save the treaure, WOW {player_name} you are selfish")
    print("Bad Ending")
    print("Game Over!")
    replay_game()

#function - replay game
def replay_game():
    while True:
        print("\nWould you like to replay the game?")
        print("1. Yes, replay the game")
        print("2. No, exit the game")

        choice = input("Enter your choice (1-2)")

        if choice == "1":
            main() #restarts game by calling menu function
            break
        elif choice == "2":
            print("Thank you for playing")
            exit()
        else:
            print("Invalid choice. Please select either 1 or 2")

#option 3 - start game
def start_game():
    if not player_name:
        print("\n You must have a player name set before you begin.")
        return

    print(f"\nStarting game as {player_name}")
    bridge_cross()

#main loop
def main():
    global player_name
    player_name = None

    while True:
        main_menu()

        choice = input(" please select an option between 1-4")

        if choice == "1":
            enter_player_name()
        elif choice == "2":
            objective_brakedown()
        elif choice == "3":
            start_game()
        elif choice == "4":
            print("Exiting game, GoodBye")
        else:
            print("Invalid Option selected. Please choose between the available options.")

#run game
main()
            
            
            

