import math

def alphabeta(depth, index, is_maximizing, values, height, alpha, beta):
    if depth == height:  # Leaf node reached
        return values[index]

    if is_maximizing:
        best = -math.inf
        for i in range(2):  # Two children (left & right)
            if index*2+i<len(values):
                val = alphabeta(depth + 1, index * 2 + i, False, values, height, alpha, beta)
                best = max(best, val)
                alpha = max(alpha, best)
                if beta <= alpha:
                    break  # Prune the remaining branches
        return best
    else:
        best = math.inf
        for i in range(2):# Two children (left & right)
            if index*2+i<len(values):
                val = alphabeta(depth + 1, index * 2 + i, True, values, height, alpha, beta)
                best = min(best, val)
                beta = min(beta, best)
                if beta <= alpha:
                    break  # Prune the remaining branches
        return best

# Get user input for leaf node values
leaf_values = list(map(int, input("Enter leaf node values (space-separated): ").split()))

# Calculate tree height (log2 of number of leaves)
tree_height = math.ceil((math.log2(len(leaf_values))))

# Run Alpha-Beta Pruning
best_score = alphabeta(0, 0, True, leaf_values, tree_height, -math.inf, math.inf)
print("Best possible outcome for the maximizing player:", best_score)
