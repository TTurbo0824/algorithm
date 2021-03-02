# 백준 온라인 저지 1758
# https://www.acmicpc.net/problem/1758

n = int(input())
tip_list = []
for i in range(n):
    tip = int(input())
    tip_list.append(tip)

tip_list.sort(reverse=True)
total = 0

for i in range(len(tip_list)):
    real_tip = tip_list[i] - ((i + 1 - 1))
    if real_tip <= 0:
        break
    total += real_tip

print(total)