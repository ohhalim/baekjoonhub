def solution(board):
    n = len(board)
    danger = [[False] * n for _ in range(n)]
    # 8방향 + 자기 자신
    dirs = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),  (0, 0),  (0, 1),
        (1, -1),  (1, 0),  (1, 1),
    ]

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                for di, dj in dirs:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < n:
                        danger[ni][nj] = True

    cnt = 0
    for i in range(n):
        for j in range(n):
            if not danger[i][j]:
                cnt += 1
    return cnt