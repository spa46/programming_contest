from queue import PriorityQueue
import sys

n = int(sys.stdin.readline())
parent = [i for i in range(n)]


def find(e):
    if e == parent[e]:
        return e
    else:
        parent[e] = find(parent[e])
        return parent[e]


def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        parent[b] = a


def checkUnion():
    a = find(parent[0])

    for i in range(1, len(parent)):
        if a != find(parent[i]):
            return False

    return True

if __name__ == '__main__':


    arr = []
    for i in range(n):
        s = sys.stdin.readline().strip()
        arr.append(list(s))

    q = PriorityQueue()
    total = 0
    for i in range(n):
        for j in range(n):
            if 'a' <= arr[i][j] <= 'z':
                arr[i][j] = ord(arr[i][j]) - ord('a') + 1
            elif 'A' <= arr[i][j] <= 'Z':
                arr[i][j] = ord(arr[i][j]) - ord('A') + 27
            else:
                arr[i][j] = 0

            total += arr[i][j]

            if i != j and arr[i][j] != 0:
                q.put((arr[i][j], (i,j)))

    i = 0
    w = 0
    edges = 0
    while not q.empty():
        val, v = q.get()

        if find(v[0]) != find(v[1]):
            union(v[0], v[1])
            w += val
            edges += 1

    if edges == n-1:
        print(total - w)
    else:
        print(-1)
    
