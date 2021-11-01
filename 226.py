# 文字列の全探索2
# https://algo-method.com/tasks/227
S = input()
new_str = S[::-1]
if S == new_str:
    print('Yes')
else:
    print('No')
