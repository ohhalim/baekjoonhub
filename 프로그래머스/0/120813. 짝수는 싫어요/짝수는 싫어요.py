def solution(n):
    result = []
    for i in range(n+1):
        if i % 2 == 1:
            result.append(i)
    return result