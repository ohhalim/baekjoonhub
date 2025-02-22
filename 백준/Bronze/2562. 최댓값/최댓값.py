N = []
for _ in range(9):
    num = int(input())
    # append는 리스트 끝에 새로운 숫자를 추가한다
    N.append(num)

max_N = max(N)
print(max_N)

count = 1 
for num in N:
    if num == max_N:
        break
    count += 1
print(count )