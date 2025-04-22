# def solution(arr):
#     result = []
#     a = sorted(arr)
#     if len(a) == 1:
#         result = -1
#     else: 
#         result = a[1]
#     return result
        
def solution(arr):
    if len(arr) == 1:
        return [-1]
    arr.remove(min(arr))
    return arr