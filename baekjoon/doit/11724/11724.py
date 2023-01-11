import sys

if __name__ == '__main__':
    n,m = map(int, input().split())

    v = [False]*n
    arr = []
    for i in range(m):
        i,j = map(int, input().split())
        if i<j:
            arr.append([i-1, j-1])
        else:
            arr.append([j-1,i-1])

    arr.sort()
    cnt = 0
    for i,j in arr:
        if v[i] and v[j]:
            continue
        elif not v[i] and not v[j]:
            cnt += 1

        v[i] = True
        v[j] = True

    for i in range(n):
        if not v[i]:
            v[i] = True
            cnt += 1

    print(cnt)