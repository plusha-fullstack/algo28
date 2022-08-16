def WordSearch(length, s, subs):
    itog_array = []
    temp_str = ''
    arr = s.split()
    for i in range(len(arr)):
        if (len(temp_str)<length) and (len(temp_str) + len(arr[i])) < length:
            temp_str += arr[i]
            temp_str+=' '
        else:
            itog_array.append(temp_str)
            temp_str = arr[i]
            temp_str +=' '
         
    if (len(temp_str) > 0):
        itog_array.append(temp_str)   
    for i in range(len(itog_array)):
        if subs in itog_array[i]:
            itog_array[i] = 1
        else:
            itog_array[i] = 0
            
    return itog_array
    
