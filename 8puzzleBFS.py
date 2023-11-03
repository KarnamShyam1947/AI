import numpy as np
import time

class Node:
    def __init__(self, state=None, parent=None, action=None):
        self.state = state
        self.parent = parent
        self.action = action

    def __repr__(self) -> str:
        return f'action: {self.action}\n{self.state[0]}\n'

def print_solution(solution, goal_node):
    steps = list()
    temp = solution

    while temp is not None:
        steps.append(temp)
        temp = temp.parent

    steps.reverse()
    print(" ")
    for step in steps:
        print(step)

    print(goal_node)
    print(f'Total cost : {len(steps) - 1}')

def is_goal_state(current_node, goal_node):
    if (current_node.state[0] == goal_node.state[0]).all():
        return True

    return False

def generate_children(current_node):
    start, (row, col) = current_node
    children = list()

    if row > 0:
        state_copy = np.copy(start)
        state_copy[row][col] = state_copy[row - 1][col]
        state_copy[row - 1][col] = 0
        children.append(('up', [state_copy, (row - 1, col)]))

    if row < 2:
        state_copy = np.copy(start)
        state_copy[row][col] = state_copy[row + 1][col]
        state_copy[row + 1][col] = 0
        children.append(('down', [state_copy, (row + 1, col)]))
    
    if col > 0:
        state_copy = np.copy(start)
        state_copy[row][col] = state_copy[row][col - 1]
        state_copy[row][col - 1] = 0
        children.append(('left', [state_copy, (row, col - 1)]))
    
    if col < 2:
        state_copy = np.copy(start)
        state_copy[row][col] = state_copy[row][col + 1]
        state_copy[row][col + 1] = 0
        children.append(('right', [state_copy, (row, col + 1)]))

    return children

class Puzzle:
    visited = None
    queue = None
    explored = None

    def __init__(self):
        self.visited = list()
        self.queue = list()
        self.explored = 0

    def is_empty(self):
        return len(self.queue) == 0
    
    def push(self, node):
        self.queue.append(node)

    def pop(self):
        return self.queue.pop(0)
    
    def is_visited(self, state):
        for st in self.visited:
            if (st.state[0] == state[0]).all():
                return True
            
        return False
    
    def contains_in_queue(self, state):
        for st in self.queue:
            if (st.state[0] == state[0]).all():
                return True
            
        return False
    
    def solver(self, start_state, start_idx, goal_state, goal_idx):
        start = [start_state, start_idx]
        start_node = Node(state=start, parent=None, action='*Start State')

        goal = [goal_state, goal_idx]
        goal_node = Node(state=goal, parent=None, action="*Goal State")

        self.push(start_node)

        print('\nBFS started.....')
        while not self.is_empty():
            self.explored += 1
            current_node = self.pop()

            if is_goal_state(current_node, goal_node):
                print('Solution Found..... :)')
                return current_node, self.explored, goal_node
            
            self.visited.append(current_node)
            children = generate_children(current_node.state)

            for action, state in children:
                if not self.contains_in_queue(state) and not self.is_visited(state):
                    child = Node(state=state, parent=current_node, action=action)
                    self.push(child)

def get_array(type):
    arr = list()

    print(f"\nEnter {type} state : ")
    for i in range(3):
        row = list(map(int, input(f"\trow-{i + 1} : ").split(" ")))
        arr.append(row)

    return np.array(arr)

def get_index(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 0:
                return (i, j)
            
    return None

if __name__ == '__main__':
    print('NAME : KARNAM SHYAM\t\t\tREG. NO. : 21MIC7182\n')
    start_state = get_array('start')
    goal_state = get_array('goal')

    if get_index(start_state) and get_index(goal_state):
        start_idx = get_index(start_state)
        goal_idx = get_index(goal_state)
    
    else:
        print("Invalid input")
    

    start_time = time.time()
    p = Puzzle()
    s, ex, goalNode = p.solver(start_state, start_idx, goal_state, goal_idx)
    end_time = time.time()

    print_solution(s, goalNode)
    execution_time = (end_time - start_time)*(10**3)

    print(f'Total Execution Time :  {execution_time:.2f}ms')
    print(f"Number of explored nodes : {ex}")
