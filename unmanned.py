def Unmanned(L, N, track):
    res = 0
    for i in range(len(track)):
        if i > 0:
            res += track[i][0] - track[i - 1][0]
        else:
            res += track[i][0]
        if (res // track[i][1]) % 2 == 0:
            res += track[i][1] - (res % track[i][1])
            
    res += (L - track[-1][0])
    
    return res
