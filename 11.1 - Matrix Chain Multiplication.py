
def matrix_chain(p):
    n = len(p) - 1
    m = [[0] * n for _ in range(n)]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            m[i][j] = float('inf')

            for k in range(i, j):
                cost = (
                    m[i][k]
                    + m[k + 1][j]
                    + p[i] * p[k + 1] * p[j + 1]
                )

                if cost < m[i][j]:
                    m[i][j] = cost

    return m[0][n - 1]


print("Enter the dimensions of the matrices:")

r1 = int(input("Enter the number of rows for matrix A: "))
c1 = int(input("Enter the number of columns for matrix A: "))

r2 = int(input("Enter the number of rows for matrix B: "))
c2 = int(input("Enter the number of columns for matrix B: "))

r3 = int(input("Enter the number of rows for matrix C: "))
c3 = int(input("Enter the number of columns for matrix C: "))

if c1 != r2 or c2 != r3:
    print("Matrix multiplication is not possible with the given dimensions.")
else:
    p = [r1, c1, c2, c3]
    min_cost = matrix_chain(p)
    print(f"The minimum number of multiplications needed is: {min_cost}")
