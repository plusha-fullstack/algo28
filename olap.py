#string [] ShopOLAP(int N, string [] items)
def ShopOLAP(N, items):
    dictionary = {}
    for i in range(len(items)):
        parsed = items[i].split(' ')
        dictionary[parsed[0]] = int(parsed[1])
        
    print(dictionary)
    
    
ShopOLAP(0,['платье1 5','сумка32 2','платье1 1','сумка23 2','сумка128 4'])



#string [] ShopOLAP(int N, string [] items)
def ShopOLAP(N, items):
    dictionary = {}
    for i in range(len(items)):
        parsed = items[i].split(' ')
        if parsed[0] in dictionary:
            dictionary[parsed[0]] += int(parsed[1])
        else:
            dictionary[parsed[0]] = int(parsed[1])
    
    sorted_tuple = sorted(dictionary.items(), key=lambda x: x[1],reverse = True)
    dictionary = dict(sorted_tuple)
        #for j in range(0, len(dictionary) - i - 1):
            #if dictionary[i] == dictionary[i + 1]:
                
        
    print(dictionary)
    
    
ShopOLAP(0,['платье1 5','сумка32 2','платье1 1','сумка23 2','сумка128 4'])
