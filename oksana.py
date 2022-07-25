def odometer(arr):
    hours = arr[1::2]
    speed = arr[::2]
    print(hours)
    print(speed)
    summ = speed[0]*hours[0] 
    for i in range(1,len(hours)):
        summ+=speed[i]*(hours[i]-hours[i-1])
    return summ
    
