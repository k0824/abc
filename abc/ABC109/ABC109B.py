# Shiritori
n = int(input())
li = []
for i in range(n):
    li.append(list(input()))
for j in range(n-1):
    if li[j][-1] == li[j+1][0]:
        for k in range(j):
            if li[j] == li[k]:
                print('No')
                exit()
    else:
        print('No')
        exit()
print('Yes')
