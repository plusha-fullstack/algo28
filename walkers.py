def look_right(village, i):
    for j in range(i + 1,len(village)):
        if village[j].isdigit():
            return j
def emenies_detection(village,left,right):
    count = 0
    for k in range(left + 1, right):
        if village[k] == '=':
            count += 1
    return count == 3        
def white_walkers(village):
    left,right = 0,0
    flag = False
    for i in range(len(village)):
        if village[i].isdigit():
            left = i
            right = look_right(village, i)
            if right != None and int(village[left]) + int(village[right]) == 10:
                if not emenies_detection(village,left,right):
                    return False
                else:
                    flag = True
    return flag
