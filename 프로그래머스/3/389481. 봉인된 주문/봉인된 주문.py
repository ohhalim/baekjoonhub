from typing import List, Dict
import bisect
import string

def solution(n: int, bans: List[str]) -> str:
    # 1) 유효한 ban만 필터링 (소문자, 길이 1~11)
    bans = [b for b in bans if b.isalpha() and b.islower() and 1 <= len(b) <= 11]
    # 중복 제거
    bans_set = set(bans)

    # 2) 길이별로 금지 문자열 분류
    bans_by_len: Dict[int, List[str]] = {L: [] for L in range(1, 12)}
    for b in bans_set:
        bans_by_len[len(b)].append(b)

    # 3) 접두사 카운트 맵 만들기: 각 길이 L에 대해 prefix -> count
    #    ex) "ae"가 금지면 "a":1, "ae":1 이 증가
    banned_prefix_count: Dict[int, Dict[str, int]] = {L: {} for L in range(1, 12)}
    for L in range(1, 12):
        pref_map = banned_prefix_count[L]
        for w in bans_by_len[L]:
            for k in range(1, L + 1):
                p = w[:k]
                pref_map[p] = pref_map.get(p, 0) + 1

    # 4) 26의 거듭제곱 미리 계산
    pow26 = [1] * 12
    for i in range(1, 12):
        pow26[i] = pow26[i - 1] * 26

    # 5) 목표 길이 L 찾기 (길이별 전체 유효 개수로 n을 깎음)
    target_len = None
    for L in range(1, 12):
        total_L = pow26[L]  # 길이 L 전체 문자열 개수
        banned_L = len(bans_by_len[L])
        valid_L = total_L - banned_L
        if n > valid_L:
            n -= valid_L
        else:
            target_len = L
            break

    # (문제에서 n이 항상 유효하다고 가정)
    if target_len is None:
        raise ValueError("n이 가능한 범위를 초과했습니다.")

    # 6) 사전순으로 한 글자씩 결정
    res = []
    letters = string.ascii_lowercase  # 'a'..'z'
    L = target_len
    pref_map = banned_prefix_count[L]

    for pos in range(L):
        for ch in letters:
            cand_prefix = "".join(res) + ch
            remain = L - (pos + 1)
            total_branch = pow26[remain]  # cand_prefix로 시작하는 전체 개수
            banned_branch = pref_map.get(cand_prefix, 0)  # 그 중 금지 개수
            valid_branch = total_branch - banned_branch

            if n > valid_branch:
                n -= valid_branch
            else:
                res.append(ch)
                break

    return "".join(res)