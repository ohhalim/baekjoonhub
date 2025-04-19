def solution(my_string):
    answer = []
    for i in my_string:  # 변수명 불일치 수정 (mystring → my_string)
        if i.isdigit():  # 문자가 숫자인지 확인하는 올바른 문법
            answer.append(int(i))  # 문자형 숫자를 정수로 변환하여 추가

    return sorted(answer)  # 정렬된 배열 반환