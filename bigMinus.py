def BigMinus(s1, s2):
    res_str = ''
    while len(s1) < len(s2):
        s1 = '0' + s1
    while len(s2) < len(s1):
        s2 = '0' + s2
        
    if s1 < s2:
        s1,s2 = s2,s1
    flag_next_digit = False
    for i in range(len(s1)-1,-1,-1):
        temp1 = int(s1[i])
        temp2 = int(s2[i])
        if flag_next_digit and temp1>0:
            temp1 -=1
            flag_next_digit = False
        if flag_next_digit and temp1==0:
            temp1 = 9
        if temp1 >= temp2:
            res_str = str(temp1 - temp2) + res_str
        else:
            flag_next_digit = True
            temp1 +=10
            res_str = str(temp1 - temp2) + res_str
            
    res_str = res_str.lstrip('0')
    return res_str
