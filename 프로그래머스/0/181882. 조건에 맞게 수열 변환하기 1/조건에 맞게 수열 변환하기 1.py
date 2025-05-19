def solution(arr):
    answer = []
    for i in arr:
        if i >= 50 and i % 2 == 0:
            answer.append(i // 2) # / 는 소수점이 나오는 나눗셈이다 
        elif i < 50 and i % 2 != 0:
            answer.append(i * 2)
        else: # 그대로 유지할때 i 그대로 
            answer.append(i)
    return answer