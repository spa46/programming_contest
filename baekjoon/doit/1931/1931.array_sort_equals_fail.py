from queue import PriorityQueue

def solve(arr):
    cnt = 1
    e = arr[0][1]

    i=0
    while i<len(arr):
        s2, e2 = arr[i]
        if s2 == e2:
            continue
        if s2>=e:
            cnt += 1
            e = e2
        i+=1


    return cnt

def main():
    n =int(input())

    q = PriorityQueue()

    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))

    arr.sort(key = lambda v: (v[1], v[0]))

    print(solve(arr))

if __name__ == '__main__':
    main()