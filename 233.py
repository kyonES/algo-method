# 複数の配列の全探索3
# https://algo-method.com/tasks/233
X, Y, Z = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
count = 0
for x in A:
    for y in B:
        for z in C:
            if x+y == z:
                count += 1
print(count)
