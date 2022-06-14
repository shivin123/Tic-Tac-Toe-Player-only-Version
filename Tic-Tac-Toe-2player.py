#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
con=0
board_start=[[" "," "," "],[" "," "," "],[" "," "," "]]

board=board_start

def print_board(board):
    print("|   | 1 | 2 | 3 |")
    print("| 1 | "+board[0][0]+" | "+board[0][1]+" | "+board[0][2]+" |")
    print("| 2 | "+board[1][0]+" | "+board[1][1]+" | "+board[1][2]+" |")
    print("| 3 | "+board[2][0]+" | "+board[2][1]+" | "+board[2][2]+" |")
    
def coin_vis(coin_vis_val):
    
    if coin_vis_val==1:
        print('       ')
        print("[-----]")
        print("[     ]")
        print("[  H  ]")
        print("[     ]")
        print("[-----]")
        print('       ')
        
    if coin_vis_val==0:
        print('       ')
        print("[-----]")
        print("[     ]")
        print("[  T  ]")
        print("[     ]")
        print("[-----]")
        print('       ')
        
coin=[0, 1]


input("Press any key to flip a coin to decided who starts: ")

speed_tie_breaker=random.choice(coin)
                                
if speed_tie_breaker==1:
    coin_vis(1)
    print('Heads')
    print('X plays first')
    p=1
if speed_tie_breaker==0:
    coin_vis(0)
    print('Tails')
    print('O plays first')
    p=0

print_board(board)

def player_input(p):
    inp=input("Enter the coorditnates of where you whish to play: ")
    am=[1,2,3]
    if int(inp[0]) not in am or int(inp[2]) not in am:
        inp=input("Enter the coorditnates of where you whish to play: ")
    if board[int(inp[0])-1][int(inp[2])-1]==" ":
        if p==1:
            board[int(inp[0])-1][int(inp[2])-1]="X"
        if p==0:
            board[int(inp[0])-1][int(inp[2])-1]="O"
        print_board(board)
        return True
    else:
        print("That spot is filled:")
        inp=input("Enter the coorditnates of where you whish to play: ")
        player_input(p)
        

ge=0
while ge==0:
    if con==9:
        print("No more spaces, game is a tie")
        ge=1
        break
    
    for i in range(3):
        if board[0][i]=="X" and board[1][i]=="X" and board[2][i]=="X":
            print("Player X wins!")
            ge=1
            break
        if board[0][i]=="O" and board[1][i]=="O" and board[2][i]=="O":
            print("Player O wins!")
            ge=1
            break
        if board[i][0]=="X" and board[i][1]=="X" and board[i][2]=="X":
            print("Player X wins!")
            ge=1
            break
        if board[i][0]=="O" and board[i][1]=="O" and board[i][2]=="O":
            print("Player O wins!")
            ge=1
            break
            
    if board[0][0]=="X" and board[1][1]=="X" and board[2][2]=="X":
        print("Player X wins!")
        ge=1
        break
    if board[0][0]=="O" and board[1][1]=="O" and board[2][2]=="O":
        print("Player O wins!")
        ge=1
        break
    if board[0][2]=="X" and board[1][1]=="X" and board[2][0]=="X":
        print("Player X wins!")
        ge=1
        break
    if board[0][2]=="O" and board[1][1]=="O" and board[2][0]=="O":
        print("Player O wins!")
        ge=1
        break
    if ge==0:    
        player_input(p)
        con+=1
        if p==1:
            p=0
        else:
            p=1
    


# In[ ]:




