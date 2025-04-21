def solution(s):
    answer = [] # 빈 리스트 생성

    s1 = s.lstrip('{').rstrip('}').split('},{') # {, }바같쪽 중괄호 제거 strip으로 그리고 split()으로 나누어서 s1 저장

    new_s = [] # 새로운 빈 리스트 생성
    for i in s1:
        new_s.append(i.split(','))# ,없이 새로운 리스트 생성

    new_s.sort(key = len) # 길이에 따라 리스트들을 정렬

    for i in new_s: 
        for j in range(len(i)):  # 각 new_s리스트에 길이 많큼 j돌리고 answer리스트에 i[j]가 없으면 append 로 집어넣어라
            if int(i[j]) not in answer:
                answer.append(int(i[j]))

    return answer

