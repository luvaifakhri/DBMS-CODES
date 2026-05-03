#1. Create a program where a simple AI plays Tic-Tac-Toe using basic rules.
import random

board = [" " for _ in range(9)]

def print_board():
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
        print("-" * 10)
    

def check_winner(player):
    # All 8 possible winning combinations
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Vertical
        [0, 4, 8], [2, 4, 6]             # Diagonal
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def human_move():
    try:
        val = int(input("Enter position (0-8): "))
        if 0 <= val <= 8 and board[val] == " ":
            board[val] = "X"
        else:
            print("Invalid move. Try again.")
            human_move()
    except ValueError:
        print("Please enter a number between 0-8.")
        human_move()

def ai_move():
    empty_spots = [i for i, spot in enumerate(board) if spot == " "]
    if empty_spots:
        move = random.choice(empty_spots)
        board[move] = "O"
        print(f"AI chose position {move}")

# --- Main Game Loop ---
while " " in board:
    print_board()
    
    # 1. Human Turn
    human_move()
    if check_winner("X"):
        print_board()
        print("Congratulations! You (X) win!")
        break
    
    if " " not in board: break # Check for Draw

    # 2. AI Turn
    ai_move()
    if check_winner("O"):
        print_board()
        print("AI (O) wins! Better luck next time.")
        break

if not check_winner("X") and not check_winner("O"):
    print_board()
    print("It's a draw!")

=========================================================================================================
#2. Write programs to perform Depth-First Search (DFS) and Breadth-First Search (BFS) on a graph or tree.
=========================================================================================================
# BFS
from collections import deque
def bfs_search(graph, start, target):
    queue = deque([start])
    visited = {start}
    while queue:
        node = queue.popleft()
        print(f"Checking node: {node}")
        if node == target:
            return f"Success! Node '{target}' found."
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return "Node not found."
# Sample Graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [], 'E': [], 'F': []
}
print(bfs_search(graph, 'A', 'B'))

#DFS
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [], 'E': [], 'F': []
}

