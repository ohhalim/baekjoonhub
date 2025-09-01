N = int(input())

numbers = input().strip()

total = 0

for i in range(N):
    total += int(numbers[i])

print(total)