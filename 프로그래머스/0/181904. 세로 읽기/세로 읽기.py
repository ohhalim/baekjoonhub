def solution(my_string, m , c):
    result =""
    num_rows = len(my_string) // m

    for i in range(num_rows):
        index = i * m + (c - 1)
        result  += my_string[index]
    return result