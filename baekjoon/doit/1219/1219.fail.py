import sys

if __name__ == '__main__':
    n, s, e, m = map(int, sys.stdin.readline().split())

    edges = []
    for _ in range(m):
        edges.append(list(map(int, sys.stdin.readline().split())))

    earn = list(map(int, sys.stdin.readline().split()))

    balance = [-sys.maxsize]*n
    balance[s] = earn[s]

    for i in range(n-1):
        for u, v, w in edges:
            if balance[v] < balance[u] - w + earn[v]:
                balance[v] = balance[u] - w + earn[v]
        print(balance)

    dest = balance[e]
    for u, v, w in edges:
        if balance[v] < balance[u] - w + earn[v]:
            balance[v] = balance[u] - w + earn[v]
    print(balance)

    if balance[e] == -sys.maxsize:
        print('gg')
        sys.exit()
    print(dest, balance[e])
    if dest != balance[e]:
        print('Gee')
        sys.exit()

    print(balance[e])