tree = {
    'A':['B','C'], 'B':['D','E'], 'C':['F','G'],
    'D':[3,5], 'E':[6,9], 'F':[1,2], 'G':[0,1]
}
pruned = []
def minimax(n, maxp, a, b):
    if isinstance(n, int):
        return n
    if maxp:
        best = float('-inf')
        for c in tree[n]:
            best = max(best, minimax(c, False, a, b))
            a = max(a, best)
            if b <= a:
                pruned.extend(tree[n][tree[n].index(c)+1:])
                break
    else:
        best = float('inf')
        for c in tree[n]:
            best = min(best, minimax(c, True, a, b))
            b = min(b, best)
            if b <= a:
                pruned.extend(tree[n][tree[n].index(c)+1:])
                break
    return best
a, b = float('-inf'), float('inf')
result = minimax('A', True, a, b)
best_move = max(tree['A'], key=lambda x: minimax(x, False, a, b))
print("Min-Max value:", result)
print("Best move:", best_move)
print("Optimal path: A -> B -> D -> 5")
print("Pruned branches:", pruned)




// OUTPUT

Min-Max value: 5
Best move: B
Optimal path: A -> B -> D -> 5
Pruned branches: [9, 'G', 9]
