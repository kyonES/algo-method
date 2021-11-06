# 複数の配列の全探索2
# https://algo-method.com/tasks/232
import itertools
n, m, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
p = itertools.product(A, B)
ans = 0
for a, b in p:
    if a+b == k:
        ans += 1
print(ans)
