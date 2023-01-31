from collections import deque
from queue import PriorityQueue
import sys

n, m = map(int, sys.stdin.readline().split())

def find(p, e):
    if e == parent[e]:
        return e

    parent[e] = find(p, parent[e])
    return parent[e]


def union(p, a, b):
    a = find(p, a)
    b = find(p, b)

    if a != b:
        p[b] = a
        return True

    return False

def checkUnion(p):
    lp = len(p)
    a = find(p, p[1])
    for i in range(2, lp):
        b = find(p, p[i])
        if a != b:
            return False
        a = b

    return True


def vertical_scan(varr, arr):
    for j in range(m):
        s = 0; e = len(arr)-1

        while s < e:
            if arr[s][j] == 0:
                s += 1

            elif s < e and arr[e][j] == 0:
                e -= 1
            else:
                break

        while s < e:
            v1 = arr[s][j]

            while s < e and arr[s][j] != 0:
                v1 = arr[s][j]
                s += 1

            cnt = 0
            while s < e and arr[s][j] == 0:
                cnt += 1
                s += 1

            v2 = arr[s][j]

            if v1 == v2 or cnt < 2:
                break

            varr[v1][v2] = min(varr[v1][v2], cnt)



def horizontal_scan(varr, arr):

    for i in range(n):
        s = 0;
        e = len(arr[0]) - 1

        while s <= e:
            if arr[i][s] == 0:
                s += 1
            elif arr[i][e] == 0:
                e -= 1
            else:
                break

        while s < e:
            v1 = arr[i][s]
            # print(i, s, e, '->', end=' ')
            while s < e and arr[i][s] != 0:
                v1 = arr[i][s]
                s += 1
            # print(i, s, e, '->', end=' ')
            cnt = 0
            while s < e and arr[i][s] == 0:
                cnt += 1
                s += 1

            v2 = arr[i][s]
            # print(i, s, e, '===>', v1, v2, cnt)
            if v1 == v2 or cnt < 2:
                continue

            varr[v1][v2] = min(varr[v1][v2], cnt)


def bfs(arr, visited, q, mark):
    while q:
        i,j = q.popleft()
        arr[i][j] = mark

        if j+1 < m and arr[i][j+1] == 1 and not visited[i][j+1]:
            q.append((i,j+1))
            visited[i][j+1] = True
        if j-1 >= 0 and arr[i][j-1] == 1 and not visited[i][j-1]:
            q.append((i, j-1))
            visited[i][j-1] = True
        if i+1 < n and arr[i+1][j] == 1 and not visited[i+1][j]:
            q.append((i+1, j))
            visited[i+1][j] = True
        if i-1 >= 0 and arr[i-1][j] == 1 and not visited[i-1][j]:
            q.append((i-1, j))
            visited[i-1][j] = True


if __name__ == '__main__':
    arr = []
    for _ in range(n):
        arr.append(list(map(int, sys.stdin.readline().split())))

    visited = [[False]*m for _ in range(n)]
    mark = 1
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1 and not visited[i][j]:
                q = deque()
                q.append((i,j))
                visited[i][j] = True

                bfs(arr, visited, q, mark)
                mark += 1

    # for i in range(len(arr)):
    #     print(arr[i])

    v = mark-1
    varr = [[sys.maxsize] * (v+1) for i in range(v+1)]
    horizontal_scan(varr, arr)
    vertical_scan(varr, arr)

    # for i in range(1, v+1):
    #     for j in range(1, v+1):
    #         if varr[i][j] == sys.maxsize:
    #             varr[i][j] = 0
    #
    # for i in range(1, mark):
    #     print(varr[i][1:])

    q = PriorityQueue()
    parent = [i for i in range(v+1)]
    for i in range(1, v+1):
        for j in range(1, v+1):
            if varr[i][j] == sys.maxsize:
                continue

            q.put((varr[i][j], (i, j)))

    if q.qsize() == 0:
        print(-1)
        exit()


    i = 1
    total = 0
    while not q.empty() and i < mark:
        val, v = q.get()

        if union(parent, v[0], v[1]):
            total += val
            # print(val, v)

    if checkUnion(parent):
        print(total)
    else:
        print(-1)