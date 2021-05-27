# 백준 온라인 저지 4714번: Lunacy
# https://www.acmicpc.net/problem/4714

# Solution 1

'''
while True:
    n = input()
    weight = format(float(n), ".2f")
    newWeight = format(float(n) *  0.167, ".2f" )
    
    if n == "-1.0":
        break

    print("Objects weighing", weight, "on Earth will weigh", newWeight, "on the moon.")
'''

# Solution 2

while True:
    weight = float(input())

    if weight == -1:
        break

    print("Objects weighing %.2f on Earth will weigh %.2f on the moon." % (weight, weight * 0.167))