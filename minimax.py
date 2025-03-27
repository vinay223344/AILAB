import math

def minimax(depth, index, is_maximizing, values, height):
    if depth == height:  # Leaf node reached
        return values[index]

    if is_maximizing:
        if index*2+1<len(values):
            return max(minimax(depth + 1, index * 2, False, values, height),
                   minimax(depth + 1, index * 2 + 1, False, values, height))
        else:
            return minimax(depth + 1, index * 2, False, values, height)
    else:
        if index*2+1<len(values):
            return min(minimax(depth + 1, index * 2, True, values, height),
                   minimax(depth + 1, index * 2 + 1, True, values, height))
        else:
            return minimax(depth + 1, index * 2, True, values, height)

# Get user input for leaf node values
leaf_values = list(map(int, input("Enter leaf node values (space-separated): ").split()))

# Calculate height of the tree (log2 of leaf count)
import math
tree_height = math.ceil(math.log2(len(leaf_values)))

# Run Minimax
best_score = minimax(0, 0, True, leaf_values, tree_height)
print("Best possible outcome for the maximizing player:", best_score)
