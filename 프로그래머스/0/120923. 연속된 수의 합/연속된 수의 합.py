def solution(num, total):
    start_num = (total - (num*(num -1) // 2 )) // num # 0 부터 num-1 까지의 합 을 .계산  // 나눗셈후 정수부분만 계산
    
    answer = []
    for i in range(num):
        answer.append(start_num +i)
    
    return answer
