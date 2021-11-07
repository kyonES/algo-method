# ペアの全探索2
# https://algo-method.com/tasks/245
L, R = map(int, input().split())
ans = 0
for i in range(L, R+1):
    for j in range(L, R+1):
        if i % 10 == j % 10 and i < j:
            ans += 1
print(ans)
