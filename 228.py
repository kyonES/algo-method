# 文字列の全探索3
# https://algo-method.com/tasks/228
S = input()
N = len(S)
ans = 0
for i in range(N-1):
    if S[i] == S[i+1]:
        ans += 1
print(ans)
