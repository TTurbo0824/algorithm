# 프로그래머스 연습문제: 소수 찾기
# https://programmers.co.kr/learn/courses/30/lessons/12921


def solution(n):
    count = 0

    for i in range(1, n + 1):
        if prime(i) == True:
            count += 1
    return count


def prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
