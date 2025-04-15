def solution(progresses, speeds):
    print(progresses)  # 현재 작업의 진행률 목록 출력
    print(speeds)      # 각 작업의 개발 속도 목록 출력
    answer = []        # 결과를 저장할 리스트 초기화
    time = 0           # 경과 시간 초기화 
    count = 0          # 한 번에 배포될 기능 수 초기화

    # 모든 작업이 배포될 때까지 반복
    while len(progresses) > 0:
        # 첫 번째 작업이 완료되었는지 확인 (진행률 + 시간*속도 >= 100)
        if (progresses[0] + time*speeds[0]) >= 100:
            progresses.pop(0)  # 첫 번째 작업 제거
            speeds.pop(0)      # 첫 번째 작업의 속도 제거
            count += 1         # 배포될 기능 수 증가
        else:
            # 첫 번째 작업이 완료되지 않았지만 이전에 완료된 작업이 있으면
            if count > 0:
                answer.append(count)  # 완료된 작업 수를 결과에 추가
                count = 0             # 카운트 초기화
            time += 1                 # 시간 증가
    
    # 마지막 배포 묶음 추가
    answer.append(count)
    return answer      # 각 배포마다 배포되는 기능의 개수 반환

