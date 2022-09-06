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
        n = int(command[2:])
        
