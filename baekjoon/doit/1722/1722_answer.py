import sys

F = [0]*21
S = [0]*21
visited = [False]*21
n = int(sys.stdin.readline())
F[0] = 1

for i in range(1, n+1):
    F[i] = F[i-1] * i

arr = list(map(int, sys.stdin.readline().split()))

if arr[0] == 1:
    k = arr[1]

    for i in range(1, n+1):
        cnt = 1
        for j in range(1, n+1):
            if visited[j]:
                continue
            # print(f'@{i}={j}, {k}, {F[n-i]}*{cnt}')
            if k <= F[n-i]*cnt:
                k -= F[n-i]*(cnt-1)
                S[i] = j
                visited[j] = True
                break

            cnt += 1
    print(' '.join(map(str, S[1:n+1])))
else:
    k = 1

    for i in range(1, n+1):
        cnt = 0

        for j in range(1, arr[i]):
            if not visited[j]:
                cnt += 1

        k += cnt * F[n-i]
        visited[arr[i]] = True
    print(k)