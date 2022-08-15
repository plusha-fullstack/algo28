def WordSearch(length, s, subs):
    arr = s.split()
    for i in range(len(arr)):
        if subs in arr[i]:
            arr[i] = 1
        else:
            arr[i] = 0
            
    return arr
