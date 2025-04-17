n = int(input())
p = list(map(int, input().split()))
result = 0
time = sorted(p)
waiting = 0

for t in time:
    waiting += t
    result += waiting
    
print(result)