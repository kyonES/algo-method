# ペアの全探索4
# https://algo-method.com/tasks/260
N = int(input())
ss = []
ans = 'No'
for i in range(N):
    S = input()
    ss.append(S)
for i, a in enumerate(ss):
    for j, b in enumerate(ss):
        if i != j and a == b:
            ans = 'Yes'
print(ans)
