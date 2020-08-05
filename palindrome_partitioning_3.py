import numpy as np
s = input()
n = len(s)
k = int(input())
cost = np.zeros((n,n))

for i in range(1,n):
	for j in range(n-i):
		if s[j]==s[j+i]:
			cost[j][j+i] = cost[j+1][j+i-1]
		else:
			cost[j][j+i] = 1 + cost[j+1][j+i-1]

dp = np.empty([n, k])
dp.fill(1000)
for i in range(n):
	dp[i][0] = cost[i][n-1]

for i in range(n-1,-1,-1):
	for j in range(1,k):
		partition = j+1
		if n-i < partition:
			break
		else:
			idx = i
			while idx + 1 < n:
				a = cost[i][idx]
				b = dp[idx+1][j-1]
				dp[i][j] = min(dp[i][j],a+b)
				idx+=1
print(dp[0][k-1])