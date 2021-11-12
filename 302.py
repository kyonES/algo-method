# Q1-1. 数字の列
# https://algo-method.com/tasks/302
N, X, Y = map(int, input().split())
A = [0]*N
# 初期値
A[0], A[1] = X, Y
for i in range(2, N):
    A[i] = (A[i-2]+A[i-1]) % 100
print(A[-1])
