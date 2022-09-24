a = [[1,2,3,4,5,6], [2,3,4,5,6,7], [3,4,5,6,7,8], [4,5,6,7,8,9]]

c = 1
start = 0

while(start < len(a) // 2):
	n = len(a) - start * 2 - 1
	for x in range(len(a)):
		a[start][start + x] = c
		c += 1
	for y in range(n):
		a[start + y][len(a[i]) - 1 - start] = c
		c += 1
	for x in range(n):
		a[len(a) - 1 - start][len(a) - 1 - start - x] = c
		c += 1
	for y in range(n):
		a[len(a) - 1 - start - y][start] = c
		c += 1

	start += 1

if len(a) % 2:
    a[start][start] = c

for i in range(len(a)):  
    for j in range(len(a[i])):
        print(a[i][j], end = ' ')
    print()   
