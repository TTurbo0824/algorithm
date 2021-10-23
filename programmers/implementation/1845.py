# 프로그래머스 찾아라 프로그래밍 마에스터: 폰켓몬
# https://programmers.co.kr/learn/courses/30/lessons/1845


def solution(nums):
    half = len(nums) // 2
    type = len(set(nums))

    return half if half < type else type
