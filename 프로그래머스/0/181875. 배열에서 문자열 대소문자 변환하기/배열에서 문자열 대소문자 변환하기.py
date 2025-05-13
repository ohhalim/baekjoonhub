def solution(strArr):
    answer = []

    for i in strArr:
        if strArr.index(i) % 2 == 1: # 홀수 인덱스 확인?
            answer.append(i.upper())
        else:
            answer.append(i.lower())

    return answer
