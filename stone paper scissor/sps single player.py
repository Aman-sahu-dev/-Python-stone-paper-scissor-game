#GAME [STONE], [PAPER],[SCISSOR]
print("\t\t\tSTONE\t\t\tPAPER\t\t\tSCISSOR")
def Start():
    n=input("DO YOU WANT TO PLAY: Y/N\n")
    if  n=='Y'  or n=='y':
        playerdata()
    elif  n=='N' or n=='n':
         print("THANKS FOR PLAYING THE GAME".center(50,"*"))
    else:
        Start()

def playerdata():
    player_1=input("Player 1 \n enter your name ---->     ")                                                   #ENTER YOUR NAME
    player_2="COMPUTER"
    play(player_1,player_2)

def play(player_1,player_2):
     import random
     a=int(input("\t\t PLAYER 1 \n\n choose the option given below \n STONE -- press 1 \n PAPER -- press 2 \n SCISSOR -- press 3 \n "))   #CHOOSE OPTIONS
     b= random.randint(1,3)
     if a==1 and b==1:                                                                                        #CHECKING FOR A=1 AND DIFFERENT VALUE OF B
         print("DRAW -- BOTH HAVE CHOOSEN THE STONE")
     elif a==1 and b==2:
         print(f"{player_2} WINS -- COMPUTER HAVE CHOOSEN THE PAPER.... \n YOU LOSE")          
     elif a==1 and b==3:
         print(f"{player_1} WINS -- COMPUTER HAVE CHOOSEN THE SCISSOR...")

     elif a==2 and b==2:                                                                                     #CHECKING FOR A=2 AND DIFFERENT VALUE OF B
         print("DRAW -- BOTH HAVE CHOOSEN THE PAPER")
     elif a==2 and b==1:
         print(f"{player_1} WINS -- COMPUTER HAVE CHOOSEN THE STONE")
     elif a==2 and b==3:
         print(f"{player_2} WINS -- COMPUTER HAVE CHOOSEN THE SCISSOR...\n YOU LOSE")

     elif a==3 and b==3:                                                                                    #CHECKING FOR A=3 AND DIFFERENT VALUE OF B
         print("DRAW -- BOTH HAVE CHOOSEN THE SCISSOR")
     elif a==3 and b==1:
         print(f"{player_2} WINS -- COMPUTER HAVE CHOOSEN THE STONE... \n YOU LOSE")
     elif a==3 and b==2:
         print(f"{player_1} WINS -- COMPUTER HAVE CHOOSEN THE PAPER")
     else:
         print("  INVALID INPUT   ".center(26,"!"))                                                       # INVALID INPUT
         Start()                                                                                           
     Start()
Start()                                                                                                   #END THE PROGRAM
                                                                  