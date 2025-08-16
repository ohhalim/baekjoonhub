N, M = map(int,input().split())
matrix_A = []
for _ in range(N):
    matrix_A.append(list(map(int, input().split())))

matrix_B = []
for _ in range(N):
    matrix_B.append(list(map(int, input().split())))

result_matrix = [[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        result_matrix[i][j] =matrix_A[i][j]+ matrix_B[i][j]

for row in result_matrix:
    print(*row)



