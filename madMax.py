def MadMax(N, Tele):
    maxx = Tele[0]
    place_of_max = -1
    for i in range(N):
        if Tele[i]>=maxx:
            maxx = Tele[i]
            place_of_max = i
    
    Tele[N//2], Tele[place_of_max] = Tele[place_of_max], Tele[N//2]
    
    Tele[:N//2] = sorted(Tele[:N//2])
    Tele[N//2+1:] = sorted(Tele[N//2+1:],reverse = True)
    
    return Tele
