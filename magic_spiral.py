n = int(input())

matrix = [[0 for j in range (n)]for i in range(n)]

for i in range(len(matrix[0])):
    matrix[0][i] = i+1
backcharge = True
counter = n+1
jump = 0
for iterat in range(n-1,0,-1):
    if (n-iterat)%2==0:
        for i in range(iterat):
            matrix[iterat-(i+1-jump)][jump-1] = counter
            counter += 1
        for j in range(iterat):
            matrix[jump][j+jump] = counter
            counter += 1
    else:
        for i in range(iterat):
            matrix[i+1+jump][n-1-jump] = counter
            counter += 1
        for j in range(iterat):
            matrix[n-1-jump][n-(j+2+jump)] = counter
            counter += 1
        jump += 1
for string in matrix:
    for letter in string:
        print(letter, end=' ')
    print()