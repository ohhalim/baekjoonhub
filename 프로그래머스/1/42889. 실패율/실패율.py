def solution(N, stages):
    # 각 스테이지별 도전 중인 사용자 수를 계산
    fail_counts = [0] * (N + 2)  # 인덱스를 1부터 시작하기 위해 N+2 크기로 생성
    for stage in stages:
        fail_counts[stage] += 1
    
    # 실패율 계산을 위한 리스트 초기화
    failure_rates = []
    
    # 해당 스테이지에 도달한 플레이어 수
    remaining_players = len(stages)
    
    # 각 스테이지의 실패율 계산
    for i in range(1, N + 1):
        # 스테이지에 도달한 플레이어가 없는 경우, 실패율은 0
        if remaining_players == 0:
            failure_rates.append((i, 0))
        else:
            failure_rates.append((i, fail_counts[i] / remaining_players))
            remaining_players -= fail_counts[i]
    
    # 실패율에 따라 내림차순 정렬, 실패율이 같은 경우 스테이지 번호 오름차순
    # key 함수에서 -x[1]은 실패율을 내림차순으로 정렬하게 함
    failure_rates.sort(key=lambda x: (-x[1], x[0]))
    
    # 정렬된 스테이지 번호만 추출하여 반환
    return [stage for stage, _ in failure_rates]

# 예제 1 테스트
N1 = 5
stages1 = [2, 1, 2, 6, 2, 4, 3, 3]
print("예제 1 결과:", solution(N1, stages1))  # [3, 4, 2, 1, 5]

# 예제 2 테스트
N2 = 4
stages2 = [4, 4, 4, 4, 4]
print("예제 2 결과:", solution(N2, stages2))  # [4, 1, 2, 3]