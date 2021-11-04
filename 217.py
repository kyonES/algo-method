# 配列の全探索9
# https://algo-method.com/tasks/217/editorial
N = int(input())
A = list(map(int, input().split()))
count = [0]*9
for x in A:
    count[x-1] += 1
for x in count:
    print(x)
