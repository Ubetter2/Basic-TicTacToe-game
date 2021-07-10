import random
import sys


def StartGame():
    gameIsOvet = False
    winner = ""
    Playing = ""
    PlX = False
    rand = random.randint(1,2)
    if rand == 1:
        Playing = "X"
        PlX = False
    elif rand == 2:
        Playing = "O"
    a1,a2,a3,b1,b2,b3,c1,c2,c3 = " "," "," "," "," "," "," "," "," "
    print("Welcome to my TicTacToe Game")
    print("  |   |")
    print("  |   |")
    print("  |   |")
    while gameIsOvet == False:
        print(f"{Playing} is Playing")
        if Playing == "X":
            inp = input("Please write input:    ")
            if (inp == "a1" and a1 != "O"and a1 != "X"):
                a1 = "X"
                PlX = True
            if (inp == "a2" and a2 != "O"and a2 != "X"):
                a2 = "X"
                PlX = True
            if (inp == "a3" and a3 != "O" and a3 != "X"):
                a3 = "X"
                PlX = True
            if (inp == "b1" and b1 != "O" and b1 != "X"):
                b1 = "X"
                PlX = True
            if (inp == "b2" and b2 != "O"and b2 != "X"):
                b2 = "X"
                PlX = True
            if (inp == "b3" and b3 != "O" and b3 != "X"):
                b3 = "X"
                PlX = True
            if (inp == "c1" and c1 != "O" and c1 != "X"):
                c1 = "X"
                PlX = True
            if (inp == "c2" and c2 != "O" and c2 != "X"):
                c2 = "X"
                PlX = True
            if (inp == "c3" and c3 != "O" and c3 != "X"):
                c3 = "X"
                PlX = True
        if Playing == "O":
            inp = input("Please write input:    ")
            if (inp == "a1" and a1 != "X" and a1 != "O"):
                a1 = "O"
                PlX = False
            if (inp == "a2" and a2 != "X" and a2 != "O"):
                a2 = "O"
                PlX = False
            if (inp == "a3" and a3 != "X" and a3 != "O"):
                a3 = "O"
                PlX = False
            if (inp == "b1" and b1 != "X" and b1 != "O"):
                b1 = "O"
                PlX = False
            if (inp == "b2" and b2 != "X" and b2 != "O"):
                b2 = "O"
                PlX = False
            if (inp == "b3" and b3 != "X" and b3 != "O"):
                b3 = "O"
                PlX = False
            if (inp == "c1" and c1 != "X" and c1 != "O"):
                c1 = "O"
                PlX = False
            if (inp == "c2" and c2 != "X" and c2 != "O"):
                c2 = "O"
                PlX = False
            if (inp == "c3" and c3 != "X" and c3 != "O"):
                c3 = "O"
                PlX = False
        elif inp != "a1" or inp != "a2" or inp != "a3" or inp != "b1" or inp != "b2" or inp != "b3" or inp != "c1" or inp != "c2" or inp != "c3":
            print("Please write letter for row(a,b,c) and number for column(1,2,3) for example (a1, b3...)")
        print(f"{a1} | {a2} | {a3}")
        print(f"{b1} | {b2} | {b3}")
        print(f"{c1} | {c2} | {c3}")
  
                
                
        if a1 == "X" and a2 == "X" and a3== "X" or b1 == "X" and b2 == "X" and b3== "X" or c1 == "X" and c2 == "X" and c3== "X":
            break
        elif a1 == "X" and b1 == "X" and c1 == "X" or a2 == "X" and b2 == "X" and c2 == "X" or a3 == "X" and b3 == "X" and c3 == "X":
            break
        elif a1 == "X" and b2 == "X" and c3 == "X" or a3 == "X" and b2 == "X" and c1 == "X":
            break
        
        if a1 == "O" and a2 == "O" and a3== "O" or b1 == "O" and b2 == "O" and b3== "O" or c1 == "O" and c2 == "O" and c3== "O":
            break
        elif a1 == "O" and b1 == "O" and c1 == "O" or a2 == "O" and b2 == "O" and c2 == "O" or a3 == "O" and b3 == "O" and c3 == "O":
            break
        elif a1 == "O" and b2 == "O" and c3 == "O" or a3 == "O" and b2 == "O" and c1 == "O":
            break
        else:
            if Playing == "X":
                if PlX == True:
                    Playing = "O"
                else:
                    Playing = "X"
            elif Playing == "O":
                if PlX == False:
                    Playing = "X"
                else:
                    Playing = "O"
            pass
        
        
            
        
        
        
    print(f"Game Over {Playing} have won!")
    wanna = input("Press Enter to leave or write (R) to play again      ")
    if wanna.lower() == "r":
        StartGame()
    elif wanna == None:
        sys.exit()
        
    
            
            

            
    
    
if __name__ == "__main__":
    StartGame()

