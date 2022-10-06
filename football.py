def first_way(F):
    sorted_array = sorted(F)
    for i in range(len(F)):
        for j in range(i + 1,len(F)):
            F[i], F[j] = F[j] , F[i]
            if F == sorted_array:
                return True
            F[j], F[i] = F[i] , F[j]
    return False
def second_way(F):
    sorted_array = sorted(F)
    for i in range(len(F)):
        for j in range(i + 1,len(F)):
            F[i:j + 1] = reversed(F[i:j + 1])
            if F == sorted_array:
                return True
            F[i:j + 1] = reversed(F[i:j + 1])
    return False
             
            
    

def Football(F, N):
    if first_way(F):
        return True
    if second_way(F):
        return True
    return False
