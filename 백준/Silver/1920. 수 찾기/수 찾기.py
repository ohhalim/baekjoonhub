# 전역 코드로 풀이
n = int(input())
A = list(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))

A_set = set(A)  # 탐색 속도를 높이기 위해 집합으로 변환

for target in targets:
    if target in A_set:
        print(1)
    else:
        print(0)