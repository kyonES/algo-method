# 文字列の全探索5
# https://algo-method.com/tasks/229
S = input()
T = input()
N = len(S)
M = len(T)
ans = False
for i in range(N-M+1):
    if S[i:i+M] == T:
        ans = True
if ans:
    print('Yes')
else:
    print('No')
