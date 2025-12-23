import math

game_tree = [
    [
        [3, 5],
        [6, 9]
    ],
    [
        [1, 2],
        [0, -1]
    ]
]

def minimax(node, depth, maximizing_player):
    if isinstance(node, int):
        return node

    if maximizing_player:
        max_eval = -math.inf
        for child in node:
            eval = minimax(child, depth+1, False)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = math.inf
        for child in node:
            eval = minimax(child, depth+1, True)
            min_eval = min(min_eval, eval)
        return min_eval

best_value = minimax(game_tree, 0, True)
print("Best achievable value for maximizing player:", best_value)
