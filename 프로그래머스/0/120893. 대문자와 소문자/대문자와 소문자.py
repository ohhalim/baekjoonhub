# def solution(my_string):
#     answer = ''
#     devid_str = my_string.split()
#     for i in devid_str:
#         if upper.devid_str == i:
#             answer.append(lower(i))
#         else:
#             answer.append(upper(i))
#     return answer

# def solution(my_string):
#     answer = []
#     devid_str = my_string.split() # split사용하면 안되었음 그래서 틀렸음
#     for i in devid_str:
#         if  i.upper() == i:
#             answer.append(i.lower())
#         else:
#             answer.append(i.upper())
#     return " ".join(answer)# 문자열을 공백으로 연결

# def solution(my_string):
#     answer = []
#     for char in my_string: # 문자열의 각 문자에 직접 접근
#         if char.isupper(): # 문자가 대문자인지 확인
#             answer.append(char.lower()) # 소문자로 변환하여 추가
#         else: # 문자가 소문자라면
#             answer.append(char.upper()) # 대문자로 변환하여 추가
#     return "".join(answer) 

def solution(my_string):
    answer = []
    for char in my_string:
        if char.isupper():
            answer.append(char.lower())
        else:
            answer.append(char.upper())
    return "".join(answer)