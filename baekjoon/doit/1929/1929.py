import math

def solve(m,n):
    arr = [1]*(n+1)
    arr[0] = 0; arr[1] = 0

    for i in range(2, int(math.sqrt(n))+1):
        if not arr[i]:
            continue

        for j in range(i+i, n+1, i):
            arr[j] = 0
            j+=1

    for i in range(m,n+1):
        if arr[i]:
            print(i)

if __name__ == '__main__':
    m,n = map(int, input().split())

    solve(m,n)

