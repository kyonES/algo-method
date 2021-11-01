# 数字の全探索3
# https://algo-method.com/tasks/222
N = int(input())
if N == 1:
    print('No')
else:
    count = 0
    for i in range(2, N):
        if N % i == 0:
            count += 1
    if count == 0:
        print('Yes')
    else:
        print('No')
