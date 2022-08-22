def UFO(N, data, octal):
    if octal:
        base = 8
    else:
        base = 16
    for i in range(len(data)):
        new_i = 0
        digit = 0
        while(data[i] > 0):
            number = data[i] % 10
            new_i += number * (base ** digit)
            data[i] = data[i] // 10
            digit +=1
        data[i] = new_i
        
    return data
