import numpy as np

def strassen(A,B):
    n = A.shape[0]

    if n==1:
        return A*B

    m = n//2

    A11 = A[:m, :m]
    A12 = A[:m, m:]
    A21 = A[m:, :m]
    A22 = A[m:, m:]
    
    B11 = B[:m, :m]
    B12 = B[:m, m:]
    B21 = B[m:, :m]
    B22 = B[m:, m:]

    M1 = strassen(A11 + A22, B11 + B22)
    M2 = strassen(A21 + A22, B11)
    M3 = strassen(A11, B12 - B22)
    M4 = strassen(A22, B21 - B11)
    M5 = strassen(A11 + A12, B22)
    M6 = strassen(A21 - A11, B11 + B12)
    M7 = strassen(A12 - A22, B21 + B22)


    C11 = M1 + M4 - M5 + M7
    C12 = M3 + M5
    C21 = M2 + M4
    C22 = M1 - M2 + M3 + M6

    C = np.vstack((np.hstack((C11, C12)), np.hstack((C21, C22))))

    return C


A = np.array([[1, 3],
              [5, 7]])

B = np.array([[2, 4],
              [6, 8]])


C = strassen(A, B)

print("Matrix A:")
print(A)

print("\n\nMatrix B:")
print(B)

print("\n\nResultant Matrix C:")
print(C)
