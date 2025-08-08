def solution(numbers):
    # 1. 영어 숫자 단어와 해당하는 숫자를 매핑하는 딕셔너리
    num_map = {
        "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
        "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
    }

    # 2. 문자열에서 영어 숫자 단어를 숫자로 대체
    for word, digit in num_map.items(): # <<< 여기에 items() 사용
        numbers = numbers.replace(word, digit)

    # 3. 최종 문자열을 정수로 변환하여 반환
    return int(numbers)