def greedy_best_first_search(graph, heuristic, cost, start, goal):
    priority_queue = [(start, [start], 0)]  # (node, path, total cost)
    visited = set()

    while priority_queue:
        # Sort queue based on heuristic value (ascending order)
        priority_queue.sort(key=lambda x: heuristic[x[0]])
        current, path, total_cost = priority_queue.pop(0)  # Pop the node with the lowest heuristic
        if current in visited:
            continue
        visited.add(current)

        # Goal check
        if current == goal:
            print("Solution Found! Path:", path, "Total Cost:", total_cost)
            return path, total_cost

        # Expand neighbors
        for neighbor, edge_cost in graph[current]:
            if neighbor not in visited:
                priority_queue.append((neighbor, path + [neighbor], total_cost + edge_cost))

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
greedy_best_first_search(graph, heuristic, graph, start, goal)
