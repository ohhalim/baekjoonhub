from collections import deque

def solution(priorities, location):
    queue = deque([(i, p) for i, p in enumerate(priorities)])
    count = 0 

    while queue:
        current = queue.popleft()
        if any(current[1] < q[1] for q in queue):
            queue.append(current)
        else:
            count += 1
            if current[0] == location:
                return count
            
    return count 