# Modulo Summation
input()
a = list(map(int, input().split()))
x = 1
for i in a:
    x *= i
print(sum(list(map(lambda j: (x - 1) % j, a))))
