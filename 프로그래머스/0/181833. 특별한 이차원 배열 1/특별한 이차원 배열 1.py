def solution(n):
    # n x n 크기의 2차원 배열을 0으로 초기화합니다.
    arr = [[0 for _ in range(n)] for _ in range(n)]

    # 배열을 순회하면서 i와 j가 같은 경우 1로 설정합니다.
    for i in range(n):
        arr[i][i] = 1
        
    return arr