import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())

    sum = 0
    cnt = 0
    j = 1
    for i in range(1,n+1):
        sum += i
        while sum > n:
            sum-=j
            j+=1

        if sum == n:
            cnt += 1

    print(cnt)

