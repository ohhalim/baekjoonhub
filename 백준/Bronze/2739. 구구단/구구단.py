#f-string 문법중 
# "i * N" 이렇게 따옴표 안에 직접 텍스트를 쓰면 그대로 출력된다 
# 변수를 사용하려면 중괄호 {} 안에 넣어야 합니다.


# 결론 f string 쓸때 변수 사용하려면 {} 써

N = int(input())


for i in range(1, 10):

 #   print(f"i * N" = i * N)
    print(f"{N} * {i} = {i * N}")
