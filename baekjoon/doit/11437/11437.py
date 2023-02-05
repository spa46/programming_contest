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
arr2 = [sys.maxsize]*(n+1)


visited[1] = True
q = deque()
q.append(1)

while q:
    v = q.popleft()
    visited[v] = True

    for i in arr[v]:
        if not visited[i]:
            depth[i] = depth[v] + 1
            visited[i] = True
            arr2[i] = v
            q.append(i)

def getRoot(a, b):
    if depth[a] < depth[b]:
        tmp = a
        a = b
        b = tmp

    while depth[a] != depth[b]:
        a = arr2[a]

    while a != b:
        a = arr2[a]
        b = arr2[b]

    return a

m = int(sys.stdin.readline())
for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    ans = getRoot(i,j)
    print(ans)