class Node:
    def __init__(self, parent = None):
        self.x = 0
        self.y = 0
        self.rule_no = 0
        self.parent = parent

    def __repr__(self) -> str:
        return f'({self.x}, {self.y})'
    
class WaterJug:
    queue = None

    def __init__(self):
        self.queue = list()

    def is_empty(self, list):
        return len(list) == 0
    
    def pushNodes(self, nodes):
        for node in nodes:
            self.queue.append(node)

    def popNode(self):
        if self.is_empty(self.queue):
            return None
        
        else:
            return self.queue.pop(0)
    
    def generateChildren(self, node):
        childrenNodes = list()

        for i in range(1, 9):
            childNode = apply_rules(node, i)

            if childNode != None:
                childrenNodes.append(childNode)

        return childrenNodes
    
    def bfs_solver(self, startState, goalState):
        self.queue.append(startState)

        while not self.is_empty(self.queue):
            currentNode = self.popNode()

            if isGoalState(currentNode, goalState):
                return currentNode
            
            childrenNodes = self.generateChildren(currentNode) 
            self.pushNodes(childrenNodes)

        return None

def apply_rules(node, rule_no):
    x = node.x
    y = node.y

    if rule_no == 1:
        if x < jug1:
            x = jug1

        else:
            return None
        
    elif rule_no == 2:
        if y < jug2:
            y = jug2

        else:
            return None
        
    elif rule_no == 3:
        if x > 0:
            x = 0

        else:
            return None
        
    elif rule_no == 4:
        if y > 0:
            y = 0

        else:
            return None
        
    elif rule_no == 5:
        if x + y >= jug1:
            y = y - (jug1-x)
            x = jug1

        else:
            return None
        
    elif rule_no == 6:
        if x + y >= jug2:
            x = x - (jug2-y)
            y = jug2

        else:
            return None
        
    elif rule_no == 7:
        if x + y < jug1:
            x = x + y
            y = 0

        else:
            return None
        
    elif rule_no == 8:
        if x + y < jug2:
            y = x + y
            x = 0

        else:
            return None

    if x == node.x and y == node.y:
        return None
    

    nextNode = Node(node)
    nextNode.x = x
    nextNode.y = y
    nextNode.rule_no = rule_no
    nextNode.parent = node

    return nextNode

def isGoalState(currentState, goalState):
    if(currentState.x == goalState.x) or (currentState.y == goalState.x):
        return True
    
    return False

def printSolution(solutionState):
    steps = list()
    temp = solutionState

    while temp is not None:
        steps.append(temp)
        temp = temp.parent

    steps.reverse()

    print('Path : ', end=" ")
    for rule, sept in enumerate(steps):
        if rule == 0:
            continue

        print(sept.rule_no, end=", ")
    print("")

    print('BFS traversal : ', end = " ")
    for sept in steps:
        print(sept, end=" -> ")

    print(f'Reached Goal State....\nTotal cost : {len(steps) - 1}')

if __name__ == '__main__':
    jug1 = int(input("Enter maximum capacity of jug1 : "))
    jug2 = int(input("Enter maximum capacity of jug2 : "))

    # goalStateInput = list(map(int, input('Enter goal state(x y) : ').split(" ")))

    startState = Node(None)

    goalState = Node(None)
    goalState.x = int(input('Enter amount to measure : '))
    goalState.y = 0

    solver = WaterJug()
    solutionState = solver.bfs_solver(startState, goalState)

    if solutionState:
        print("\n\nSolution found...... :)")
        printSolution(solutionState)

    else:
        print("\n\nFailed to find Solution...... :( ")
