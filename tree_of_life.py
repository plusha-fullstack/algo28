def rost(H,W,tree):
    for i in range(H):
        for j in range(W):
            tree[i][j] += 1
                    
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
        if N % 2 == 0:
            tree = rost(H,W,tree)
        
        
    return tree
            
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
print(TreeOfLife(3,4,12, [".+..","..+.",".+.."]))
