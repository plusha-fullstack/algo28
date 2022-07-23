def squirrel(N):
    factorial = 1
    for i in range(2, N+1):
        factorial *= i
    factorial = str(factorial)
    return int(factorial[0])
