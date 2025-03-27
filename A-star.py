def a_star_search(graph, heuristic, start, goal):
    open_list = [(start, [start], 0)]  # (current_node, path, total_cost g)
    visited = set()

    while open_list:
        # Sort list by f(n) = g(n) + h(n)
        open_list.sort(key=lambda x: x[2] + heuristic[x[0]])

        current, path, g_cost = open_list.pop(0)  # Node with lowest f(n)

        if current in visited:
            continue
        visited.add(current)

        # Goal check
        if current == goal:
            print("Solution Found! Path:", path, "Total Cost:", g_cost)
            return path, g_cost

        # Expand neighbors
        for neighbor, edge_cost in graph[current]:
            if neighbor not in visited:
                open_list.append((neighbor, path + [neighbor], g_cost + edge_cost))

    print("No Solution Found!")
    return None, None

# Taking user input for the graph
nodes = int(input("Enter number of nodes: "))
graph = {i: [] for i in range(nodes)}

print("Enter edges in format: node1 node2 cost (Enter -1 -1 -1 to stop)")
while True:
    u, v, c = map(int, input().split())
    if u == -1 and v == -1 and c == -1:
        break
    graph[u].append((v, c))
    graph[v].append((u, c))  # Assuming an undirected graph

# Taking heuristic values from the user
heuristic = {}
print("Enter heuristic values for each node:")
for i in range(nodes):
    heuristic[i] = int(input(f"Heuristic for node {i}: "))

# Taking start and goal nodes from the user
start = int(input("Enter the start node: "))
goal = int(input("Enter the goal node: "))

# Running the search
a_star_search(graph, heuristic, start, goal)
