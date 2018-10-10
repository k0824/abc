# Card Game for Two
n = int(input())
a = sorted(list(map(int, input().split())), reverse=True)
p = 0
ans = 0
for i in a:
    if p % 2 == 0:
        ans += i
    else:
        ans -= i
    p += 1
print(ans)
