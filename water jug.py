def water_jug_solver(a, b, g, method="bfs"):
    visited = set()
    container = [(0, 0, [])]
    while container:
        if method == "bfs":
            x, y, path = container.pop(0)
        else:
            x, y, path = container.pop()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        path = path + [(x, y)]
        
        print(x, y)
        
        if x == g or y == g or x+y==g:
            print("Goal Found!!!")
            print("Path:", path)
            return
        # Possible moves
        temp = [
            (a, y, path),  # Fill Jug 1
            (x, b, path),  # Fill Jug 2
            (0, y, path),  # Empty Jug 1
            (x, 0, path),  # Empty Jug 2
            (x - min(x, b - y), y + min(x, b - y), path),  # Pour Jug 1 -> Jug 2
            (x + min(y, a - x), y - min(y, a - x), path)   # Pour Jug 2 -> Jug 1
        ]
        for state in temp:
            if (state[0], state[1]) not in visited:
                container.append(state)
    print("Goal Not Found!!!")

# Input
a, b = map(int, input("Enter the Jug Capacities: ").split())
g = int(input("Enter the Goal Capacity: "))
if a+b<g or g<0:
    print("Not Possible")
    exit(0)
method = input("Enter method (bfs/dfs): ").strip().lower()
water_jug_solver(a, b, g, method)
