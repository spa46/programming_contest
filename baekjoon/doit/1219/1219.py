import sys

if __name__ == '__main__':
    n, s, e, m = map(int, sys.stdin.readline().split())

    edges = []
    for _ in range(m):
        edges.append(list(map(int, sys.stdin.readline().split())))

    earn = list(map(int, sys.stdin.readline().split()))

    balance = [-sys.maxsize]*n
    balance[s] = earn[s]

    for i in range(n+101):
        for u, v, w in edges:
            if balance[u] == -sys.maxsize:
                continue
            elif balance[u] == sys.maxsize:
                balance[v] = sys.maxsize
            elif balance[v] < balance[u] - w + earn[v]:
                balance[v] = balance[u] - w + earn[v]

                if i >= n-1:
                    balance[v]=sys.maxsize
        # print(balance)

        # print(balance)
    if balance[e] == -sys.maxsize:
        print('gg')
    elif balance[e] == sys.maxsize:
        print('Gee')
    else:
        print(balance[e])
