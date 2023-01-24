import sys
sys.setrecursionlimit(10**8) # 10^8 까지 늘림.

n = int(input())
m = int(input())

c = [i for i in range(200)]

def find(e):
    if e == c[e]:
        return e

    c[e] = find(c[e])
    return c[e]

def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        c[b] = a

def traverse(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return True

    return False

if __name__ == '__main__':
    arr = []
    for i in range(n):
        t = list(input().split())
        for j in range(i, n):
            if t[j] == '1':
                union(i, j)
        # print(c[:n])
    plan = list(map(int, input().split()))

    for i in range(1, m):
        a = plan[i-1]-1
        b = plan[i]-1
        if not traverse(a, b):
            print('NO')
            exit(0)

    print('YES')