# 二重ループの全探索
# https://algo-method.com/tasks/234
N = int(input())
A = list(map(int, input().split()))
ans = 0
for a in A:
    is_prime = True
    if a == 1:
        is_prime = False
    for k in range(2, a):
        if a % k == 0:
            is_prime = False
    if is_prime:
        ans += 1
print(ans)
