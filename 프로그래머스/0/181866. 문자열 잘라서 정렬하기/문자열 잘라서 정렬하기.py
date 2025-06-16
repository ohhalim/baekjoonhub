
def solution(myString):
    temp_list = myString.split("x")
    answer = []

    for part in temp_list:
        if part:
            answer.append(part)
    answer.sort() # return amswer.sort() 이거 작동하지 않음. 파이썬에서 list.sort() 메서드는 리스트를 제자리에서(in-place) 정렬하고, 아무것도 반환하지 않습니다. 즉, None을 반환합니다.
    return answer
