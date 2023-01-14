import sys

def solve(n, arr):
    visited = [False]*(n+1)
    q = arr[1]
    visited[1] = True
    cnt = 0
    for i in range(len(arr)):
        print(arr[i])
    while q:
        v,w = q.pop()
        print(v , w)
        cnt = max(cnt, w)
        while arr[v]:
            v2, w2 = arr[v].pop(0)
            if not visited[v2]:
                q.append([v2, w+w2])
                visited[v2] = True
    return cnt

def main():
    n = int(input())

    arr = [[0,0]]
    for i in range(n):
        tmp = list(map(int, input().strip().split()))
        v1 = []

        i=0; j=1
        v = []
        while j<len(tmp)-1:
            v.append([tmp[j], tmp[j+1]])
            j+=2
        arr.append(v)

    print(solve(n, arr))

if __name__ == '__main__':
    main()