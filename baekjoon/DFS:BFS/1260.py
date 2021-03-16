# 백준 온라인 저지 1260번: DFS와 BFS
# www.acmicpc.net/problem/1260

N, M, V = map(int, input().split())

graph = [[0] * (N + 1) for i in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

def dfs(current_node, visited):
    visited += [current_node]
    for search_node in range(len(graph[current_node])):
        if graph[current_node][search_node] and search_node not in visited:
            visited = dfs(search_node, visited)
    return visited

def bfs(start_node):
    queue = [start_node]
    visited = [start_node]
    while queue:
        current_node = queue.pop(0)
        for search_node in range(len(graph[current_node])):
            if graph[current_node][search_node] and search_node not in visited:
                visited += [search_node]
                queue += [search_node]
    return visited

print(*dfs(V, []))
print(*bfs(V))