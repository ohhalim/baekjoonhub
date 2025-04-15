# ai가 짜준거 
from collections import deque
test_case_num = int(input())

for _ in range(test_case_num):
    n, m = map(int, input().split())
    priorities = list(map(int, input().split()))

    queue =deque([(idx, priority) for idx, priority in enumerate(priorities)])
    count = 0

    while queue:
        current = queue.popleft()
        if any(current[1] < item[1] for item in queue):
            queue.append(current)
        else:
            count += 1

            if current[0] == m:
                print(count)
                break