# this program works for 2**n x 2**n matrices - please put 0s in the other places.
import numpy as np
def Strassen(n, A, B):
    # see wikipedia page
    if n == 0:
        return A @ B
    
    M = 2**(n-1)
    A11 = A[:M, :M]
    B11 = B[:M, :M]
    A12 = A[:M, M:]
    B12 = B[:M, M:]
    A21 = A[M:, :M]
    B21 = B[M:, :M]
    A22 = A[M:, M:]
    B22 = B[M:, M:]
    M1 = Strassen(n-1, (A11 + A22), (B11 + B22))
    M2 = Strassen(n-1, (A21 + A22), B11)
    M3 = Strassen(n-1, A11, (B12 - B22))
    M4 = Strassen(n-1, A22, (B21 - B11))
    M5 = Strassen(n-1, A11 + A12, B22)
    M6 = Strassen(n-1, (A21 - A11), (B11 + B12))
    M7 = Strassen(n-1, (A12 - A22), (B21 + B22))

    X1 = M1 + M4 - M5 + M7
    X2 = M3 + M5
    X3 = M2 + M4
    X4 = M1 - M2 + M3 + M6

    return np.concatenate((np.concatenate((X1, X3), axis = 0), np.concatenate((X2, X4), axis = 0)), axis=1)
#find n in 2**n
matrix_1 = np.random.randint(1, 10, size=(2, 2)) 
matrix_2 = np.random.randint(1, 10, size=(2, 2))  # Creating a random 4x8 matrix
print("straaaaassseeennnnn babeh\n", Strassen(1, matrix_1, matrix_2))