import heapq

def print_solution(solution):
    steps = list()
    temp = solution

    while temp is not None:
        steps.append(temp)
        temp = temp.parent

    steps.reverse()
    
    for step in steps:
        print(step)


class Node:
    def __init__(self, state, parent=None):
        self.state = state  
        self.parent = parent  

    def __repr__(self) -> str:
        return f'({self.state[0], self.state[1]})'

    def __lt__(self, other):
        return self.heuristic() < other.heuristic()

    def is_goal(self, target):
        return self.state == target

    def heuristic(self):
        # Heuristic function (you can choose a different heuristic)
        # In this example, we use the sum of the two jug's contents as a heuristic
        return self.state[0] + self.state[1]

    def apply_rules(self, state, rule_no):
        x, y = state

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
            
        return (x, y)

    def generate_children(self, capacities):
        children = []
        for i in range(1, 9):
            child = self.apply_rules(self.state, i)

            if child is not None:
                children.append(Node(child, self))

        return children

def best_first_search(start, target, capacities):
    visited = set()
    priority_queue = [start]

    while priority_queue:
        current_node = heapq.heappop(priority_queue)

        if current_node.is_goal(target):
            
            solution_path = []
            while current_node:
                solution_path.insert(0, current_node.state)
                current_node = current_node.parent

            return solution_path

        visited.add(current_node.state)

        children = current_node.generate_children(capacities)
        for child in children:
            if child.state not in visited:
                heapq.heappush(priority_queue, child)

    return None  

if __name__ == "__main__":
    jug1 = int(input('Enter max capacity of jug1 : '))
    jug2 = int(input('Enter max capacity of jug2 : '))

    capacities = (jug1, jug2)  

    target_state = (int(input('Enter amount to measure : ')), 0)  

    start_state = (0, 0)  
    start_node = Node(start_state)
    solution_path = best_first_search(start_node, target_state, capacities)

    if solution_path:
        for state in solution_path:
            print(state, end=" -> ")

        print("Goal reached")    
        print(f'Total Cost : {len(solution_path) - 1}')

    else:
        print("No solution found.")
