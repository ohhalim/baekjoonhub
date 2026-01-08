from collections import deque

def solution(maps):
    n = len(maps)      # 행 개수
    m = len(maps[0])   # 열 개수
    
    # 상하좌우 이동
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # 방문 체크 + 거리 저장
    distance = [[0] * m for _ in range(n)]
    
    # BFS 큐 (deque 사용 - 빠름)
    queue = deque()
    
    # 시작점
    queue.append((0, 0))
    distance[0][0] = 1
    
    # BFS 시작
    while queue:
        x, y = queue.popleft()  # 큐에서 꺼냄
        
        # 도착점이면 끝
        if x == n - 1 and y == m - 1:
            return distance[x][y]
        
        # 상하좌우 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 범위 안 && 길(1) && 방문 안함
            if 0 <= nx < n and 0 <= ny < m \
               and maps[nx][ny] == 1 \
               and distance[nx][ny] == 0:
                
                distance[nx][ny] = distance[x][y] + 1
                queue.append((nx, ny))
    
    # 도착 못하면 -1
    return -1