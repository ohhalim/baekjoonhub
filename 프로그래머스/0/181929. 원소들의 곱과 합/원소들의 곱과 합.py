
def solution(num_list):
    total_sum = sum(num_list)

    total_square = total_sum * total_sum

    total_product = 1
    for num in num_list:
        total_product *= num

    if total_product < total_square:
        return 1 
    else: 
        return 0 