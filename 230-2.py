# 関数を定義する
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


N = int(input())
A = list(map(int, input().split()))
ans = 0
for a in A:
    if is_prime(a):
        ans += 1
print(ans)
