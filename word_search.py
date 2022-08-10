#string = '1) строка разбивается на набор строк через выравнивание по заданной ширине.'
#print(len(string))  75
#print(75/12) 6.25

def WordSearch(length, s, subs):
    size_of_array = len(s)//length + 1
    array = [''] * size_of_array
    start_of_word = 0
    j = 0
    for i in range(len(s)):
        if s[i] == ' ':
            end_of_word = i-1
            if len(array[j]) + (end_of_word - start_of_word)  < length:
                temp_str1 = s[j]
                temp_str2 = s[start_of_word:end_of_word+1]
                s[j] = temp_str1 + temp_str2
            else:
                temp_str1 = s[j+1]
                temp_str2 = s[start_of_word:end_of_word+1]
                s[j+1] = temp_str1 + temp_str2
                j+=1
                
            start_of_word = i+1
        
    
    
    
    
    
    
    
    return array
    
    
    
print(WordSearch(12,'1) строка разбивается на набор строк через выравнивание по заданной ширине.','строк'))
