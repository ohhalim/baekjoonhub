def solution(myString, pat):
    low_my = myString.lower()
    low_pat = pat.lower()
    answer = 0 # 정수를 표현하려면 0으로 해야함
    
    if low_pat in low_my:
        return 1
    else:
        return 0
