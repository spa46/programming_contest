from collections import deque
import sys

n = int(sys.stdin.readline())

depth = [10001]*(n+1)
arr = [[] for _ in range(n+1)]
depth[1] = 0


for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)

visited = [False]*(n+1)
visited[1] = True
q = deque()
q.append(1)

maxdepth = 0
i=1

while i < n:
    maxdepth += 1
    i <<= 1

parent = [[0]*(n+1) for _ in range(maxdepth)]

while q:
    v = q.popleft()
    visited[v] = True

    for i in arr[v]:
        if not visited[i]:
            depth[i] = depth[v] + 1
            visited[i] = True
            parent[0][i] = v
            q.append(i)
            

for i in range(1, maxdepth):
    for j in range(1, n+1):
        parent[i][j] = parent[i-1][parent[i-1][j]]

m = int(sys.stdin.readline())
for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())

    if depth[i] > depth[j]:
        t = i
        i = j
        j = t

    for k in range(maxdepth-1, -1, -1):
        if pow(2,k) <= depth[j]-depth[i]:
            if depth[i] <= depth[parent[k][j]]:
                j = parent[k][j]

    for k in range(maxdepth-1, -1, -1):
        if i == j: break
        # print(i, j)
        if parent[k][i] != parent[k][j]:
            i = parent[k][i]
            j = parent[k][j]

    ans = i
    if i != j:
        print(parent[0][ans])
    else:
        print(ans)
