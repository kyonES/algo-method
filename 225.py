# 数字の全探索5
# https://algo-method.com/tasks/225
N = int(input())
for i in range(1, N+1):
    if i % 15 == 0:
        print('FizzBuzz')
    elif i % 5 == 0:
        print('Buzz')
    elif i % 3 == 0:
        print('Fizz')
    else:
        print(i)
