#GAME [STONE], [PAPER],[SCISSOR]
print("START THE GAME")
n=int(input(" ENTER 1 To START  "))                                                                                            #START 
if n==1:
     player_1=input("player_1 \n enter your name ---->     ")                                                                  #ENTER YOUR NAME
     player_2=input(" player_2 \n enter your name ---->     ")                                                                 #ENTER YOUR NAME


a=int(input(" PLAYER 1 \n choose the option given below \n STONE -- press 1 \n PAPER -- press 2 \n SCISSOR -- press 3 \n "))   #CHOOSE OPTIONS
b=int(input(" PLAYER 2 \n choose the option given below \n STONE -- press 1 \n PAPER -- press 2 \n SCISSOR -- press 3 \n "))
if a==1 and b==1:                                                                                                              #CHECKING FOR A=1 AND DIFFERENT VALUE OF B
    print("DRAW")
elif a==1 and b==2:
    print(f"{player_2} WINS")          
elif a==1 and b==3:
    print(f"{player_1} WINS")

elif a==2 and b==2:                                                                                                           #CHECKING FOR A=2 AND DIFFERENT VALUE OF B
    print("DRAW")
elif a==2 and b==1:
    print(f"{player_1} WINS")
elif a==2 and b==3:
    print(f"{player_2} WINS")

elif a==3 and b==3:                                                                                                          #CHECKING FOR A=3 AND DIFFERENT VALUE OF B
    print("DRAW")
elif a==3 and b==1:
    print(f"{player_2} WINS")
elif a==3 and b==2:
    print(f"{player_1} WINS")
else:
    print("  INVALID INPUT   ".center(26,"!"))                                                                            # INVALID INPUT

print("THANKS FOR PLAYING THE GAME".center(50,"*"))                                                                       #END THE PROGRAM