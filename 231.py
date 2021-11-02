# 二重ループの全探索2
# https://algo-method.com/tasks/235
N, K = map(int, input().split())


def count_divisor(n):
    count = 1
    # 約数の数を数える
    for i in range(2, n+1):
        if n % i == 0:
            count += 1
    return count


ans = 0
for i in range(1, N+1):
    if count_divisor(i) == K:
        ans += 1
print(ans)
