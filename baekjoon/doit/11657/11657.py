from collections import deque

import sys

if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())

    edges = []
    d = [sys.maxsize]*(n+1)
    q = deque()

    for _ in range(m):
        a, b, c = map(int, sys.stdin.readline().split())
        edges.append((a, b, c))

    d[1] = 0

    for _ in range(n-1):
        for s, e, t in edges:
            if d[s] != sys.maxsize and d[e] > d[s] + t:
                d[e] = d[s] + t

    has_cycle = False
    for s, e, t in edges:
        if d[s] != sys.maxsize and d[e] > d[s] + t:
            has_cycle = True

    if has_cycle:
        print(-1)
    else:
        for i in range(2, n+1):
            if d[i] == sys.maxsize:
                print(-1)
            else:
                print(d[i])
