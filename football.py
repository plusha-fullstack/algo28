def first_way(F):
    sorted_array = sorted(F)
    for i in range(len(F)):
        for j in range(len(F)):
            F[i], F[j] = F[j] , F[i]
            if F == sorted_array:
                return True
            F[j], F[i] = F[i] , F[j]
    return False
'''
for (int i = 0; i < n/2; i++) {
		    temp = a[n-i-1];
	i 0	    a[n-i-1] = a[i];
	j 1 	    a[i] = temp;
'''
def second_way(F):
    sorted_array = sorted(F)
    for i in range(len(F)):
        for j in range(1,len(F)):
            for 
            
    

def Football(F, N):
    if first_way(F):
        return True
    #if second_way(F):
        #return True
    return False
    
print(first_way([1, 0, 3, 2, 5]))



a = [1,3,0,2,7,4,5]
#b = a.copy()
n = len(a)
#for i in range(n//2):
#    a[i],a[n-i - 1] = a[n-i - 1], a[i]
#print(a)
print(a)
#0, (int)(k/2)
#r = (5-2 + 1)//2
#print(r)
for i in range(2,2 + (6-2)//2):
    print(i)
    a[i],a[6 -i +1  ] = a[6 -i +1], a[i]
    
print(a)
    
# 2 3 4 5 
#2 to (5-2 + 1)//2   ???????????????????
