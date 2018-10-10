# AtCoder Beginner Contest 111
n = int(input())
if n % 111 == 0:
    print(n)
else:
    print(n - n % 111 + 111)
