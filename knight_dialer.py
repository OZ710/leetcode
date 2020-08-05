import numpy as np

N = int(input())

a = 10 ** 9 + 7
paths = [[4,6], [6,8], [7,9], [4,8], [0,3,9], [], [0,1,7], [2,6],
                 [1,3], [2,4]]

dp = np.zeros(((N+1),10))

for i in range(10):
	dp[1][i] = 1

for i in range(2,N+1):
	for j in range(10):
		for x in paths[j]:
			dp[i][j] = (dp[i][j] + dp[i-1][x]) % a
res = 0
for i in range(10):
	res  = (res + dp[N][i]) % a

print(int(res))