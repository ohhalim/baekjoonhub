def solution(board, k):
    num = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if i + j <= k:
                num += board[i][j]
    return num
                