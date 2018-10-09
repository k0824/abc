# Shift only
n = int(input())
a = [int(s) for s in input().split()]
count = 0
dev_flag = 0
while dev_flag == 0:
	dev_flag = 0
	for num in a:
		if num % 2 == 1:
			dev_flag += 1
	if dev_flag == 0:
		index = 0
		for num in a:
			a[index] = num / 2
			index += 1
		count += 1
print(count)
