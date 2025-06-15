# 내가 생각한 방법
# def solution(strArr):
#     for i in range(strArr):
#         if strArr(i) in "ad":
#             strArr.remove(strArr(i))
#         else:
#             continue

#     return strArr

def solution(strArr):
    result = []
    for s in strArr:
        if "ad" not in s:
            result.append(s)
    return result