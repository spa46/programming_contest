from collections import deque


def func(n):
    cost = [0]*(n+1)
    gmap = [[] for _ in range(n+1)]
    t = [0] * (n + 1)

    for i in range(1,n+1):
        a = list(map(int, input().split()))

        for j in a[1:-1]:
            gmap[j].append(i)

        cost[i] = a[0]
        t[i] = len(a[1:-1])

    return cost, gmap, t


def solve(cost, gmap, t):
    q = deque()

    out = [0] * (n + 1)

    for i in range(1, n + 1):
        if t[i] == 0:
            q.append(i)

    while q:
        i = q.popleft()

        for next in gmap[i]:
            t[next] -= 1
            out[next] = max(out[next], out[i]+cost[i])
            # print(i, next, out)
            if t[next] == 0:
                q.append(next)

    for i in range(1, n + 1):
        print(cost[i]+out[i])


if __name__ == '__main__':
    n = int(input())

    cost, gmap, t = func(n)

    solve(cost, gmap, t)