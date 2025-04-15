# ai가 해준거 
n = int(input())
cards = set(map(int, input().split()))  # cards를 집합으로 변환
m = int(input())
m_cards = map(int, input().split())

result = []  # 결과를 저장할 리스트

for card in m_cards:
    if card in cards:  # cards에 card가 있는지 확인
        result.append(1)
    else:
        result.append(0)

print(' '.join(map(str, result)))  # 결과를 공백으로 구분하여 출력

# 저장할리스트를 for문 돌리기 전에 민들어서 if 문의 출력내용이 저장할수있게 했구나
#