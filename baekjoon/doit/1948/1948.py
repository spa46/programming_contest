from collections import deque

if __name__ == '__main__':
    n = int(input())
    m = int(input())

    arr = [[] for _ in range(n+1)]
    inv = [[] for _ in range(n + 1)]
    v = [0]*(n+1)
    mtime = [0]*(n+1)

    for _ in range(m):
        _s, _e, _t = map(int, input().split())
        arr[_s].append([_e, _t])
        v[_e] += 1
        inv[_e].append([_s, _t])

    s, e = map(int, input().split())

    q = deque()
    for i in range(1, n+1):
        if v[i] == 0:
            q.append([i, 0])

    while q:
        i, _ = q.popleft()

        for j, jt in arr[i]:
            v[j] -= 1
            mtime[j] = max(mtime[j], mtime[i] + jt)

            if v[j] == 0:
                q.append([j, jt])

    out = []
    out.append(mtime[j])
    visited = [False] * (n + 1)

    q = deque()
    q.append([j, mtime[j]])
    visited[j] = True

    cnt = 0

    while q:
        # print('q:', list(q))
        i, it = q.popleft()

        for j, jt in inv[i]:
            # print('     visit:', j, jt)
            if mtime[i]-jt == mtime[j]:
                cnt += 1

                if visited[j]:
                    continue

                q.append([j, it-jt])
                visited[j] = True
                # print('HIT:', j)


    out.append(cnt)
    print(' '.join(map(str, out)))