def solution(n, lost, reserve):
    # 모든 학생이 체육복 1개씩 가지고 있다고 초기화
    student = [1] * n
    
    # 도난당한 학생은 체육복 -1
    for l in lost:
        student[l-1] -= 1
    
    # 여벌 가진 학생은 체육복 +1
    for r in reserve:
        student[r-1] += 1
    
    # 체육복 빌려주기
    for i in range(n):
        # 체육복이 없는 학생인 경우
        if student[i] == 0:
            # 앞번호 학생에게 빌릴 수 있는지 확인 (인덱스 범위 체크도 필요)
            if i > 0 and student[i-1] == 2:
                student[i] += 1
                student[i-1] -= 1
            # 뒷번호 학생에게 빌릴 수 있는지 확인
            elif i < n-1 and student[i+1] == 2:
                student[i] += 1
                student[i+1] -= 1
    
    # 체육복이 1개 이상인 학생 수 카운트
    count = 0
    for s in student:
        if s >= 1:
            count += 1
    
    return count