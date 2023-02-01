import sys
sys.setrecursionlimit(10**9)

n = int(sys.stdin.readline())
p = [-1]*(n+1)

arr = [[]*(n+1) for _ in range(n+1)]
visited = [False]*(n+1)
out = [0]*(n+1)


def traverse(node):
    visited[node] = True

    for i in arr[node]:
        if not visited[i]:
            out[i] = node
            traverse(i)


for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)

traverse(1)

for v in out[2:]:
    print(v)