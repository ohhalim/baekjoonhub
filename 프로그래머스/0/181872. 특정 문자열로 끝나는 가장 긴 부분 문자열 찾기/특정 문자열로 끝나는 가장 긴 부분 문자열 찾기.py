def solution(myString, pat):
    for i in range(len(myString), 0, -1):
        substring = myString[:i]
        if substring.endswith(pat):
            return substring