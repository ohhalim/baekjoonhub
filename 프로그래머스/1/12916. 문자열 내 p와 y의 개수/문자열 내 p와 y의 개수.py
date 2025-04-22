def solution(s):
    result_p = 0
    result_y = 0
    S = s.lower
    
    for i in S:
        if i == "p":
            result_p += 1
        elif i == "y":
            result_y += 1
    
    if result_p == result_y:
        result = True
    else:
        result = False
        
    return result

# 매서드 count 쓰면 해당 문자의 횟수를 알수있구나 

def solution(s):
    s = s.lower()
    return s.count('p') == s.count('y')