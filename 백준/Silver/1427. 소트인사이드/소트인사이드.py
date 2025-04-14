# n = list(map(int, input().split()))
n = input()
# list_n = reversed(sorted(n)) # 이터레이터를 반환해서 안됌
list_n = sorted(map(int, n), reverse=True)
result = ''.join(map(str, list_n))
#answer = sum(list_n) 이거 아님 조인함수 써야함

# map 데이터 타입변환, 리스트 튜플 정수 문자열 등등
#join 문자열 결합
#    result = ''.join(digits)  # '123'가 됩니다.
print(result)
# 이터러블 -> 반복가능한 객체 -> 리스트, 튜플, string , dict, set