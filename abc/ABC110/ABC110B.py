# 1 Dimensional World's Tale
n, m, x, y = map(int, input().split())
x_max = max(list(map(int, input().split())))
y_min = min(list(map(int, input().split())))
if x_max < y and x_max < y_min and x < y_min:
    print('No War')
else:
    print('War')
