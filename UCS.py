def sort_based_on_costs(l):
    g={}
    w=sorted(l.values())
    for x in w:
        for y in l.keys():
            if x == l[y]:
                if y not in g.keys():
                    g.update({y: x})
    return g

def uniform_cost_search(adj_list, start, goal):
    l = {start: 0}
    visited = {node: 0 for node in adj_list.keys()}
    parent = {start: None}
    cm = {node: float('inf') for node in adj_list.keys()}
    cm[start] = 0
    
    while l:
        a = list(l.keys())[0]
        
        if a == goal:
            print("Goal Found!!!")
            result = [goal]
            q = parent[goal]
            while q is not None:
                result.append(q)
                q = parent[q]
            print("Path to be followed is:", '->'.join(str(e) for e in result[::-1]))
            print("Cost required is", cm[a])
            return
        
        l.pop(a)
        visited[a] = 1
        h = {}
        
        for neighbor, cost in adj_list.get(a, []):
            if visited[neighbor] != 1:
                newcost = cost + cm[a]
                if newcost < cm[neighbor]:
                    parent[neighbor] = a
                    cm[neighbor] = newcost
                    h[neighbor] = cm[neighbor]
        
        l.update(h)
        l = sort_based_on_costs(l)
    
    print("Goal cannot be Found!!!")

# Example usage
adj_list = {
    0: [(1, 6), (2, 4)],
    1: [(3, 4)],
    2: [(5, 8)],
    3: [(6, 2)],
    4: [],
    5: [(4, 9), (7, 7)],
    6: [(4, 9), (7, 3)],
    7: [(4, 4)]
}
adjacency_list = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('D', 2), ('E', 5)],
    'C': [('A', 4), ('F', 3)],
    'D': [('B', 2)],
    'E': [('B', 5), ('F', 2)],
    'F': [('C', 3), ('E', 2)]
}

goal =input("Enter the Goal: ")
uniform_cost_search(adjacency_list, 'E', goal)
