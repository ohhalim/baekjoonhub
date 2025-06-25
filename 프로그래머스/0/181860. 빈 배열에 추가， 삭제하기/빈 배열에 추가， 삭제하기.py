def solution(arr, flag):
    x = []
    for i in range(len(arr)):
        if flag[i]:
            x.extend([arr[i]] * (arr[i] * 2))
        else:
            x = x[:-arr[i]]
    return x