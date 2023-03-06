n = int(input())
a = {}
for i in range(n):
	key = input()
	if key in a:
		a[key] += 1
	else:
		a[key] = 1
for i, j in sorted(a.items() key = lambda `):
	print(i, j)