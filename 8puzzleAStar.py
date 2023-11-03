import numpy as np
import time

def print_solution(node):
    temp = node
    steps = list()

    while temp is not None:
        steps.append(temp)
        temp = temp.parent

    steps.reverse()

    for step in steps:
        print(step)

    print('Total cost : ', len(steps) - 1)

class Node:
    def __init__(self,data,level,f_value, action, parent):
        self.state = data
        self.level = level
        self.f_value = f_value
        self.action = action
        self.parent = parent

    def __repr__(self) -> str:
        return f'action : {self.action}\n{self.state}\n'
    
    def generate_children(self, current_node):
        state = current_node.state
        row, col = self.find(current_node.state, 0)
        children = list()

        if row > 0:
            state_copy = np.copy(state)
            state_copy[row][col] = state_copy[row - 1][col]
            state_copy[row - 1][col] = 0

            child_node = Node(state_copy,current_node.level+1,0, 'up', current_node)
            children.append(child_node)

        if row < 2:
            state_copy = np.copy(state)
            state_copy[row][col] = state_copy[row + 1][col]
            state_copy[row + 1][col] = 0

            child_node = Node(state_copy,current_node.level+1,0, 'down', current_node)
            children.append(child_node)
        
        if col > 0:
            state_copy = np.copy(state)
            state_copy[row][col] = state_copy[row][col - 1]
            state_copy[row][col - 1] = 0

            child_node = Node(state_copy,current_node.level+1,0, 'left', current_node)
            children.append(child_node)
        
        if col < 2:
            state_copy = np.copy(state)
            state_copy[row][col] = state_copy[row][col + 1]
            state_copy[row][col + 1] = 0

            child_node = Node(state_copy,current_node.level+1,0, 'right', current_node)
            children.append(child_node)

        return children
                   
    def find(self,puz,x):
        
        for i in range(0,len(self.state)):
            for j in range(0,len(self.state)):
                if puz[i][j] == x:
                    return i,j
                
        return None

class Puzzle:
    def __init__(self,size):
        
        self.n = size
        self.open = []
        self.closed = []

    def input_puzzle(self):
        
        state = []
        for i in range(0,self.n):
            row = list(map(int, input(f"\trow-{i + 1} : ").split(" ")))
            state.append(row)

        return state

    def f(self,start,goal):
        return self.h(start.state,goal)+start.level

    def h(self,start,goal): # number of misplaced titles
        count = 0
        for i in range(0,self.n):
            for j in range(0,self.n):
                if start[i][j] != goal[i][j] and start[i][j] != 0:
                    count += 1

        return count
        
    def solver(self):
        
        print("\nEnter the start state matrix")
        start = self.input_puzzle()

        print("\nEnter the goal state matrix")        
        goal = self.input_puzzle()

        start = Node(start,0,0, "*Start Node", None)
        start.f_value = self.f(start,goal)
        
        self.open.append(start)
        explored = 0
        start_time = time.time()

        print('\nAStar started.....')
        while True:
            explored += 1
            cur = self.open[0]
            
            if(self.h(cur.state,goal) == 0):
                end_time = time.time()
                execution_time = (end_time - start_time)*(10**3)
                print('Solution Found..... :)\n')
                return cur, explored, execution_time

            for i in cur.generate_children(cur):
                i.f_value = self.f(i,goal)
                self.open.append(i)
                
            self.closed.append(cur)
            del self.open[0]

            
            self.open.sort(key = lambda x:x.f_value,reverse=False)


if __name__ == '__main__':
    print('NAME : KARNAM SHYAM\t\t\tREG. NO. : 21MIC7182\n')
    solver = Puzzle(3)
    solution, explored_nodes, execution_time = solver.solver()

    print_solution(solution)

    print(f'Total Execution Time :  {execution_time:.2f}ms')
    print('Number of explored nodes : ', explored_nodes)
