import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())

    arr = []
    for _ in range(n):
        arr.append(list(map(int, sys.stdin.readline().split())))

    for k in range(n):
        for s in range(n):
            for e in range(n):
                if not arr[s][e]:
                    arr[s][e] = arr[s][k] and arr[k][e]

    for i in range(n):
        print(' '.join(map(str, arr[i])))