from queue import PriorityQueue
import sys

c = '0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
n = int(sys.stdin.readline())
parents = [i for i in range(n)]

def find(e):
    if e == parents[e]:
        return e
    else:
        parents[e] = find(parents[e])
        return parents[e]

def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        parents[b] = a
        return True

    return False

def checkUnion(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return True

    return False

if __name__ == '__main__':


    arr = []
    for i in range(n):
        s = sys.stdin.readline().strip()
        arr.append(list(s))

    q = PriorityQueue()
    total = 0
    for i in range(n):
        for j in range(n):
            arr[i][j] = c.index(arr[i][j])
            total += arr[i][j]

            if arr[i][j] == 0 or (n > 1 and i == j):
                arr[i][j] = sys.maxsize

            q.put((arr[i][j], (i,j)))
    # print(arr)

    if q.qsize() == 1:
        val, v = q.get()

        if val == sys.maxsize:
            print(0)
            sys.exit()

    i = 0
    while not q.empty() and i<n:
        val, v = q.get()

        if val == sys.maxsize:
            if q.qsize() == (n*n)-1:
                print(-1)
            else:
                print(0)
            sys.exit()

        if union(v[0], v[1]):
            total -= val

        i+=1

    for i in range(1, n):
        if not checkUnion(parents[i-1], parents[i]):
            print(-1)
            sys.exit()

    print(total)


