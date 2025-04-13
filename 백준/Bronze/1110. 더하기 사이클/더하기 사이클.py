def cycle_length(N):
    original = N
    count = 0
    
    while True:
        # 10보다 작으면 앞에 0을 붙인다 (계산을 위해)
        if N < 10:
            tens = 0
            ones = N
        else:
            tens = N // 10
            ones = N % 10
        
        # 각 자리 숫자의 합
        digit_sum = tens + ones
        
        # 새로운 수 생성: 기존 수의 오른쪽 자리 + 합의 오른쪽 자리
        N = ones * 10 + digit_sum % 10
        
        count += 1
        
        # 원래 수로 돌아오면 종료
        if N == original:
            break
            
    return count

# 입력 받기
N = int(input())
print(cycle_length(N))