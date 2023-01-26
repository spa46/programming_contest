import sys
from queue import PriorityQueue
from math import inf

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    m = int(sys.stdin.readline())
    arr = [[] for _ in range(n+1)]
    visited = [False]*(n+1)
    cost = [inf] * (n+1)

    for _ in range(m):
        s, e, c = map(int, sys.stdin.readline().split())
        arr[s].append((e, c))

    s, e = map(int, sys.stdin.readline().split())

    q = PriorityQueue()
    q.put((0, s))
    cost[s] = 0

    while not q.empty():
        i = q.get()[1]

        if visited[i]:
            continue
        visited[i] = True

        for j, jt in arr[i]:
            if cost[j] > cost[i] + jt:
                cost[j] = cost[i] + jt
                q.put((cost[j], j))

    print(cost[e])
