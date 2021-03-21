# 백준 온라인 저지 1697번: 숨바꼭질
# https://www.acmicpc.net/problem/1697

from collections import deque

def bfs(start, target):
    queue = deque()
    queue.append(start)
    
    while queue:
        current = queue.popleft()
        if current == target:
            print(graph[current])
            break
        for next_node in [current - 1, current + 1, 2 * current]:
            if 0 <= next_node <= MAX and not graph[next_node]:
                graph[next_node] = graph[current] + 1
                queue.append(next_node)

MAX = 10 ** 5               
N, K = map(int, input().split())
graph = [0] * (MAX + 1)
bfs(N, K)