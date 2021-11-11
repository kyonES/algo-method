# Q3-1. 部分和問題 (導入編)
# https://algo-method.com/tasks/336
N, M = map(int, input().split())
A = list(map(int, input().split()))
# N*Mの配列
dp = [[False]*M for _ in range(N)]
# 初期状態
dp[0][0] = True
for i in range(N-1):
    for j in range(M):
        if not dp[i][j]:
            continue
        dp[i+1][j] = True
        if j+A[i] < M:
            dp[i+1][j+A[i]] = True
print(len(list(filter(lambda x: x, dp[N-1]))))
