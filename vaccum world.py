def get_user_input():
    """ Get user input for number of rooms and their cleanliness status """
    num_rooms = int(input("Enter the number of rooms: "))
    dirt_positions = []

    for i in range(num_rooms):
        status = input(f"Is room {i} dirty? (yes/no): ").strip().lower()
        if status == "yes":
            dirt_positions.append(i)  # Store dirty rooms

    start_room = int(input("Enter the starting room number: "))
    
    return num_rooms, dirt_positions, start_room

# Get input from user
num_rooms, dirt_positions, start_room = get_user_input()

def get_next_states(state, num_rooms):
    """ Generate valid next states (moving between rooms and cleaning) """
    vacuum_pos, dirt_remaining = state
    next_states = []

    # Cleaning action
    if vacuum_pos in dirt_remaining:
        new_dirt = dirt_remaining.copy()
        new_dirt.remove(vacuum_pos)  # Remove cleaned room
        next_states.append((vacuum_pos, new_dirt))  # Clean the current room

    # Move left
    if vacuum_pos > 0:
        next_states.append((vacuum_pos - 1, dirt_remaining.copy()))

    # Move right
    if vacuum_pos < num_rooms - 1:
        next_states.append((vacuum_pos + 1, dirt_remaining.copy()))

    return next_states

def vacuum_world_search(method='bfs'):
    """ Solve the Vacuum World problem using BFS or DFS """
    start_state = (start_room, dirt_positions)  # (Vacuum Position, Remaining Dirt)
    
    structure = [(start_state, [])]  # (current_state, path)
    visited = []
    parent_map = {}  # For search tree

    print(f"\nRunning {method.upper()}...\nSearch Tree Generation:")

    while structure:
        state, path = (structure.pop(0) if method == 'bfs' else structure.pop())  # BFS (queue) or DFS (stack)
        
        if state in visited:
            continue
        visited.append(state)

        # Print search tree structure
        if path:
            print(f"Parent: {path[-1]} -> Child: {state}")

        # Store parent-child relationships
        if path:
            parent_map[(state[0], tuple(state[1]))] = (path[-1][0], tuple(path[-1][1]))  # Fix here
##
        # Add current state to path
        new_path = path + [state]

        # Goal check (all rooms cleaned)
        if not state[1]:
            print("\nSolution Found!")
            for step in new_path:
                print(step)

            # Print full search tree
            print("\nFull Search Tree:")
            for child, parent in parent_map.items():
                print(f"{parent} -> {child}")

            return new_path

        # Expand search tree
        for next_state in get_next_states(state, num_rooms):
            if next_state not in visited:
                structure.append((next_state, new_path))

    print("No solution found!")
    return None

# Choose BFS or DFS dynamically
method = input("Choose search method (bfs/dfs): ").strip().lower()
if dirt_positions==[]:
    print('No Action Needed')
    exit(0)
vacuum_world_search(method)
