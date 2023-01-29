import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    m = int(sys.stdin.readline())

    arr = [[sys.maxsize]*(n+1) for _ in range(n+1)]
    for _ in range(m):
        a, b, c = list(map(int, sys.stdin.readline().split()))
        arr[a][b] = min(arr[a][b], c)


    for k in range(1, n+1):
        for s in range(1, n+1):
            for e in range(1, n+1):
                if s == e:
                    continue
                arr[s][e] = min(arr[s][e], arr[s][k]+arr[k][e])

    for i in range(1, n+1):
        for j in range(1, n+1):
            if arr[i][j] == sys.maxsize:
                arr[i][j] = 0
            print(arr[i][j], end=' ')
        print()