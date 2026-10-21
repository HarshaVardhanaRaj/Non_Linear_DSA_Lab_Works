def attack(board, row, col):
    n = len(board)

    for i in range(row):
        if board[i][col] == 1:
            return True

    i, j = row-1, col-1

    while i>=0 and j>=0:
        if board[i][j] == 1:
            return True
        i -= 1
        j -= 1

    i, j = row-1, col+1


    while i>=0 and j<n:
        if board[i][j] == 1:
            return True
        i -= 1
        j += 1

    return False



def solve_n_queens(n=8):

    def backtrack(row=0):
