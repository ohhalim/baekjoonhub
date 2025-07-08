def solution(n):
    arr  = [[0] * n for _ in range(n)]
    directions = [ (0, 1), (1, 0), (0, -1), (-1, 0)]
    direction_idx = 0

    row, col = 0, 0

    for num in range(1, n*n +1):
        arr[row][col] = num

        next_row = row + directions[direction_idx][0]
        next_col = col + directions[direction_idx][1]
        if (next_row < 0 or next_row >= n or
            next_col < 0 or next_col >= n or 
            arr[next_row][next_col] != 0):
            direction_idx = (direction_idx + 1) % 4
            next_row = row + directions[direction_idx][0]
            next_col = col + directions[direction_idx][1]
        row, col = next_row, next_col
        
    return arr 