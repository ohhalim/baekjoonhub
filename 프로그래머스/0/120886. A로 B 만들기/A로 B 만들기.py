
def solution(before, after):
    if len(before) != len(after):
        return 0
    char_count = {}
    for char in before:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char in after:
        if char not in char_count or char_count[char] == 0:
            return 0
        char_count[char] -= 1
        
    return 1