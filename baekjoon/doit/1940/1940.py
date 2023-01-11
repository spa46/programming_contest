import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    m = int(sys.stdin.readline().strip())
    arr = list(map(int, sys.stdin.readline().strip().split()))

    arr.sort()
    i=0; j=1
    sum = 0
    cnt = 0

    tmp = []
    for v in arr:
        r = m-v
        if v not in tmp:
            tmp.append(r)
        else:
            tmp.remove(v)
            cnt+=1

    print(cnt)

