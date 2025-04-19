def solution(my_string, s, e):
    return my_string[:s] + my_string[s:e+1][::-1] + my_string[e+1:] # 인덱스에 e+1 이런게 가능하구나