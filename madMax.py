def MadMax(N, Tele):
    Tele = sorted(Tele)
    
    Tele[N//2], Tele[-1] = Tele[-1], Tele[N//2]
    Tele[N//2+1:] = sorted(Tele[N//2+1:],reverse = True)
    return Tele
