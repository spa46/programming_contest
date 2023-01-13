from queue import PriorityQueue

def solve(q):
    cnt = 1
    e = q.get()[1][1]

    while not q.empty():
        s2, e2 = q.get()[1]
        if s2>=e:
            cnt += 1
            e = e2

    return cnt

def main():
    n =int(input())

    q = PriorityQueue()

    for i in range(n):
        t = list(map(int, input().split()))

        q.put([t[1], t])

    print(solve(q))

if __name__ == '__main__':
    main()