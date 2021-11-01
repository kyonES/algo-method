# 数字の全探索2
# https://algo-method.com/tasks/221
N = int(input())
count = 0
for i in range(1, N+1):
    if N % i == 0:
        count += 1
print(count)
