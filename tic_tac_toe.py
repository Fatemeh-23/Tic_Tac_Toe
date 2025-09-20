import os
import sys
import random

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def reset_game():
    CELLS = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    return CELLS

def draw_map(CELLS):
    print("", " | ".join(CELLS[0:3]))
    print("-----------")
    print("", " | ".join(CELLS[3:6]))
    print("-----------")
    print("", " | ".join(CELLS[6:9]))


def help():
    clear()
    CELL = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    print("*Reminder:\n")
    print("", " | ".join(CELL[0:3]))
    print("-----------")
    print("", " | ".join(CELL[3:6]))
    print("-----------")
    print("", " | ".join(CELL[6:9]))

    input("\nPress 'Enter' to continue...")


def win_lose(CELLS):
    wins = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]
    for win in wins:
        if CELLS[win[0]] == CELLS[win[1]] == CELLS[win[2]] in ["X", "O"]:
            return True
    return False


def play_again():
    print("Do you want to play again? [y/n]")
    ask = input("> ")
    if ask.lower() != "n":
        game_loop()
    else:
        print("\nThanks for playing! Have a nice day!\n")
        sys.exit()
      

def single_player():
    CELLS = reset_game()
    moves = []
    player = 1
    while True:
        clear()
        print("Enter a number between 1 to 9\n")
        draw_map(CELLS)

        try:
            if player == 1:
                house = int(input("\nYou: "))
                if CELLS[house - 1] not in ["X", "O"]:
                    CELLS[house - 1] = "X"
                    moves.append(house)
                    if win_lose(CELLS):
                        clear()
                        draw_map(CELLS)
                        print("\nYou won!\n")
                        break
                    player = 2
                else:
                    print("\nHouse already taken! Try again!")
                    input("Press 'Enter' to continue...")
            else:
                while True:
                    rand = random.randint(1 , 9)
                    if CELLS[rand - 1] not in ["X", "O"]:
                        CELLS[rand - 1] = "O"
                        moves.append(rand)
                        break
                    
                if win_lose(CELLS):
                    clear()
                    draw_map(CELLS)
                    print("\nComputer has won!\n")
                    break
                player = 1
                
        except ValueError:
                print("\nEnter a number 1 to 9...Try again!")
                input("Press 'Enter' to continue...")

        if len(moves) == 8:
            clear()
            draw_map(CELLS)
            print("\nDraw!\n")
            break

    play_again()

def multi_player():
    CELLS = reset_game()
    moves = []
    player = 1
    while True:
        clear()
        print("Enter a number between 1 to 9\n")
        draw_map(CELLS)

        try:   
            if player == 1:
                house = int(input("\nPlayer 1: "))
                if CELLS[house - 1] not in ["X", "O"]:
                    CELLS[house - 1] = "X"
                    moves.append(house)
                    if win_lose(CELLS):
                        clear()
                        draw_map(CELLS)
                        print("\nPlayer 1 has won!\n")
                        break
                    player = 2
                else:
                    print("\nHouse already taken! Try again!")
                    input("Press 'Enter' to continue...")
            else:
                house = int(input("\nPlayer 2: "))
                if CELLS[house - 1] not in ["X", "O"]:
                    CELLS[house - 1] = "O"
                    moves.append(house)
                    if win_lose(CELLS):
                        clear()
                        draw_map(CELLS)
                        print("\nPlayer 2 has won!\n")
                        break
                    player = 1
                else:
                    print("\nHouse already taken! Try again!")
                    input("Press 'Enter' to continue...")
        except ValueError:
                print("\nEnter a number 1 to 9...Try again!")
                input("Press 'Enter' to continue...")

        if len(moves) == 8:
            clear()
            draw_map(CELLS)
            print("\nDraw!\n")
            break    

    play_again()


def game_loop():
    clear()
    print("\n** Welcome to Tic-Tac-Toe! **\n")
    try:
        start = int(input("""
Single Player : 1
Multi Player  : 2
↳ """))
        if start == 1:
            help()
            single_player()
        elif start == 2:
            help()
            multi_player()
    except ValueError:
        play_again()

clear()
game_loop()
