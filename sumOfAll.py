def SumOfThe(N, data):
    summ_of_all_elems = 0
    for number in data:
        summ_of_all_elems += number
    
    for number in data:
        if summ_of_all_elems - number == number:
            return number
