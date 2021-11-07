# ペアの全探索5
# https://algo-method.com/tasks/261
N = int(input())
S = input()
count = 0
for x, a in enumerate(S):
    for y, b in enumerate(S):
        if a == b and x < y:
            count += 1
print(count)
