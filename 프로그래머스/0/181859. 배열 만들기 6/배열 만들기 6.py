def solution(arr):
    stk =[]
    i = 0

    while i < len(arr):
        if not stk: # 스텍이 비어있으면 
            stk.append(arr[i])
        elif stk[-1] == arr[i]:
            stk.pop()
        else:
            stk.append(arr[i])
        i += 1
    return stk if stk else [-1]
