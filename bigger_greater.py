def BiggerGreater(input_str):
    flag = True
    left_digit = 0
    for i in range(len(input_str) - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            if input_str[i] > input_str[j]:
                flag = False
                left_digit = j
                input_str = list(input_str)
                input_str[i], input_str[j] = input_str[j], input_str[i]
                input_str = ''.join(input_str)
                break
        if not flag:
            break
    if flag:
        return ''
    string = ''.join(sorted(input_str[left_digit + 1:]))
    input_str = input_str[:left_digit+1]
    input_str += string
    return input_str
