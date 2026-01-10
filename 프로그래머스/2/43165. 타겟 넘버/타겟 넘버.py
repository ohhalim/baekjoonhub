# def solution(numbers, target):
#     # DFS 함수 정의
#     def dfs(idx, current_sum):
#         # 종료 조건: 모든 숫자를 처리했을 때
#         if idx == len(numbers):
#             # 현재 합계가 타겟과 일치하면 1, 아니면 0 반환
#             return 1 if current_sum == target else 0
        
#         # 현재 숫자를 더하는 경우
#         plus = dfs(idx + 1, current_sum + numbers[idx])
        
#         # 현재 숫자를 빼는 경우
#         minus = dfs(idx + 1, current_sum - numbers[idx])
        
#         # 두 경우의 수를 합산하여 반환
#         return plus + minus
    
#     # DFS 시작 (인덱스 0, 초기 합계 0에서 시작)
#     return dfs(0, 0)

def solution(numbers, target):
    def dfs(index, current_sum):
        # 종료 조건
        if index == len(numbers):
            return 1 if current_sum == target else 0
        
        # +로 갔을 때 경우의 수 + -로 갔을 때 경우의 수
        return dfs(index + 1, current_sum + numbers[index]) + \
               dfs(index + 1, current_sum - numbers[index])
    
    return dfs(0, 0)