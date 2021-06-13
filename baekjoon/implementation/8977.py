# 백준 온라인 저지 8977번: DISPLEJ
# https://www.acmicpc.net/problem/8977

import sys

input = sys.stdin.readline

# Solution 1

n, k, b = map(int, input().split())
nums = list(map(int, input().split()))
answer = 0

for i in range(k):
    r = b % n
    if r + i - 1 >= n:
        r = (r + i) % n - i
    answer += nums[r+i-1]

print(answer)

# Solution 2

'''
def main():
    n, k, b = map(int, input().split())
    nums = list(map(int, input().split()))
    answer = 0

    for i in range(k):
        r = b % n
        if r + i - 1 >= n:
            r = (r + i) % n - i
        answer += nums[r+i-1]

    print(answer)

if __name__ == '__main__':
    sys.exit(main())
'''