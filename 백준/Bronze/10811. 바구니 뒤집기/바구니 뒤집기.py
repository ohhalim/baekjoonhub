# 바구니의 개수 N과 순서를 바꿀 횟수 M 입력
N, M = map(int, input().split())
# 바구니 초기화
baskets = list(range(1, N + 1))

# M번 만큼의 순서 변경 입력
for _ in range(M):
    i, j = map(int, input().split())
    # i번째부터 j번째까지 역순으로 변경
    baskets[i-1:j] = baskets[i-1:j][::-1]

# 결과 출력
print(*baskets)