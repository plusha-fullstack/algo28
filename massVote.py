def MassVote(N, Votes):
    max1 = -1
    max2 = -1
    k = -1
    summ = 0
    for i in range(len(Votes)):
        summ += Votes[i]
        if Votes[i] >= max1:
            max2 = max1
            max1 = Votes[i]
            k = i
    k+=1
    if max1 == max2:
        return "no winner"
    elif (max1/summ) > 0.5:
        return "majority winner " + str(k)
    else:
        return "minority winner " + str(k)
    
