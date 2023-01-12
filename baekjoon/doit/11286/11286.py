import heapq
import sys

if __name__ == '__main__':
    n = int(input())

    minheap = []
    for i in range(n):
        v = int(input())
        if v != 0:
            heapq.heappush(minheap, (abs(v), v))
        else:
            if minheap:
                print(heapq.heappop(minheap)[1])
            else:
                print(0)

    # print(arr)
