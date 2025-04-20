    # len(int_my_string): 배열의 길이꺄지
    # range() 인덱스 슬라이싱 이랑 같다
def solution(my_string):
    int_my_string = list(my_string.split())
    result = int(int_my_string[0])  # 첫 번째 숫자로 시작
    
    for i in range(1, len(int_my_string), 2):# 인덱스화해서 range를 사용할수있구나
        
        operator = int_my_string[i]
        operand = int(int_my_string[i+1])
        
        if operator == "+":
            result += operand
        elif operator == "-":
            result -= operand
            
    return result