def solution(num, k):
    num_str = str(num)
    k_str = str(k)

    for i, char in enumerate(num_str):
        if char == k_str:
            return i + 1
    return -1
