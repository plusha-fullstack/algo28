list_of_instances = []
current_str = ''
def BastShoe(command):
    global current_str
    global list_of_instances
    operation = command[0]
    if not operation.isnumeric():
        return current_str
    if operation == '1':
        current_str += command[2:]
        list_of_instances.append(current_str)
        return current_str
    
    if operation == '2':
        if not command[2:].isnumeric():
            return current_str
        n = int(command[2:])
        if n > len(current_str):
            current_str = ''
            list_of_instances.append(current_str)
            return current_str
        else:
            current_str = current_str[:-n]
            list_of_instances.append(current_str)
            return current_str
    
    if operation == '3':
        if not command[2:].isnumeric():
            return current_str
        digit = int(command[2:])
        if len(current_str) <= digit:
            return ''
        return current_str[digit]
        
