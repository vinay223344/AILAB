def get_user_input():
    """ Get user input for the number of missionaries and cannibals """
    m = int(input("Enter number of Missionaries: "))
    c = int(input("Enter number of Cannibals: "))
    b_capacity = int(input("Enter Boat Capacity: "))  # Boat can carry more people
    return m, c, b_capacity

# Get input values
m, c, boat_capacity = get_user_input()

# Initial and goal states
initial_state = (m, c, 1)  # (Missionaries, Cannibals, Boat Side: 1=Left, 0=Right)
goal_state = (0, 0, 0)  # (0 Missionaries, 0 Cannibals, Boat at Right)

# Generate all possible moves up to the boat's capacity
moves = [(x, y) for x in range(boat_capacity + 1) for y in range(boat_capacity + 1) if 1 <= x + y <= boat_capacity]

def is_valid(state):
    """ Check if state is valid (no missionaries get eaten) """
    m, c, _ = state
    if m < 0 or c < 0 or m > initial_state[0] or c > initial_state[1]:  # Out of bounds
        return False
    if (m > 0 and m < c) or (initial_state[0] - m > 0 and initial_state[0] - m < initial_state[1] - c):  
        return False  # More cannibals than missionaries on either side
    return True

def get_next_states(state):
    """ Generate valid next states """
    m, c, b = state
    next_states = []
    for move in moves:
        new_m, new_c = m + move[0] * (-1 if b == 1 else 1), c + move[1] * (-1 if b == 1 else 1)
        new_state = (new_m, new_c, 1 - b)
        if is_valid(new_state):
            next_states.append(new_state)
    return next_states

def missionaries_cannibals(method):
    """ Solve using BFS and generate search tree """
    structure = [(initial_state, [])]  # (current_state, path)
    visited = set()
    parent_map = {}  # To store search tree
    while structure:
        state, path = (structure.pop(0) if method == 'bfs' else structure.pop())  # BFS using list
        if state in visited:
            continue
        visited.add(state)
        if path:
            print(f"Parent: {path[-1]} -> Child: {state}")

        # Store parent-child relationships
        if path:
            parent_map[state] = path[-1]
        # Add current state to path
        new_path = path + [state]

        # Check goal state
        if state == goal_state:
            print("\nSolution Found!")
            for step in new_path:
                print(step)
            print("\nFull Search Tree:")
            for child, parent in parent_map.items():
                print(f"{parent} -> {child}")
            return new_path

        # Expand search tree
        for next_state in get_next_states(state):
            if next_state not in visited:
                structure.append((next_state, new_path))

    print("No solution found!")
    return None

# Run  the problem
method = input("Choose search method (bfs/dfs): ").strip().lower()
missionaries_cannibals(method)
