n, m = map(int, input().split())
truth = list(map(int, input().split()))
parents = [i for i in range(n + 1)]


def find(e):
    if e == parents[e]:
        return e

    parents[e] = find(parents[e])
    return parents[e]


def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        parents[b] = a

def canGo(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return False

    return True


if __name__ == '__main__':

    cnt = 0
    if truth[0] <= 0:
        print(m)
        exit(0)

    for i in range(2, truth[0]+1):
        union(truth[i-1], truth[i])

    arr = []
    for i in range(m):
        item = list(map(int, input().split()))
        h = item[0]
        t = item[1:]
        arr.append(t)

        for i in range(2, h+1):
            union(item[i-1], item[i])
    
    for i in range(len(arr)):
        if canGo(truth[1], arr[i][0]):
            cnt += 1

    print(cnt)



