def solution(clothes):
    # 1. 종류별로 개수 세기
    count = {}
    
    for name, category in clothes:
        # 카테고리가 없으면 0으로 시작
        if category not in count:
            count[category] = 0
        count[category] += 1
    
    # 2. 경우의 수 계산
    result = 1
    
    for category in count:
        # (해당 종류 개수 + 안 입는 경우 1)
        result *= (count[category] + 1)
    
    # 3. 아무것도 안 입는 경우 제외
    return result - 1