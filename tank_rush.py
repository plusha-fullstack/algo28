def looking_sub(str1,str2):
    for i in range(len(str1) - len(str2) +1):
        print(i)
        for j in range(len(str2)):
            if str1[i + j ] != str2[j]:
                break
        if j == len(str2) - 1:
            return True
    return False
            
            
    

def TankRush(H1, W1, S1, H2, W2, S2):
    str1 = S1.split()
    str2 = S2.split()
    
    
