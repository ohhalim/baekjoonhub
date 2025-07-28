def solution(n):
    n_str = str(n)
    answer  = 0 
    
    for dight in n_str:
        answer += int(dight)
    return answer