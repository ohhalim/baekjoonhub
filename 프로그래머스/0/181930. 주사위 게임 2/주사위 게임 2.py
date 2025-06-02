

def solution(a, b, c):
    if a == b and b == c: # 세 숫자가 모두 같은 경우
        return (a + b + c) * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)
    elif a == b or b == c or a == c: # 세 숫자 중 두 숫자가 같은 경우 (세 숫자 모두 같은 경우는 위에서 걸러짐)
        return (a + b + c) * (a**2 + b**2 + c**2)
    else: # 세 숫자가 모두 다른 경우
        return a + b + c