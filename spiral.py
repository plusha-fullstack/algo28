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


matrix = [[1,2,3,4,5,6], [2,3,4,5,6,7], [3,4,5,6,7,8], [4,5,6,7,8,9]]

left,right = 0,len(matrix[0])
top,bottom = 0,len(matrix)
# 1 2 3 4 
while left < right and top < bottom:
    for i in range(left, right):
        if i != right:
            matrix[top][i + 1] = matrix[top][i]
        #print(matrix[top][i])
    top += 1
    for i in range(top, bottom):
        if i != bottom:
            matrix[i][right - 1] = matrix[i + 1][right - 1]
        #print(matrix[i][right - 1])
    right -= 1
    
    if not (left < right and top < bottom):
        break
    
    for i in range(right - 1, left - 1, -1):
        print(matrix[bottom - 1][i])
    bottom -= 1
    
    for i in range(bottom - 1, top - 1, -1):
        print(matrix[i][left])
    left += 1
    
