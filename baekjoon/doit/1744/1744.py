from queue import PriorityQueue
import sys

def solve(plusQ, minusQ):
    total = 0
    while plusQ.qsize()>1:
        a = plusQ.get()[1]
        b = plusQ.get()[1]
        if a == 1 or b == 1:
            total += a+b
        else:
            total += a*b

    while minusQ.qsize()>1:
        a = minusQ.get()[1]
        b = minusQ.get()[1]
        total += a*b

    if not plusQ.empty():
        a = plusQ.get()[1]
        total += a

    if not minusQ.empty():
        a = minusQ.get()[1]
        total += a

    return total

def main():
    n =int(input())

    plusQ = PriorityQueue()
    minusQ = PriorityQueue()

    for i in range(n):
        num = int(input())
        if num>0:
            plusQ.put([-1*num, num])
        else:
            minusQ.put([num, num])

    print(solve(plusQ, minusQ))

if __name__ == '__main__':
    main()