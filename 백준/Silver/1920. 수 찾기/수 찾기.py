import sys
input = sys.stdin.readline

n = int(input())
a = set(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

result = []
for x in b:
    if x in a:
        result.append('1')
    else: 
        result.append('0')
        
print('\n'.join(result))