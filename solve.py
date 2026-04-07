===================================================
#Code Pair 1
#Q1. Tic-Tac-Toe Board (Matrix format)
board = [[' ' for _ in range(3)] for _ in range(3)]

def print_matrix_board():
    for row in board:
        print("|".join(row))
        print("-" * 5)

print_matrix_board()
----------------------------------------------------
#Q2. Student Records Dictionary
students = {}

def manage_students():
    while True:
        action = input("Enter 'add' to add, 'view' to display, or 'exit': ").lower()
        if action == 'add':
            roll = input("Roll No: ")
            name = input("Name: ")
            students[roll] = name
        elif action == 'view':
            print("Records:", students)
        elif action == 'exit':
            break

manage_students()
========================================================
#Code Pair 2
#Q1. AI Random Move
import random
# Using your board logic
def ai_play(board):
    empty_spots = [i for i, val in enumerate(board) if val == " "]
    if empty_spots:
        ai_move = random.choice(empty_spots)
        board[ai_move] = "O"
--------------------------------------------------------
#Q2. Menu-driven Calculator
def calc():
    x = float(input("Num 1: "))
    y = float(input("Num 2: "))
    op = input("Op (+, -, *, /): ")
    if op == '+': print(x + y)
    elif op == '-': print(x - y)
    elif op == '*': print(x * y)
    elif op == '/': print(x / y if y != 0 else "Error")

calc()
=========================================================
#Code Pair 3
#Q1. Check Win Conditions
def check_win(board, p):
    win_conditions = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for a, b, c in win_conditions:
        if board[a] == board[b] == board[c] == p:
            return True
    return False
---------------------------------------------------------
#Q2. List Operations
nums = [10, 20, 30]
nums.append(40)      # Insertion
nums.remove(20)      # Deletion
print(30 in nums)    # Searching (True)
==========================================================
#Code Pair 4
#Q1. Input Validation
def user_play(board):
    while True:
        try:
            pos = int(input("Enter pos (1-9): ")) - 1
            if 0 <= pos <= 8 and board[pos] == " ":
                board[pos] = "X"
                break
            else:
                print("Invalid or occupied!")
        except ValueError:
            print("Enter a number.")
----------------------------------------------------------
#Q2. Python Modules (Random/Math)
import math, random
print(math.sqrt(16))     # Op 1: Square root
print(math.factorial(5)) # Op 2: Factorial
print(random.randint(1,10)) # Op 3: Random Int
===========================================================
#Code Pair 5
#Q1. Complete Game
import random 
board=[' ']*9
def print_board():
    print()
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--|---|---")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--|---|---")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()
def check_win (p):
    win=((0,1,2),(3,4,5),(6,7,8),
         (0,3,6),(1,4,7),(2,5,8),
         (0,4,8),(2,4,6))
    for a,b,c in win:
        if board[a]==p and board[b]==p and board[c]==p:
            return True
def user_play():
    user=int(input("enter the position (1 to 9):"))-1
    if board[user]==" ":
        board[user]="X"
    else:
        print("not valid input retry")
        user_play()
def ai_play():
    while True:
        ai=random.randint(0,8)
        if board[ai]==" ":
            board[ai]="O"
            break
def draw():
    return " " not in board
while True:
    print_board()
    user_play()
   
    if check_win('X'):
        print_board()
        print("user win")
        break
    
    ai_play()
    
    if check_win('O'):
        print_board()
        print("ai win")
        break
    
    if draw():
        print_board()
        print("match was draw")
        break
------------------------------------------------------------
#Q2. List Stats
nums = [5, 12, 8, 20, 3]
print("Max:", max(nums))
print("Min:", min(nums))
print("Avg:", sum(nums)/len(nums))
============================================================
#Code Pair 6
#Q1. Check Draw
def check_draw(board):
    return " " not in board
------------------------------------------------------------
#Q2. Unique Elements
items = input("Enter items separated by space: ").split()
unique_items = list(set(items))
print("Unique:", unique_items)
============================================================
#Code Pair 7
#Q1. Enhanced AI (Block Move)
def enhanced_ai(board):
    # Check if opponent (X) is about to win and block
    win_conditions = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for a, b, c in win_conditions:
        line = [board[a], board[b], board[c]]
        if line.count("X") == 2 and line.count(" ") == 1:
            # Find the empty spot and fill it
            for pos in (a, b, c):
                if board[pos] == " ":
                    board[pos] = "O"
                    return
    ai_play() # Fallback to random if no block needed
------------------------------------------------------------------
#Q2. Prime Number Check
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

num = int(input("Check prime: "))
print(is_prime(num))
==================================================================



















