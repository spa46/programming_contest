from queue import PriorityQueue
import sys

v, e = map(int, sys.stdin.readline().split())
parent = [i for i in range(v+1)]

def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        parent[b] = a
        return True

    return False

if __name__ == '__main__':
    q = PriorityQueue()
    for _ in range(e):
        a, b, c = map(int, sys.stdin.readline().split())
        q.put((c, a, b))

    out = 0
    vcnt = 0
    while not q.empty() and vcnt < v:
        c, a, b = q.get()

        if union(a, b):
            vcnt += 1
            out += c

    print(out)