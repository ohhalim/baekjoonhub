

N, X = map(int, input().split())

A = list(map(int, input().split()))

# A 정수중 X 보다 작은것만 출력 
for num in A:
    if num < X:
        # 그 수들을 공백으로 구분
        print(num, end=' ')