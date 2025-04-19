def solution(n, numlist):
    answer = []
    for i in numlist:
        if i % n == 0:
           # answer += i # append 매서드 써야해
            answer.append(i)
    return answer