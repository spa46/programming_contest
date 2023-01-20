from collections import deque

send = [2,2,1,1,0,0]
receiver = [0,1,0,2,1,2]


def bfs(b,c,v):
    q = deque()
    q.append(c)
    v[0][0] = True

    out = [c[2]]

    while q:
        t = q.popleft()

        for i in range(len(send)):
            c = t[:]

            s = send[i]
            r = receiver[i]
            tmp = c[s]+c[r]

            if tmp>b[r]:
                c[s] = tmp-b[r]
                c[r] = b[r]
                i = c[0]; j = c[1]

                if v[i][j]:
                    continue
                v[i][j] = True

                q.append(c)

                if c[0]<=0:
                    out.append(c[2])
            else:
                c[r] = c[s]+c[r]
                c[s] = 0
                i = c[0]; j = c[1]

                if v[i][j]:
                    continue
                v[i][j] = True

                q.append(c)

                if c[0]<=0:
                    out.append(c[2])
    return out

if __name__ == '__main__':
    b = list(map(int, input().split()))
    c = [0, 0, b[2]]
    v = [[False]*201 for _ in range(201)]

    out = bfs(b,c,v)
    out.sort()
    print(' '.join(map(str, out)))

