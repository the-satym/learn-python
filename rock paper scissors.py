#date: 15 jan 2025

choose=int(input(" enter '1' for first way and enter '2' for second:-   "))
import random
import sys
if choose==1:
    moves={'rock':' 🪨', 'paper': '📃' , 'scissors': '✂️'}
    valid_moves=list(moves.keys())
    while True:
        print("enter 'exit' if you want to exit")
        user_moves=input("rock, paper , scissors ????  :-   ").lower()
        if user_moves=='exit':
            print("GOODBYE!!! ")
            sys.exit()
        if user_moves not in moves.keys():
            print("invalid choice!!! choose between the given options:   ")
            continue
        ai_moves=random.choice(valid_moves)
        print(f"YOU : {moves[user_moves]}")
        print(f"AI  :  {moves[ai_moves]}")
        # conditions
        if user_moves==ai_moves:
            print("it's a tie ")
        elif user_moves=='rock' and ai_moves=='scissors':
            print("you wins")
        elif user_moves=='scissors' and ai_moves=='paper':
            print("you wins")
        elif user_moves=='paper' and ai_moves=='rock':
            print('you wins')
        else:
            print("ai wins")

if choose==2:
    a={"rock","paper","scissor"}
    print('''choose anyone of these
    rock
    paper
    scissor''')
    b=str(input("enter your choice"))
    c=a.pop()
    print(c)
    if b==c:
        print("match draw")
    elif b=="rock" and c=="scissor" or b=="scissor" and c=="paper" or b=="paper" and c=="rock":
        print("you won")
    else:
        print("computer won")
else:
    print("wrong choice")