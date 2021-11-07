# ペアの全探索1
# https://algo-method.com/tasks/244
N, K = map(int, input().split())
A = list(map(int, input().split()))
count = 0
for i, x in enumerate(A):
    for j, y in enumerate(A):
        if i < j and x+y <= K:
            count += 1
print(count)
