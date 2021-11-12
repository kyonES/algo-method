# Q1-2. マスの移動 (1)
# https://algo-method.com/tasks/303
N = int(input())
A = list(map(int, input().split()))
dp = [0]*N
dp[1] = A[1]
for i in range(2, N):
    dp[i] = min(dp[i-1]+A[i], dp[i-2]+A[i]*2)
print(dp[-1])
