def TankRush(H1, W1, S1, H2, W2, S2):
    str1 = S1.split()
    str2 = S2.split()
    for i in range(len(str1)):
        str1[i] = list(str1[i])
    for i in range(len(str2)):
        str2[i] = list(str2[i])
    flag = True
    for i in range(len(str1)):
        for j in range(len(str1[i])):
            if str2[0][0] == str1[i][j]:
                flag = True
                for m in range(len(str2)):
                    for k in range(len(str2[m])):
                        try:
                            if str1[i + m][j + k] != str2[m][k]:
                                flag = False
                        except IndexError:
                            flag = False
                if flag == True:
                    return True
    return False
        
    
