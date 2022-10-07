def Keymaker(k):
    arr = [1] * k
    for step in range(1,k):
        for i in range(step,k,step + 1):
            arr[i] = 1 if arr[i] == 0 else 0
    arr = ''.join(str(e) for e in arr)
    return arr
