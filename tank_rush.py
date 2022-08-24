def looking_sub(str1,str2):
    if str2 in str1:
        return True
    return False
            
    

def TankRush(H1, W1, S1, H2, W2, S2):
    str1 = S1.split()
    str2 = S2.split()
    for j in range(len(str2)):
        flag = False
        for i in range(len(str1)):
            if looking_sub(str1[i],str2[j]):
                flag = True
                break
        if flag == False:
            return flag
    return flag
    
