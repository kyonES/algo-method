# ペアの全探索3
# https://algo-method.com/tasks/259
N = int(input())
A = list(map(int, input().split()))
count = 0
for i, x in enumerate(A):
    for j, y in enumerate(A):
        for k, z in enumerate(A):
            if i < j and j < k and max(x, y, z) == y:
                count += 1
print(count)
