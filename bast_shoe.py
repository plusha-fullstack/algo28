list_of_instances = []
current_str = ''
where_i_am = -1
def BastShoe(command):
    global current_str
    global list_of_instances
    global where_i_am
    operation = command[0]
    if not operation.isnumeric():
        return current_str
    if operation == '1':
        if where_i_am < len(list_of_instances) - 1:
            list_of_instances = list_of_instances[:where_i_am + 1]
        current_str += command[2:]
        list_of_instances.append(current_str)
        where_i_am += 1
        return current_str
    
    if operation == '2':
        if not command[2:].isnumeric():
            return current_str
        if where_i_am < len(list_of_instances) - 1:
            list_of_instances = list_of_instances[:where_i_am + 1]
        n = int(command[2:])
        if n > len(current_str):
            current_str = ''
            list_of_instances.append(current_str)
            where_i_am += 1
            return current_str
        else:
            current_str = current_str[:-n]
            list_of_instances.append(current_str)
            where_i_am += 1
            return current_str
    
    if operation == '3':
        if not command[2:].isnumeric():
            return current_str
        digit = int(command[2:])
        if len(current_str) <= digit:
            return ''
        return current_str[digit]
        
    if operation == '4':
        if where_i_am > 0:
            current_str = list_of_instances[where_i_am - 1]
            where_i_am -= 1
        return current_str
    
    if operation == '5':
        if where_i_am < len(list_of_instances) - 1:
            current_str = list_of_instances[where_i_am + 1]
            where_i_am +=1
        return current_str
