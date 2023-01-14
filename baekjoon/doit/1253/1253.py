import sys

def solve(n, arr):
    cnt = 0

    for k in range(n):
        i=0; j=n-1
        find = arr[k]
        while i<j:
            # print(i, j, k)
            # print(arr[i], arr[j], find)
            if arr[i]+arr[j] == find:
                if i!=k and j!=k:
                    cnt+=1
                    break
                elif j == k:
                    j -= 1
                elif i == k:
                    i += 1
            elif arr[i]+arr[j] < find:
                i+=1
            else:
                j-=1
            # print('     ',i,j,k)

    return cnt

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(solve(n, arr))

if __name__ == '__main__':
    main()