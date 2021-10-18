# 프로그래머스 해시: 완주하지 못한 선수
# https://programmers.co.kr/learn/courses/30/lessons/42576

import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
