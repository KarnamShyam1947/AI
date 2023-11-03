class Node:
    def __init__(self, state, parent=None, action=None):
        self.state = state
        self.parent = parent
        self.action = action

    def __hash__(self):
        return hash(self.state)

class WaterJugProblem:
    def __init__(self, capacities, goal_amount):
        self.capacities = capacities
        self.goal_amount = goal_amount
        self.initial_state = Node((0, 0))
        self.visited = set()

    def is_goal_state(self, node):
        state = node.state
        return state[0] == self.goal_amount or state[1] == self.goal_amount

    def get_successors(self, node):
        successors = []
        a, b = node.state
        ca, cb = self.capacities

        # Fill jug A
        successors.append(Node((ca, b), node, "Fill A"))

        # Fill jug B
        successors.append(Node((a, cb), node, "Fill B"))

        # Empty jug A
        successors.append(Node((0, b), node, "Empty A"))

        # Empty jug B
        successors.append(Node((a, 0), node, "Empty B"))

        # Pour water from A to B
        pour = min(a, cb - b)
        successors.append(Node((a - pour, b + pour), node, "Pour A to B"))

        # Pour water from B to A
        pour = min(ca - a, b)
        successors.append(Node((a + pour, b - pour), node, "Pour B to A"))

        return successors

    def heuristic(self, node):
        state = node.state
        return abs(state[0] - self.goal_amount) + abs(state[1] - self.goal_amount)

    def greedy_search(self):
        open_list = [(self.initial_state, 0)]

        while open_list:
            open_list.sort(key=lambda x: self.heuristic(x[0]))
            current_node, current_cost = open_list.pop(0)

            if current_node.state in self.visited:
                continue

            self.visited.add(current_node.state)

            if self.is_goal_state(current_node):
                solution_path = [current_node]
                while current_node.parent:
                    solution_path.insert(0, current_node.parent)
                    current_node = current_node.parent
                return solution_path

            for successor in self.get_successors(current_node):
                if successor not in self.visited:
                    open_list.append((successor, current_cost + 1))

        return None

    def solve(self):
        solution_path = self.greedy_search()
        if solution_path:
            print("Solution found:")
            for node in solution_path:
                print(node.state, end=" -> ")

            print("Goal reached.... ")
            print(f'Total cost : {len(solution_path) - 1}')
        else:
            print("No solution found.")

if __name__ == "__main__":
    x = int(input("Enter max capacity of jug1 : "))
    y = int(input("Enter max capacity of jug2 : "))

    capacities = (x, y)  

    goal_amount = int(input("Enter amount to measure : ")) 

    problem = WaterJugProblem(capacities, goal_amount)
    problem.solve()
