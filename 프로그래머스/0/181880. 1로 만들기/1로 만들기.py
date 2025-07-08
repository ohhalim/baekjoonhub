def solution(num_list):
    total_count = 0

    for num in num_list:
        count = 0
        while num != 1:
            if num % 2 == 0:
                num = num //2 
            else: 
                num = (num - 1) // 2 
            count += 1
        total_count += count
    return total_count
    