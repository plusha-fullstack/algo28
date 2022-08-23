def Unmanned(L, N, track):
    res = 0
    clear_track = []
    for i in range(len(track)):
        if track[i][0] < L:
            clear_track.append(track[i])
            
    
    if clear_track == []:
        return L
    for i in range(len(clear_track)):
        if i > 0:
            res += clear_track[i][0] - clear_track[i - 1][0]
        else:
            res += clear_track[i][0]
        if (res // clear_track[i][1]) % 2 == 0:
            res += clear_track[i][1] - (res % clear_track[i][1])
    
    
    res += (L - clear_track[-1][0])
    
    return res
