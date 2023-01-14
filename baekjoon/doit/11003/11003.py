import heapq
import sys

def solve(l, arr):
    i=0; j=0
    sum=0

    d = []

    while j<l:
        heapq.heappush(arr[j])
        d.append(heapq.nsmallest())
        j+=1



def main():
    n, l = map(int,input().split())
    arr = list(map(int, input().split()))
    print(solve(l, arr))

if __name__ == '__main__':
    main()