from collections import Counter
from itertools import combinations

def _sum_distribution(dice_subset):
    # 합 분포를 Counter로 계산 (컨볼루션)
    dist = Counter({0: 1})
    for faces in dice_subset:
        nxt = Counter()
        for s, c in dist.items():
            for f in faces:
                nxt[s + f] += c
        dist = nxt
    return dist

def solution(dice):
    n = len(dice)
    k = n // 2
    all_indices = list(range(n))

    best_wins = -1
    best_choice = None

    # 모든 조합 탐색
    for A_idx in combinations(all_indices, k):
        B_idx = [i for i in all_indices if i not in A_idx]

        A_dist = _sum_distribution([dice[i] for i in A_idx])
        B_dist = _sum_distribution([dice[i] for i in B_idx])

        # 누적합 준비 (B 합의 최댓값 찾기)
        max_sum = 0
        if B_dist:
            max_sum = max(B_dist.keys())
        if A_dist:
            max_sum = max(max_sum, max(A_dist.keys()))

        cumB = [0] * (max_sum + 1)
        for s, cnt in B_dist.items():
            cumB[s] += cnt
        # 누적합: <= t 까지의 경우의 수
        for t in range(1, max_sum + 1):
            cumB[t] += cumB[t - 1]

        # A가 이기는 경우의 수 계산
        wins = 0
        for a_sum, a_cnt in A_dist.items():
            if a_sum - 1 >= 0:
                wins += a_cnt * cumB[a_sum - 1]
            # a_sum == 0이면 이길 수 없음

        if wins > best_wins:
            best_wins = wins
            best_choice = sorted([i + 1 for i in A_idx])  # 1-based, 오름차순

    return best_choice