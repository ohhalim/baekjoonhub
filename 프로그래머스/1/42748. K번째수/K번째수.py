# def solution(array, commands):
#     # 인덱스 사용한다 
#     # sorted로 정렬한다
#     # 몇 번째 숫자인지 찾는다
#     # 그걸 리스트로 만들기
#     answer = []
#     for command in commands:
#         i, j, k = command
#         result = sorted(array[i-1:j])
#         answer.append(result[k-1])

#     return answer

def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        result = sorted(array[i-1:j])
        answer.append(result[k-1])
    return answer