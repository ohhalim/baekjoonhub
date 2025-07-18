def solution(myString, pat):
    count = 0
    start = 0
    
    while True:
        pos = myString.find(pat, start)
        if pos == -1:
            break
        count += 1
        start = pos + 1
    
    return count

# print(solution('banana', 'ana'))