def can_be_sorted(a,b,c):
    li_st = [a,b,c]
    order_list = sorted(li_st)
    return (order_list == [c,a,b] or order_list == [b,c,a])


def MisterRobot(N, data):
    flag = True
    while flag:
        flag = False
        for i in range(len(data) - 2):
            if can_be_sorted(data[i], data[i + 1], data[i + 2]):
                flag = True
                data[i:i + 3] = sorted(data[i:i + 3])
        

    return data == sorted(data)
