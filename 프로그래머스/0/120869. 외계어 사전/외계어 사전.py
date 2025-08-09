def solution(spell, dic):
    # 1. spell 배열의 알파벳들을 정렬하여 기준 문자열 생성
    # join을 사용하기 위해 spell 리스트를 정렬한 후 문자열로 변환합니다.
    sorted_spell = "".join(sorted(spell))

    # 2. dic의 각 단어에 대해 확인
    for word in dic:
        # 현재 단어의 알파벳들을 정렬
        sorted_word = "".join(sorted(word))

        # 3. 정렬된 단어가 spell의 정렬된 문자열과 동일하고 길이가 같은지 확인
        # 길이가 다른 경우는 spell의 모든 원소를 사용하지 않았거나,
        # spell에 없는 문자를 사용한 경우이므로 필터링합니다.
        if len(word) == len(spell) and sorted_word == sorted_spell:
            return 1 # 일치하는 단어를 찾으면 1 반환

    # 4. 일치하는 단어를 찾지 못하면 2 반환
    return 2