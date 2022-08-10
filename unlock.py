def PatternUnlock(N, hits):
    secret_key = 0
    for i in range(1,N+1):
        if hits[i] == 6:
            if hits[i-1] == 5:
                secret_key+=1
            if hits[i-1] == 1:
                secret_key+=1
            if hits[i-1] == 2:
                secret_key+=2**0.5
                
        if hits[i] == 5:
            if hits[i-1] == 6:
                secret_key+=1
            if hits[i-1] == 2:
                secret_key+=1
            if hits[i-1] == 4:
                secret_key+=1
            if hits[i-1] == 1:
                secret_key+=2**0.5
            if hits[i-1] == 3:
                secret_key+=2**0.5
                
        if hits[i] == 4:
            if hits[i-1] == 5:
                secret_key+=1
            if hits[i-1] == 3:
                secret_key+=1
            if hits[i-1] == 2:
                secret_key+=2**0.5
                
        if hits[i] == 1:
            if hits[i-1] == 6:
                secret_key+=1
            if hits[i-1] == 9:
                secret_key+=1
            if hits[i-1] == 2:
                secret_key+=1
            if hits[i-1] == 5:
                secret_key+=2**0.5
            if hits[i-1] == 8:
                secret_key+=2**0.5
                
        if hits[i] == 2:
            if hits[i-1] == 1:
                secret_key+=1
            if hits[i-1] == 5:
                secret_key+=1
            if hits[i-1] == 3:
                secret_key+=1
            if hits[i-1] == 8:
                secret_key+=1
            if hits[i-1] == 6:
                secret_key+=2**0.5
            if hits[i-1] == 9:
                secret_key+=2**0.5
            if hits[i-1] == 4:
                secret_key+=2**0.5
            if hits[i-1] == 7:
                secret_key+=2**0.5
        
        if hits[i] == 3:
            if hits[i-1] == 4:
                secret_key+=1
            if hits[i-1] == 2:
                secret_key+=1
            if hits[i-1] == 7:
                secret_key+=1
            if hits[i-1] == 5:
                secret_key+=2**0.5
            if hits[i-1] == 8:
                secret_key+=2**0.5
                
        if hits[i] == 9:
            if hits[i-1] == 1:
                secret_key+=1
            if hits[i-1] == 8:
                secret_key+=1
            if hits[i-1] == 2:
                secret_key+=2**0.5
        
        if hits[i] == 8:
            if hits[i-1] == 2:
                secret_key+=1
            if hits[i-1] == 9:
                secret_key+=1
            if hits[i-1] == 7:
                secret_key+=1
            if hits[i-1] == 1:
                secret_key+=2**0.5
            if hits[i-1] == 3:
                secret_key+=2**0.5
                
        if hits[i] == 7:
            if hits[i-1] == 3:
                secret_key+=1
            if hits[i-1] == 8:
                secret_key+=1
            if hits[i-1] == 2:
                secret_key+=2**0.5
    

    secret_key = round(secret_key,5)
    secret_key = str(secret_key)
    secret_key = secret_key.replace('0', '')
    secret_key = secret_key.replace('.', '')
    return secret_key
