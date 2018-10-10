# Time limit Exceeded
n, largeT = map(int, input().split())
ans = []
for i in range(n):
    c, t = map(int, input().split())
    if t <= largeT:
        ans.append(c)
try:
    print(min(ans))
except ValueError:
    print('TLE')
