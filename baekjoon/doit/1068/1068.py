import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
d = int(sys.stdin.readline())

arr2 = [[] for _ in range(n)]

root = -1
for i in range(n):
    if arr[i] == -1:
        root = i
        continue

    if i != d and arr[i] != d:
        arr2[arr[i]].append(i)

visited = [False]*n
def traverse(i):
    visited[i] = True

    if not arr2[i]:
        return 1

    leaf = 0
    for j in arr2[i]:
        if not visited[j]:

            leaf += traverse(j)
            visited[i] = True

    return leaf

# print(arr2)
if arr[d] == -1:
    print(0)
else:
    ans = traverse(root)
    print(ans)