def dfs_search(graph, node, target, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(node)
    print(f"Checking node: {node}")
    
    if node == target:
        return True # Found it!

    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            if dfs_search(graph, neighbor, target, visited):
                return True
                
    return False
# Execution
target_node = 'B'
if dfs_search(graph, 'A', target_node):
    print(f"Success! Node '{target_node}' found.")
else:
    print("Node not found.")

===============================================================
#3. Solve the "Tower of Hanoi" using a set of production rules.
================================================================
def tower_of_hanoi(n, source, destination, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    tower_of_hanoi(n-1, source, auxiliary, destination)
    print(f"Move disk {n} from {source} to {destination}")
    tower_of_hanoi(n-1, auxiliary, destination, source)

tower_of_hanoi(3, 'A', 'C', 'B')

=========================================================================
#4. Analyse a problem like a chess game and list its key characteristics.
=========================================================================
def analyze_chess():
    print("Chess Game - Problem Characteristics\n")
    print("1. Number of Players   : Two-player")
    print("2. Type of Game        : Adversarial")
    print("3. Turn-Based          : Yes")
    print("4. Environment         : Fully Observable")
    print("5. Deterministic       : Yes")
    print("6. Nature of Game      : Zero-sum")
    print("7. State Space         : Very Large")
    print("8. Search Type         : Minimax / Adversarial Search")
    print("9. Information         : Perfect Information")
    print("10. Goal               : Checkmate the opponent")

analyze_chess()

====================================================================
#5. Solve the "8 Puzzle Problem" using the generate-and-test method.
====================================================================
import random

# The Goal State we want to reach
goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
# Initial scrambled state
state = [1, 2, 0, 3, 4, 6, 7, 5, 8]
def show(p):
    """Helper function to print the board as a 3x3 grid"""
    print(p[0:3])
    print(p[3:6])
    print(p[6:9])
    print()
def generate(p):
    """Generates a random legal move for the blank space (0)"""
    new = p[:]
    i = new.index(0) # Find position of blank space
    moves = []    
    # Check legal moves (Up, Down, Left, Right)
    if i > 2: moves.append(i - 3)      # move up
    if i < 6: moves.append(i + 3)      # move down
    if i % 3 != 0: moves.append(i - 1) # move left
    if i % 3 != 2: moves.append(i + 1) # move right 
    # Pick one move randomly
    j = random.choice(moves)    
    # Swap the blank space with the chosen neighbor
    new[i], new[j] = new[j], new[i]
    return new
# --- Main Execution ---
count = 0
print("Initial State:")
show(state)
# The "Test" part of Generate and Test
while state != goal:
    state = generate(state)
    count += 1
    # Note: show(state) is optional here if you want to see every step    
print("Goal State Reached!")
show(state)
print("Generated States (Total Steps):", count)

======================================================================
#6. Solve the "Monkey Banana Problem" using a set of production rules.
======================================================================
# Initial positions
monkey = "A"
box = "B"
banana = "C"
on_box = False
has_banana = False

print(f"Initial State: Monkey at {monkey}, Box at {box}, Banana at {banana}")

# Rule 1: If monkey is on floor AND at box -> climb on box
def move_to_box():
    global monkey
    if monkey != box:
        print(f"Action: Monkey moves from {monkey} to {box}")
        monkey = box

# Rule 2: If monkey is on floor AND at box -> push box to banana position
def push_box():
    global monkey, box
    if monkey == box and box != banana:
        print(f"Action: Monkey pushes box from {box} to {banana}")
        box = banana
        monkey = banana

# Rule 3: If monkey and box are at banana -> climb box
def climb_box():
    global on_box
    if monkey == box == banana:
        print("Action: Monkey climbs on the box")
        on_box = True

# Rule 4: If monkey on box AND at banana -> grasp banana
def grasp_banana():
    global has_banana
    if on_box and monkey == banana:
        print("Action: Monkey grasps the banana!")
        has_banana = True

# --- Execution of Production Rules ---
move_to_box()
push_box()
climb_box()
grasp_banana()

if has_banana:
    print("Goal State Reached: Monkey has the banana.")

==========================================================================================
#7. Write a program to find the best solution for a numerical problem using hill climbing.
==========================================================================================
def function(x): return -(x**2) + 10  # A hill with a peak at x=0

def hill_climbing(start_x):
    current_x = start_x
    step = 0.1
    while function(current_x + step) > function(current_x):
        current_x += step
    return current_x

print(f"Best solution: {hill_climbing(-2)}")

===================================================================================
#8. Create a program to perform Best-First Search on a graph and display the steps.
===================================================================================
# Sample Graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [], 'E': [], 'F': []
}

# Heuristic values (estimated distance to goal)
h = {'A': 5, 'B': 2, 'C': 4, 'D': 0, 'E': 1, 'F': 6}

def best_first_search(graph, start, target):

    open_list = [start]
    visited = set()
    
    print("Best-First Search Steps :")
    
    while open_list:
        current = min(open_list, key=lambda x: h[x])
        open_list.remove(current)
        
        print(f"Visiting: {current}")
        
        if current == target:
            print("Goal reached!")
            return
        
        visited.add(current)
        
        # Add neighbors to the open_list
        for neighbor in graph[current]:
            if neighbor not in visited and neighbor not in open_list:
                open_list.append(neighbor)

# Execution
best_first_search(graph, 'A', 'D')

========================================================================
#9. Solve a problem using AND-OR graphs and implement the AO* algorithm.
========================================================================
graph = {
    'A': [['B'], ['C']], 
    'B': [['D', 'E']],
    'C': [['F', 'G']],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

h = {'D': 1, 'E': 2, 'F': 2, 'G': 1, 'B': 0, 'C': 0, 'A': 0}

def AO_star(node):
    
    if graph[node] == []:
        return h[node], [node]
    
    best_cost = float('inf')
    best_path = []
    for children in graph[node]:
        cost = 0
        path = []        
        for c in children:
            c_cost, c_path = AO_star(c)
            cost += c_cost
            path += c_path            
        if cost < best_cost:
            best_cost = cost
            best_path = [node] + path
            
    return best_cost, best_path

# Run AO* from root
cost, path = AO_star('A')
print("Best Solution Path:", path)
print("Minimum Cost:", cost)

===========================================================
#10. Write a program to check logical statements for truth.
===========================================================
def check_logic(p, q):
    statement = p and q
    return f"P={p}, Q={q} | Statement (P and Q) is {statement}"

print(check_logic(True, False))
print(check_logic(True, True))
print(check_logic(False, True))

===========================================================
#11. Create a decision tree to classify or make decisions.
===========================================================
def classify(color, texture):
    if color == "Red":
        if texture == "Smooth":
            return "Apple"
        else:
            return "Strawberry"
    else:
        return "Broccoli"

print(f"The item is a: {classify('Red', 'Smooth')}")
