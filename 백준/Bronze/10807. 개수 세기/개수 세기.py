# list로 공백을 기준으로 구분된 정수들을 리스트로 변화
N = int(input())
S = list(map(int, input().split()))
v = int(input())


numbers = S.count(v)

print(numbers)
