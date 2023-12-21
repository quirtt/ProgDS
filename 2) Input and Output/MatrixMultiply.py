rows1 = int(input("number of rows of matrix 1: "))
columns1 = int(input("number of columns of matrix 1: "))
rows2 = int(input("number of rows of matrix 2: "))
columns2 = int(input("number of columns of matrix 2: "))
#(rows1 x columns1) x (rows2 x columns2) = (rows1 x columns2)
multiplication=False
if(columns1 == rows2):
    multiplication = True
if(multiplication):
    matrix1 = [[0 for j in range(columns1)] for i in range(rows1)]
    matrix2 = [[0 for j in range(columns2)] for i in range(rows2)]
    for i in range(rows1):
        for j in range(columns1):
            matrix1[i][j] = int(input("Row {}, Column {} in matrix 1: ".format(i+1, j+1)))

    for i in range(rows2):
        for j in range(columns2):
            matrix2[i][j] = int(input("Row {}, Column {} in matrix 2: ".format(i+1, j+1)))

print(matrix1, matrix2)

multiplicationMatrix = [[0 for j in range(columns2)] for i in range(rows1)]
for i in range(rows1):
    for j in range(columns2):
        answer = 0
        for x in range(columns1):
            answer += matrix1[i][x] * matrix2[x][j]
        multiplicationMatrix[i][j] = answer

print(multiplicationMatrix)