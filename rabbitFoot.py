def TheRabbitsFoot(s, encode):
    if encode:
        s = s.replace(" ", "")
    length = len(s)
    N = (length**0.5)//1
    M = N+1
    if (length > N + M):
        N+=1
    N,M = int(N), int(M)
    
    matrix =  [ ['0']*M for i in range(N) ]
    
    if encode == True:
        len_of_str = len(s)
        k = 0
        flag_out = False
        for i in range(N):
            for j in range(M):
                matrix[i][j] = s[k]
                k+=1
                len_of_str -= 1
                if len_of_str == 0:
                    flag_out = True
                if flag_out:
                    break
            if flag_out:
                break
    if encode == False:
        matrix = s.split()
        for i in range(len(matrix)):
            matrix[i] = list(matrix[i])
            
    res_str = ''
    if encode:
        for i in range(N):
            for j in range(M):
                if matrix[j][i]!='0':
                    res_str+=matrix[j][i]
            res_str+=' '
    if encode == False:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])+1):
                try:
                    res_str += matrix[j][i]
                except IndexError:
                    pass
    
  
    res_str = res_str.strip()
    return res_str
