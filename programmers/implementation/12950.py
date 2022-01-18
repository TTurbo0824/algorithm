# 프로그래머스 연습문제: 행렬의 덧셈
# https://programmers.co.kr/learn/courses/30/lessons/12950


def solution(arr1, arr2):
    answer = [[0] * len(arr1[0]) for _ in range(len(arr1))]

    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            answer[i][j] = arr1[i][j] + arr2[i][j]
    return answer
