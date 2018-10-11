# Skip
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


n, large_x = map(int, input().split())
x = (list(map(int, input().split())))
d = -1
if n == 1:
    print(abs(x[0] - large_x))
    exit()
for i in range(n):
    x[i] = x[i] - large_x
for i in range(n):
    if d == -1:
        d = gcd(x[0], x[1])
    d = gcd(d, x[i])
print(d)
