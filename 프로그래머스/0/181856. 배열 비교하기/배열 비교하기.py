def solution(arr1, arr2):
    # 배열 길이 비교
    if len(arr1) != len(arr2):
        if len(arr1) < len(arr2):
            return -1  # arr2가 더 길므로 arr2가 더 큼
        else:  # len(arr1) > len(arr2)
            return 1   # arr1이 더 길므로 arr1이 더 큼
    
    # 배열 길이가 같은 경우: 원소의 합 비교
    if sum(arr1) < sum(arr2):
        return -1      # arr2의 합이 더 크므로 arr2가 더 큼
    elif sum(arr1) > sum(arr2):
        return 1       # arr1의 합이 더 크므로 arr1이 더 큼
    else:  # sum(arr1) == sum(arr2)
        return 0       # 길이도 같고 합도 같으므로 두 배열은 같음