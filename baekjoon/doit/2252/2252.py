from collections import deque

def topological_sort(arr, v):
    t = []

    q = deque()
    for i in range(1, len(v)):
        if v[i] == 0:
            q.append(i)

    while q:
        i = q.popleft()
        t.append(i)

        for j in arr[i]:
            v[j] -= 1
            if v[j] == 0:
                q.append(j)
    # print(v, q, t)
    return t

if __name__ == '__main__':
    n, m = map(int, input().split())

    arr = [[] for _ in range(n+1)]
    v = [0]*(n+1)
    for _ in range(m):
        a, b = map(int, input().split())
        if a == b:
            continue

        arr[a].append(b)
        v[b] += 1

    ans = topological_sort(arr, v)
    print(' '.join(map(str, ans)))
