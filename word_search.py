def WordSearch(length, s, subs):
    itog_array = []
    clean_str = ''
    temp_str = ''
    arr = s.split()
    for i in range(len(arr)):
        if len(arr[i])>length:
            temp_str = arr[i]
            temp_str  =  temp_str[:length] + ' ' + temp_str[length:]
            arr[i] = temp_str
            
    for i in range(len(arr)):
        clean_str += arr[i]+' '
        
    arr = clean_str.split()    
    temp_str = ''
    for i in range(len(arr)):
        if (len(temp_str)<length) and (len(temp_str) + len(arr[i])) < length:
            temp_str += arr[i]
            temp_str+=' '
        else:
            if temp_str != '':
                itog_array.append(temp_str)
            temp_str = arr[i]
            temp_str+=' '
            
    if (len(temp_str) > 0):
        itog_array.append(temp_str) 
        
    for i in range(len(itog_array)):
        temp_str = str(itog_array[i])
        temp_arr = temp_str.split()
        if subs in temp_arr:
            itog_array[i] = 1
        else:
            itog_array[i] = 0    
    

    return itog_array
    
