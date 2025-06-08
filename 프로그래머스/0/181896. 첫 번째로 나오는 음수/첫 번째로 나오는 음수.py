# 내가 생각했던 방식
# def solution(num_list):
#     for i in range(len(num_list)):
#         if num_list[i] < 0:
#             return i-1
#         else:
#             return -1

def solution(num_list):
    for i in range(len(num_list)):
        if num_list[i] < 0:
            return i 
        
    return -1