import numpy as np

class Node:
    def __init__(self, state = None, parent = None, action = None):
        self.state = state
        self.parent = parent
        self.action = action

    def __repr__(self) -> str:
        return f'{self.action}\n{self.state[0]}'

def is_goal_state(current_node, goal_node):
    if (current_node == goal_node).all():
        return True
    
    return False

def valid_rules(current_state):
    _, (row, col) = current_state
    rules = list()

    if row > 0: # up
        rules.append(1)
    
    if row < 2: # down
        rules.append(2)
    
    if col > 0: # left
        rules.append(3)
    
    if col < 2: # right
        rules.append(4)
    
    return rules
    
def apply_rule(current_state, rno):
    state, (row, col) = current_state

    if rno == 1: # up
        state_copy = np.copy(state)
        state_copy[row][col] = state_copy[row - 1][col]
        state_copy[row - 1][col] = 0
        return [state_copy, (row - 1, col)]
    
    if rno == 2: # down
        state_copy = np.copy(state)
        state_copy[row][col] = state_copy[row + 1][col]
        state_copy[row + 1][col] = 0
        return [state_copy, (row + 1, col)] 

    if rno == 3: # left
        state_copy = np.copy(state)
        state_copy[row][col] = state_copy[row][col - 1]
        state_copy[row][col - 1] = 0
        return [state_copy, (row, col - 1)] 
    
    if rno == 4: # right
        state_copy = np.copy(state)
        state_copy[row][col] = state_copy[row][col + 1]
        state_copy[row][col + 1] = 0
        return [state_copy, (row, col + 1)] 

def generate_children(current_state):
    state, (row, col) = current_state
    children = list()

    if row > 0: # up
        state_copy = np.copy(state)
        state_copy[row][col] = state_copy[row - 1][col]
        state_copy[row - 1][col] = 0
        children.append(('up', [state_copy, (row - 1, col)])) 
    
    if row < 2: # down
        state_copy = np.copy(state)
        state_copy[row][col] = state_copy[row + 1][col]
        state_copy[row + 1][col] = 0
        children.append(('down', [state_copy, (row + 1, col)])) 

    if col > 0: # left
        state_copy = np.copy(state)
        state_copy[row][col] = state_copy[row][col - 1]
        state_copy[row][col - 1] = 0
        children.append(('left', [state_copy, (row, col - 1)])) 
    
    if col < 2: # right
        state_copy = np.copy(state)
        state_copy[row][col] = state_copy[row][col + 1]
        state_copy[row][col + 1] = 0
        children.append(('right', [state_copy, (row, col + 1)])) 

    return children

def print_solution(solution_node):
    steps = list()
    temp = solution_node

    while temp.parent is not None:
        steps.append(temp)
        temp = temp.parent

    steps.reverse()
    for state in steps:
        print(f'{state}')

class Puzzle:
    queue = None
    visited = None

    def solve_puzzle(self, start_state, start_idx, goal_state, goal_idx):
        start = [start_state, start_idx]

        current = start
        steps = 0

        while True:
            steps += 1
            rules = valid_rules(current)
            print('\nCurrent State : ')
            print(current[0])

            print("\nValid rules : ")
            for rule in rules:
                if rule == 1:
                    print("1 : up")

                if rule == 2:
                    print("2 : down")

                if rule == 3:
                    print("3 : left")

                if rule == 4:
                    print("4 : right")

            rno = int(input(f"Enter rule number : "))

            if rno not in rules:
                print("invalid rule..... :( \n")
                continue

            res = apply_rule(current, rno)

            current = res

            if is_goal_state(current[0], goal_state):
                print("Goal state reached.... :) \n")
                print(f"you reached goal state in {steps} steps")
                break
        
def input_array(type:str):
    arr = list()

    print(f"Enter {type} state : ")
    for i in range(3):
        row = list(map(int, input(f"\trow-{i+1} : ").split(" ")))
        arr.append(row)

    state = np.array(arr)

    idx = tuple(map(int, input("Enter empty element position : ").split(" ")))
    return state, idx

if __name__ == '__main__':
    start_state, start_idx = input_array("start")
    goal_state, goal_idx = input_array("goal")

    print('\nstart state:')
    print(start_state)

    print('\ngoal state:')
    print(goal_state)

    p = Puzzle()   
    solution = p.solve_puzzle(start_state, start_idx, goal_state, goal_idx)
    
    print("")