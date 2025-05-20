def solution(names):
    # 어떻게 5씩 나눌까?
    # 나누지 않아도 상관엾어 그냥 인덱스로 5간격으로 있는 사람을 뽑으면 되잖아
    answer = names[::5]
    return answer

# 테스트 함수 작성해보자
def test_solution():
    test_names = ["nami", "ahri", "jayce", "garen", "ivern", "vex", "jinx"]
    result = solution(test_names)
    print(result)

test_solution()