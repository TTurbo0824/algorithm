# 백준 온라인 저지 11724번: 연결 요소의 개수
# https://www.acmicpc.net/problem/11724

import sys

sys.setrecursionlimit(10000)

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[0] * (N + 1) for i in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1


def dfs(current_node, foot_prints):
    foot_prints += [current_node]
    for search_node in range(len(graph[current_node])):
        if graph[current_node][search_node] and search_node not in foot_prints:
            foot_prints = dfs(search_node, foot_prints)
    return foot_prints


answer = []
count = 0
for i in range(1, len(graph)):
    if i not in answer:
        answer.extend(dfs(i, []))
        count += 1

print(count)
