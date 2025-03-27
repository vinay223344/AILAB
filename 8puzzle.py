goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
goal_positions = {value: (i, j) for i, row in enumerate(goal_state) for j, value in enumerate(row)}
def calculate_heuristic(state):
    """Calculate the Manhattan Distance heuristic for the given state."""
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:  # Ignore the empty space
                goal_x, goal_y = goal_positions[value]
                distance += abs(i - goal_x) + abs(j - goal_y)
    return distance

def get_neighbors(state):
    """Generate possible next states by moving the blank space."""
    moves = []
    x, y = [(i, row.index(0)) for i, row in enumerate(state) if 0 in row][0]  # Find blank space

    directions = {
        "Up": (x - 1, y),
        "Down": (x + 1, y),
        "Left": (x, y - 1),
        "Right": (x, y + 1)
    }

    for move, (new_x, new_y) in directions.items():
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
            moves.append((new_state, move))
    
    return moves

def a_star_8_puzzle(initial_state, goal_state):
    """A* search algorithm for solving the 8-puzzle."""
    open_list = [(initial_state, [])]  # (state, path)
    visited = set()
    
    while open_list:
        # Sort the open list based on f(n) = g(n) + h(n)
        open_list.sort(key=lambda x: calculate_heuristic(x[0]))
        current_state, path= open_list.pop(0)

        if current_state == goal_state:
            print("\nSolution Found!")
            print("Steps to Goal:")
            for step in path:
                print(step)
            print("Total Cost:", len(path))

        visited.add(tuple(map(tuple, current_state)))  # Convert state to a tuple for set storage

        for neighbor, move in get_neighbors(current_state):
            if tuple(map(tuple, neighbor)) not in visited:
                open_list.append((neighbor, path + [move]))

    print("No Solution Found!")

# Taking user input for the initial state
print("Enter the initial 8-puzzle state row by row (use 0 for the empty space):")
initial_state = [list(map(int, input().split())) for _ in range(3)]
a_star_8_puzzle(initial_state, goal_state)
