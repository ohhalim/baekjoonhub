
A, B = map(int, input().split())
C = int(input())

total_time = A * 60 + (B + C)

H = (total_time // 60) % 24 # 정수나눗셈 연산자로 해야함 > / 로 하면 실수로(0.1231341)나옴 정수나눗셈 연산자 // 씀
M = total_time % 60 

print(H, M)