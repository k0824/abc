# Pyramid
n = int(input())
data = []
h_ = 0
for i in range(n):
    data.append(list(map(int, input().split())))
data = sorted(data, key=lambda x: x[2], reverse=True)
for cx in range(101):
    for cy in range(101):
        for j in range(n):
            if j == 0:
                h_ = data[0][2] + abs(cx - data[0][0]) + abs(cy - data[0][1])
            else:
                if data[j][2] == max(0, h_ - abs(cx - data[j][0]) - abs(cy - data[j][1])):
                    if j == n - 1:
                        print('{0} {1} {2}'.format(cx, cy, h_))
                        exit()
                    else:
                        continue
                else:
                    break
