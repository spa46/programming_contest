import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
k = int(sys.stdin.readline())
total = 0

for i in range(len(arr)):
    total += arr[i]

ans = 0
for i in range(n):
    j = 0
    tmp = 1
    while j<k:
        tmp *= (arr[i] - j)/(total - j)
        j+=1
    ans += tmp

print(ans)
