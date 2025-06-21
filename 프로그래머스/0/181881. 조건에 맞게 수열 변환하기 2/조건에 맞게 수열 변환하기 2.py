def solution(arr):
    def transform(num):
        if num >= 50 and num % 2 == 0:
            return num // 2
        elif num < 50 and num % 2 == 1:
            return num * 2 + 1
        return num

    prev_arr = arr
    count = 0
    
    while True:
        new_arr = [transform(num) for num in prev_arr]
        if new_arr == prev_arr:
            return count
        prev_arr = new_arr
        count += 1