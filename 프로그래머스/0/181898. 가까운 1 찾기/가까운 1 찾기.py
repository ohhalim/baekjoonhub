def solution(arr, idx):
    # idx 보다 큰 인덱스 중 값이 1 인 가장 작은 인덱스를 찾아서 반환해라

    # for i in range(idx + 1, len(arr)):  # idx보다 큰 인덱스부터 시작
    #     if arr[i] == 1:  # 현재 인덱스의 값이 1인지 확인
    #         return i  # 값이 1인 경우 해당 인덱스를 반환
    # return -1  # 반복이 끝나고도 값을 찾지 못하면 -1을 반환


    for i in range(idx, len(arr)): # idx보다 큰 인덱스부터 시작
        if arr[i] == 1:
            return i
        
    return -1 # 반복이 끝났는데도 없으면 -1 을 반환