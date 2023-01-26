from queue import PriorityQueue
import sys

if __name__ == '__main__':
    V, E = map(int, sys.stdin.readline().split())
    s = int(sys.stdin.readline())

    arr = [[] for _ in range(V+1)]
    visited = [False]*(V+1)
    cost = [sys.maxsize]*(V+1)

    for _ in range(E):
        u, v, w = map(int, sys.stdin.readline().split())
        arr[u].append((v, w))

    q = PriorityQueue()
    q.put((0, s))
    cost[s] = 0

    while not q.empty():
        i = q.get()[1]

        if visited[i]:
            continue

        visited[i] = True

        for v, w in arr[i]:
            # print(cost[v], cost[i], w)
            if cost[v] > cost[i] + w:
                cost[v] = min(cost[v], cost[i]+w)
                q.put((cost[v], v))

        # print(cost)
    for i in range(1, V+1):
        if visited[i]:
            print(cost[i])
        else:
            print('INF')
