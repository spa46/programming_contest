import sys

t = int(sys.stdin.readline())

arr = []
w, h = 0, 0
for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    arr.append((a, b))
    w = max(w, a)
    h = max(w, b)

dp = [[0]*(w+1) for _ in range(h+1)]

for i in range(1, h+1):
    dp[i][1] = i
    if i <= w:
        dp[i][i] = 1

for i in range(3, h + 1):
    for j in range(2, w + 1):
        dp[i][j] = dp[i-1][j] + dp[i-1][j-1]

# for i in range(h+1):
#     print(dp[i])

for i, j in arr:
    print(dp[j][i])