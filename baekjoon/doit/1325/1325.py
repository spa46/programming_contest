from collections import deque

def bfs(arr, v, c, s):
    if v[s]:
        return 0
    q = deque()
    q.append(s)
    while q:
        i = q.popleft()
        v[i] = True

        for j in arr[i]:
            if v[j]:
                continue

            q.append(j)
            c[j] += 1
            v[j] = True


if __name__ == '__main__':
    n,m = map(int, input().split())

    arr = [[] for _ in range(n+1)]

    c = [0]*(n+1)
    for _ in range(m):
        a, b = map(int, input().split())
        arr[a].append(b)

    for i in range(1, len(arr)):
        v = [False] * (n + 1)
        bfs(arr, v, c, i)

    out = []
    mmax = 0
    for i in range(1, len(arr)):
        if c[i] > mmax:
            out = [i]
            mmax = c[i]
        elif c[i] == mmax:
            out.append(i)

    print(' '. join(map(str, out)))
