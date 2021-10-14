# 프로그래머스 월간 코드 챌린지 시즌2: 음양 더하기
# https://programmers.co.kr/learn/courses/30/lessons/76501


def solution(absolutes, signs):
    answer = 0

    for idx in range(0, len(absolutes)):
        if signs[idx] == True:
            answer += absolutes[idx]
        else:
            answer -= absolutes[idx]

    return answer
