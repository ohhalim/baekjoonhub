# def solution(my_string, letter):
#     answer = my_string.replace(letter, "") # pop() 리스트에서 사용하는 매서드[] / 문자열 str 에서 안씀
#     return answer

# def solution(my_string, letter): 
#     a = list(letter)
#     b = list(my_string)
#     result = map(str, b.pop(a))
#     return b 

def solution(my_string, letter): 
    answer = my_string.replace(letter, "")
    return answer