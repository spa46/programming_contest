import sys

def solve(n, m, arr):
    visited = [[False]*m for i in range(n)]
    q = [[0, 0]]
    visited[0][0] = True

    cnt = 0
    while q:
        i,j = q.pop(0)
        # print(i,j)
        if j+1<m and arr[i][j+1] != 0 and not visited[i][j+1]:
            arr[i][j+1] = arr[i][j]+1
            q.append([i, j+1])
            visited[i][j+1] = True
        if i+1<n and arr[i+1][j] != 0 and not visited[i+1][j]:
            arr[i+1][j] = arr[i][j]+1
            q.append([i+1, j])
            visited[i+1][j] = True
        if j-1>=0 and arr[i][j-1] != 0 and not visited[i][j-1]:
            arr[i][j-1] = arr[i][j]+1
            q.append([i, j-1])
            visited[i][j-1] = True
        if i-1>=0 and arr[i-1][j] != 0 and not visited[i-1][j]:
            arr[i-1][j] = arr[i][j]+1
            q.append([i-1, j])
            visited[i-1][j] = True

        if i == n-1 and j == m-1:
            return arr[n-1][m-1]

    return arr[n-1][m-1]

def main():
    n, m = map(int,input().split())
    arr = [[0]*m for i in range(n)]
    for i in range(n):
        str = input()
        for j in range(m):
            arr[i][j] = int(str[j])

    print(solve(n, m, arr))

if __name__ == '__main__':
    main()