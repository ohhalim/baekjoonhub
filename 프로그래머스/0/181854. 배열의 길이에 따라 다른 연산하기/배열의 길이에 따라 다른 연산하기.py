def solution(arr, n):
    if len(arr) % 2 == 0:  # 배열 길이가 짝수인 경우
        return [arr[i] + n if i % 2 == 1 else arr[i] for i in range(len(arr))]
    else:  # 배열 길이가 홀수인 경우
        return [arr[i] + n if i % 2 == 0 else arr[i] for i in range(len(arr))]