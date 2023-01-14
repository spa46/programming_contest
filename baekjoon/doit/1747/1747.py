import math
import sys

N = 10000001
def is_palindrome(n):
    s = str(n)
    i=0; j=len(s)-1

    while i<j:
        if s[i] != s[j]:
            return False
        i+=1; j-=1

    return True

def solve(n):
    arr = [1]*N
    arr[0]=0; arr[1]=0
    for i in range(2, int(math.sqrt(N))+1):
        for j in range(i+i, N, i):
            arr[j] = 0

    out = []
    for i in range(n,N):
        if arr[i]:
            if is_palindrome(i):
                return i

    return 0

def main():
    n =int(input())

    print(solve(n))


if __name__ == '__main__':
    main()