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
    
    
    
    
ConquestCampaign(3,4,2,[2,2,3,4])



 #for row in battlefield:         
 #       for elem in row:
 #           print(elem, end = ' ')
 #       print()
