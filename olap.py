def ShopOLAP(N, items):
    dictionary = {}
    out = []
    for i in range(len(items)):
        parsed = items[i].split(' ')
        if parsed[0] in dictionary:
            dictionary[parsed[0]] += int(parsed[1])
        else:
            dictionary[parsed[0]] = int(parsed[1])
    
    sorted_tuple = sorted(dictionary.items(), key=lambda x: x[0])
    dictionary = dict(sorted_tuple)
    sorted_tuple = sorted(dictionary.items(), key=lambda x: x[1],reverse = True)
    dictionary = dict(sorted_tuple)
    
    for k, v in dictionary.items():
        out.append(str(k) + ' ' + str(dictionary[k]))
    
    return out
