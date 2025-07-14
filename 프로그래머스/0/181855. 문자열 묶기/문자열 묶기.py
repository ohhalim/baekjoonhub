def solution(strArr):
    length_count = {}

    for s in strArr:
        length = len(s)
        length_count[length] = length_count.get(length, 0) + 1

    return max(length_count.values())