# 바이러스에 걸리게 되는 컴퓨터 수를 찾아라
computer_count = int(input())
connect_pair_count = int(input())
graph = [[] for _ in range(computer_count + 1)]

for _ in range(connect_pair_count):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

visited =[False] * (computer_count + 1)

def dfs(start):
    visited[start] = True
    for next_computer in graph[start]:
        if not visited[next_computer]:
            dfs(next_computer)

dfs(1)

infected_count = visited.count(True) - 1

print(infected_count)