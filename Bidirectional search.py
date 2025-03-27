from collections import deque
def bidirectional_search(graph, start, goal):
    if start == goal:
        print("Start and goal are the same node.")
        return [start]
    
    queue1 = deque([(start, [start])])  # Queue stores (node, path)
    queue2 = deque([(goal, [goal])])
    visited1 = {start: [start]}
    visited2 = {goal: [goal]}
    
    while queue1 and queue2:
        # Expand from start side
        node1, path1 = queue1.popleft()
        for neighbor in graph[node1]:
            if neighbor not in visited1:
                new_path = path1 + [neighbor]
                queue1.append((neighbor, new_path))
                visited1[neighbor] = new_path
            if neighbor in visited2:
                print("Path Exists between Root and Goal!")
                return visited1[neighbor] + visited2[neighbor][::-1][1:]
        
        # Expand from goal side
        node2, path2 = queue2.popleft()
        for neighbor in graph[node2]:
            if neighbor not in visited2:
                new_path = path2 + [neighbor]
                queue2.append((neighbor, new_path))
                visited2[neighbor] = new_path
            if neighbor in visited1:
                print("Path Exists between Root and Goal!")
                return visited1[neighbor] + visited2[neighbor][::-1][1:]
    
    print("Path does not exist between Root and Goal Nodes!")
    return []
graph= {
    0: [1, 2, 3],
    1: [0, 4],
    2: [0, 5, 6],
    3: [0, 9],
    4: [1],
    5: [2, 7],
    6: [2, 8],
    7: [5],
    8: [6],
    9: [3, 10, 11],
    10: [9],
    11: [9, 12],
    12: [11]
}
start_node = 3
goal_node = 4
path = bidirectional_search(graph, start_node, goal_node)
print("Path:", path)
