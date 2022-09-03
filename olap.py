#string [] ShopOLAP(int N, string [] items)
def ShopOLAP(N, items):
    dictionary = {}
    for i in range(len(items)):
        parsed = items[i].split(' ')
        dictionary[parsed[0]] = int(parsed[1])
        
    print(dictionary)
    
    
ShopOLAP(0,['платье1 5','сумка32 2','платье1 1','сумка23 2','сумка128 4'])
