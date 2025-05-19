def solution(num_list):
    if len(num_list) > 10:
        answer = sum(num_list)
    else:
        answer = 1 # 곱셈의 초기값은 1이어야 한다
        for i in num_list:
            answer *= i
    return answer