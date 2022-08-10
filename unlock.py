def PatternUnlock(N, hits):
    secret_key = 0
    for i in range(1,N+1):
        if hits[i] - hits[i-1] == 0:
            pass
        elif hits[i] - hits[i-1] == 1:
            secret_key += 1
        else:
            secret_key += 2**0.5
    

    secret_key = round(secret_key,5)
    secret_key = str(secret_key)
    secret_key = secret_key.replace('0', '')
    secret_key = secret_key.replace('.', '')
    return secret_key
    
