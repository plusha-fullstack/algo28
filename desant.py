def ConquestCampaign(N, M, L, battalion):#n-shirina m-dlina
    battlefield = [ [0]*M for i in range(N) ]
    #airdrop
    for k in range(0, len(battalion)-1,2):
        x = battalion[k]
        y = battalion[k+1]
        battlefield[x-1][y-1] = 1
    
    
        
    
    
    for row in battlefield:         
        for elem in row:
            print(elem, end = ' ')
        print()
    
    
        for i in range(N):
        for j in range(M):
            #angles
            if (i == 0 and j == 0):
                if battlefield[i+1][j+1] == 1:
                    battlefield[i][j]=1
            
            if (i == N - 1 and j == 0):
                if battlefield[i-1][j+1] == 1:
                    battlefield[i][j]=1
                    
            if (i == 0 and j == M - 1):
                if battlefield[i+1][j-1] == 1:
                    battlefield[i][j]=1
                    
            if (i == N-1 and j == M-1):
                if battlefield[i-1][j-1] == 1:
                    battlefield[i][j]=1
            
            
            #sides
            if (i != 0 and j == 0 and i!= N-1):
                if battlefield[i+1][j] == 1 or battlefield[i+1][j]==1 or battlefield[i][j+1]==1:
                    battlefield[i][j]=1
            
            if (i == 0 and j != 0 and j!= M-1):
                if battlefield[i][j+1] == 1 or battlefield[i][j-1]==1 or battlefield[i+1][j]==1:
                    battlefield[i][j]=1
                    
            if (i != 0 and j == M - 1 and i!= N-1):
                if battlefield[i+1][j] == 1 or battlefield[i-1][j]==1 or battlefield[i][j-1]==1:
                    battlefield[i][j]=1
                    
            if (i == N-1 and j !=0 and j!= N-1):
                if battlefield[i][j-1] == 1 or battlefield[i][j+1] or battlefield[i-1][j]:
                    battlefield[i][j]=1
    
    
ConquestCampaign(3,4,2,[2,2,3,4])



 #for row in battlefield:         
 #       for elem in row:
 #           print(elem, end = ' ')
 #       print()
