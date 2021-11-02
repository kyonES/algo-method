# 文字列の全探索1
# https://algo-method.com/tasks/226
S = input()
c = input()
N = len(S)

ans = False
for i in range(N):
    if S[i] == c:
        ans = True
if ans:
    print('Yes')
else:
    print('No')
