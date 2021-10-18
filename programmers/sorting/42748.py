# 프로그래머스 정렬: K번째수
# https://programmers.co.kr/learn/courses/30/lessons/42748


def solution(array, commands):
    answer = []

    for i in range(0, len(commands)):
        answer.append(
            sorted(array[commands[i][0] - 1 : commands[i][1]])[commands[i][2] - 1]
        )

    return answer
