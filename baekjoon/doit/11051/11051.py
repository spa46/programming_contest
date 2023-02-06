import sys

n, r = map(int, sys.stdin.readline().split())

dp =[[0]*(n+1) for _ in range(n+1)]
for i in range(len(dp)):
    dp[i][i] = 1
    dp[i][0] = 1

for i in range(1, len(dp)):
    for j in range(1, i):
        dp[i][j] = (dp[i-1][j] + dp[i-1][j-1]) % 10007

# for i in range(len(dp)):
#     print(dp[i])

print(dp[n][r])