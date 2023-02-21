import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

F = [n-i+1 for i in range(n+1)]
S = [0]*(n+1)
for i in range(n-1, -1, -1):
    F[i] = F[i]*F[i + 1]

visited = [False]*(n+1)
visited[0] = True
out = []

if arr[0] == 1:
    k = arr[1]

    for i in range(1, n+1):
        cnt = 1

        for j in range(1, n+1):
            if visited[j]:
                continue
            print(i, k, cnt*F[i], F[i])
            if k <= cnt*F[i]:
                k -= (cnt-1)*F[i]

                S[i] = j
                visited[j] = True
                break
            cnt += 1

    print(' '.join(map(str, S[1:])))

else:
    K = 1

    for i in range(1, n):
        cnt = 0

        for j in range(1, arr[i]):
            if not visited[j]:
                cnt += 1
        # print(arr[i], cnt, F[i])
        K += cnt * F[i+1]
        visited[arr[i]] = True
    print(K)

