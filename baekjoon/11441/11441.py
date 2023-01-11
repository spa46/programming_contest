import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    arr = list(map(int,sys.stdin.readline().split()))

    sum = 0
    arr1 = [0]
    for i in range(n):
        sum += arr[i]
        arr1.append(sum)

    m = int(sys.stdin.readline())
    for _ in range(m):
        i,j = list(map(int, sys.stdin.readline().split()))

        if i<1:
            print(0)
            continue

        print(arr1[j]-arr1[i-1])
