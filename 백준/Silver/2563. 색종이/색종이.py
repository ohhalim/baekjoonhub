# 1. 100x100 도화지 배열 생성
paper = [[False] * 100 for _ in range(100)]

# 2. 색종이 개수 입력
n = int(input())

# 3. 각 색종이마다 10x10 영역 마킹
for _ in range(n):
    x, y = map(int, input().split())
    
    # (x, y)부터 10x10 칸을 True로 마킹
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            paper[i][j] = True

# 4. True인 칸 개수 세기
count = 0
for i in range(100):
    for j in range(100):
        if paper[i][j]:
            count += 1

print(count)