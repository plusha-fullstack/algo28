def SherlockValidString(s):
    dic = {
        'a': 0, 
        'b': 0,
        'c': 0 ,
        'd': 0 ,
        'e': 0 ,
        'f': 0 ,
        'g': 0 ,
        'h': 0 ,
        'i': 0 ,
        'j': 0 ,
        'k': 0 ,
        'l': 0 ,
        'm': 0 ,
        'n': 0 ,
        'o': 0 ,
        'p': 0 ,
        'q': 0 ,
        'r': 0 ,
        's': 0 ,
        't': 0 ,
        'u': 0 ,
        'v': 0 ,
        'w': 0 ,
        'x': 0 ,
        'y': 0 ,
        'z': 0 ,
    }
    for i in s:
        if i in dic:
            dic[i] += 1
    max_number = 0
    min_number = 1000
    count_of_mins = 0
    count_of_maxs = 0
    count_of_1 = 0
    
    for k, v in dic.items():
        #print(k)
        #print(dic[k])
        if dic[k] > 0:
            if dic[k] == min_number:
                count_of_mins += 1
            elif dic[k] < min_number:
                min_number = dic[k]
                count_of_mins = 1
            if dic[k] == 1:
                count_of_1 += 1
    
    
    #if min_number == 1:
        
    another_elems = 0
    difference = 0
    for k, v in dic.items():
        if dic[k] > min_number:
            another_elems += 1
            difference = dic[k] - min_number
            
    
    if another_elems < 2 and difference < 2 :
        print('True')
    else:
        print('False')
            
    #print(max_number,count_of_maxs,min_number,count_of_mins)
    
    
        
        
    
SherlockValidString('xyz')
SherlockValidString('xyzaa')
SherlockValidString('xyyzz')
SherlockValidString('xyzzz')
SherlockValidString('xxyyza')
SherlockValidString('xxyyzabc')
