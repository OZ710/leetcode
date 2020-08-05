l1 = [4, 3 , 2]
l2 = [3, 0, 0]
for i in range(len(l1)-1):
	if l1[i] >= l2[i]:
		d = l1[i] - l2[i]
		l1[i]-=d
		l1[i+1]-=d
		flag = 1
	else:
		flag = 0
		break

if flag == 0:
	print("NO")
else:
	print("YES")
