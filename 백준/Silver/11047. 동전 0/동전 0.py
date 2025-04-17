n, k = map(int, input().split())
coins = []
for _ in range(n): # 이렇게 차례대로 입력되는값을 리스트에 집어 넣는구나
    coins.append(int(input()))

# 먼저 coins =[ ] 로 초기값 설정하고
# 순회하면서 
# coins 리스트에 계속 더한다 정수값을

coins.sort(reverse = True) # 역순정렬

count = 0 # 초기값
for coin in coins:
    count += k // coin # 초기값이 있는 변수에 순환된 값들 넣는다
    k %= coin

    if k == 0:
        break

print(count)

