n = int(input())
# data = [list(map(int, input().split())) for _ in range(n)]
# data = [tuple(map(int, input().split())) for _ in range(n)]


data = []

for _ in range(n):
    weight, height = map(int, input().split())
    data.append((weight, height))

ranks = []

for i in range(n):
    count = 0

    for j in range(n): 
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
            count += 1 
    ranks.append(count + 1)

print(' '.join(map(str, ranks)))