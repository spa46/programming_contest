import sys
from queue import PriorityQueue
from math import inf

if __name__ == '__main__':
    n, m, k = map(int, sys.stdin.readline().split())
    cost = [-1]*(n+1)

    arr = [[] for _ in range(n+1)]
    d = [[sys.maxsize] * k for _ in range(n+1)]
    q = PriorityQueue()

    for _ in range(m):
        a, b, c = map(int, sys.stdin.readline().split())
        arr[a].append((b, c))

    q.put((0, 1))
    d[1][0] = 0

    while not q.empty():
        w, i = q.get()

        for j, jt in arr[i]:
            if d[j][k-1] > w+jt:
                d[j][k-1] = w+jt
                d[j].sort()
                q.put((w+jt, j))

    # print(d)
    for i in range(1, len(d)):
        if d[i][k-1] == sys.maxsize:
            print(-1)
        else:
            print(d[i][k-1])
