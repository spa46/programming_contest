import sys
t = int(sys.stdin.readline())

df = 1
dr = 1
arr = []
for i in range(t):
    f = int(sys.stdin.readline())
    r = int(sys.stdin.readline())
    arr.append((f, r))
    df = max(df, f)
    dr = max(dr, r)

dp = [[0]*(dr+1) for _ in range(df+1)]

for j in range(dr+1):
    dp[0][j] = j

for i in range(df+1):
    dp[i][0] = 1

for i in range(1, df+1):
    sum = 0
    for j in range(1, dr + 1):
        sum += dp[i-1][j]
        dp[i][j] = sum

# for i in range(df+1):
#     print(dp[i])

for i, j in arr:
    print(dp[i][j])