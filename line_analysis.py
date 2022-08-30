def LineAnalysis(line):
    if line[0] != '*' or line[-1] != '*':
        return False
    length = len(line)
    for i in range(length//2):
        if line[i] != line[length - i - 1]:
            return False
    return True
