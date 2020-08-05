n = 13
lst = []
i = 1
if n<2:
	print(n)
	exit(0)
while i*i <= n:
	lst.append(i*i)
	i+=1
tocheck = {n}
cnt = 0
while tocheck:
	temp = set()
	cnt+=1
	for i in tocheck:
		for j in lst:
			if i == j:
				print(cnt)
				exit(0)
			elif i < j:
				break
			temp.add(i - j)
		tocheck = temp

print(cnt)