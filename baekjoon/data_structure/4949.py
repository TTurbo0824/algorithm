# 백준 온라인 저지 4949번: 균형잡힌 세상
# https://www.acmicpc.net/problem/4949

import sys

input = sys.stdin.readline

while True:
    s = input().rstrip()
    if s == '.':
        break
    stack = []
    isBalanced = True

    if s.count('(') != s.count(')') or s.count('[') != s.count(']'):
        isBalanced = False
    elif s.count('(') == s.count(')') == s.count('[') == s.count(']') == 0:
        isBalanced = True
    else:
        for ch in s:
            if ch == '(' or ch == '[':
                stack.append(ch)
            elif ch == ')' or ch == ']':
                if stack and ch == ')'and stack[-1] == '(':
                    stack.pop()
                elif stack and ch == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    isBalanced = False
                    break

    print('no' if isBalanced == False else 'yes')