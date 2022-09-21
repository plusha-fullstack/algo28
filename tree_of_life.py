def rost(H,W,tree):
    for i in range(H):
        for j in range(W):
            tree[i][j] += 1
                   
    return tree

def withering(H,W,tree):
    for i in range(H):
        for j in range(W):
            tree[i][j] += 1
    for i in range(H):
        for j in range(W):
            try:
                if tree[i + 1][j] > 2 and tree[i][j] < 3:
                    tree[i][j] = 0
                    continue
            except IndexError:
                pass
            try:
                if tree[i - 1][j] > 2 and tree[i][j] < 3 and i > 0:
                    tree[i][j] = 0
                    continue
            except IndexError:
                pass
            try:
                if tree[i][j + 1] > 2 and tree[i][j] < 3:
                    tree[i][j] = 0
                    continue
            except IndexError:
                pass
            try:
                if tree[i][j - 1] > 2 and tree[i][j] < 3 and j > 0:
                    tree[i][j] = 0
                    continue
            except IndexError:
                pass
            
    for i in range(H):
        for j in range(W):
            if tree[i][j] > 2:
                tree[i][j] = 0
    
    return tree
    
                
    
    
def TreeOfLife(H, W, N, tree):
    for i in range(len(tree)):
        tree[i] = list(tree[i])
    for i in range(H):
        for j in range(W):
            if tree[i][j] == '+':
                tree[i][j] = 1
            else:
                tree[i][j] = 0
    for i in range(N):
        if i % 2 == 0:
            tree = rost(H,W,tree)
        else:
            tree = withering(H,W,tree)
    for i in range(H):
        for j in range(W):
            if tree[i][j] > 0:
                tree[i][j] = '+'
            else:
                tree[i][j] = '.'
               
    for i in range(len(tree)):
        tree[i] = ''.join(tree[i])
        
    return tree
