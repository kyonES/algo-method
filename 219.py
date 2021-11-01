# 配列の全探索10
# https://algo-method.com/tasks/219
import numpy as np
N = int(input())
A = list(map(int, input().split()))
count = [0] * 9
for x in A:
    count[x-1] += 1
print(np.argmax(count)+1)
