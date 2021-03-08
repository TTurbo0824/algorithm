import sys

arr = []
for _ in range(9):
    arr.append(sys.stdin.readline().strip())


max_num = max(arr)
print(arr.index(max_num))
