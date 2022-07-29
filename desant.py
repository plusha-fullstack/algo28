def ConquestCampaign(N, M, L, battalion):
    battlefield = [ [0]*M for i in range(N) ]
    for k in range(0, len(battalion)-1,2):
        x = battalion[k]
        y = battalion[k+1]
        battlefield[x-1][y-1] = 1
    
    days_of_war = 1
    number_of_elements = N*M
    war = True
    summ=0
    for i in range(N):
        for j in range(M):
            summ+=battlefield[i][j]
    if summ == number_of_elements:
            return 1
    
    while war:
    
        for i in range(N):
            for j in range(M):
                if True:
                    if (i == 0 and j == 0):
                        if battlefield[i+1][j] == 1 or battlefield[i][j+1] == 1:
                            battlefield[i][j]=2
                    
                    if (i == N - 1 and j == 0):
                        if battlefield[i-1][j] == 1 or battlefield[i][j+1] == 1:
                            battlefield[i][j]=2
                            
                    if (i == 0 and j == M - 1):
                        if battlefield[i+1][j] == 1 or battlefield[i][j-1] == 1:
                            battlefield[i][j]=2
                    if (i == N-1 and j == M-1):
                        if battlefield[i-1][j] == 1 or battlefield[i][j-1] == 1:
                            battlefield[i][j]=2
                
                
                if True:
                    if (i != 0 and j == 0 and i!= N-1):
                        if battlefield[i+1][j] == 1 or battlefield[i-1][j]==1 or battlefield[i][j+1]==1:
                            battlefield[i][j]=2
                    
                    if (i == 0 and j != 0 and j!= M-1):
                        if battlefield[i][j+1] == 1 or battlefield[i][j-1]==1 or battlefield[i+1][j]==1:
                            battlefield[i][j]=2
                            
                    if (i != 0 and j == M - 1 and i!= N-1):
                        if battlefield[i+1][j] == 1 or battlefield[i-1][j]==1 or battlefield[i][j-1]==1:
                            battlefield[i][j]=2
                            
                    if (i == N-1 and j !=0 and j!= M - 1):
                        if battlefield[i][j-1] == 1 or battlefield[i][j+1] or battlefield[i-1][j]:
                            battlefield[i][j]=2
                        
                
                if i>0 and j>0 and i<N-1 and j<M-1:
                    if battlefield[i+1][j] == 1 or battlefield[i-1][j]==1 or battlefield[i][j+1]==1 or battlefield[i][j-1]==1:
                        battlefield[i][j] = 2
                        
                
        for i in range(N):
            for j in range(M):
                if battlefield[i][j] == 2:
                    battlefield[i][j] = 1
                    
        days_of_war+=1
        summ=0
        for i in range(N):
            for j in range(M):
                summ+=battlefield[i][j]
                    
        
        if summ == number_of_elements:
            war = False
    
    return days_of_war
    
