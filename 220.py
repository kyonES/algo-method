# 数字の全探索1
# https://algo-method.com/tasks/220
N = int(input())
count = 0
for i in range(1, N+1):
    if i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
        count += 1
print(count)
