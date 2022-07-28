def ConquestCampaign(N, M, L, battalion):#n-shirina m-dlina
    battlefield = [ [0]*M for i in range(N) ]
    #airdrop
    for k in range(0, len(battalion)-1,2):
        x = battalion[k]
        y = battalion[k+1]
        battlefield[x-1][y-1] = 1
    
    days_of_war = 1
    number_of_elements = N*M
    war = True
    
    while war:
    
        for i in range(N):
            for j in range(M):
                #angles
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
                
                
                #sides
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
        for row in battlefield:
            for element in row:
                summ+=battlefield[i][j]
                print(summ)
                    
        for row in battlefield:         
            for elem in row:
                print(elem, end = ' ')
            print()
        
        if summ == number_of_elements:
            war = False
    
    
        print(summ)
        print(days_of_war)
        for row in battlefield:         
            for elem in row:
                print(elem, end = ' ')
            print()


ConquestCampaign(3,4,2,[2,2,3,4])
