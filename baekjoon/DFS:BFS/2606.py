# 백준 온라인 저지 2606번: 바이러스
# www.acmicpc.net/problem/2606

n = int(input())
m = int(input())

graph = [[0] * (n + 1) for i in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1


def dfs(start, infected):
    infected += [start]
    for search_node in range(len(graph[start])):
        if graph[start][search_node] and search_node not in infected:
            infected = dfs(search_node, infected)
    return infected

print(len(dfs(1, [])) - 1)
