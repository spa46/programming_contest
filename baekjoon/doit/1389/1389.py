import sys

if __name__ == '__main__':
    n,m = map(int, sys.stdin.readline().split())

    arr = [[sys.maxsize]*(n+1) for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        arr[a][b] = 1
        arr[b][a] = 1

    for i in range(1, n+1):
        arr[i][i] = 0

    for k in range(1, n+1):
        for s in range(1, n + 1):
            for e in range(1, n + 1):

                arr[s][e] = min(arr[s][e], arr[s][k]+arr[k][e])

    minkbacon = sys.maxsize
    ans = sys.maxsize
    for i in range(1, n+1):
        kbacon = 0
        for j in range(1, n + 1):
            if arr[i][j] != sys.maxsize:
                kbacon += arr[i][j]
        if minkbacon > kbacon:
            minkbacon = kbacon
            ans = i

    print(ans)

