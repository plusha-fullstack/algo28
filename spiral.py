def MatrixTurn(matrix, M, N, T):
    for i in range(len(matrix)):
        matrix[i] = list(matrix[i])
    a = len(matrix[0])
    b = len(matrix)
    r  = min(a,b) // 2;
    while T > 0:
        for i in range(r):
            k1, k2 = i, i
            while ((k1 + 1 + i) < b):
                matrix[k1][k2], matrix[k1 + 1][k2] = matrix[k1 + 1][k2], matrix[k1][k2]
                k1 += 1
            while ((k2 + 1 + i) < a):
                matrix[k1][k2], matrix[k1][k2 + 1] = matrix[k1][k2 + 1], matrix[k1][k2]
                k2 += 1
            while ((k1 - 1 - i) >= 0):
                matrix[k1][k2], matrix[k1 - 1][k2] = matrix[k1 - 1][k2], matrix[k1][k2]
                k1 -= 1
            while ((k2 - 1 - i) > 0):
                matrix[k1][k2], matrix[k1][k2 - 1] = matrix[k1][k2 - 1], matrix[k1][k2]
                k2 -= 1
        T -= 1
    
