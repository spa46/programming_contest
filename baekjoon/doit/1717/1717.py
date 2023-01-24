# 0 1 0 1 0 0
# 0 1 0 1 5 5

n, m = list(map(int, input().split()))
parent = [i for i in range(n+1)]


def find(e):
    if e == parent[e]:
        return e
    else:
        parent[e] = find(parent[e])
        return parent[e]


def union(a, b):
    a = find(a)
    b = find(b)

    if a!= b:
        parent[b] = a

def isSame(a, b):
    e1 = find(a)
    e2 = find(b)

    if e1 == e2:
        return 'YES'

    return 'NO'


if __name__ == '__main__':

    for _ in range(m):
        op, a, b = list(map(int, input().split()))

        if op == 0:
            union(a, b)
        else:
            print(isSame(a, b))
